import re
haslo=input("Wprowadź hasło:")
if re.search("[a-z]",haslo)==None:
    print("Hasło nie zawiera litery [a-z]")
elif re.search("[A-Z]",haslo)==None:
    print("Hasło nie zawiera litery [A-Z]")
elif re.search("[0-9]",haslo)==None:
    print("Hasło nie zawiera cyfry [0-9]")
elif re.search("[$#@]",haslo)==None:
    print("Hasło nie zawiera znaku specjalnego [$#@]")
elif len(haslo)<6:
    print("Hasło zawiera mniej niż 6 znaków")
elif len(haslo)>16:
    print("Hasło zawiera więcej niż 16 znaków")
else:
    print("Wpisane hasło jest prawidłowe")
