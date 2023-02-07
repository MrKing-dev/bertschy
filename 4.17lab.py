while True:
    user_input = input().split()
    user_word = user_input[0]
    if user_word == 'quit':
        break
    user_num = user_input[1]
    print(f'Coding {user_num} {user_word} a day keeps IT away!')
