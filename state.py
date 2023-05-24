from turtle import Turtle


class State(Turtle):
    def __init__(self, name="State", x_pos=0, y_pos=0):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.state_position(x_pos,y_pos)
        self.state_name(name)

    def state_position(self, x, y):
        self.setposition(x, y)

    def state_name(self, name):
        self.write(arg=name, align="center")

