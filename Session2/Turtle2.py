from turtle import *

color('red')
speed(-1)

for i in range(3,7):
    for j in range(i):
        forward(100)
        left(360/i)


mainloop()