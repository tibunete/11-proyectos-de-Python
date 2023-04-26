def is_palindrome(word):
    return word == word[::-1]

words = []
for i in range(5):
    word = input(f"Ingrese la palabra #{i+1}: ")
    words.append(word)

palindromes = []
for word in words:
    if is_palindrome(word):
        palindromes.append(word)
if palindromes:
    print(f"Las siguientes palabras son palíndromos: {', '.join(palindromes)}")
else:
    print("No se encontraron palíndromos.")
