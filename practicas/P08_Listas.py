# Convierta la lista  a=[1,[2,[3,4]],5] en [1,[2,[3,4],[6,7]],5]
a=[1,[2,[3,4]],5]
print(a)
a[1].insert(2, [6,7])
print(a)