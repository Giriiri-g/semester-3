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

strin = input("Enter a string to exchange first and last character: ")
print(strin[-1]+strin[1:-1]+strin[0])


## [2.d]

strin = input("Enter a sentence to count the words: ")
words = [i for i in strin.split()]
word_count = {i:words.count(i) for i in set(words)}
for i in sorted(word_count, key=lambda k: word_count[k], reverse=True):
     print("{:<10} : {:>4}".format(i, word_count[i]))

## [2.e]

strin = input("Enter a sentence to convert into upper and lower cases: ")
print(f"Upper Case : {strin.upper()}")
print(f"Lower Case : {strin.lower()}")


## [3]

strin = input("Enter a comma seperated sequence of words: ")
print(','.join(sorted(list(set(strin.split(','))))))


## [4]

def Eliminate_Letter(word,letter):
     return word.replace(letter, '')
     
print(Eliminate_Letter("malayalam", 'a'))


## [5.a]

def Replace_vowels(word):
     return word.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')

print(Replace_vowels("education"))


## [5.b]

def modify_case(word):
     return ''.join([i.lower() if i.isupper() else i.upper() for i in list(word)])

print("HeLlo TheRe")
print(modify_case("HeLlo TheRe"))


## [5.c]

def get_char(word,position):
     if position<len(word) and position>=-len(word):
          return word[position]
     else:
          return f"Invald Indexing: {position}"

print(get_char('Malayalam', 2))

## [6]

def ispal(x):
     if isinstance(x, str) == False:
          raise ValueError ("ValueError: invalid Literal for the type 'str'")
     rev = x[::-1]
     if x == rev:
          return True
     return False

print(ispal("malayalam"))
print(ispal("education"))


## [7]

strin = input("Enter your Full Name: ")

print(strin[0].upper()+". ", end='')
for i, val in enumerate(strin):
     if val == " ":
          print(strin[i+1].upper()+". ", end="")

#Ajay Kumar Garg = A. K. G.



## [8]

def shuffleWord(word):
    for i in range(len(word)+1):  
        print(word[i:] + word[:i]) 

shuffleWord("SHIFT")

## [9]

strin = input("Enter a password to check validity: ")
def passwordCheck(paswrd):
     pass_stat = stat(paswrd)
     if len(paswrd)<8:
          print("Invalid Password: The password must be at least eight characters long.")
          return

     if pass_stat[4]==0:
          print('Invalid Password: It must contain at least one uppercase letter.')
          return

     if pass_stat[5]==0:
          print('Invalid Password: It must contain at least one lowercase letter.')
          return

     if pass_stat[0]==0:
          print("Invalid Password: It must contain at least one numeric digit.")
          return
     print(f"Valid Password: The given Password {paswrd} satisfies all condition")

def stat(x):
     dg = 0
     void = 0
     vow = 0
     alpha = 0
     up = 0
     low = 0
     for i in x:
          if i.isdigit():
               dg += 1
          if i.isspace():
               void += 1
          if i in ['a', 'e', 'i', 'o', 'u']:
               vow += 1
          if i.isalpha():
               alpha += 1
          if i.isupper():
               up+=1
          if i.islower():
               low+=1
     return dg, void, vow, alpha, up, low

passwordCheck(strin)
passwordCheck("HelloKitty95")
