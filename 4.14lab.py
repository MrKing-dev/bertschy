user_text = input()
text_check = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=/<>?;:[]{}|')
user_test_list = list(user_text)
count = 0
for i in user_test_list:
    if i in text_check:
        count += 1

print(count)