from tabulate import tabulate
import os
import sys


"""Global const"""
DATA = []


# Code adapted from: https://www.101computing.net/python-typing-text-effect/
def clearScreen():
  os.system("clear")


#Code adapted from: https://www.freecodecamp.org/news/python-exit-how-to-use-an-exit-function-in-python-to-stop-a-program/#:~:text=The%20exit()%20function%20in,immediately%20stop%20running%20and%20exit.
def exit_program():
    print("Exiting the program...")
    sys.exit(0)


def start():
    """
    The function expalin how the program it's working and for what it is.
    """
    print("Welcome to Your Salary/Income Calculator!")
    print("The 40/40/20 System:")
    print()
    print("First, enter your income for a month ")
    print("which will be divided as follows:")
    print("-40 percentages - needs ")
    print("-40 percentages - savings/investments")
    print("-20 percentages - living expenses.")
    print()
    print("Example for NEEDS:")
    print("This is your insuarance for the car,")
    print("bills, credits, food and etc.")
    print("The things without you can't live.")
    print()
    print("-Example for SAVINGS/INVESTMENTS:")
    print("this is where you will write the money for")
    print("education, your holiday, investments in stocks and etc.")
    print("Some place where you want to invest.")
    print()
    print("-Example for LIVING EXPENSES:")
    print("here you need to fill your money for")
    print("cigaretes, parties, restaurants and etc.")
    print("Something without you can survive.")
    print()
    print("If the information you want to add doesn't apply")
    print("to any of the columns, just add 0")
    print()
    print("Good Luck!\n")


def get_income():
    """
    The function calculate the sum to be always float, if it's a string it'll be 
    displayed error, if it's less then 4 digits it will print again error message
    """
    while True: 
        try:
            print("Enter your income (at least 4 digits):")
            user_income = input("")
            income = float(user_income)
            clearScreen()
            if income >= 1000:  
                return income
            else:
                print("Income must be at least 4 digits. Please try again.")
        except ValueError:
            print("Invalid data. Please enter a number with at least 4 digits.")


def calculate_income(income):
    """ 
    The def calculate the income in % for needs, savings
    and living
    """
    needs = 0.4 * income
    savings = 0.4 * income
    living = 0.2 * income
    return needs, savings, living


def take_data():
    """
    The function take data from the user.
    Check the inputs if it's validate,
    and pass the data to the paaramethers.
    """
    while True:
        print("Please provide name for the data which you will add...")
        name = input("")
        clearScreen()
        if name.isalpha():
            break
        else:
            print("Invalid data, please add only letters!")
    while True:
        try:
            print("If your expense it is not Needs, then add value - 0")
            print("Enter value for Needs:")
            needs_value = float(input(""))
            clearScreen()
            print("If your expense it is not Savings/Investments, then add value - 0")
            print("Enter new Savings/Investments:")
            savings_value = float(input(""))
            clearScreen()
            print("If your expense it is not Living Expenses, then add value - 0")
            print("Enter new Living Expenses:")
            living_value = float(input(""))
            clearScreen()
            break
        except Exception:
            print("Invalid data, please add only numbers:")
    return name, needs_value, savings_value, living_value 


def calculate_expenses(calculation_needs, calculation_savings, calculation_living, needs_value, savings_value, living_value):
    """ The def subtracts right operand from 
    the left operand and assign the result to left operand.
    And after that return all left operands.
    It will be in use to calculate the end result.
    """
    calculation_needs -= needs_value
    calculation_savings -= savings_value
    calculation_living -= living_value
    return calculation_needs, calculation_savings, calculation_living


def build_table(needs, savings, living, name, needs_value, savings_value, living_value, calculation_needs, calculation_savings, calculation_living):
    """ 
    The function, build a table.
    Give an options to navigate between
    user to see the table with or 
    without calculations, or
    to continue to continue to 
    another function which will 
    provide different options.
    """
    headers = ["Name", "Needs", "Savings/Investments", "Living Expenses"]
    info_income = [["Income", f"${needs}", f"${savings}", f"${living}"]]
    calculation = [["Calculation:", f"${calculation_needs}", f"${calculation_savings}", f"${calculation_living}"]]
    whole_table = info_income + DATA
    whole_table_with_calculation = info_income + DATA + calculation 
    while True:
        try:
            print()
            print("Write 'yes' to see the table without calculations!")
            print("Write 'no' to see the table with calculations.")
            print("Write 'continue' to see another options.")
            show_the_table = input("")
            clearScreen()
            if show_the_table.lower() == 'yes':
                print(tabulate(whole_table, headers=headers, tablefmt="simple"))
            elif show_the_table.lower() == 'no':
                print(tabulate(whole_table_with_calculation, headers=headers, tablefmt="simple"))
            elif show_the_table.lower() == 'continue':
                menu(needs, savings, living, name, needs_value, savings_value, living_value, calculation_needs, calculation_savings, calculation_living)
            else:
                raise ValueError("Invalid input: Please select one of the options (yes/no/continue).\n")
        except ValueError as e:
            print(e)


def menu(needs, savings, living, name, needs_value, savings_value, living_value, calculation_needs, calculation_savings, calculation_living):
    """
    Giving options to the user 
    to navigate between different options.
    """
    while True:
        print("Press '1',if you would like to add more data.")
        print("Press '2', if you would like to see the table.")
        print("Press '3', if you would like to Exit the program.")
        question = input("")
        clearScreen()
        if question.lower() == '1':
            name, needs_value, savings_value, living_value = take_data()
            global DATA
            DATA.append([name, f"${needs_value}", f"${savings_value}", f"${living_value}"])
            calculation_needs, calculation_savings, calculation_living = calculate_expenses(calculation_needs, calculation_savings, calculation_living, needs_value, savings_value, living_value)
        elif question.lower() == '2':
            build_table(needs, savings, living, name, needs_value, savings_value, living_value, calculation_needs, calculation_savings, calculation_living)
        elif question.lower() == '3':
             exit_program()
        else:
            print("Invalid input, please add yes or no values!")
   

def main():
    """ 
    Run all program functions 
    """
    income = get_income()
    needs, savings, living = calculate_income(income)
    calculation_needs, calculation_savings, calculation_living = needs, savings, living
    name, needs_value, savings_value, living_value = take_data()
    global DATA
    DATA.append([name, f"${needs_value}", f"${savings_value}", f"${living_value}"])
    calculation_needs, calculation_savings, calculation_living = calculate_expenses(calculation_needs, calculation_savings, calculation_living, needs_value, savings_value, living_value)
    menu(needs, savings, living, name, needs_value, savings_value, living_value,calculation_needs, calculation_savings, calculation_living)
    
    
start()
main()
 
