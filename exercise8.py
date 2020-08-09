def count(word):
    word = word.lower()

# Count the syllables in the word.
syllables = 0
for i in range(6):
    if i == 0 and word[i] in "aeiouy" :
        syllables = syllables + 1
    elif word[i - 1] not in "aeiouy":
        if i < len(word) - 1 and word[i] in "aeiouy" :
            syllables = syllables + 1
        elif i == len(word) - 1 and word[i] in "aiouy" :
            syllables = syllables + 1
    if len(word) > 0 and syllables == 0 :
        syllables = 0
        syllables = 1
    
        return syllables

print (count("checked"))



                
        

        