# Složené příkazy v jazyce Python obsahují(skupiny) jiných příkazů; určitým způsobem ovlivňují nebo řídí provádění těchto jiných příkazů.

# Asi nejznámějším typem příkazu je příkaz if. Klíčové slovo if se používá k vytvoření podmíněného příkazu, který po kontrole, zda je jeho
# výraz True, provede nějaký zadaný kód. Python používá k definování bloků kódu odsazení:

if value > 1000:
    # Odsazený blok: print("Je to velké číslo!") # Odsazený blok
    a += 1  # Odsazený blok

print("Mimo blok!")

# Blok kódu začíná odsazením a končí prvním neodsazeným řádkem. Velikost odsazení musí být v celém bloku konzistentní.
# Obecně se pro odsazení používají čtyři bílé znaky nebo jednotlivé tabulátory. Nesprávné odsazení způsobí chybu IndentationError.


name = "John"
age = 17

if name == "John" or age == 17:   # Zkontroluje, zda je jméno "John" nebo věk 17 let. Pokud ano, vytiskne další 2 řádky.
    print("name is John")
    print("John is 17 years old")

tasks = ["task1", "task2"]    # Vytvoření nového seznamu

# TODO: Napište příkaz if s podmínkou, která zkontroluje, zda je seznam `tasks` prázdný.
    print("Not an empty list!")

tasks.clear()  # Vyprázdnění seznamu

# TODO: Zkontrolujte, zda je seznam nyní prázdný, a pokud ano, vypište 'Now empty!'
