import os 

def read_file(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]
        return data
        
def output_keys_file(data):
    output_dict = {}
    for line in range(0, len(data), 2):
        if data[line] in output_dict:
            output_dict[data[line]] += '; ' + data[line+1]
        else:
            output_dict[data[line]] = data[line+1]
    print(output_dict)
    output_keys = open('output_keys.txt', 'w')
    for key, value in sorted(output_dict.items()):
        output_keys.write(key + ': ' + value + '\n')
    output_keys.close()

def output_values_file(data):
    output_dict = {}
    for line in range(0, len(data), 2):
        output_dict[data[line]] = data[line+1]

    def value_sort(item):
        return item[1]

    output_titles = open('output_titles.txt', 'w')
    for key, value in sorted(output_dict.items(), key=value_sort):
        output_titles.write(value + '\n')
    output_titles.close()

if 'file1.txt' in os.listdir():
    output_keys_file(read_file('file1.txt'))
    output_values_file(read_file('file1.txt'))

elif 'file2.txt' in os.listdir():
    output_keys_file(read_file('file2.txt'))
    output_values_file(read_file('file2.txt'))

elif 'file3.txt' in os.listdir():
    output_keys_file(read_file('file3.txt'))
    output_values_file(read_file('file3.txt'))

else:
    print('No files found')

