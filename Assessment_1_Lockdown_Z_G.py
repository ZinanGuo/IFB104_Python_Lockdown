
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 2, 2021.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
student_number = 00000000 # put your student number here as an integer
student_name   = 'Z Guo' # put your name here as a character string
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  LOCKDOWN
#
#  This assessment item tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "track_entities".  You are required to
#  complete this function so that when the program runs it fills
#  a grid with various symbols, using data stored in a list to
#  determine which symbols to draw and where.  See the various
#  "client briefings" in Blackboard for full details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by the client.
#  This single template file will be used for all parts and you will
#  submit your final solution as a single Python 3 file only, whether
#  or not you complete all requirements for the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You must NOT change
# any of the code in this section.
#

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values unless
# instructed.
cell_size = 100 # pixels (default is 100)
grid_width = 8 # squares (default is 8)
grid_height = 7 # squares (default is 7)
x_margin = cell_size * 2.5 # pixels, the size of the margin left/right of the grid
y_margin = cell_size // 2 # pixels, the size of the margin below/above the grid
window_height = grid_height * cell_size + y_margin * 2
window_width = grid_width * cell_size + x_margin * 2
small_font = ('Arial', cell_size // 5, 'normal') # font for the coords
big_font = ('Arial', cell_size // 4, 'normal') # font for any other text

# Validity checks on grid size - do not change this code
assert cell_size >= 80, 'Cells must be at least 80x80 pixels in size'
assert grid_width >= 7, 'Grid must be at least 7 squares wide'
assert (grid_height >= 5) and (grid_height % 2 != 0), \
       'Grid must be at least 5 squares high and height must be odd'

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  Do NOT change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(bg_colour = 'light grey',
                          line_colour = 'slate grey',
                          draw_grid = True,
                          label_spaces = False): # NO! DON'T CHANGE THIS!
    
    # Set up the drawing canvas with enough space for the grid and
    # spaces on either side
    setup(window_width, window_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the grid
    left_edge = -(grid_width * cell_size) // 2 
    bottom_edge = -(grid_height * cell_size) // 2

    # Optionally draw the grid
    if draw_grid:

        # Draw the horizontal grid lines
        setheading(0) # face east
        for line_no in range(0, grid_height + 1):
            penup()
            goto(left_edge, bottom_edge + line_no * cell_size)
            pendown()
            forward(grid_width * cell_size)
            
        # Draw the vertical grid lines
        setheading(90) # face north
        for line_no in range(0, grid_width + 1):
            penup()
            goto(left_edge + line_no * cell_size, bottom_edge)
            pendown()
            forward(grid_height * cell_size)

        # Draw each of the labels on the x axis
        penup()
        y_offset = cell_size // 3 # pixels
        for x_label in range(0, grid_width):
            goto(left_edge + (x_label * cell_size) + (cell_size // 2), bottom_edge - y_offset)
            write(str(x_label + 1), align = 'right', font = small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = cell_size // 5, cell_size // 10 # pixels
        for y_label in range(0, grid_height):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_size) + (cell_size // 2) - y_offset)
            write(chr(y_label + ord('A')), align = 'center', font = small_font)

        # Mark the two "special" cells
        goto(-cell_size * grid_width // 2 + 0.5 * cell_size, 0)
        dot(cell_size // 6)
        goto(cell_size * grid_width // 2 - 0.5 * cell_size, 0)
        dot(cell_size // 6)

    # Optionally mark the blank spaces ... NO! YOU CAN'T CHANGE ANY OF THIS CODE!
    if label_spaces:
        # Left side
        goto(-((grid_width + 1.15) * cell_size) // 2, -(cell_size // 2))
        write('Draw the\ntwo states of\nyour first\nentity here', align = 'right', font = big_font)    
        # Right side
        goto(((grid_width + 1.15) * cell_size) // 2, -(cell_size // 2))
        write('Draw the\ntwo states of\nyour second\nentity here', align = 'left', font = big_font)    

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends.  Call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#


#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "track_entities" function.  ALL of your solution code
#  must appear in, or be called from, function "track_entities".  Do
#  NOT put any of your code in other parts of the program and do NOT
#  change any of the provided code except as allowed in the main
#  program below.
#

import turtle as t
t.speed(2)


# All of your code goes in, or is called from, this function
def printImageA(x,y):
    #Entity 1 - Healthy
    x11_pos = x
    y11_pos = y
    x011_pos = x11_pos+50
    y011_pos = y11_pos-50
    penup()
    goto (x11_pos,y11_pos)
    pendown()
    t.fillcolor("dodger blue")
    t.begin_fill()
    for i in range(4):
        forward(100)
        right(90)
    t.end_fill()
    penup()
    goto (x11_pos+20,y11_pos)
    pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.seth(335)
    t.fd(60)
    t.seth (270)
    t.fd(20)
    for i in range(2):
        right(90)
        fd(5)
    t.seth(170)
    t.fd(40)
    t.seth(180)
    t.fd(20)
    t.seth(20)
    t.fd(25)
    t.seth(160)
    t.fd(25)
    t.seth(5)
    t.fd(25)
    goto (x11_pos+20,y11_pos)
    t.end_fill()
    penup()
    goto(x11_pos+28,y11_pos-32)
    pendown()
    t.fillcolor("cornsilk")
    t.begin_fill()
    t.seth(270)
    t.fd(15)
    t.seth(225)
    t.fd(9)
    t.seth(315)
    t.circle(28,70)
    penup()
    goto(x11_pos+29,y11_pos-60)
    pendown()
    t.seth(310)
    t.circle(22,130)
    t.seth(280)
    t.circle(5,180)
    t.circle(3,180)
    goto(x11_pos+72,y11_pos-42)
    t.end_fill()
    penup()

    #Body
    t.fillcolor("white")
    t.begin_fill()
    goto(x011_pos-20,y011_pos-19)
    pendown()
    t.seth(250)
    t.forward(30)

    t.seth(0)
    t.forward(60)
    t.seth(110)
    t.forward(30)
    t.seth (180)
    goto(x011_pos-20,y011_pos-19)
    t.end_fill()
    penup()

    #Arms
    goto(x011_pos-15,y011_pos-19)
    pendown()
    t.seth(270)
    t.forward(30)
    penup()

    goto(x011_pos+15,y011_pos-19)
    pendown()
    t.seth(270)
    t.forward(30)
    penup()


    #Ribbon
    goto(x011_pos,y011_pos-19)
    pendown()
    t.fillcolor("hot pink")
    t.begin_fill()
    t.seth(210)
    t.forward(20)
    t.seth(100)
    t.forward(12)
    goto(x011_pos,y011_pos-19)

    t.seth(330)
    t.forward(20)
    t.seth(80)
    t.forward(12)
    goto(x011_pos,y011_pos-19)
    t.end_fill()
    penup()

    #Eyes
    goto (x011_pos+5,y011_pos-2)
    pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.seth(30)
    t.circle(7,90)
    t.circle(4,90)
    t.circle(7,90)
    t.circle(4,90)
    penup()
    goto (x011_pos+5,y011_pos+3)
    t.seth(180)
    t.forward(2)
    t.pensize(3)
    t.dot()
    penup()

    goto (x011_pos-10,y011_pos)
    pendown()
    pensize(1)
    t.seth(30)
    t.circle(7,90)
    t.circle(4,90)
    t.circle(7,90)
    t.circle(4,90)
    t.end_fill()
    penup()
    goto (x011_pos-12,y011_pos+5)
    pendown()
    t.seth(0)
    t.forward(2)
    t.pensize(3)
    t.dot()
    t.pensize(1)
    penup()
    t.seth(0)


def printImageB(x,y):
    #Entity 1 - Sick
    x12_pos = x
    y12_pos = y
    x012_pos = x12_pos+50
    y012_pos = y12_pos-50
    
    #Frame
    goto(x12_pos,y12_pos)
    pendown()
    pensize(1)
    t.fillcolor("brown")
    t.begin_fill()
    for i in range(4):
     forward(100)
     right(90)
    t.end_fill()
    penup()
    
    #hair
    t.fillcolor("white")
    t.begin_fill()
    goto(x012_pos,y012_pos+40)
    pendown()
    for i in range(10):
        t.seth(60-(i*36))
        t.circle(-10,120)
    t.end_fill()
    penup()

    #burnt hair
    goto(x012_pos+30,y012_pos+35)
    pendown()
    t.seth(45)
    t.forward (5)
    t.circle(2)
    t.seth(40)
    t.forward(7)
    penup()

    #face
    goto(x12_pos+40,y12_pos-35)
    pendown()
    t.fillcolor("cornsilk")
    t.begin_fill()
    t.seth(270)
    t.forward(15)
    t.seth(225)
    t.forward(9)

    # mouth
    t.seth(315)
    t.forward(5)
    for i in range(5):
        t.seth(300)
        t.forward(5)
        t.seth(60)
        t.forward(5)
    penup()

    
    goto(x12_pos+39,y12_pos-60)
    pendown()
    t.seth(310)
    t.circle(22,130)
    t.seth(280)
    t.circle(5,180)
    t.circle(3,180)
    goto(x12_pos+72,y12_pos-45)
    t.seth(90)
    t.forward(10)
    t.left(90)
    goto(x12_pos+40,y12_pos-35)
    t.end_fill()
    penup()

    #Eyes
    goto (x012_pos+15,y012_pos-2)
    pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.seth(30)
    t.circle(7,90)
    t.circle(4,90)
    t.circle(7,90)
    t.circle(4,90)
    penup()

    #Cross sign eyes
    goto (x012_pos+10,y012_pos-2)
    pendown()
    t.seth(60)
    t.forward(13)
    #t.seth(180)
    #t.forward(2)
    #t.pensize(3)
    #t.dot()
    penup()

    goto(x012_pos+10,y012_pos+8)
    pendown()
    t.seth(300)
    t.forward(13)
    penup()

   
    

    goto (x012_pos,y012_pos)
    pendown()
    pensize(1)
    t.seth(30)
    t.circle(7,90)
    t.circle(4,90)
    t.circle(7,90)
    t.circle(4,90)
    t.end_fill()
    penup()
    #goto (x012_pos-2,y012_pos+5)
    #pendown()
    #t.seth(0)
    #t.forward(2)
    #t.pensize(3)
    #t.dot()
    #penup()

    goto(x012_pos-5,y012_pos+7)
    pendown()
    t.seth(0)
    t.forward(10)
    penup()

    goto(x012_pos-3,y012_pos+12)
    pendown()
    t.seth(270)
    t.forward(15)
    penup()

    #Bang signs
    goto(x12_pos+15,y12_pos-40)
    pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(10):
        t.seth(60-i*36)
        t.circle(6,180)
    t.end_fill()
    penup()

    #body
    t.fillcolor("darkslategray2")
    t.begin_fill()
    goto(x012_pos-15,y012_pos-19)
    pendown()
    t.seth(250)
    t.forward(30)

    t.seth(0)
    t.forward(60)
    t.seth(110)
    t.forward(30)
    goto(x012_pos-15,y012_pos-19)
    t.end_fill()
    penup()
    #arm!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    goto(x012_pos-22,y012_pos-30)
    t.fillcolor("darkslategray2")
    t.begin_fill()
    pendown()
    t.seth(155)
    t.forward(25)
    t.right(90)
    t.forward(7)
    t.right(90)
    t.forward(25)
    goto(x012_pos-15,y012_pos-30)
    t.end_fill()
    #t.forward(20)
    #t.seth(240)
    #t.forward(15)
    #t.seth(330)
    #t.forward(16)
    penup()

    
#Ribbon
    goto(x012_pos+4,y012_pos-17)
    pendown()
    t.fillcolor("hot pink")
    t.begin_fill()
    t.seth(210)
    t.forward(20)
    t.seth(100)
    t.forward(12)
    goto(x012_pos+4,y012_pos-17)

    t.seth(330)
    t.forward(20)
    t.seth(80)
    t.forward(12)
    goto(x012_pos+4,y012_pos-17)
    t.end_fill()
    penup()
    t.seth(0)

def printImageC(x,y):
    #entity2-Healthy
    
    x21_pos = x
    y21_pos = y
    x021_pos= x21_pos + 50
    y021_pos= y21_pos - 50
    goto(x21_pos,y21_pos)
    t.seth(0)
    pendown()
    t.fillcolor("orchid")
    t.begin_fill()
    for i in range(4):
     forward(100)
     right(90)
    penup()
    t.end_fill()

 #body
    goto(x021_pos+11,y021_pos-18)
    t.seth(180)
    t.fillcolor("sky blue")
    t.begin_fill()
    pendown()
    goto(x021_pos-11,y021_pos-18)
    t.seth(270)
    t.forward(5)
    t.seth(180)
    t.forward(8)
    t.seth(200)
    t.circle(40,55)
    goto(x21_pos+4,y21_pos-100)
    penup()

    goto(x021_pos+11,y021_pos-18)
    t.seth(270)
    pendown()
    t.forward(5)
    t.seth(0)
    t.forward(8)
    t.seth(340)
    t.circle(-40,55)
    goto(x21_pos+98,y21_pos-100)
    goto(x21_pos+96,y21_pos-100)
    goto(x21_pos+4,y21_pos-100)
    t.end_fill()
    penup()



    #neck
    goto(x021_pos-11,y021_pos-18)
    t.fillcolor("cornflower blue")
    t.begin_fill()
    t.seth(300)
    pendown()
    t.circle(25,75)
    t.seth(60)
    t.forward(3)
    goto(x021_pos+11,y021_pos-18)
    end_fill()
    penup()

    goto(x021_pos+11,y021_pos-18)
    t.fillcolor("cornflower blue")
    t.begin_fill()
    t.seth(240)
    pendown()
    t.circle(-25,75)
    t.seth(120)
    t.forward(3)
    goto(x021_pos-11,y021_pos-18)
    end_fill()
    penup()

    goto(x021_pos-11,y021_pos-18)
    t.seth(340)
    t.fillcolor("cornsilk")
    pendown()
    t.begin_fill()
    #t.circle(27,52)
    goto(x021_pos+11,y021_pos-18)
    t.seth(240)
    t.circle(-25,33)
    t.seth(130)
    t.circle(25,33)
    goto(x021_pos-11,y021_pos-18)
    t.end_fill()
    penup()


    #hair
    goto(x21_pos+24,y21_pos-42)
    t.seth(90)
    pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.forward(16)
    t.seth(45)
    t.circle(-36,90)
    t.seth(270)
    t.forward(16)
    t.seth(60)
    t.circle(30,40)
    t.seth(123)
    t.circle(46,45)
    t.seth(180)
    t.forward(6)
    t.seth(210)
    t.circle(90,20)
    t.seth(270)
    t.circle(30,37)
    t.end_fill()
    penup()

    #face
    goto(x21_pos+24,y21_pos-42)
    t.seth(270)
    pendown()
    t.fillcolor("cornsilk")
    t.begin_fill()
    t.forward(4)
    t.circle(25,190)
    penup()
    goto(x21_pos+24,y21_pos-42)
    t.seth(90)
    pendown()
    t.forward(16)
    t.seth(45)
    t.circle(-36,90)
    t.seth(270)
    t.forward(16)
    goto(x021_pos+26,y021_pos+8)
    t.end_fill()
    penup()

    #ear
    goto(x21_pos+24,y21_pos-42)
    t.seth(180)
    t.fillcolor("cornsilk")
    t.begin_fill()
    pendown()
    t.circle(6,190)
    goto(x21_pos+24,y21_pos-42)
    t.end_fill()
    penup()

    goto(x021_pos+25,y021_pos+8)
    t.seth(0)
    t.fillcolor("cornsilk")
    t.begin_fill()
    pendown()
    t.circle(-6,190)
    goto(x021_pos+25,y021_pos+8)
    t.end_fill()
    penup()



    #eyebrown
    goto(x021_pos-7,y021_pos+27)
    pendown()
    t.seth(180)
    t.circle(15,75)
    penup()
    goto(x021_pos+7,y021_pos+27)
    pendown()
    t.seth(0)
    t.circle(-15,75)
    penup()

    #glasses
    goto(x21_pos+24,y21_pos-40)
    t.seth(0)
    pendown()
    t.forward(52)
    penup()


    goto(x021_pos+18,y021_pos+10) #Right
    t.seth(90)
    pendown()
    t.fillcolor("white")
    t.begin_fill()
    circle(7)
    t.end_fill()
    penup()
    t.seth(180) #eye
    t.forward(10)
    t.pensize(3)
    t.dot()
    t.pensize(1)

    goto(x021_pos-4,y021_pos+10) #Left
    t.seth(90)
    pendown()
    t.fillcolor("white")
    t.begin_fill()
    circle(7)
    t.end_fill()
    penup()
    
    t.seth(180) #eye
    t.forward(10)
    t.pensize(3)
    t.dot()
    penup()
    t.pensize(1)



    #smile
    goto(x021_pos-8,y021_pos-6)
    t.seth(315)
    pendown()
    circle(12,120)
    penup()
    t.seth(0)


def printImageD(x,y):
    #entity2-Sick
    x22_pos=x
    y22_pos=y
    x022_pos=x+50
    y022_pos=y-50

    #Frame
    goto(x22_pos,y22_pos)
    pendown()
    t.fillcolor("pale green")
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        right(90)
    penup()
    t.end_fill()

#Body
    goto(x22_pos+4,y22_pos-100)
    t.fillcolor("medium purple")
    t.begin_fill()
    pendown()
    t.seth(90)
    t.circle(-30,100)
    t.seth(90)
    t.forward(5)
    t.seth(0)
    t.forward(20)
    t.seth(270)
    t.forward(5)
    t.seth(0)
    t.circle(-30,90)
    goto(x22_pos+4,y22_pos-100)
    t.end_fill()
    penup()

#Collar
    goto(x022_pos-20,y022_pos-20)
    pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.seth(250)
    t.circle(10,180)
    t.seth(290)
    t.circle(10,180)   
    goto(x022_pos,y022_pos-28)
    goto(x022_pos-20,y022_pos-20)
    t.end_fill()
    penup()
    
#Neck
    goto(x022_pos-20,y022_pos-20)
    pendown()
    t.fillcolor("cornsilk")
    t.begin_fill()
    goto(x022_pos,y022_pos-28)
    goto(x022_pos+18,y022_pos-20)
    goto(x022_pos-20,y022_pos-20)
    t.end_fill()
    penup()

#head
    #goto(x022_pos-26,y022_pos+6)
    #hair
    goto(x22_pos+24,y22_pos-42)
    t.seth(90)
    pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.forward(16)
    t.seth(45)
    t.circle(-36,90)
    t.seth(270)
    t.forward(16)
    t.seth(60)
    t.circle(30,40)
    t.seth(123)
    t.circle(46,45)
    t.seth(180)
    t.forward(6)
    t.seth(210)
    t.circle(90,20)
    t.seth(270)
    t.circle(30,37)
    t.end_fill()
    penup()

    #face
    goto(x22_pos+24,y22_pos-42)
    t.seth(270)
    pendown()
    t.fillcolor("cornsilk")
    t.begin_fill()
    t.forward(4)
    t.circle(25,190)
    penup()
    goto(x22_pos+24,y22_pos-42)
    t.seth(90)
    pendown()
    t.forward(16)
    t.seth(45)
    t.circle(-36,90)
    t.seth(270)
    t.forward(16)
    goto(x022_pos+26,y022_pos+8)
    t.end_fill()
    penup()

    #ear
    goto(x22_pos+24,y22_pos-42)
    t.seth(180)
    t.fillcolor("cornsilk")
    t.begin_fill()
    pendown()
    t.circle(6,190)
    goto(x22_pos+24,y22_pos-42)
    t.end_fill()
    penup()

    goto(x022_pos+25,y022_pos+8)
    t.seth(0)
    t.fillcolor("cornsilk")
    t.begin_fill()
    pendown()
    t.circle(-6,190)
    goto(x022_pos+25,y022_pos+8)
    t.end_fill()
    penup()



    #eyebrown
    goto(x022_pos-7,y022_pos+27)
    t.pensize(2)
    pendown()
    t.seth(220)
    t.circle(-15,75)
    penup()
    goto(x022_pos+7,y022_pos+27)
    pendown()
    t.seth(320)
    t.circle(15,75)
    penup()
    pensize(1)

    #glasses
    goto(x22_pos+24,y22_pos-40)
    t.seth(0)
    pendown()
    t.forward(52)
    penup()

    goto(x022_pos+18,y022_pos+10) #Right
    t.seth(90)
    pendown()
    t.fillcolor("white")
    t.begin_fill()
    circle(7)
    t.end_fill()
    t.seth(125) #eye
    t.forward(5)
    t.seth(215)
    t.forward(10)
    
    #t.pensize(3)
    #t.dot()
    #t.pensize(1)

    goto(x022_pos-4,y022_pos+10) #Left
    t.seth(90)
    pendown()
    t.fillcolor("white")
    t.begin_fill()
    circle(7)
    t.end_fill()
    t.seth(215)
    t.forward(5)
    t.seth(135)
    t.forward(12)
    penup()

    #mask
    t.fillcolor("cyan")
    t.begin_fill()
    goto(x022_pos,y022_pos)
    pendown()
    t.seth(180)
    t.forward(15)
    t.left(90)
    t.forward(12)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(12)
    goto(x022_pos,y022_pos)
    t.end_fill()
    penup()

    #mask ties 1
    goto(x022_pos-15,y022_pos)
    pendown()
    t.seth(165)
    t.forward(12)
    penup()

    #mask ties 2
    goto(x022_pos-15,y022_pos-12)
    pendown()
    t.seth(205)
    t.forward(6)
    penup()

    #mask ties 3
    goto(x022_pos+15,y022_pos)
    pendown()
    t.seth(15)
    t.forward(12)
    penup()

    #mask ties 4
    pendown()
    goto(x022_pos+15,y022_pos-12)
    t.seth(345)
    t.forward(2) 
    penup() 
    t.seth(0)



    
def track_entities(list):
    print("List:", list)
    # pass

    goto(-600, 280)
    t.write(arg = "SUNEO the $Rich$ Kid", move = False, align = "left", font = ("Arial", 12, "normal"))
    goto(450, 280)
    t.write(arg = "NOBITA, the Chosen One", move = False, align = "left", font = ("Arial", 12, "normal"))
 
    printImageA(-600, 250)  # Output for Entity 1 (SUNEO) Healthy
    goto(-600, 120)
    t.write(arg = "NOBITA, you cannot win me", move = False, align = "left", font = ("Arial", 10, "normal"))

    printImageB(-600, -150)  # Output for Entity 1 (SUNEO) Sick
    goto(-600, -280)
    t.write(arg = "I think I need to retreat ...", move = False, align = "left", font = ("Arial", 10, "normal"))

    printImageC(500, 250)  # Output for Entity 2 (NOBITA) Healthy
    goto(440, 120)
    t.write(arg = "SUNEO, I know all your tricks", move = False, align = "left", font = ("Arial", 10, "normal"))

    printImageD(500, -150)  # Output for Entity 2 (NOBITA) Sick
    goto(500, -280)
    t.write(arg = "I failed ...", move = False, align = "left", font = ("Arial", 10, "normal"))

    # Extract list from action list  
    status = list[0] # Index 0 list (leftStatus, rightStatus) in action list 
    leftStatus = status[0] # Index 0 item (leftStatus) of Index 0 list (leftStatus, rightStatus) in action list
    rightStatus = status[1] # Index 1 item (rightStatus) of Index 0 list (leftStatus, rightStatus) in action list
    print("leftStatus:", leftStatus)
    print("rightStatus:", rightStatus)

    # Set boundary for grids
    LeftGridBoundary = -400
    RightGridBoundary = 300
    TopGridBoundary = 350
    BottomGridBoundary = -250
    MiddleGridBoundary = 0

    # print healthy / unwell images on either side of screen
    if (leftStatus == 'Healthy'):
        printImageA(-400, 50)
    else:
        printImageB(-400, 50)

    if (rightStatus == 'Healthy'):
        printImageC(300, 50)
    else:
        printImageD(300, 50)

    # set start coordinate for both entities
    leftXPosition = -400
    leftYPosition = 50
    rightXPosition = 300
    rightYPosition = 50

    # start looping through action list
    for moves in range(1, len(list)):        
        entity = list[moves][0]
        direction = list[moves][1]
        step = list[moves][2]

       
        # Movement for left entity
        if (entity == "Left entity"):
            if direction == "North":
                Grid = range (step)
                for step in Grid:                
                    if (leftYPosition < TopGridBoundary):
                        leftYPosition += 100
                        if ((rightStatus == "Unwell") and (leftXPosition >= MiddleGridBoundary)) or (leftStatus == "Unwell"): 
                            printImageB(leftXPosition, leftYPosition) # Unwell when enter infected area or Status is unwell. Same for all followings
                        else:
                            printImageA(leftXPosition, leftYPosition) # Otherwise, healthy pictures for all movements. Same for all followings

                  
            elif direction == "South":
                Grid = range (step)
                for step in Grid:                
                    if (leftYPosition > BottomGridBoundary):
                        leftYPosition -= 100
                        if ((rightStatus == "Unwell") and (leftXPosition >= MiddleGridBoundary)) or (leftStatus == "Unwell"): 
                            printImageB(leftXPosition, leftYPosition)
                        else:
                            printImageA(leftXPosition, leftYPosition)

            elif direction == "West":
                Grid = range (step)
                for step in Grid:                
                    if (leftXPosition > LeftGridBoundary): 
                        leftXPosition -= 100
                        if ((rightStatus == "Unwell") and (leftXPosition >= MiddleGridBoundary)) or (leftStatus == "Unwell"): 
                            printImageB(leftXPosition, leftYPosition)
                        else:
                            printImageA(leftXPosition, leftYPosition)
            else:
                Grid = range (step)
                for step in Grid:                
                    if (leftXPosition < RightGridBoundary): 
                        leftXPosition += 100
                        if ((rightStatus == "Unwell") and (leftXPosition >= MiddleGridBoundary)) or (leftStatus == "Unwell"): 
                            printImageB(leftXPosition, leftYPosition)
                        else:
                            printImageA(leftXPosition, leftYPosition)

               
                      
    
        # Movement for right entity   
        if (entity == "Right entity"):
            if direction == "North":                
                Grid = range (step)
                for step in Grid:                
                    if (rightYPosition < TopGridBoundary):
                        rightYPosition += 100
                        if ((leftStatus == "Unwell") and (rightXPosition < MiddleGridBoundary)) or (rightStatus == "Unwell"): 
                            printImageD(rightXPosition, rightYPosition) # Unwell when enter infected area or Status is unwell. Same for all followings
                        else:
                            printImageC(rightXPosition, rightYPosition) # Otherwise, healthy pictures for all movements. Same for all followings
                  
            elif direction == "South":
                Grid = range (step)
                for step in Grid:                
                    if (rightYPosition > BottomGridBoundary):
                        rightYPosition -= 100
                        if ((leftStatus == "Unwell") and (rightXPosition < MiddleGridBoundary)) or (rightStatus == "Unwell"): 
                            printImageD(rightXPosition, rightYPosition)
                        else:
                            printImageC(rightXPosition, rightYPosition)

            elif direction == "West":
                Grid = range (step)
                for step in Grid:                
                    if(rightXPosition > LeftGridBoundary):
                        rightXPosition -= 100
                        if ((leftStatus == "Unwell") and (rightXPosition < MiddleGridBoundary)) or (rightStatus == "Unwell"): 
                            printImageD(rightXPosition, rightYPosition)
                        else:
                            printImageC(rightXPosition, rightYPosition)
                   
            else:
                Grid = range (step)
                for step in Grid:                
                    if (rightXPosition < LeftGridBoundary):
                        rightXPosition += 100
                        if ((leftStatus == "Unwell") and (rightXPosition < MiddleGridBoundary)) or (rightStatus == "Unwell"): 
                            printImageD(rightXPosition, rightYPosition)
                        else:
                            printImageC(rightXPosition, rightYPosition)  

        
        

   
    

   




#
#--------------------------------------------------------------------#



#-----Initialisation Steps-------------------------------------------#
#
# This code checks that the programmer's identity has been provided
# and whether or not the data generation function is available.  You
# should NOT change any of the code in this section.
#

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()

### Define the function for generating data sets, using the
### client's data generation function if available, but
### otherwise creating a dummy function that returns an empty
### list
if isfile('entity_data.py'):
    print('\nData module found\n')
    from entity_data import entity_actions
    def actions(new_seed = None):
        seed(new_seed)
        return entity_actions(grid_width, grid_height)
else:
    print('\nNo data module available!\n')
    def actions(dummy_parameter = None):
        return []

#
#--------------------------------------------------------------------#



#-----Main Program to Create Drawing Canvas--------------------------#
#
# This main program sets up the canvas, ready for you to start
# drawing your solution.  Do NOT change any of this code except
# as indicated by the comments marked '*****'.  Do NOT put any of
# your solution code in this area.
#

# Set up the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and other elements, by
# ***** providing arguments to this function call
create_drawing_canvas()

# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slooooowly around the screen
tracer(True)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's
# ***** overall theme
title("Trace Suneo and Nobita")

# Call the student's function to process the data set
# ***** While developing your program you can call the
# ***** "actions" function with a fixed seed for the
# ***** random number generator, but your final solution must
# ***** work with "actions()" as the argument to "track_entities",
# ***** i.e., for any data set that can be returned by
# ***** calling function "actions" with no seed.
track_entities(actions()) # <-- no argument for "actions" when assessed

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible when the program
# ***** terminates as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#
