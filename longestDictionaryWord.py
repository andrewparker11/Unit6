#Andrew Parker
#12/6/17
#fileDemo.py - how to read a file

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
