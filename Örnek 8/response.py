import validators

# Kullanıcıdan e-posta adresi al
email = input("Bir e-posta adresi girin: ")

# E-posta doğrulaması yap
if validators.email(email):
    print("Valid")
else:
    print("Invalid")
