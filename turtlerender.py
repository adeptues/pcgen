
import turtle

class turtlerender:
    turtle.setup(500,500,0,0)
    wn = turtle.Screen()

    def __init__(self,distance = 5,angle = 90):
        self.distance = distance
        self.angle = angle
        self.myturtle = turtle.Turtle()
        self.myturtle.color("red", "green")
        self.myturtle.penup()
        self.myturtle.setpos(-200.00,-200.00)
        self.myturtle.pendown()

    def exitonclick(self):
        turtle.exitonclick()

    def draw(self,word):
        """

        renders an lsysem product according to the turtle graphics spec and the grammar rules, which define 
        what the turtle is supposed to do.
        
        TODO parse the remaining grammar, add support for branching sequences
        """
        distance = 5
        angle  = 90
        for i in word:
            if i is 'F':
                self.myturtle.forward(distance)
            elif i is '+':
                self.myturtle.left(angle)
            elif i is '-':
                self.myturtle.right(angle)
