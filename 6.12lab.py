input_list = []

def calculate (list):
    average = sum(list) / len(list)
    average = int(average)
    max = 0
    for i in list:
        if i > max:
            max = i
    return average, max

if __name__ == "__main__":
    input = input("Enter any number of numbers: ")
    input_list = input.split()
    input_list = [int(i) for i in input_list]
    output = calculate(input_list)
    print(f"{output[0]} {output[1]}")
    