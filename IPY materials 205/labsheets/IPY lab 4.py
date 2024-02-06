## [1.a]

strin = input("Enter a string input: ")
print("First and last 2 characters: ", end="")
print(strin[:2] + strin[-2:])

## [1.b]
print("\n\n\n")
print("Repetition operator if size>=2: ", end='')
if len(strin)<2:
     print("''")
else:
     print(strin*2)


## [2.a]

strin = input("Enter a string input: ")
i0 = strin[0]
print(i0+strin.replace(i0, "$")[1:])

## [2.b]

strin = input("Enter a string to remove the nth index char: ")
ind = int(input("Enter the index of the character: "))
print(strin[:ind]+strin[ind+1:])

## [2.c]

strin = input("Enter a sentence to count the words: ")
[for i in strin.split()]
