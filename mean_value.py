# Medelvärde
def average_value(values: str):
    filtered_values = []
    number_string = ''
    for ch in range(len(values)):
        
        if values[ch] == '' or values[ch] == ',':
            filtered_values.append(number_string)
            number_string = ''
            continue
        
        number_string += values[ch]
    
    integer_values = [int(num) for num in filtered_values]
    print(filtered_values)
    print(integer_values)
    return sum(integer_values)/len(integer_values)
    
    
def main():
    # Skriv din lösning här nedan. Byt ut "pass" mot din kod.
    values = '1, -2, 3, 7, -5' #input('What are the values? ')
    print(average_value(values))

if __name__ == "__main__":
    main()
