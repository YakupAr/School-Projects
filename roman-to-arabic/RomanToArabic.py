def roman_to_arabic(roman):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    arabic = 0
    prev_value = 0
    
    # Loop through the Roman numeral characters in reverse order
    for symbol in reversed(roman):
        value = roman_numerals[symbol]
        if value >= prev_value:
            arabic += value
        else:
            arabic -= value
        prev_value = value
    
    return arabic

def arabic_to_roman(arabic):
    arabic_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    
    roman = ''
    
    # Loop through the Arabic numeral values in descending order
    for value, symbol in arabic_numerals.items():
        while arabic >= value:
            roman += symbol
            arabic -= value
    
    return roman

def main():
    while True:
        print("1. Convert Roman to Arabic")
        print("2. Convert Arabic to Roman")
        print("3. Quit")
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            roman = input("Enter a Roman numeral: ")
            arabic = roman_to_arabic(roman)
            print(f"Arabic numeral: {arabic}")
        elif choice == 2:
            arabic = int(input("Enter an Arabic numeral: "))
            roman = arabic_to_roman(arabic)
            print(f"Roman numeral: {roman}")
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
