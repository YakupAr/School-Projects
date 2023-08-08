## Date checker to check if date is valid
def date_checker(date):
    try:
        year = int(date[4:8])
        month = int(date[2:4])
        day = int(date[:2])
        
        if year < 1 or month < 1 or month > 12 or date < 1:
            return False
        
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
# Check for leap year and adjust February's day count if needed
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            month_days[1] = 29

        if day > month_days[month - 1]:
            return False
        
        return True
    except:
        return False

date = input("Date (DDMMYYYY): ")


# Check if the provided date is valid using the function
if date_checker(date):
    print("True")
else:
    print("False")
