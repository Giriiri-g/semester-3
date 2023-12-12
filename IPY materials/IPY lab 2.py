## [Question 1]

def namaste(n):
     print("Namaste\n"*n)


## [Question 2]

def revnum(n):
     print(str(n)[::-1])


## [Question 3]

def fact(x):
    if isinstance(x, str) == True:
        raise ValueError ("invalid literal for fact() with base 10")
    if isinstance(x, int) == False:
        raise ValueError ("invalid literal for fact() with base 10")
    l = []
    for i in range(1, x):
        if  x%i == 0:
            l.append(i)
    return l


## [Question 4]


def fct_(x):
    if x==0:
        return 1
    else:
        return x*fct_(x-1)


def sumfct(*n):
     sum_=0
     for i in n:
          sum_ += fct_(i)
     return sum_


## [Question 5]

def calculate_factorial(n):
    if n==0: return 1
    else: return n*fct_(n-1)

def calculate_term(x, n):
     return pow(x, n)/calculate_factorial(n)

def calculate_series_sum(x, n):
     sum_ = 0
     for i in range(0, 2*n + 1, 2):
          sum_ += calculate_term(x, i)
     return sum_


## [Question 6]

def costcalc(product_cost, tax_rate=0.07, shipping_cost=5):
     return product_cost + tax_rate + shipping_cost
