import hashlib
import json

# Lire les mots de passe existants à partir du fichier passwords.json
try:
    with open('passwords.json', 'r') as f:
        passwords = json.load(f)

except:
    # dictionnaire vide pour stocker les mots de pass
    passwords = {}

# Boucle infinie pour demander les mots de passe à l'utilisateur
while True:

    # Demander à l'utilisateur de choisir un mot de passe
    password = input("Choisissez un mot de passe: ")
    # Vérifier si le mot de passe est suffisamment long (8 caractères ou plus)
    if len(password) < 8:  # Vérifier si le mot de passe est suffisamment long (8 caractères ou plus)
        print("Le mot de passe doit contenir au moins 8 caractères.")

    # Verifier si le mot de passe contient au moins une lettre minuscule
    elif not any(c in "abcdefghijklmnopqrstuvwxyz" for c in password):
        print("Le mot de passe doit contenir au moins une lettre minuscule. ")

    # Vérifier si le mot de passe contient au moins une lettre majuscule
    elif not any(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in password):
        print("Le mot de passe doit contenir au moins une lettre  majuscule.")

    # Vérifier si le mot de passe contient au moins un chiffre
    elif not any(c in "0123456789" for c in password):
        print("Le mot de passe doit contenir au moins un chiffre.")

    # Vérifier si le mot de passe contient au moins un caractère spécial (!, @, #, $, %, ^, &, *)
    elif not any(c in "!@#$%^&*" for c in password):
        print("Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")

    else:
        print("Mot de passe valide!")
        # Crypter le mot de passe en utilisant l'algorithme SHA-256
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        # vérifier si le mot de passe existe déjà dans les valeurs du dictionnaire
        if password in passwords:
            print("Ce mot de passe existe déjà.")
        else:
            # Ajouter le mot de passe et le mot de passe crypté au dictionnaire
            passwords[password] = [hashed_password]
            print("mot de pass: ", password)
            print("Mot de passe crypte: ", hashed_password)
        # Demander à l'utilisateur s'il souhaite entrer un autre mot de passe
        repeat = input("Voulez-vous entrer un autre mot de passe? (o/n)")
        if repeat == 'n':
            break

# Enregistrer les mots de passe dans un fichier JSON
with open('passwords.json', 'w') as f:
    # l'option separators et l'option indent pour séparer les différents mots de passe enregistrés dans le fichier JSON
    json.dump(passwords, f, separators=(', ', ': '), indent=4)
