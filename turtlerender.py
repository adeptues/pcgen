
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
        self.myturtle.speed(200)
        self.myturtle.pendown()
        self.myturtle.setheading(90)
    def exitonclick(self):
        turtle.exitonclick()

    def draw(self,word):
        """

        renders an lsysem product according to the turtle graphics spec and the grammar rules, which define 
        what the turtle is supposed to do.
        
        TODO parse the remaining grammar, add support for branching sequences
        """
        state = []
        self.myturtle.hideturtle()
        for i in word:
            if i is 'F':
                self.myturtle.forward(self.distance)
            elif i is '+':
                self.myturtle.right(self.angle)
            elif i is '-':
                self.myturtle.left(self.angle)
            elif i is '[':
                pos = self.myturtle.pos()
                heading = self.myturtle.heading()
                state.append((pos,heading))
            elif i is ']':
                info  = state.pop()
                pos = info[0]
                heading = info[1]
                self.myturtle.penup()
                self.myturtle.setpos(pos)
                self.myturtle.setheading(heading)
                self.myturtle.pendown()
        self.myturtle.showturtle()
