#Andrew Parker
#Dec 7 2017

dictionary = open('engmix.txt')

n = [0]*22


for word in dictionary:
    length = len(word.strip())
    
    n[length] = n[length] + 1
    
print(n)

i = 0
x = 1
for num in n:
    if i<23:
        print('There are', n[i], 'words with', x,'letters')
    i = i+1
    x = x+1
