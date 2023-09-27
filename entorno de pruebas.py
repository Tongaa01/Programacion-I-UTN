alpha = ["_"]
word = "albatroz"
new = list(alpha*len(word))
letter = "a"
print(new)
for i in range(0, len(word), 1):
    if word[i]==letter:
        new[i] = letter
print("")
new = "".join(new)


print(new)



    
