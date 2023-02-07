input_list = []

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

    

if __name__ == '__main__':
    input = input()
    input_list = input.split()
    words, num_times = occurences(input_list)
    for i in words:
        print(i, num_times[words.index(i)])

        
