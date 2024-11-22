from math import tan 
from math import radians as rad
PI=3.14
print('Введите радиус круга (см):')
R=float(input())
C=2*PI*R
S=PI*R**2
a_kvadrat= R * (2**0.5)
a_treugolnik= R * (3**0.5)
A_kvadrat= 2*R
A_treugolnik=6*R /(3**0.5)
A_vosmiugolnik=2*R*tan(rad(22.5))
print('Длина окружности в сантиметрах:',C)
print('Длина окружности в метрах:',C/100,)
print('Площадь круга в сантиметрах²',S)
print('Площадь круга в метрах²',S/10000)
print('Сторона вписанного квадрата:',a_kvadrat,
      'Сторона правильного вписанного треугольника:',a_treugolnik)
print('Сторона описанного квадрата:',A_kvadrat,
      'Сторона правильного описанного треугольника:',A_treugolnik,
      'Сторона правильного описанного восьмиугольника:',A_vosmiugolnik)
