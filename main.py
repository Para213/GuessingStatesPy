import turtle

import pandas as pd
from turtle import Turtle

cursor = Turtle()
cursor.penup()
cursor.hideturtle()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

corecte = 0
frame = pd.read_csv("50_states.csv")
all_states = frame.state.to_list()
guessed = []

while corecte != 50:
    answer_state = screen.textinput(title=f"{corecte}/50 State corecte", prompt="Ghiceste alt stat")
    answer_state = answer_state.title()
    if answer_state in all_states and answer_state not in guessed:
        corecte += 1
        state_data = frame[frame.state == answer_state]
        cursor.goto(int(state_data.x), int(state_data.y))
        cursor.write(state_data.state.item())
        guessed.append(answer_state)
    elif answer_state == "Exit":
        break

# for state in all_states:
#     if state not in guessed:
#         state_ramase.append(state)
# new_data = pd.DataFrame(state_ramase)
# new_data.to_csv("gresite.csv")

new_data = [state for state in all_states if state not in guessed]
new_data = pd.DataFrame(new_data)
new_data.to_csv("gresite.csv")
