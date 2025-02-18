def days_since_birthday():
    birthday = input("Enter your birthday (DD-MM-YYYY): ")
    birth_year = int(birthday.split("-")[2])
    current_year = int(input("Enter the current year: "))
    whole_years = current_year - birth_year - 1
    days_passed = whole_years * 365
    return days_passed

print(days_since_birthday())
