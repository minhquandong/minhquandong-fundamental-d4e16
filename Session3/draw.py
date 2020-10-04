from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
a = len(colors)
for i in range(a):
    color(colors[i])
    for j in range((i+3)):
        forward(100)
        left(360/(i+3))

mainloop()