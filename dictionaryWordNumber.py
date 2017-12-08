#Andrew Parker
#Dec. 8, 2017
#Dictionary Word Number

dictionary = open('engmix.txt')

num = int(input('Enter a number: ')

word = []

for line in dictionary:
    word.append(line.strip())
    
print(word[num])