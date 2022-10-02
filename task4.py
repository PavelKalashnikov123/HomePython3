# Напишите программу, 
# которая будет преобразовывать десятичное число в двоичное.


binary = ""
n = int(input("Введите число : "))
while n != 0:
    binary = str(n%2) + binary
    n //=2
print(binary)