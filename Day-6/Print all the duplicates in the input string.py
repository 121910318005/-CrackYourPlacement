'''
Write an efficient program to print all the duplicates and their counts in the input string 

Method 1: Using hashing
Algorithm: Let input string be “geeksforgeeks” 
1: Construct character count array from the input string.
count[‘e’] = 4 
count[‘g’] = 2 
count[‘k’] = 2 
……
2: Print all the indexes from the constructed array which have values greater than 1.
'''

word = input('Enter string - ')

d=dict()

for i in range(len(word)):
    if word[i] not in d:
        d[word[i]]=1
    else:
        d[word[i]]+=1

for i in d:
    if d[i]>1:
        print(i, d[i])
