# exercise
number_of_halls = int(input())
capacity = int(input())
number_of_viewers = int(input())
plan = number_of_halls * capacity
print(number_of_viewers <= plan)

# exercise
a = int(input())
b = int(input())
c = int(input())
print(a < b < c)


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