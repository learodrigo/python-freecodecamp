char_name = "Bla bla"
char_age = "35"

print("There was a man named " + char_name + ",")
print("he was " + char_age + " yo.")

char_name = "Mike"
char_age = "353"
char_age = "353"

print("He really liked his name " + char_name)
print("but didn't like being " + char_age)

print("")

random_text = 'Line\nnew\n"quotes"\nand\\and'

print(random_text.upper() + "\n" + char_name.lower() + " cool")
print("")
print(random_text.upper().isupper())
print("")
print(random_text + " has :" + str(len(random_text)) + " chars")
print("")
print(random_text[0])

my_phrase = "This will return the index of my letter G in my phrase"

print(my_phrase.index("G"))
print(my_phrase.replace("G", "another letter"))
