# Import the hash function from the hashing script
from hashing import pass_hash

# Read the hashes from the `hashes` file and split them by the 0xff stop byte
with open("extracted_hashes.txt", "rb") as f:
    hashes_data = f.read().split(b'\xff')

# Read passwords from bad_passwords.txt
with open("bad_passwords.txt", "r") as f:
    passwords = [line.strip() for line in f]

# Compare each password's hash to the hashes in `hashes_data`
cracked_passwords = {}
for password in passwords:
    hashed_password = pass_hash(password).encode('utf-8')
    print(hashed_password)
    if hashed_password in hashes_data:
        cracked_passwords[password] = hashed_password

# Display any matches found
if cracked_passwords:
    for pwd, hashed in cracked_passwords.items():
        print(f"Password: {pwd} | Hash: {hashed}")
else:
    print("No matches found.")

print("Cracked Passwords: ")
print(cracked_passwords)
