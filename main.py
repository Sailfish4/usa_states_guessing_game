from turtle import Turtle, Screen
import turtle
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "/Users/simon/OneDrive/Dokumenty/Python/100dnů.py/den25/us_states_game/blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("/Users/simon/OneDrive/Dokumenty/Python/100dnů.py/den25/us_states_game/50_states.csv")
states = data["state"].tolist()
correct_states = []
score = 0

while len(correct_states) != 50:
    answer_state = screen.textinput(f"{score}/50 States Correct", "What's another state's name").title()
    if answer_state == "Exit":
        states_you_missed = [state for state in states if state not in correct_states]
        pandas.DataFrame(states_you_missed).to_csv("./den25/us_states_game/states you missed.csv")
        break
    if answer_state in correct_states:
        pass
    elif answer_state in states:
        x = int(data[data["state"] == answer_state].x)
        y = int(data[data["state"] == answer_state].y)
        state = Turtle()
        state.penup()
        state.hideturtle()
        state.goto(x,y)
        state.write(answer_state, align = "center", font = ("Arial", 8, "normal"))
        correct_states.append(answer_state)
        score += 1