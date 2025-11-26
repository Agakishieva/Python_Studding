# exercise
andy_height = int(input())
ben_height = int(input())
if andy_height > ben_height:
    print(True)
else:
    print(False)


# exercise
age = int(input())
if age < 18:
    print("Minor")
elif 18 <= age <= 64:
    print("Adult")
else:
    print("Senior")

# exercise
number = int(input())
word = input()
if number == 1:
    print(number, word)
else:
    print(number, word + 's')

# exercise
a = int(input())
b = int(input())
if a > b:
    print(a)
    print(b)
elif a < b:
    print(b)
    print(a)
else:
    print(a)
    print(b)

#exercise
a = int(input())
if a >= 0:
    a = -a
    print (a)
    print("The number is negative")
else:
    a = 0 - a
    print (a)
    print("The number is positive")

# exercise
year = int(input())

if (4 != 0 or 100 == 0) and 400 != 0:
     print("Ordinary")
else:
     print("Leap")


# exercise
def xor(a, b):
    if bool(a) == bool(b):
        return False
    else:
        return b if not a else a