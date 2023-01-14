import random
import sys

def menu()->None:
    print("-- Password Generator --")
    print("Choose option:")
    print("1: generate password")
    print("2: exit the program")
    inp = input("Your choice:")
    if inp == "1":
        gen_pass_menu()
    elif inp == "2":
        print("Bye!")
        sys.exit()
    else:
        print("Please enter a correct value\n")
        menu()

def gen_pass_menu()->None:
    length = int(input("Provide password length: "))
    upper = input("Use upper case letters (y/N): ").lower()
    digits = input("Use digits (y/N): ").lower()
    special = input("Use special characters (y/N): ").lower()
    print(f"\nGenerated password: {gen_pass(length, upper, digits, special)}")

def gen_pass(length:int, upper:str, digit:str, special:str)->str:
    alpha = "abcdefghijklmnopqrstuxyz"
    alpha_big = "ABCDEFGHIJKLMNOPQRSTUXYZ"
    digits = "0123456789"
    specials = "^!\"§$%&/()=?+*-:,;_#"

    useables = alpha
    if upper == "y":
        useables += alpha_big
    if digit == "y":
        useables += digits
    if special == "y":
        useables += specials
    
    password = ""
    for _ in range(length):
        password += random.choice(useables)

    return password





if __name__=="__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\n\nBye!")
        sys.exit()