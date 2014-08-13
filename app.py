""" This is an implementation of l stsrems"""
#!/usr/bin/python

import lsystem
import turtle

turtle.setup(500,500,0,0)
wn = turtle.Screen()
myturtle = turtle.Turtle()

def main():
    myturtle.color("red", "green")
    myturtle.penup()
    myturtle.setpos(-200.00,-200.00)
    myturtle.pendown()
    ls = lsystem.Lsystem(myturtle)
    ls.compute_system(3,'F')
    turtle.exitonclick()
if __name__ == '__main__':
    main()
