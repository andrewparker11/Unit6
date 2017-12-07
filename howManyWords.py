#Andrew Parker

dictionary = open('engmix.txt')

n = [0]*22

i = 1
x = 1
for word in dictionary:
    length = len(word)
    
    n[length] = n[length] + 1
    
print(n)


