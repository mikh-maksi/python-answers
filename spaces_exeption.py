
try:
    a = int(input())
except ValueError:
    print("Введен некоректний символ")
else:
    if a>0:
        print("Введено положительное число")
    else:
        print("Введено отрицательное число")
