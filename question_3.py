import datetime

a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

word = "6800923757255865070000705685527573290086"
print(palindrome(word))

