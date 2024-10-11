""" ==Libraries== """
import requests
from bs4 import BeautifulSoup
import csv

""" ==Functions== """


# Function to clean name by removing academic titles and punctuation
def clean_name(name):
    # Remove common academic titles (Dr., Ph.D., different degrees in general, business degrees, etc.)
    titles = ['Dr.', 'Ph.D.', 'MBA', 'MS', 'MA.', 'M.Ed.', 'CPA', 'CFA', 'CIA', 'CFE', 'CRMA', 'D.B.A', 'J.D.', 'LL.M',
              'CMA', '.', ',', '(', ')', '"', "'"]
    for title in titles:
        name = name.replace(title, '').strip()
    return name


# Function to scrape the university directory
def scrape_directory(url):
    # Fetching the page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')  # Parsing the HTML

    # Finding all people entries
    entries = soup.find_all('div', class_='cn-list-item')  # Each person is in a div with the class 'cn-list-item'
    result = []  # List to store the results

    # Iterating through each entry
    for entry in entries:
        # Extract the person's name
        name_tag = entry.find('a', title=True)  # The name is in an anchor tag with a title attribute
        # Only add if name exists
        if name_tag:
            name = name_tag.text.strip()  # Extract the name
            clean_name_value = clean_name(name)  # Clean the name by removing titles and quotes

            # Extract the person's email
            # The email is in an anchor tag with an href attribute starting with 'mailto:'
            email_tag = entry.find('a', href=lambda href: href and 'mailto:' in href)

            # Only add if email exists
            if email_tag:
                email = email_tag.text.strip().replace('mailto:', '')  # Extract the email
                result.append({'name': clean_name_value, 'email': email})  # Add the name and email to the result list

    return result


# Function to save scraped data to CSV
def save_to_csv(data, filename='email_list.csv'):
    keys = data[0].keys()  # Get the keys from the first dictionary in the list
    with open(filename, 'w', newline='') as output_file:  # Open the file in write mode
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)  # Create a DictWriter object
        dict_writer.writeheader()  # Write the header
        dict_writer.writerows(data)  # Write the data


""" ==Main Program== """
# URL of the directory to scrape
directory_url = 'https://www.latech.edu/faculty-staff/single-entry/cat/college-of-business/'
email_list = scrape_directory(directory_url)  # Scrape the directory

# Save results to CSV if there are valid emails
if email_list:
    save_to_csv(email_list)
    print(f"Successfully saved {len(email_list)} entries to 'email_list.csv'.")
else:
    print("No valid emails found.")
