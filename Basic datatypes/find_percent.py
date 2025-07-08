# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
# https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    student_marks = {}  # Initializes an empty dictionary to store student names and their marks.

    for _ in range(n):
        name, *line = input().split() # Reads a line, splits it into name and the rest (marks).
        # The * operator allows us to capture all remaining parts of the line as a list.
        scores = list(map(float, line)) # Converts the marks from strings to floats.
        # The map function applies float conversion to each element in the line.
        # The list function converts the map object to a list.
        student_marks[name] = scores  # Stores the scores list in the dictionary with the student's name as the key.

    query_name = input()

    for key,value in student_marks.items():
            if key == query_name:
                total = 0
                for i in value:
                    total += i
                average = total/len(scores)
    print("{:.2f}".format(average))
# The code reads the number of students and their marks, stores them in a dictionary, and calculates the average marks for a specific student.