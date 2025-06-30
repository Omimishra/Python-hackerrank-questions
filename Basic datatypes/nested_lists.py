# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    scores_list=[]
    records=[]

    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores_list.append(score)
        records.append([name, score])
   # Get the unique scores and sort them
    sorted_scores = sorted(set(scores_list))
    second_lowest_score = sorted_scores[1]
    # Sort the records by name
    records.sort()
    for element in records: 
        # If the score matches the second lowest score, print the name
        if(element[1]==second_lowest_score): 
            print(element[0])
    