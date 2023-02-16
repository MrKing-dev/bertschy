import csv

#initilize variables
input_list = []

#function to count occurences of words
def occurences (words):
    word_dict = {}
    count = 0
    for i in words:
        for j in words:
            if i == j:
                count += 1
                word_dict[i] = count
        count = 0
    return word_dict

#main 
file = open('input1.csv', 'r') #open file
data = list(csv.reader(file, delimiter=',')) #read file
file.close() #close file
for row in data: #loop through rows
    for i in row: #loop through items in row
        input_list.append(i) #add items to list
    
words = occurences(input_list) #call function, assign return values to variables
for i in words: #loop through words
    print(i, words[i]) #print word and number of times it appears