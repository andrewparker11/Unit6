#Andrew Parker
#Dec. 13, 2017
#quiz6

#Program 1 
dictionary = open('engmix.txt')

words = []

for line in dictionary:
    words.append(line.strip())

for word in words:
    if word.count('c') == 3:
        if word.count('p') == 2:
            print(word,'have the letter c three times and the letter p two times)



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
"""