#Exercis1----------------------------------------------------
def square_generator(N):
    for i in range(N+1):
        yield i**2

N = int(input("Enter the value of N: "))
for square in square_generator(N):
    print(square)
#Exercis2----------------------------------------------------
def even_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))
even_numbers = even_generator(n)
print(','.join(map(str, even_numbers)))
#Exercis3----------------------------------------------------
def divisible_by_3_and_4_generator(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n_second = int(input("Enter the value of n: "))
for num in divisible_by_3_and_4_generator(n_second):
    print(num)
#Exercis4----------------------------------------------------
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))

for square in squares(a, b):
    print(square)
#Exercis5----------------------------------------------------
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n_third = int(input("Enter a number (n): "))

for num in countdown(n_third):
    print(num)
