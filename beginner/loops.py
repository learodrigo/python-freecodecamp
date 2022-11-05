i = 0
while i <= 10:
    print(i, "via while")
    i += 1

print()

friends = ["Leandro", "Rodrigo", "Karen"]
for f in friends:
    print(f, "for in")

print()

for f in range(len(friends)):
    print(friends[f], "for")

print()

for letter in "Hello there!":
    print(letter, "for with string")

print()

for i in range(10):
    print(i, "for with range")

print()

for i in range(5, 10):
    print(i, "for with range 2")
