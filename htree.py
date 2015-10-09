from tkinter import *

'''
program to produce an H-tree fractal
Roger Milton, 9th October 2015
'''

def draw_h_tree( d, x, y, size, level ):

    # x,y are the coordinates of the centre of the H
    # size is the width and height of the H
    # level is the recursive level

    # work out the extremities of the lines needed to
    # draw the H

    # this is the off set from the centre of the H
    
    half_size = size / 2

    # the left of the H
    x1 = x - half_size
    # the right of the H
    x2 = x1 + size
    # the top of the H
    y1 = y - half_size
    # the bottom of the H
    y2 = y1 + size

    # draw the H
    
    h = d.create_line(x1,y1,x1,y2)
    h = d.create_line(x1,y,x2,y)
    h = d.create_line(x2,y1,x2,y2)

    # if another level required, draw add four more smaller H's
    # these H's will be centred at the tips of the H, and half the size
    
    if level > 1:
        h = draw_h_tree(d,x1,y1,half_size,level-1)
        h = draw_h_tree(d,x1,y2,half_size,level-1)
        h = draw_h_tree(d,x2,y1,half_size,level-1)
        h = draw_h_tree(d,x2,y2,half_size,level-1)

#end of draw_h_tree
        
# create a window
window = Tk()

# crate a drawing area
drawing = Canvas(window, height=800, width=800)
drawing.pack()

# draw the fractal
fractal = draw_h_tree(drawing, 400,400, 350,7)
