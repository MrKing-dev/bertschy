def replace_words(input_dict, sentence):
    for key, value in input_dict.items():
        sentence = sentence.replace(key, value)
    return sentence

word_dict_input = input()
#word_dict = dict(zip(word_dict_input.split()[::2], word_dict_input.split()[1::2]))
word_list = word_dict_input.split()
word_dict = {}
for i in range(0, len(word_list), 2):
    word_dict[word_list[i]] = word_list[i + 1]

sentence = input()

print(replace_words(word_dict, sentence))

