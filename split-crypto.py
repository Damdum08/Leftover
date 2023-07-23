# Description:
# Ce script permet de séparer les différentes valeurs (appartenant à un fichier) comprises entre un caractère spécial entré par l'utilisateur.
# Et demande quelle colonne veut il extraire et l'envoyer dans un fichier afin de pouvoir le traiter.
# Utilisation : dans mon cours de cryptographie afin de déchiffrer les mots de passe d'un fichier.

# Description:
# This script allows to separate the different values (belonging to a file) located between a special character entered by the user.
# It also asks which column the user wants to extract and send to a file for further processing.
# Usage: in my cryptography class to decrypt passwords from a file.

file_to_read = input("File to read: ")

try:
    file_content = open(file_to_read, "r")
except FileNotFoundError:
    print("File not found")
    exit()

carac = input("character to remove: ")

print("\n!!!!!! 0: first column !!!!!!\n")
column_choice = int(input("Column to extract (0-indexed): "))
output_file = input("Name output file: ") 

i = 0  # compteur de ligne

with open(output_file, "w") as file_password:
    for line in file_content:
        line = line.strip()
        line_values = line.split(carac)

        if column_choice < len(line_values):
            value_to_extract = line_values[column_choice]
            file_password.write(value_to_extract + "\n")
        else:
            print(f"The column {column_choice} doesn't exist in : {line}")

        i += 1

file_content.close()
