from collections import Counter
a="sssaaabbb"
my_counter=Counter(a)
print(my_counter)
print(my_counter.values())
print(my_counter.items())
print(my_counter.most_common(1))
print(my_counter.most_common(1)[0][0])
#most common element
print(my_counter.most_common(1)[0][1])
#most common element count
print(list(my_counter.elements()))

