input_list = []

def nonneg (list):
    output = []
    for i in list:
        if i >= 0:
            output.append(i)
    output.sort()
    return output

if __name__ == '__main__':
    input = input("Enter any number of numbers: ")
    input_list = input.split()
    input_list = [int(i) for i in input_list]
    for i in nonneg(input_list):
        print(i, end=" ")