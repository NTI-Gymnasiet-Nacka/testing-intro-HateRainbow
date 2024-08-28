# Gradkonverterare
def farenheit_to_celsius(x: float) -> float:
    return x*9/5+32

def main():
    # Skriv din lösning här nedan. Byt ut "pass" mot din kod.
    farenheit_temp = float(input('What is the temperature in °F? '))
    
    print(f'The temperature in °C is {farenheit_to_celsius(farenheit_temp)}')

if __name__ == "__main__":
    main()
    