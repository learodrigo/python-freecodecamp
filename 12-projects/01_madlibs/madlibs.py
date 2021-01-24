# # string concat
# # suppose we want to creat a str that says "subscribte to _______"
# youtuber = "free Code Camp"
#
# # a few ways to do this
# print("Subscribe to", youtuber)
# print("Subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjetive: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")


madlibs = f"Computer programming is so {adj}! It makes me so excited all the time because I love to {verb1}." \
          f"Stay hydrated and {verb2} like you're {famous_person}!"

print(madlibs)
