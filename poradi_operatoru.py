# Booleovské operátory se nevyhodnocují zleva doprava.
#  Pro booleovské operátory existuje pořadí operací:
#  NOT se vyhodnocuje jako první,
#  AND se vyhodnocuje jako další a
#  OR se vyhodnocuje jako poslední.

name = "John"
age = 17

print(name == "John" or not age > 17)

print(name == "John" and not age == 17)

# TODO: Napište výraz, který se vyhodnotí jako True, pokud je jméno "John" nebo "Jane", kteří jsou starší 16 let, ale mladší 25 let.
print('???')