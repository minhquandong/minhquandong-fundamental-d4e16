from turtle import *

color('blue')
speed(-1)

for i in range(2, 50):
    for j in range(4):
        forward(10 + i*2)
        left(90)
    left(10)

mainloop()