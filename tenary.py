from tkinter import *
from math import sin, cos, pi

'''
draw a tenary tree
Roger Milton, 11th October 2015
'''

def draw_tree( d, x, y, length, level ):  

    xoffset = length * cos( pi / 6.0 )
    yoffset = length * sin( pi / 6.0 )

    # work out co-ords of the end of the lines
    x1 = x - xoffset
    x2 = x + xoffset
    y1 = y - length
    y2 = y + yoffset

    # draw the three lines
    d.create_line(x,y,x,y1)
    d.create_line(x,y,x1,y2)
    d.create_line(x,y,x2,y2)

    if level > 1:

        # recursively draw the next level down
        
        length = length * 0.45

        draw_tree(d,x,y1,length,level-1)
        draw_tree(d,x1,y2,length,level-1)
        draw_tree(d,x2,y2,length,level-1)

        
#create a window
window = Tk()

#crate a drawing area
drawing = Canvas(window, height=700, width=500)
drawing.pack()

# draw the fractal
draw_tree(drawing, 250,400, 125,6)
