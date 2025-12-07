import random


def func(n):
    counter = 0
    for _ in range(n):
        a = random.random()
        b = random.random()
        if (a**2 + b**2)**0.5 <= 1:
            counter += 1
    print(4 * counter / n)


func(10)
func(1000)
func(100000)
func(10000000)

#შედეგები უახლოვდება PI-ს მნიშვნელობას. ეს ფუნქცია წარმოადგენს PI-ს გამომთვლელ პროგრამას მონტე-კარლოს აპროქსიმაციის მეთოდით.