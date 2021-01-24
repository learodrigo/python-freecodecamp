lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Jim", "Oscar", "Leandro", "Toby"]
friends.extend(lucky_numbers)
friends.insert(1, "Kelly")
friends.remove("Jim")
friends.append("Jim")
f_pop = friends.pop()

print()
print(friends)
print()
print(f_pop)
print()
print(friends.index("Leandro"))
print()
print(friends.count("Jim"))

print()
lucky_numbers.reverse()
print(lucky_numbers)

lucky_num_2 = lucky_numbers.copy()
lucky_num_2.remove(4)
print()
print(lucky_num_2)
