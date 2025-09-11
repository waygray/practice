import sys

class calc:
    def __init__(self):
        self.display = 0

    def show_display(self):
        return self.display

    def add(self,a,b):
        self.display = a+b
        return self.display

    def subtract(self,a,b):
        self.display = a-b
        return self.display

    def multiply(self,a,b):
        self.display = a*b
        return self.display

    def divide(self,a,b):
        if b == 0:
            raise ZeroDivisionError("Make Sure Neither Number is 0 Please!")
        self.display = a / b
        return self.display

def user_menu():
    return(["What would you like to do?","1)Add","2)Subtract","3)Divide","4)Multiply","5)Quit"])

def getUserChoice(string):
    while True:
        user_input = input(string)
        user_input = user_input.strip()
        if user_input:
            break
    return user_input

def getAandB():
    while True:
        try:
            first_num = getUserChoice("Please enter the first number: ")
            a = float(first_num)
            break
        except ValueError:
            print("Please enter a valid number!")

    while True:
        try:
            second_num = getUserChoice("Please enter the second number: ")
            b = float(second_num)
            break
        except ValueError:
            print("Please enter a valid number!")

    return (a,b)





def userOption():
    c = calc()
    user_input = getUserChoice("What would you like to do?")
    user_input = user_input.strip().lower()
    if user_input == "1":
        print(c.add(*getAandB()))
    elif user_input == "2":
        print(c.subtract(*getAandB()))
    elif user_input == "3":
        print(c.divide(*getAandB()))
    elif user_input == "4":
        print(c.multiply(*getAandB()))
    elif user_input == "5":
        raise sys.exit()
    else:
        print("Please enter one of the 5 options!")

def main():
    c = calc()
    print("Welcome to Calculator")

    while True:
        menu_items = user_menu()
        for item in menu_items:
            print(item)
        result = userOption()

        if result == 5:
            print("Thanks for using the calculator")
            raise sys.exit()

    print(f"Current display: {c.show_display()}")
    print("-" * 30)


if __name__ == '__main__':
    main()

#
