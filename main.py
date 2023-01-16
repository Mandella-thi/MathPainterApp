from Canvas import Canvas
from Shapes import Rectangle, Square

#canvas = Canvas(height=20, width=30, color=(255, 255, 255))
#r1= Rectangle(x=1, y=6, height=7, width=10, color=(100, 200, 125))
#r1.draw(canvas)
#s1= Square(x=1, y=3, side=3, color=(0, 100, 222))
#s1.draw(canvas)
#canvas.make('canvas.png')
#Get canvas width and height from the user
canvas_width= int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

#make a dictionary of color codes and prompt for color
colors ={"white":(255,255,255), "black": (0,0,0)}
canvas_color =input("enter canvas color(white or black)")

#create a canvas with the user data
canvas =Canvas(height=canvas_height,width=canvas_width,color=colors[canvas_color])

while True:
    shape_type= input("What do you like to draw? Enter quit to quit. ")
    #ask for rectangle data and create rectangle if user entered rectangle
    if shape_type.lower()=="rectangle":
        rec_x= int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width =int(input("Enter the width of the rectangle: "))
        rec_height =int(input("Enter the heigth of the rectangle: "))
