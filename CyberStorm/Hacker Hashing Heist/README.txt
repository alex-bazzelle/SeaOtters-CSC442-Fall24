
Reversible Hashing

The setup

John Hackerman set up a website one day. He knew that it was dangerous to store users' actual passwords on his server, as any data breach would mean that all of his users' passwords would be released in plaintext. John thought he would be clever and implement his own hashing function and store the hashed versions of the passwords for authentication purposes.

Unfortunately, John's website was indeed hacked, and all of his users' hashed passwords were released!

Your are a black hat hacker. Your job is to crack the passwords given to you. You are given a file containing each username line-by-line entitled, "users.txt". You are also given a file simply titled, "hashes" which is a binary file containing hashed passwords each signalled by a stop byte of 0xff. Your username was "Jane_Doe" and your password was "password". Finally, you're given the algorithm that John Hackerman used to hash passwords in the file "hashing.py".

Hints:

- For some (but not all) of the passwords, you may find the contents of the file "bad_passwords.txt" to be useful. http://www.whatsmypass.com/the-top-500-worst-passwords-of-all-time
- John didn't include any restrictions for what passwords could be, as long as they were between 1 and 12 characters 
long and ascii encoded. 
- The admin password is the most valuable, but is also nearly impossible to brute force.
- John didn't know much about cryptography, so his hashing function might be missing some of the characteristics of 
a good cryptographic hashing function.
- You are guaranteed, though, that no two different passwords will give the same hash.