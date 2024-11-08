from hashing import pass_hash


# This function reads and extracts hashes from the binary 'hashes' file
def extract_hashes(filename):
    hashes = []
    with open(filename, 'rb') as file:
        current_hash = b""
        while byte := file.read(1):
            if byte == b"\xff":  # 0xff indicates the end of a hash
                hashes.append(current_hash)
                current_hash = b""
            else:
                current_hash += byte
    return hashes


def verify_password(known_password, target_hash):
    hashed_password = pass_hash(known_password)
    return hashed_password == target_hash


def dictionary_attack(hashes, dictionary_file):
    cracked_passwords = {}
    with open(dictionary_file, 'r') as f:
        for word in f:
            word = word.strip()
            hashed_word = pass_hash(word)
            if hashed_word in hashes:
                cracked_passwords[hashed_word] = word
    return cracked_passwords


def map_users_to_passwords(usernames_file, cracked_hashes):
    with open(usernames_file, 'r') as f:
        usernames = [line.strip() for line in f]
    return {usernames[i]: password for i, password in enumerate(cracked_hashes.values())}


def main():
    hashes = extract_hashes("hashes")
    cracked_hashes = dictionary_attack(hashes, "bad_passwords.txt")
    user_passwords = map_users_to_passwords("users.txt", cracked_hashes)
    for user, password in user_passwords.items():
        print(f"User: {user} | Password: {password}")
    print("Cracked Passwords: ")
    print(cracked_hashes)


if __name__ == "__main__":
    main()
