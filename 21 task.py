unique_words = set()

while True:
    word = input("Word: ")
    
    if word == "":
        break
    
    unique_words.add(word)

print(f"You know {len(unique_words)} unique word(s)!")
