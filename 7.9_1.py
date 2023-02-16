import os 

output_dict = {}

if 'file1.txt' in os.listdir():
    with open('file1.txt', 'r') as file:
        #data = file.read().splitlines()
        data = file.readlines()
        data = [line.rstrip() for line in data]
        for line in range(0, len(data),2):
            if data[line] in output_dict:
                output_dict[data[line]] += '; ' + data[line+1]
        else:
            output_dict[data[line]] = data[line+1]

elif 'file2.txt' in os.listdir():
    with open('file2.txt', 'r') as file:
        #data = file.read().splitlines()
        data = file.readlines()
        data = [line.rstrip() for line in data]
        for line in range(0, len(data),2):
            if data[line] in output_dict:
                output_dict[data[line]] += '; ' + data[line+1]
            else:
                output_dict[data[line]] = data[line+1]

elif 'file3.txt' in os.listdir():
    with open('file3.txt', 'r') as file:
        #data = file.read().splitlines()
        data = file.readlines()
        data = [line.rstrip() for line in data]
        for line in range(0, len(data),2):
            if data[line] in output_dict:
                output_dict[data[line]] += '; ' + data[line+1]
            else:
                output_dict[data[line]] = data[line+1]

else:
    print('No files found')

    



output_keys = open('output_keys.txt', 'w')
for key, value in sorted(output_dict.items()):
    output_keys.write(key + ': ' + value + '\n')
output_keys.close()

def value_sort(item):
    return item[1]

output_titles = open('output_titles.txt', 'w')
for key, value in sorted(output_dict.items(), key=value_sort):
    output_titles.write(value + '\n')
output_titles.close()

#print(output_dict)