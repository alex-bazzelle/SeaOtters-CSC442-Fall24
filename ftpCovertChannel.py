import ftplib

# FTP connection variables
FTP_HOST = ""  # FTP host address or IP
FTP_PORT = 21  # Default FTP port is 21, change if needed
FTP_USER = "anonymous"  # FTP username
FTP_PASS = ""  # FTP password, can be blank for anonymous
FTP_DIR = "/"  # Directory to initially browse to
METHOD = 10 # Use 7 or 10 depending on the required method
USE_PASSIVE = True  # set to False if the connection times out


# Function to connect to FTP and retrieve file listings
def fetch_ftp_file_permissions():
    # Attempt to connect to the FTP server
    try:
        # Connect to the FTP server
        ftp = ftplib.FTP()  # Create an FTP object
        ftp.connect(FTP_HOST, FTP_PORT)  # Connect to the FTP server
        ftp.login(FTP_USER, FTP_PASS)  # Login to the FTP server
        ftp.set_pasv(USE_PASSIVE)  # Set passive mode if required (i.e. True unless initial request timed out)

        # Change to the specified directory
        ftp.cwd(FTP_DIR)

        # Retrieve file listing including permissions
        files = []  # List to store file permissions
        ftp.dir(files.append)  # Append each file listing to the list

        # Disconnect from the FTP server
        ftp.quit()

        return files
    except ftplib.all_errors as e:  # Catch all FTP errors
        print(f"FTP error: {e}")  # Print the error message
        return None  # Return None if an error occurred


# Function to decode permissions to a message
def decode_permissions(files, method):
    message_bits = []  # List to store the message bits

    for file_info in files:  # Iterate through each file listing
        # Extract the permission string (first 10 characters)
        permissions = file_info[:10]  # Extract the first 10 characters

        # Check if we are using 7-bit or 10-bit method
        if method == 7:
            # Filter out files where the first 3 bits are not '-'
            if permissions[0:3] != '---':
                continue
            # Take the last 7 bits
            bits = permissions[3:]
        elif method == 10:
            # Use all 10 bits
            bits = permissions
        else:  # Invalid method
            print(f"Invalid method: {method}")
            return None

        # Convert permissions to binary (0 for -, 1 otherwise)
        binary_string = ''.join(['0' if char in '-' else '1' for char in bits])

        # Append the last 7 or 10 bits as binary to the message bits list
        message_bits.append(binary_string)

    # Join all the bits into a continuous binary string
    binary_message = ''.join(message_bits)

    # Convert the binary string into characters
    covert_message = ''
    for i in range(0, len(binary_message), 7):  # Iterate through the binary string in 7-bit chunks
        byte = binary_message[i:i + 7]  # Extract the next 7 bits
        if len(byte) == 7:  # Ensure it's a full 7-bit chunk
            ascii_value = int(byte, 2)  # Convert to integer
            # Only append if it's a printable ASCII character
            if 32 <= ascii_value <= 126:  # ASCII printable range
                covert_message += chr(ascii_value)  # Convert to ASCII character and append

    return covert_message


# Main program execution
if __name__ == "__main__":
    # Fetch file permissions from the FTP server
    file_listings = fetch_ftp_file_permissions()

    if file_listings:  # Check if file listings were successfully retrieved
        # Decode the permissions to reveal the covert message
        covert_message = decode_permissions(file_listings, METHOD)

        # Print the covert message
        print(covert_message)
