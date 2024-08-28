# Vokalräkning
VOCAL = ['a','e','i','o','u','y','å','ä','ö']

def vowl_counter(word: str) -> int:
    counter = 0
    for ch in word:
        if ch in VOCAL:
            counter+=1
        else:
            continue
    return counter

def main():
    # Skriv din lösning här nedan. Byt ut "pass" mot din kod.
    word = input('What is the word? ')
    
    print(word, vowl_counter(word.lower()))

if __name__ == "__main__":
    main()
