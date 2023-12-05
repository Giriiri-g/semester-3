## [  ]

def leapyr(year):
     """
Leap Year conditions:
     • divisible by 4
     • not divisible by 100
     • but divisible by 400 is acceptable
     """
     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(leapyr(1700))
