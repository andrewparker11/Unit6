#Andrew Parker


dictionary = open('engmix.txt')

i = 0
x = 'b'
for word in dictionary:
    length = len(word)
    if length > i:
        i = length
        x = word

print(i)
print(x)
