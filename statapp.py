import fileinput
import math
import sys
import time

def horizontal_histogram(scores,lb,ub,inc):
  scores.sort()
  print(type(scores))
  print((scores))
  print(scores)
  j = 0
  i = lb
  while (i <= ub):
    count = 0
    while (j < len(scores) and scores[j] >= i and scores[j] < i+inc):
      count=count+1
      j=j+1
    print('{0:3}'.format(i),"*"*count)
    i=i+inc

# Using input() function
input_line = input("Enter text: ") # 77,82,95,100,90
print(input_line)
scores=input_line.split(",")
print(len(scores))
for i in range(len(scores)):
 print(i)
 scores[i]=int(scores[i])
print(scores)
mean = sum(scores) / len(scores)
res = sum((i - mean) ** 2 for i in scores) / len(scores)
sd = math.sqrt(res)

# printing result
print("The mean of list is : " + str(mean))
print("The variance of list is : " + str(res))
print("The sd of list is : " + str(sd))
horizontal_histogram(scores,0,100,10)
time.sleep(5)
print(scores)
