import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
ALIGN, FONT = "center",("Courier",10,"normal")


df = pd.read_csv("50_states.csv")




states = df.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        #for state in states:
          #  if state not in guessed_states:
           #     missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df["state"]==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(str(answer_state), align=ALIGN, font=FONT)
        guessed_states.append(answer_state)
    else:
        print("That is not a state")


print("You won")






screen.exitonclick()