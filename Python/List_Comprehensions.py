# Problem: List Comprehensions
# Platform: HackerRank
# Topic: Basic Data Types
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/list-comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    res =[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if (i+j+k) != n:
                    res.append([i,j,k])
    print(res)
               


