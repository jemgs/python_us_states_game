import turtle
import pandas
from state import State

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = pandas.read_csv("50_states.csv")
guessed_states = 0
Win = True

while True:
    if guessed_states == 50:
        won = turtle.Turtle()
        won.speed("fastest")
        won.penup()
        won.hideturtle()
        won.color("blue")
        if Win:
            won.write(arg="YOU WON", align="center", font=("Arial", 20, "normal"))
        break

    answer_state = screen.textinput(title=f"{guessed_states}/50 States correct",
                                    prompt="Write the name of a USA State").title()

    if answer_state == "Exit":
        Win = False
        missing_states = []
        for check_answer in states["state"]:
            x_pos = states.loc[states["state"] == check_answer, "x"].values[0]
            y_pos = states.loc[states["state"] == check_answer, "y"].values[0]
            state = State(check_answer, x_pos, y_pos)
            states = states.drop(states[states["state"] == check_answer].index)
            missing_states.append(check_answer)
            guessed_states += 1
        pandas.DataFrame(missing_states).to_csv("your_missed_states.csv")

    for check_answer in states["state"]:
        if answer_state == check_answer:
            x_pos = states.loc[states["state"] == check_answer, "x"].values[0]
            y_pos = states.loc[states["state"] == check_answer, "y"].values[0]
            state = State(answer_state, x_pos, y_pos)
            states = states.drop(states[states["state"] == check_answer].index)
            guessed_states += 1


screen.exitonclick()
