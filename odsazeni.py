import datetime # Import modulu datetime, který nám umožňuje přístup k dnešnímu datu

# TODO: Opravte příkaz if-else

if datetime.date.today().day < 15:
print("Ještě je začátek měsíce!")
else:
print("Už není začátek měsíce :(")