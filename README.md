Phase 1: Python Fundamentals
1. Introduction to Python
Definition: Python is a high-level programming language used to develop software, automate tasks, analyze data, and build Artificial Intelligence and Machine Learning applications.
Example:
print("Hello, World!")



Output:
Hello, World!


2. Variables
Definition: A variable is a name used to store a value in a program.
Example:
student_name = "Ali"age = 18print(student_name)print(age)



3. Data Types
Definition: Data types define the kind of value a variable stores.
Common Python data types include:
Data Type	Definition	Example
str	Stores text	"Hello"
int	Stores whole numbers	25
float	Stores decimal numbers	85.5
bool	Stores True or False	True
list	Stores multiple items in order	[10, 20, 30]
dict	Stores key-value pairs	{"name": "Ali"}
Example:
name = "Ali"marks = 85.5is_passed = Trueprint(type(name))print(type(marks))print(type(is_passed))



4. Input and Output
Definition: Input allows a program to receive data from a user, while output displays information to the user.
Example:
name = input("Enter your name: ")print("Welcome,", name)



5. Operators
Definition: Operators are symbols or keywords used to perform calculations, comparisons, and logical operations.
Example:
a = 10b = 5print(a + b)   # Addition: 15print(a - b)   # Subtraction: 5print(a * b)   # Multiplication: 50print(a / b)   # Division: 2.0print(a > b)   # Comparison: True



6. Conditional Statements
Definition: Conditional statements allow a program to make decisions based on whether a condition is true or false.
Example:
marks = 75if marks >= 50:    print("Pass")else:    print("Fail")



Output:
Pass


7. Loops
Definition: Loops execute a block of code repeatedly, either for a sequence of items or while a condition remains true.
Example:
for number in range(1, 4):    print(number)



Output:
1
2
3


8. Strings
Definition: A string is a sequence of characters used to represent text.
Example:
message = "Hello Python"print(message.upper())print(message.lower())print(message.strip())



upper() converts text to uppercase, lower() converts it to lowercase, and strip() removes whitespace from the beginning and end.
9. Lists
Definition: A list is an ordered, mutable collection that can store multiple items.
Example:
marks = [80, 90, 70]print(marks[0])print(len(marks))print(sum(marks))



Output:
80
3
240


10. Functions
Definition: A function is a reusable block of code designed to perform a specific task.
Example:
def add(a, b):    return a + bresult = add(10, 5)print(result)



Output:
15


11. Exception Handling
Definition: Exception handling allows a program to manage runtime errors without stopping unexpectedly.
Example:
try:    number = int(input("Enter a number: "))    print(number)except ValueError:    print("Invalid input. Please enter an integer.")



If the user enters text such as abc, the program handles the ValueError.
12. File Handling
Definition: File handling allows a program to create, read, write, and update files to store information.
Example:
with open("notes.txt", "w") as file:    file.write("I am learning Python.")



This creates notes.txt if it does not exist and writes the text into it. If the file already exists, "w" overwrites its previous contents.
13. Program Organization with main()
Definition: A main() function organizes the main steps of a program into one function. The if __name__ == "__main__": statement allows the function to run when the file is executed directly.
Example:
def main():    print("Welcome to Phase 1")if __name__ == "__main__":    main()



Output:
Welcome to Phase 1


14. Git and GitHub Basics
Definition: Git is a version control system used to track changes in code. GitHub is an online platform where developers can store and share Git repositories.
Example commands:
git add .
git commit -m "Add Python practice"
git push


- git add . stages changes.
- git commit records the staged changes.
- git push uploads committed changes to the connected remote repository.

Phase 1 Summary
By completing Phase 1, a learner should understand Python's basic syntax, variables, data types, input/output, operators, conditions, loops, strings, lists, functions, exception handling, file handling, and basic Git/GitHub workflows.
acThese concepts provide the foundation for the next stage: 
