## [Question 1]

def namaste(n):
     print("Namaste\n"*n)


## [Question 2]

def revnum(n):
     print(str(n)[::-1])


## [Question 3]

def fact(x):
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


## [Question 7]

def calculate_volume(length, width, height):
     return length*width*height


## [Question 8]

item_count=0

def add_item_to_cart():
     global item_count
     item_count+=1
     print("Item added to shopping cart")


def view_shopping_cart():
     global item_count
     print(f"The Number of items in the shopping cart is {item_count}.")


# main program

add_item_to_cart()
add_item_to_cart()
add_item_to_cart()
view_shopping_cart()


## [Question 9]

def calcBaseTax(income):
     if income>100000:
          return income*0.3
     if income>50000:
          return income*0.2
     if income>10000:
          return income*0.1
     return income*0.05


def calcTaxBonus(age, num_child=None):
     bonus=0
     if age>65:
          bonus+=500
     if num_child is not None:
          bonus += 200*num_child
     return bonus


def calcTax(income, age, num_child=None):
     Base_Tax = calcBaseTax(income)
     deductions = calcTaxBonus(age, num_child)
     incomeTax = Base_Tax - deductions
     afterIncomeTax = income - incomeTax
     print(f"Your Base income Tax is ${Base_Tax:.2f}.")
     print(f"Dependecies Deductions: ${deductions:.2f}")
     print(f"Total Income Tax      : ${incomeTax:.2f}")
     print(f"Income after Tax      : ${afterIncomeTax:.2f}")
     return afterIncomeTax, incomeTax
     

## [Question 10]

def pizzaDelivery():
     confirm = '0'
     while confirm!='1':
          print("Welcome to Digital Pizza Delivery Services")
          size = input("Enter pizza size (S, M, L): ").upper()
          if size not in ['S', 'M', 'L']:
               print("Invalid Size: Please choose from small(S), Medium(M), Large(L)")
               continue
          cheese = input("Do you want extra cheese? (Y or N): ").upper()
          if cheese not in ['Y', 'N']:
               print("Invalid choice: Please choose from Yes(Y) or No(N)")
               continue
          cheese = cheese=='Y'
          pepperoni = input("Do you want pepperoni? (Y or N): ").upper()
          if pepperoni not in ['Y', 'N']:
               print("Invalid choice: Please choose from Yes(Y) or No(N)")
               continue
          pepperoni = pepperoni=='Y'

          print(f"Order Confirmation:\nPizza Size: {size}\nExtra Cheese: {cheese}\nPepperoni: {pepperoni}")
          confirm = input("Press 1 to confirm your order: ")
     cost = calcCost(size, cheese, pepperoni)
     Bill(size, cheese, pepperoni, cost)


def calcCost(size, cheese, pepperoni):
     sizecost = {'S': 8, 'M': 10, 'L': 12}
     cost = sizecost[size]
     if cheese:
          cost+=1
     if pepperoni:
          cost+=2
     return cost


def Bill(size, cheese, pepperoni, cost):
     print("\nOrder Summary:")
     print(f"Pizza Size   : {size}")
     print(f"Extra Cheese : {cheese}")
     print(f"Pepperoni    : {pepperoni}")
     print(f"Total Cost   : ${cost:.2f}")

pizzaDelivery()


          
