# Palindrome
def is_palindrom(word: str) -> bool:
    return word == word[::-1]

def main():
    # Skriv din lösning här nedan. Byt ut "pass" mot din kod.
    word = input('Give the word ').lower()
    print(is_palindrom(word))

if __name__ == "__main__":
    main()
