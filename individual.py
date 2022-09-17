import math
a = float(input("Введите длину большего основания a:"))
b = float(input("Введите длину меньшего основания b:"))
alpha = float(input("Введите угол при большем основании в градусах:"))
alphar = alpha*math.pi/180
print("Площадь трапеции равна",(a**2-b**2)/4*math.tan(alphar))
      
