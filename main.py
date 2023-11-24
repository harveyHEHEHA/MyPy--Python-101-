import datetime

userIN = input("Enter your birth year: ")
today = datetime.date.today()
year = today.year
result = year - int(userIN)
print("Your birth year is", userIN, "making you", result, "years old.")
