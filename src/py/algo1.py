year = int(input("Enter a year: "))
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  
            else:
                return False 
        else:
            return True 
    else:
        return False 



while True:
    if is_leap_year(year):
        print(year, "is a leap year.")
        break
    else:
        print(year, "is not a leap year.")
    year = int(input("Enter a year: ")) 
        


