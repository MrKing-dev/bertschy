import csv

#initilize variables
input_list = []

#function to count occurences of words
def occurences (words):
    num_times = []
    count = 0
    for i in words:
        for j in words:
            if i == j:
                count += 1
        num_times.append(count)
        count = 0
    return words, num_times

#main 
file = open('input1.csv', 'r') #open file
data = list(csv.reader(file, delimiter=',')) #read file
file.close() #close file
for row in data: #loop through rows
    for i in row: #loop through items in row
        input_list.append(i) #add items to list
    
words, num_times = occurences(input_list) #call function, assign return values to variables
for i in words: #loop through words
    print(i, num_times[words.index(i)]) #print word and number of times it appears