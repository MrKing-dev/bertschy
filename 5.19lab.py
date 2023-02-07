def exact_change(user_total): # 120
    num_dollars = user_total // 100 # 1
    user_total = user_total % 100 # 20
    num_quarters = user_total // 25 # 0
    user_total = user_total % 25 # 20
    num_dimes = user_total // 10 # 2
    user_total = user_total % 10
    num_nickels = user_total // 5
    user_total = user_total % 5
    num_pennies = user_total

    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    dollar_string = "dollars" if num_dollars != 1 else "dollar"
    quarter_string = "quarters" if num_quarters != 1 else "quarter"
    dime_string = "dimes" if num_dimes != 1 else "dime"
    nickel_string = "nickels" if num_nickels != 1 else "nickel"
    penny_string = "pennies" if num_pennies != 1 else "penny"

    if input_val <= 0:
        print("no change")
    else:
        if num_dollars > 0:
            print(f"{num_dollars} {dollar_string}")
        if num_quarters > 0:
            print(f"{num_quarters} {quarter_string}")
        if num_dimes > 0:
            print(f"{num_dimes} {dime_string}")
        if num_nickels > 0:
            print(f"{num_nickels} {nickel_string}")
        if num_pennies > 0:
            print(f"{num_pennies} {penny_string}")