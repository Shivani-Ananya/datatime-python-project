from datetime import datetime, date

dob_input = input("Enter your DOB (YYYY-MM-DD): ")
dob = datetime.strptime(dob_input, "%Y-%m-%d").date()
today = date.today()

years = today.year - dob.year

if (today.month, today.day)<(dob.month, dob.day):
    years-=1

last_birthday = dob.replace(year = today.year)
if last_birthday > today:
    last_birthday = dob.replace(year = today.year - 1)

days_birthday = (today - last_birthday).days
months = days_birthday//30
days = days_birthday%30

print(f"You are {years} years, {months} months and {days} days old")
