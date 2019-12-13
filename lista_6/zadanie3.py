#znalezione na oeis
#https://oeis.org/search?q=1%2C11%2C21%2C1211%2C111221&language=polish&go=Wyszukaj

import re

def lookandsay(limit, sequence = 1):

    if limit > 1:

        return lookandsay(limit-1, "".join([str(len(match.group()))+match.group()[0] for matchNum, match in enumerate(re.finditer(r"(\w)\1*", str(sequence)))]))

    else:

        return sequence

n=int(input("Podaj n-ty wyraz ciągu: "))
print(lookandsay(n))