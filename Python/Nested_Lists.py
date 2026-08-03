# Problem: Nested Lists
# Platform: HackerRank
# Topic: Basic Data Types
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/nested-list

if __name__ == '__main__':
    records = []
    scores = []
    result = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        scores.append(score)
    for i in records:
        if i[1] != min(scores):
            result.append(i)
    
    second_lowest = min([student[1] for student in result])

names = []
for student in result:
    if student[1] == second_lowest:
        names.append(student[0])

names.sort()
for name in names:
    print(name)
    
  

