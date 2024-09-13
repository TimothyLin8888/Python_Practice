print("How many r's are in the word 'strawberry'")
word = 'strawberry'
counter = 0
for n in word:
    if n == 'r':
        counter+=1
print("There are {:d} r's in strawberry".format(counter))