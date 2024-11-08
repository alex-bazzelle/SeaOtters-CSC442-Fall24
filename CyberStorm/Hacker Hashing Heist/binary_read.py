# Step 1: Open the binary file and read content
with open("hashes", "rb") as file:
    hashes_data = file.read()

# Step 2: Split the data by the stop byte (0xff) to get each hash
# We use `split(b'\xff')` to separate each hash
hashes_list = hashes_data.split(b'\xff')

# Now `hashes_list` contains each individual hash (except for the empty last entry if it ends with 0xff)
print("Extracted hashes:", hashes_list)
