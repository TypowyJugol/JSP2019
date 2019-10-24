import itertools

x=[[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]

y=list(itertools.chain.from_iterable(x))


print(y)