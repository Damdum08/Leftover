import hashlib
import sys

# Read the hashed passwords and store them in a list
hashed_passwords = [] # Create an empty list
with open("hash_password.txt", "r") as file: # Open the file for reading
    hashed_passwords = [line.strip() for line in file] # Read each line and add it to the list (without the \n). Remove the .strip() if you want to keep the \n.
    # .strip() removes the \n at the end of each line or spaces at the beginning and end of each line

# Read the list of possible words and store them in a list
possible_passwords = []
with open("rockyou.txt", "r", encoding='latin-1') as file: 
    possible_passwords = [line.strip() for line in file]

# List to store the cracked passwords
cracked_passwords = []

# Counter to keep track of the number of tested words
tested_count = 0

# Set the length of the loading bar
total_passwords = len(possible_passwords)
bar_length = 40

for possible_password in possible_passwords:
    hashed_possible_password = hashlib.md5(possible_password.encode()).hexdigest()
    #.encode converts the string 'possible_password' to bytes. It's necessary to use the hashlib (for the hash)
    #.hexdigest() converts the hash to a string
    if hashed_possible_password in hashed_passwords: # If the hash is in the list of hashed passwords
        cracked_passwords.append(possible_password) # Add the hash and the password to the list
        print(f"\nHash cassé : {hashed_possible_password}")

    # Chatgpt area
    # Mettre à jour le compteur et afficher la barre de chargement
    tested_count += 1
    progress = int(bar_length * tested_count / total_passwords)
    bar = "[" + "=" * progress + " " * (bar_length - progress) + "]"
    sys.stdout.write(f"\rProgression : {bar} {tested_count}/{total_passwords}")
    sys.stdout.flush()

# Write the cracked passwords to a file
with open("passwords_broke.txt", "w") as file:
    for password in cracked_passwords:
        file.write(f"Mot de passe : {password}")

print("\nCassage des hash terminé.")

