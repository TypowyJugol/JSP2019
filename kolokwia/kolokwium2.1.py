plik = open("text_na_zajecia.txt", "r")
str = (plik.read())
str = str.lower()
alphabet = "qwertyuiopasdfghjklzxcvbnm"
def check_freq(str):
    freq = {}
    for c in str:
        if c in alphabet:
            freq[c] = str.count(c)
    return freq

print(check_freq(str))

