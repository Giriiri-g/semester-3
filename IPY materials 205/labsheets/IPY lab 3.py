## [ Question 1 ]

l = [8, 9, 10]

print(l)
l[2] = 17    #a
print(f"a. Set the second index to 17: {l}\n")

l.extend([4, 5, 6]) #b
print(f"b. Add 4, 5, and 6 to the end of the list: {l}\n")

l.pop(0)  #c
print(f"c. Remove the first entry from the list: {l}\n")

l.sort()  #d
l.reverse()
print(f"d. Sort the list in descending order: {l}\n")

l.insert(3, 25)     #e
print(f"e. Insert 25 at index 3: {l}\n")

print("f. ??\n")

l.reverse()    #g
print(f"g. Reverse the List: {l}\n")


print(f"h. Print the list: {l}\n") #h

print("i. Print the count of each element in the list: ")
for i in list(set(l)):   #i
     print(f"{i} : {l.count(i)}")
print()

print(f"j. Maximum : {max(l)}\nMinimum : {min(l)}\n")     #j

l2 = [1, 2, 5, 3, 4, 6, 7, 12, 8]


print(f"k. l2 = {l2}")
print(f"k. Extract the first five elements from the list: {l2[:5]}\n")
print(f"k. Extract the elements from the 3rd to the 7th position (inclusive) : {l2[3:8]}\n")
print(f"k. Extract the last three elements from the list: {l2[-3:]}\n")


## [ Question 2 ]


n = int(input("Enter the size of the List: "))
l3 = [None]*n

for i in range(n):
     l3[i] = int(input(f"Enter the Value for {i}th Element: "))

def Listpop(l, index):
     """
     l2 = list()
     for i in range(len(l)):
          if i == index:
               continue
          else:
               l2.append(l[i])
     """
     l2 = [i for i in l if l.index(i) != index]
     return l2

index = int(input("Enter an Index to pop the Element: "))
if (index not in range(n)) and (index not in range(-1, -n-1, -1)):
     print(index not in range(n), index not in range(-1, -n-1, -1))
     print("IndexError: Index out Bounds")
else:
     l4 = Listpop(l3, index)
     print(f"After popping the value at Index {index}: {l4}")

## [ Question 3 ]


def Listswap(l, ind1, ind2):
     l[ind1-1], l[ind2-1] = l[ind2-1], l[ind1-1]
     return l

List = [23, 65, 19, 90]
pos1 = 1
pos2 = 3
print(f"List: {List}\nPos1: {pos1}\nPos2: {pos2}\nAfter swapping: {Listswap(List, pos1, pos2)}")

## [ Question 4 ]


def ListHalfswap(l):
     if not len(l)%2:
          l[len(l)//2:], l[:len(l)//2] = l[:len(l)//2], l[len(l)//2:]
     else:
          l[len(l)//2+1:], l[:len(l)//2] = l[:len(l)//2], l[len(l)//2+1:]
     return l

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"List before swapping: {l}\nList after swapping: {ListHalfswap(l)}")
l = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"List before swapping: {l}\nList after swapping: {ListHalfswap(l)}")
