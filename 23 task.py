word1, word2 = input("Enter words: ").split()

w1 = word1.lower()
w2 = word2.lower()

def is_super_anagram(w1, w2):
    
    if w1[0] != w2[0] or w1[-1] != w2[-1]:
        return False
    
    return sorted(w1) == sorted(w2)

if is_super_anagram(w1, w2):
    print("Super Anagram!")
else:
    print("Huh?")
