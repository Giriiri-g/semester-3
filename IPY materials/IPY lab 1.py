## [ Question 1 ]

def leapyr(year):
     """
Leap Year conditions:
     • divisible by 4
     • not divisible by 100
     • but divisible by 400 is acceptable
     """
     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(leapyr(1700))


## [ Question 2 ]


def grade_calculator(mark):
     if mark>100 or mark<0:
          print("Invalid mark")
     elif mark >= 95:
          print("O Grade")
     elif mark >=90:
         print("A grade")
     elif mark >=80:
         print("B grade")
     elif mark >=70:
         print("C grade")
     elif mark >=60:
         print("D grade")
     else:
         print("F grade")


## [ Question 3 ]

def shipping_cost(weight, distance):
     cost = 0
     if weight > 10:
          cost += 20
     elif weight > 2:
          cost += 10
     else:
          cost += 5
     if distance > 500:
          cost += 10
     elif distance > 100:
          cost += 5
     return f"The Total cost of the shipping is ${cost}."


## [ Question 4 ]

name = input("Enter your name: ") # String Input
age = int(input("Enter your age: "))# Integer Input
marks = float(input("Enter your marks: ")) # Float Input
print("The name is:", name)
print("The age is:", age)
print("The marks is:", marks)


## [ Question 5 ]

def convtime(sec):
     min_ = sec//60
     sec -= min_*60
     hour = min_//60
     min_ -= hour*60
     return f"{hour}:{min_}:{sec}"

## [ Question 6 ]


## [ Question 7 ]

for i in range(0, 101):
     if (i%3 == 0) or (i%5 == 0):
          continue
     print(i)


## [ Question 8 ]

def revnumber(num):
     strn = str(num)
     n = len(strn)
     for i in range(n):
          print(strn[i])
     for i in range(n):
          print(strn[n-i-1])


## [ Question 9 ]

def ispal(num):
     num = str(num)
     revnum = ""
     for i in num:
          revnum = i+revnum
     if revnum == num:
          return True
     return False

def ispal2(num):
     num = str(num)
     n = len(num)
     for i in range(n//2):
          if num[i] != num[n-i-1]:
               return False
     return True


## [ Question 10 ]

def series1(n):
     from math import factorial
     sum_ = 1
     for i in range(2, n+1):
          sum_ += 1/factorial(i)
     return sum_

def series2(x, n):
     from math import factorial
     sum_ = 0
     for i in range(n+1):
          sum_ += x**i/factorial(i)
     return sum_


## [ Question 11 ]

def strong(n):
     if type(n) != int:
          print("[ ERROR ]: Invalid Literal for strong(n) with base 10")
          return
     strn = str(n)
     res = 0
     from math import factorial
     for i in strn:
          res += factorial(int(i))
     return res == n


## [ Question 12 ]

def patterna(n):
     for i in range(n):
          print(" "*(n-i-1)+"*"*(i+1))

def patternb(n):
     for i in range(n):
          print(" "*i + "*"*(n-i))

def patternc(n):
     for i in range(n):
          print(" "*i + "* "*(n-i))

def patternd(n):
     for i in range(n):
          print("*"*(i+1) + " "*(n-i-1)*2 + "*"*(i+1))

def patterne(n):
     for i in range(n//2 +1):
          print(" "*i + "*"*(n-i*2))
     for i in range(3, n+1, 2):
          print(" "*int(((n-i)/2)) + "*"*i)


## [ Question 13 ]

def pattern1(n):
     for i in range(1, n+1):
          for j in range(1, i+1):
               print(j, end="")
          print("")


def pattern2(n):
     for i in range(1, n+1):
          print(" "*(n-i), end="")
          for j in range(1, i+1):
               print(j, end="")
          print("")


def pattern3(n):
     for i in range(1, n+1):
          print(" "*(n-i), end="")
          for j in range(1, i+1):
               print(j, end="")
          for j in range(i, 0, -1):
               print(j, end="")
          print("")
