# Salary/Income Calculator

[The live project can be viewed here](https://calculator-for-salary-6e04ba66476c.herokuapp.com/)

The Salary/Income Calculator is an open-source, interactive command-line utility tailored for efficient income and expense management. It applies the 40/40/20 rule, a guiding principle in wealth creation. According to this rule, 40% of your gross income should be allocated for taxes/needs, another 40% should be saved/invested, and the remaining 20% should cover living expenses. This tool simplifies financial tracking, ensuring users can easily implement this strategy to optimize their savings and budgeting efforts.

## Table of Contents
* [User Stories](#user-stories)
* [Features](#features)
* [Future Features](#future-features)
* [Flowchart](#flowchart)
* [Technology Used](#technology-used)
   + [Languages Used](#languages-used)
   + [Libraries and Programs Used](#libraries-and-programs-used)
* [Testing](#testing)
   + [Code Validation](#code-validation)
   + [Bugs](#bugs)
   + [Further Testing](#further-testing)
   + [Feature Testing](#feature-testing)
* [Deployment](#deployment)
   + [Before the deployment of the project](#before-the-deployment-of-the-project)
   + [Deployed in Heroku](#deployed-in-heroku)
   + [Forking the GitHub Repository](#forking-the-github-repository)
   + [Making a Local Clone](#making-a-local-clone)
* [Credits](#credits)
   + [Content](#content)

   

## User Stories

1. As a user, I want to accurately calculate my income and expenses to see the final result. Specifically, I want to ensure that all my financial data is correctly processed and displayed so that I have a clear understanding of my financial situation.
2. As a user, I want to identify if I am spending too much money in a certain area to see where my expenses are concentrated. Specifically, I like the ability to analyze my spending patterns and make informed decisions to regulate my income and expenses better.
3. As a user, I want to validate the data I input so that I can be confident it is correct. Specifically, I want the system to notify me if there are any errors or inconsistencies in the data I provide.
4. As a user, I want to understand the program's function at a glance so that I can immediately know what it is for. Specifically, I want a clear and intuitive interface that guides me through the program's features without confusion.
5. As a user, I want to know what I am doing wrong and how to correct it so that I can improve my financial management. Specifically, I want the program to provide feedback and suggestions when I make mistakes, helping me to learn and make better decisions.

## Features

**Start Program**

1. Welcome Banner:
+ The section begins with a welcoming banner, introducing users to the program and offering a clear message about the system’s purpose and functionality.

2. Introduction Message:
+ Following the welcome banner, a brief explanation is provided, instructing users to first enter their monthly income. The system then outlines how this income will be distributed across various sections and the corresponding percentages.

3. Section Explanations:
+ Each section is explained individually, helping users understand how to correctly enter their data. These explanations include examples for clarity, with the title of each section highlighted in a different color to distinguish it from the description.

4. Important Notice:
+ In a standout color distinct from the titles and descriptions, the most crucial information is prominently displayed in the center of the program. It reads: "If the information you want to add doesn't apply to any of the columns, just add 0."

5. Monthly Income Input:
+ The feature concludes with an input field where users can enter their monthly income, allowing them to begin the process of tracking and managing their finances.

![Start function](readme-images/start-function-one.png) 
![Start function Two](readme-images/start-function-two.png)

**Taking data from the user**

1. Expense Name Collection:
+ With the correct income data entered, the program proceeds to collect expenses data from the user.
+ A clear banner is displayed, indicating that the user needs to enter the name of the expense.
+ A brief message follows, explaining the types of data that will be accepted for the Expense Name.
+ Finally, the input field is provided for the user to enter the name of the expense.
![Name Input](readme-images/name-input.png) 

2. Needs Data Collection:
+ With the Expense Name correctly entered, the program will then prompt the user to provide Data for Needs.
+ A clear banner is displayed, indicating that the user needs to enter Data for Needs.
+ A brief message follows, explaining what data should be entered and advising that if the user does not wish to update this column, they should enter "0."
+ Finally, the input field is provided for the user to enter the Data for Needs.
![Needs Input](readme-images/needs-input.png)

3. Savings/Inv. Data Collection:
+ With the Needs Data correctly entered, the program will then prompt the user to provide Data for Savings/Inv.
+ A clear banner is displayed, indicating that the user needs to enter Data for Needs.
+ A brief message follows, explaining what data should be entered and advising that if the user does not wish to update this column, they should enter "0."
+ Finally, the input field is provided for the user to enter the Data for Needs.
![Savings Input](readme-images/savings-input.png)

4. Living Expenses Data Collection:
+ With the Savings/Inv. correctly entered, the program will then prompt the user to provide Data for Living Expenses.
+ A clear banner is displayed, indicating that the user needs to enter Data for Needs.
+ A brief message follows, explaining what data should be entered and advising that if the user does not wish to update this column, they should enter "0."
+ Finally, the input field is provided for the user to enter the Data for Needs.
![Living Expenses Input](readme-images/living-expenses-input.png)

**Navigation Menu**
+ After the user correctly enters the data for Living Expenses, they are directed to the navigation menu. The navigation menu is shown at this stage, rather than at the beginning of the program, because, at this point, the user is only able to enter information and view the table. In future stages of the project, this sequence may be updated.
![Navigation Menu](readme-images/menu.png)
+ A clear banner is presented, indicating that this is the navigation menu.
+ On the right side of the screen, the user can choose one of three options:
1. Selecting this option will allow the user to start entering information again, beginning with the name of the expense, followed by needs, savings, and living expenses, and returning to the navigation menu.
2. This option will redirect the user to a new menu to see the table.
3. Selecting this option will terminate the program.
![Table Menu](readme-images/exit-program.png)


**Table Menu**
+ After successfully entering Option 2, the user will be directed to the Table Menu. This stage provides options for viewing and interacting with your data.
+ A clear banner is presented, indicating the Table Menu.
![Table Menu](readme-images/table-menu.png)
1. Selecting Option 1, the user can see the table without any calculations(just the raw information on how it was added). When the option is chosen the user will be able to see the table with the table menu under it(to choose another option after that if he wants).
![Table Without Calculations](readme-images/table-without-calc.png)
2. Selecting Option 2 the user can see the table with all calculations applied. This view will include calculated totals and summaries. When the option it chosen the user will be able to see the table with the table menu under it(to choose another option after that if he wants).
![Table With Calculations](readme-images/table-with-calc.png) 
3. Selecting Option 3(Go back) the user will be sent to the previous menu(Navigation menu).

**Input Validation Process**

+ Each time users provide input, the program performs validation to ensure the data meets the required standards. Before entering any data, users are informed about the specific type of input needed.

+ If an invalid input is detected, an error message is displayed, prompting users to re-enter their data. This process repeats in a loop until valid input is provided.

+ For single-letter inputs, both uppercase and lowercase letters are accepted. Inputs cannot be empty. Amounts must be entered as positive numbers, and negative numbers are not permitted. No empty inputs are allowed, ensuring that all required fields are filled correctly.

Screenshots for all possibility invalid inputs:

+ Income input:

![Testing Income](readme-images/test-income-one.png) 
![Testing Income Two](readme-images/test-income-two.png) 
+ Name for Expenses input:

![Name Input Error](readme-images/name-input-error.png) 
+ Needs input:

1.![Needs Input Error One](readme-images/needs-input-error-one.png) 
2.![Needs Input Error Two](readme-images/needs-input-error-two.png) 
+ Savings input:

1.![Savings Input Error One](readme-images/savings-input-error-one.png) 
2.![Savings Input Error Two](readme-images/savings-input-error-two.png)
+ Living Expenses input:

1.![Living Expenses Input Error One](readme-images/living-expenses-error-one.png) 
2.![Living Expenses Error Two](readme-images/living-expenses-error-one.png) 
+ Navigation menu input:

![Navigation Menu Error](readme-images/menu-error.png) 
+ Table menu input:

![Table Menu Input Error](readme-images/table-menu-error.png)

## Future Features
+ Implement a section to add a spreadsheet, allowing users to save all pieces of information and track their spending progress effectively.

+ Update the program to show the selection menu first, enabling users to choose where to enter information by splitting it into different sections. This improvement will allow for more organized data entry and a better user experience.

+ Enhance the program by adding the ability for users to manage their saved inputs. This feature will allow users to select, edit, or delete any of their entries, even after they have been confirmed and saved to Google Sheets. Additionally, introduce an option to clear all expenses, enabling users to reset the tracker to zero when necessary.

+ Introduce a section where users can input data categorized by day, month, or year, allowing for more detailed and organized tracking of information over time.
## Flowchart

[Lucidchart](https://www.lucidchart.com/pages/?) was used during the planning phase to create a flowchart, aiding in the visualization of the project's structure and flow.
![Flow Chart](readme-images/flow-chart.png)

## Technology Used
### Languages Used

The application has been created with [Python](https://en.wikipedia.org/wiki/Python_(programming_language)).

### Libraries and Programs Used

+ [Lucidchart](https://www.lucidchart.com/pages/?): Used during the planning phase to create a flowchart, aiding in the visualization of the project's structure and flow.
+ [GitHub](https://github.com/): Used for version control and as a repository to store the project, ensuring code integrity and collaboration.
+ [GitPod](https://www.gitpod.io/): Served as the primary environment for writing code, committing changes, and pushing updates to GitHub, facilitating seamless development.
+ [Heroku](https://id.heroku.com/login): Deployed to host and deploy the final project, providing a reliable platform for public access.
+ [Colorama](https://pypi.org/project/colorama/): Employed to add color to terminal outputs, enhancing the visual experience during execution.
+ [Tabulate](https://pypi.org/project/tabulate/): Implemented to format and display expense data in well-organized tables, improving data readability.
+ [Os](https://docs.python.org/3/library/os.html): Leveraged to clear the screen when navigating between different menus or views, maintaining a clean user interface.
+ [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview): Utilized to assess and measure the quality of the web page, ensuring optimal performance and accessibility.
+ [PEP8 Online Checker](https://pep8ci.herokuapp.com/#): Used to validate Python code, ensuring adherence to coding standards and best practices.

## Testing
### Code Validation

1. The code was tested with [CI Python Linter](https://pep8ci.herokuapp.com/#). No errors were found in its final testing.

![Pep8ci Validation](readme-images/pep8ci-validation.png)

### Bugs

1. Bug Fix: Data Overwrite on New Entries:
+ I encountered a bug where each new data entry erased previous information, retaining only the latest input. To fix this, I introduced a `global constant` that captures and stores the initial data in the main function. Then,in the `def menu: option 1`(adding new information), I updated the logic to `append new data` instead of overwriting the existing entries. Finally, I adjusted the `build_table function` to ensure all data is displayed correctly. This solution successfully resolved the data persistence issue.
2. Bug Fix: Incomplete Expense Calculation
+ I encountered a bug where the income minus expenses calculation only worked for the first data entry, ignoring subsequent entries. After some trial and error, I resolved this by updating the `calculate_expenses function` to include parameters for both individual sections and their corresponding calculations. In the `main function`, I ensured all six parameters were correctly aligned with each other. I then updated these parameters in the `menu function: option 1`, to ensure they reflected the correct calculations. Finally, I modified the `build_table function` to display a new column with the calculated values when the user selects the option to view the table with calculations.

### Further Testing

1. Feedback from friends and family members was sought to identify any bugs or user experience issues.

2. Browsers and devices testing:

Browser | Outcome | Pass/Fail
--- | --- | ---
Google Chrome | No issues. | Pass
Safari | The program starts but no user input is recognized and the program can't continue. | Fail
MacBook Air M1" | No issues with appearance or functionality. | Pass
IPhone 15 | The program doesn't start, probably because the iPhone uses Safari. | Fail
Samsung Galaxy A22 | No issues with appearance or functionality. | Pass

3. Lighthouse testing on desktop screen:

![Lighthouse Testing](readme-images/lighthouse.png)

### Feature Testing

Feature | Outcome | Screenshot | Pass/Fail
--- | --- | --- | ---
General Screen Function | The logo banner is displayed correctly, providing an overview of the program as intended. Upon completing the start function, the prompt for entering income/salary is presented as expected. | ![Start function](readme-images/start-function-one.png) ![Start function Two](readme-images/start-function-two.png)| Pass
Salary/Income Input Validation | 1. Invalid inputs (e.g., alphabetic characters, special symbols, empty input) trigger an appropriate error message. 2. Inputs with less than 4 digits or negative values also prompt an error.  | 1.![Testing Income](readme-images/test-income-one.png) 2.![Testing Income Two](readme-images/test-income-two.png) | Pass
After the validation of the input for salary/income | After successful validation of the income input, the program transitions to the expenses name input. The banner is displayed correctly at the top, with a brief guide on how to fill out the input field shown accurately below it. The input field is positioned correctly on the screen. | ![Name Input](readme-images/name-input.png)  | Pass
Expenses Name Input Validation | If the input contains invalid characters such as numbers, special symbols, or whitespace, an error message is displayed.  | ![Name Input Error](readme-images/name-input-error.png)  | Pass
After the validation of the input for Expenses Name Input | After successful validation of the Expenses Name Input, the program transitions to the Data for Needs input. The banner is displayed correctly at the top, with a brief guide on how to fill out the input field shown accurately below it. The input field is positioned correctly on the screen.  | ![Needs Input](readme-images/needs-input.png) | Pass
Data for Needs Input Validation | 1. If the input contains invalid characters such as alphabetic signs an error message is displayed. 2. Or special symbols, whitespace, negative value an error message is displayed. | 1.![Needs Input Error One](readme-images/needs-input-error-one.png) 2.![Needs Input Error Two](readme-images/needs-input-error-two.png) | Pass
After the validation of the input for Data Needs | After successful validation of the Data Needs Input, the program transitions to the Data for Savings/Inv. input. The banner is displayed correctly at the top, with a brief guide on how to fill out the input field shown accurately below it. The input field is positioned correctly on the screen.  | ![Savings Input](readme-images/savings-input.png) | Pass
Data for Savings/Inv. Input Validation | 1. If the input contains invalid characters such as alphabetic signs an error message is displayed and will sent back to the Needs Input. 2. Or special symbols, whitespace, or negative value an error message is displayed and will send the user back to the Needs Input. | 1.![Savings Input Error One](readme-images/savings-input-error-one.png) 2.![Savings Input Error Two](readme-images/savings-input-error-two.png) | Pass
After the validation of the input for Savings/Inv. | After successful validation of the Savings/Inv. Input, the program transitions to the Data for Living Expenses input. The banner is displayed correctly at the top, with a brief guide on how to fill out the input field shown accurately below it. The input field is positioned correctly on the screen.  | ![Living Expenses Input](readme-images/living-expenses-input.png) | Pass
Data for Living Expenses Input Validation | 1. If the input contains invalid characters such as alphabetic signs an error message is displayed and will sent back to the Needs Input. 2. Or special symbols, whitespace, or negative value an error message is displayed and will send the user back to the Needs Input. | 1.![Living Expenses Input Error One](readme-images/living-expenses-error-one.png) 2.![Living Expenses Error Two](readme-images/living-expenses-error-one.png) | Pass
After the validation of the input Living Expenses | After successful validation of the Living Expenses Input, the program transitions to the Navigation Menu, which gives the user 3 different options. The banner is displayed correctly at the top, with a brief guide on how to fill out the input field shown accurately below it. The input field is positioned correctly on the screen.  | ![Navigation Menu](readme-images/menu.png) | Pass
Navigation Menu Input Validation | If the input contains invalid characters such as alphabetic signs or special symbols, whitespace, or negative value an error message is displayed. | ![Navigation Menu Error](readme-images/menu-error.png) 
Navigation  Menu Validation and Option Selection | After successful validation of the input with possible choices (1, 2, 3), if the user selects option 1 (to add more data), the program transitions back to the Expenses Name input screen. The previous steps repeat until the user returns to the Main Table Menu function. | | Pass
Navigation Menu Validation and Option Selection | After successful validation of the input with possible choices (1, 2, 3), if the user selects option 2 (to see the table), the program transitions to a new function with the banner "Your Table Menu!" which position is correct. Under the possible choices (1, 2, 3) the user to choose the future steps. And in the end, input where the user can add his choice. | ![Table Menu](readme-images/table-menu.png) | Pass
Table Menu Input Validation | If the input contains invalid characters such as alphabetic signs or special symbols, whitespace, or negative value an error message is displayed. | ![Table Menu Input Error](readme-images/table-menu-error.png) | Pass
Table Menu Input Validation and Option Selection | After successful validation of the input with possible choices (1, 2, 3), if the user selects option 1 (to see the table without calculations), the table without calculations will be  displayed at the top of the screen. Below the table, the Table Menu with possible choices is presented again. | ![Table Without Calculations](readme-images/table-without-calc.png) | Pass
Table Menu Input Validation and Option Selection | After successful validation of the input with possible choices (1, 2, 3), if the user selects option 2 (to see the table with calculations), the table with calculations will be  displayed at the top of the screen. Below the table, the Table Menu with possible choices is presented again. | ![Table With Calculations](readme-images/table-with-calc.png) | Pass
Table Menu Input Validation and Option Selection | After validating the input with possible choices (1, 2, 3), if the user selects option 3 (to go back), the program transitions back to the Navigation Menu. |  | Pass
Navigation Menu Validation and Option Selection | After validating the input with possible choices (1, 2, 3), if the user selects option 3 (to exit the program), the program will close.| ![Table Menu](readme-images/exit-program.png) | Pass

## Deployment

### Before the deployment of the project:
+ With the command `git add.`, all at the command line prompt in your local project directory to add the files or changes to the repository.
+ After, the command `git commit -m` permanently stores the contents of the index in the local repository.
+ In the end, `git push` is used - to upload local repository content to a remote repository.

### Deployed in [Heroku](https://id.heroku.com/login)
1. Updating the `requirements.txt`
+ Run the following command in the terminal: `pip3 freeze > requirements.txt`
+ The update isn't complete until you add, commit, and push the changes to GitHub (keep this in mind).

2. Creating an account in [Heroku](https://id.heroku.com/login).
+ From the Heroku dashboard click on `Create new app`.
+ Enter a name and select a region for the project deployment, then click `Create App`.

3. Navigate to the `Settings` tab.
+ In the `Config Vars` add the following information:

      KEY = 'PORT', VALUE = '8000'
+ Then, click the `Add` button.

4. Updating `Buildpacks` in `Settings`:
+ Click `Add Buildpacks`.
+ Select `Python` and then click `Save Changes`.
+ Click `Add Buildpacks` again to add other Buildpacks.
+ Select `nodejs` and click `Save Changes`.

5. Going to the `Deploy` section.
+ Choose `GitHub` as the `Deployment method`.
+ Confirm the connection to `GitHub`.
+ Search for the project by the name of our template and click the button `Connect`.
+ Select either `Automatic Deploys` or `Manual Deploys` and click `Deploy Branch`.

6. Once deployment has been completed, click `View` to view the deployed project.

### Forking the GitHub Repository
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the GitHub Repository
2. At the top of the Repository between the Watch and Star buttons on the menu, is the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone
To clone this repository, follow these steps:

1. On the repository's GitHub page, click on the Code button.
2. In the dropdown, click on Clone to copy the repository's URL to your clipboard.
3. Open your terminal.
4. Go to the directory where you want to clone the repository.
5. Use the git clone command followed by the URL you copied, then hit ENTER.
6. Done, cloned to your local machine!

## Credits
### Content

+ The code for the function to clean the screen was adapted from [101computing.net](https://www.101computing.net/python-typing-text-effect/).
+ The code for the function to end the program was adapted from [freecodecamp.org]( https://www.freecodecamp.org/newspython-exit-how-to-use-an-exit-function-in-python-to-stop-a-program/#:~:text=The%20exit()%20function%20in,immediately%20stop%20running%20and%20exit.).
+ How to line break in Python was adapted from [datacamp.com](https://www.datacamp.com/tutorial/how-to-line-break-in-python).
