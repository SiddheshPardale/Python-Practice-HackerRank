# Problem: Find the Runner-Up Score!
# Platform: HackerRank
# Topic: Basic Data Types
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max1 = max(sorted(arr))
    res = []
    for i in arr:
        if i != max1:
            res.append(i)
    print(max(res))

