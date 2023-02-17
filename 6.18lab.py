# Read the name of the input file
input_file = input("Enter the name of the input file: ")

# Read the contents of the input file into a list
with open(input_file, "r") as f:
    lines = f.readlines()

# Create a dictionary with number of seasons as keys and a list of TV shows as values
d = {}
for i in range(0, len(lines), 2):
    seasons = int(lines[i].strip())
    show = lines[i+1].strip()
    if seasons in d:
        d[seasons].append(show)
    else:
        d[seasons] = [show]

# Sort the dictionary by keys
d_keys = dict(sorted(d.items()))

# Write the sorted dictionary to a file named output_keys.txt
with open("output_keys.txt", "w") as f:
    for key, value in d_keys.items():
        f.write(str(key) + ": " + "; ".join(value) + "\n")

# Sort the dictionary by values
d_values = {key: sorted(value) for key, value in d.items()}
sorted_d_values = dict(sorted(d_values.items(), key=lambda item: item[1]))

# Write the sorted values to a file named output_titles.txt
with open("output_titles.txt", "w") as f:
    for value in sorted_d_values.values():
        for show in value:
            f.write(show + "\n")
