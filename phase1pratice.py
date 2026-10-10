'''
Exercise 1: Student marks calculator
Requirements
Write a Python program that:
1. Stores a student's name and a list of marks.
2. Defines a function called calculate_average.
3. Returns the average of the marks.
4. Handles an empty marks list appropriately.
5. Prints the student's name and average to two decimal places.
Example output
Student: Ali
Average marks: 82.50
'''


def calculate_average(marks):
    """Calculate the average of marks."""
    if len(marks) == 0:
        raise ValueError("Marks ki list khaali hai!")

    return sum(marks) / len(marks)


def main():
    try:
        student_name = input("Enter student name: ").strip()

        if not student_name:
            raise ValueError("Student name khaali nahi ho sakta!")

        marks = [
            float(input("Enter English marks: ")),
            float(input("Enter Physics marks: ")),
            float(input("Enter Mathematics marks: "))
        ]

        for mark in marks:
            if mark < 0 or mark > 100:
                raise ValueError("Marks 0 se 100 ke darmiyan hone chahiye!")

        average = calculate_average(marks)

        result = (
            f"Student Name: {student_name}\n"
            f"Marks: {marks}\n"
            f"Average: {average:.2f}\n"
        )

        print(result)

        # Save result in a file
        with open("student_results.txt", "a") as file:
            file.write(result + "\n")

        print("Result file mein save ho gaya!")

    except ValueError as error:
        print("Input Error:", error)

    except OSError as error:
        print("File Error:", error)


if __name__ == "__main__":
    main()

