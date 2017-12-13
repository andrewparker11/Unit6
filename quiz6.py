#Andrew Parker
#Dec. 13, 2017
#quiz6

"""

#Program 4
dictionary = open('engmix.txt')
letter = int(input('Enter a letter: ')

words = []

for line in dictionary:
    words.append(line.strip())
    
for word in words:
    if word :
        if word.count('p') == 2:
            print(word)



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

"""




#Program 1 
dictionary = open('engmix.txt')

words = []

for line in dictionary:
    words.append(line.strip())

for word in words:
    if word.count('c') == 3:
        if word.count('p') == 2:
            print(word)


"""
#Program 2 
dictionary = open('engmix.txt')

words = []

for line in dictionary:
    words.append(line.strip())

for word in words:
    if len(word) > 0:
        if word[0] == 'r':
            print(word)
        

"""


#Program 3
dictionary = open('engmix.txt')

number = int(input('Enter a number: '))

words = [] 

for line in dictionary:
    words.append(line.strip())

for word in words:
    if len(word) == number:
        print(word)
        break 




#Program 5 

dictionary = open('engmix.txt')

words = []

for line in dictionary:
    words.append(line.strip())
    
print(words[len(words)/2])