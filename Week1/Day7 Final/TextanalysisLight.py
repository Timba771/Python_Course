
text = input("Enter a random text")

print("How long", len(text.replace(" ", "")))
print("How many words? ", len(text.split(" ")))
print("How many e`s: ", (text.lower()).count("e"))