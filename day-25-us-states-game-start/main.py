import turtle
import pandas

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("STATES GUESSER")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 CORRECT!", prompt="Enter a state name:").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv") #states not guessed
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())

        # t.write(state_data.state.item()) alt
        t.write(answer_state)

turtle.mainloop() #in lieu of exitonclick
screen.exitonclick()
