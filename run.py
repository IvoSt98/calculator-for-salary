from tabulate import tabulate
import os
import sys
import colorama
from colorama import Back, Fore, Style, init
init(autoreset=True)

"""
Global const
"""
DATA = []


# Code adapted from: https://www.101computing.net/python-typing-text-effect/
def clearScreen():
    os.system("clear")


"""
Code adapted from: https://www.freecodecamp.org/news/python
-exit-how-to-use-an-exit-function-in-python-to-stop-a-program/#:
~:text=The%20exit()%20function%20in,immediately%20stop%20runnin
g%20and%20exit.
"""


def exit_program():
    print("Exiting the program...")
    sys.exit(0)


def start():
    """
    The function explains how the program works and for what it is.
    """
    print(Fore.CYAN + "                       "
          "Welcome to Your Salary/Income Calculator!")
    print(Fore.CYAN + "                               "
          "The 40/40/20 System:")
    print()
    print(Fore.GREEN + "First, enter your income for a month ")
    print(Fore.GREEN + "which will be divided as follows:\n")
    print("     "
          "NEEDS - 40 percent ")
    print("     "
          "SAVINGS/INVESTMENTS - 40 percent")
    print("     "
          "LIVING EXPENSES - 20 percent")
    print()
    print(Fore.GREEN + "Example for NEEDS:\n")
    print("     "
          "This is your insurance for the")
    print("     "
          "car, bills, credits, food, etc.")
    print("     "
          "The things without you can't live.")
    print()
    print(Fore.GREEN + "Example for SAVINGS/INVESTMENTS:\n")
    print("     "
          "This is where you will write the money for")
    print("     "
          "education, your holiday, investments in stocks and etc.")
    print("     "
          "Some place where you want to invest.")
    print()
    print(Fore.GREEN + "Example for LIVING EXPENSES:\n")
    print("     "
          "Here you need to fill your money for")
    print("     "
          "cigarettes, parties, restaurants and etc.")
    print("     "
          "Something without you can survive.")
    print()
    print(Fore.YELLOW + "                   "
          "If the information you want to add doesn't apply")
    print(Fore.YELLOW + "                         "
          "to any of the columns, just add 0.\n")


def get_income():
    """
    The function calculates the sum to be always floating,
    if it's a string it'll be
    displayed error, if it's less than 4 digits
    it will print again an error message.
    """
    while True:
        try:
            print("     "
                  "First enter your income (at least 4 digits):")
            user_income = input("")
            income = float(user_income)
            clearScreen()
            if income >= 1000:
                return income
            else:
                print("Income must be at least 4 digits. Please try again.")
        except ValueError:
            print("Invalid data. Please povide data with at least 4 digits.")


def calculate_income(income):
    """
    The def calculates the income in % for needs, savings
    and living
    """
    needs = 0.4 * income
    savings = 0.4 * income
    living = 0.2 * income
    return needs, savings, living


def take_data():
    """
    The function takes data from the user.
    Check the inputs if it's validated,
    and pass the data to the parameters.
    """
    while True:
        print("")
        print(Fore.CYAN + "                       "
              "Your Name for Expenses!\n")
        print("     "
              "The name must be only alphabetical signs -"
              " without any space!\n")
        print("Enter value for Name:")
        name = input("")
        clearScreen()
        if name.isalpha():
            break
        else:
            print("Invalid data, please add only letters")
            print("without any white space or spacial signs!")
            print("")
            print("Example for data which will be approved:")
            print("food, Party, CarPayment")
            print("")
            print("Example for data which will be not approved:")
            print("Car Payment, sam.pary, Sport-card")
    while True:
        try:
            print("")
            print(Fore.CYAN + "                       "
                  "Your Data for Needs!\n")
            print("     "
                  "If your expense is not Needs, then add - 0\n")
            print("Enter value for Needs:")
            needs_value = float(input(""))
            if needs_value < 0:
                raise ValueError("Please add only positive numbers.")
            clearScreen()
            print("")
            print(Fore.CYAN + "                       "
                  "Your Data for Savings/Inv.!\n")
            print("     "
                  "If your expense is not Savings/Inv., then add - 0\n")
            print("Enter new Savings/Investments:")
            savings_value = float(input(""))
            if savings_value < 0:
                raise ValueError("Please add only positive numbers.")
            clearScreen()
            print("")
            print(Fore.CYAN + "                       "
                  "Your Your Data for Living Expenses!\n")
            print("     "
                  "If your expense is not Living Expenses, then add - 0\n")
            print("Enter new Living Expenses:")
            living_value = float(input(""))
            if living_value < 0:
                raise ValueError("Please add only positive numbers.")
            clearScreen()
            break
        except ValueError as e:
            print(e)
    return name, needs_value, savings_value, living_value


def calculate_expenses(
    calculation_needs, calculation_savings, calculation_living,
    needs_value, savings_value, living_value
):
    """
    The def subtracts the right operand from
    the left operand and assigns the result to the left operand.
    And after that return all left operands.
    It will be used to calculate the result.
    """
    calculation_needs -= needs_value
    calculation_savings -= savings_value
    calculation_living -= living_value
    return calculation_needs, calculation_savings, calculation_living


def build_table(
    needs, savings, living, name,
    needs_value, savings_value, living_value, calculation_needs,
    calculation_savings, calculation_living
):
    """
    The function, build a table.
    Give an option to navigate between
    user to see the table with or
    without calculations, or
    to continue to continue to
    another function which will
    provide different options.
    """
    headers = ["Name", "Needs", "Savings/Investments", "Living Expenses"]
    info_income = [["Income", f"${needs}", f"${savings}", f"${living}"]]
    calculation = [["Calculation:", f"${calculation_needs}",
                    f"${calculation_savings}", f"${calculation_living}"]]
    whole_table = info_income + DATA
    whole_table_with_calculation = info_income + DATA + calculation
    while True:
        try:
            print()
            print(Fore.CYAN + "                       "
                  "Your Table Menu!\n")
            print("            "
                  "Choose one of the following options:")
            print()
            print("     "
                  "1. To see the table without calculations.")
            print("     "
                  "2. To see the table with calculations.")
            print("     "
                  "3. To go back.")
            show_the_table = input("")
            clearScreen()
            if show_the_table == '1':
                print()
                print(Fore.YELLOW + tabulate(whole_table,
                      headers=headers, tablefmt="mixed_outline"))
            elif show_the_table == '2':
                print()
                print(Fore.YELLOW + tabulate(whole_table_with_calculation,
                      headers=headers, tablefmt="mixed_outline"))
            elif show_the_table == '3':
                menu(needs, savings, living, name,
                     needs_value, savings_value, living_value,
                     calculation_needs, calculation_savings,
                     calculation_living)
            else:
                raise ValueError("Please select one of the options (1/2/3).\n")
        except ValueError as e:
            print(e)


def menu(
    needs, savings, living,
    name, needs_value, savings_value,
    living_value, calculation_needs,
    calculation_savings, calculation_living
):
    """
    Giving options to the user
    to navigate between different options.
    """
    while True:
        print()
        print(Fore.CYAN + "                       "
              "Navigation Menu!\n")
        print("            "
              "Choose one of the following options:")
        print()
        print("     "
              "1. To add more data.")
        print("     "
              "2. To see the table.")
        print("     "
              "3. To Exit the program.")
        question = input("")
        clearScreen()
        if question == '1':
            name, needs_value, savings_value, living_value = take_data()
            global DATA
            DATA.append([name, f"${needs_value}",
                        f"${savings_value}", f"${living_value}"])
            calculation_needs,\
                calculation_savings,\
                calculation_living = calculate_expenses(
                                                    calculation_needs,
                                                    calculation_savings,
                                                    calculation_living,
                                                    needs_value,
                                                    savings_value,
                                                    living_value)
        elif question == '2':
            build_table(needs, savings, living, name,
                        needs_value, savings_value, living_value,
                        calculation_needs, calculation_savings,
                        calculation_living)
        elif question == '3':
            exit_program()
        else:
            print("Please select one of the options (1/2/3).\n")


def main():
    """
    Run all program functions
    """
    income = get_income()
    needs, savings, living = calculate_income(income)
    calculation_needs, calculation_savings, \
        calculation_living = needs, savings, living
    name, needs_value, savings_value, living_value = take_data()
    global DATA
    DATA.append([name, f"${needs_value}",
                f"${savings_value}", f"${living_value}"])
    calculation_needs,\
        calculation_savings,\
        calculation_living = calculate_expenses(
                                                calculation_needs,
                                                calculation_savings,
                                                calculation_living,
                                                needs_value,
                                                savings_value,
                                                living_value)
    menu(needs, savings, living, name, needs_value,
         savings_value, living_value, calculation_needs,
         calculation_savings, calculation_living)


if __name__ == '__main__':
    start()
    main()
