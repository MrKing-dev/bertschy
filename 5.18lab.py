def swap_values(user_val1, user_val2):
   user_val1, user_val2 = user_val2, user_val1
   return user_val1, user_val2

if __name__ == '__main__':
    inpA = int(input())
    inpB = int(input())
    inpA, inpB = swap_values(inpA, inpB)
    print(inpA, inpB)