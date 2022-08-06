import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

correct_answers = 0
df = pd.read_csv("50_states.csv")
all_states = df.state.to_list()
print(all_states)


def aux_function(state):
    timmy = turtle.Turtle()
    timmy.penup()
    state_data = df[df.state == state]
    timmy.goto(int(state_data.x), int(state_data.y))
    timmy.write(state)
    all_states.remove(state)


while correct_answers < 50:
    answer_state = screen.textinput(title=f"Guess the state {correct_answers}/50", prompt="What's another state's name? ").title()
    if answer_state in all_states:
        aux_function(answer_state)
        correct_answers += 1

screen.mainloop()
