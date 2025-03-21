def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""

    for char in text:
        if char not in vowels:
            result += char

    return result

user_input = input("Bir metin girin: ")

output = remove_vowels(user_input)

print("Ünlüler atlandı:", output)

