#Andrew Parker
#12/6/17
#fileDemo.py - how to read a file

dictionary = open('engmix.txt')

i = 0
y = 'b'
for word in dictionary:
    length = len(word)
    if length > i:
        i = length
        y = word

print(i)
print(y)
