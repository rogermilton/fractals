from tkinter import *
'''
program to draw a Sierpinski triangle/seive
https://en.wikipedia.org/wiki/Sierpinski_triangle
Roger Milton, 9th October 2015
'''

def draw_sier( d, x, y, length, level ):
    #draw triangle
    if level == 1:
        x1 = x - length
        y1 = y + length
        x2 = x + length

        # draw the triangle
        triangle=d.create_polygon(x,y,x1,y1,x2,y1)
    else:
        new_length = length / 2.0
        draw_sier(d,x,y,new_length,level-1)
        draw_sier(d,x-new_length,y+new_length,new_length,level-1)
        draw_sier(d,x+new_length,y+new_length,new_length,level-1)
    
#create a window
window = Tk()

#crate a drawing area
drawing = Canvas(window, height=500, width=800)
drawing.pack()

# draw the fractal
seive = draw_sier(drawing, 400,50, 400,7)
