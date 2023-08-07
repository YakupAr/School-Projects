## CHECKS FOR VALID FINNISH IBANS

IBAN = input('IBAN: ')

def checker(IBAN):
    
    ## Removes spaces
    IBAN_without_spaces = IBAN.replace(" ", "")
    
    ## Checks the lenght of IBAN, if not 18, returns false.
    if len(IBAN_without_spaces) != 18:
        return False
    
    ## Moves the country code and two-digit verification number to the end of the IBAN
    IBAN_reordered = IBAN_without_spaces[4:] + IBAN_without_spaces[:4]
    
    ## Replaces all the letters to numbers, A = 10, B = 11, ..., Z = 35
    IBAN_numerical = ""
    for character in IBAN_reordered:
        if character.isalpha():
            numerical_value = ord(character.upper()) - ord("A") + 10
            IBAN_numerical += str(numerical_value)
        else:
            IBAN_numerical += character

    ## Calculates the remainder of the IBAN converted to an integer when the number is divided by 97. If 1 = True.
    remainder = int(IBAN_numerical) % 97
    if remainder != 1:
        return False
    else:
        return True

print(checker(IBAN))
