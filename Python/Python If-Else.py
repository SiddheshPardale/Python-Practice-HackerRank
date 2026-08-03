# Problem: Python If-Else 
# Platform: HackerRank
# Topic: Introduction
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/py-if-else

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0:
        print("Weird")
    elif n >=2 and n<=5:
        print("Not Weird")
    elif n>=6 and n<=20:
        print("Weird")
    elif n>20:
        print("Not Weird")
