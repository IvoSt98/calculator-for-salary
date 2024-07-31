from tabulate import tabulate

"""Global storage"""
data = []

def start():

    """ 
    The function expalin how the program it's working and for what it is.
    """
   
    print("     Welcome to Your Salary/Income Calculator!\n     ")
    print("     The 40/40/20 System:\n      ")
    print(" First, enter your income for a month, which will be divided as follows: ")
    print(" 40 percentages - needs, 40 percentages - savings/investments, and 20 percentages - living expenses.\n   ")
    print("-Example for NEEDS: this is your insuarance for the car, bills, credits, food and etc. The things without you can't live. ")
    print("-Example for SAVINGS/INVESTMENTS: this is where you will write the money for education, for your holiday, investments in stocks and etc.")
    print("-Example for LIVING EXPENSES: here you need to fill your money for cigaretes, parties, restaurants and etc. Something without you can survive\n")
    print(" Next, add your expenses by selecting a category and entering the purpose and amount. ")
    print(" In the end, you'll know if you're managing your finances well.\n ")
    print("     Good Luck!\n        ")

def get_income():
    
    """ 
    The function calculate the sum to be always float, if it's a string it'll be 
    displayed error, if it's less then 4 digits it will print again error message
    """

    while True: 
        try:
            user_income = input("Enter your income (at least 4 digits): ")
            income = float(user_income)
            if income >= 1000:  
                return income
            else:
                print("Income must be at least 4 digits. Please try again.")
        except ValueError:
            print("Invalid data. Please enter a number with at least 4 digits.")

def calculate_income(income):

    """ 
    The def calculate the month income in % for needs, savings
    and living
    """

    needs = 0.4 * income
    savings = 0.4 * income
    living = 0.2 * income
    return needs, savings, living

def build_table(needs, savings, living, name, needs_value, savings_value, living_value):
    """ 
    The function, build a table with tabulate.
    Print first the headers. After that the income.
    And the last the values for name, needs, savings and living.
    """

    headers = ["Name", "Needs", "Savings/Investments", "Living Expenses"]
    info_income = [["-", f"${needs}", f"${savings}", f"${living}"]]
    table= [[f"{name}", f"{needs_value}",f"{savings_value}",f"{ living_value}"]]
    data.append(table[0])
    whole_table= info_income + data 
    try:
        show_the_table = input("Do you want to see the table?) yes/no: ")
        if show_the_table.lower() == 'yes':
            print(tabulate(whole_table, headers=headers, tablefmt="simple"))
        elif show_the_table.lower() == 'no':
            print()
        else:
            raise ValueError("Invalid input: Please select one of the options (yes/no).\n")
    except ValueError as e:
            print(e)
      
def take_data():
    """
    The function take data from the user.
    Check the inputs if it's validate.
    """
    while True:
        name = input("Enter new name: ")
        if name.isalpha():
            break
        else:
            print("Invalid data, please add only letters!")
    while True:
        try:
            print("If your expense it is not Needs, then add value - 0")
            needs_value = float(input(f"Enter value for Needs: "))
            break
        except:
            print("Invalid data, please add only numbers:")
    while True:
        try:
            print("If your expense it is not Savings/Investments, then add value - 0")
            savings_value = float(input(f"Enter new Savings/Investments: "))
            break
        except:
            print("Invalid data, please add only numbers:")
    while True:
        try:
            print("If your expense it is not Living Expenses, then add value - 0")
            living_value = float(input(f"Enter new Living Expenses: "))
            break
        except:
            print("Invalid data, please add only numbers:")

    return name, needs_value, savings_value, living_value 
    
def main():
    income = get_income()
    needs, savings, living = calculate_income(income)
    name, needs_value, savings_value, living_value = take_data()
    build_table(needs, savings, living, name, needs_value, savings_value, living_value)

    while True:
        question = input("Do you want to continue with adding data? (yes/no):\n")
        if  question.lower() == 'yes':
            name, needs_value, savings_value, living_value = take_data()
            build_table(needs, savings, living, name, needs_value, savings_value, living_value )
        elif question.lower() == 'no':
            break
        else:
            print("Invalid input, please add yes or no values!")
   
if __name__ == "__main__":
    start()
    main()
 
