import turtle
import pandas

screen = turtle.Screen()
screen.title("Turkey cities game")
screen.tracer(0)
img = "turkey.gif"
screen.addshape(img)
turtle.shape(img)
screen.setup(height=560, width=1020)
data = pandas.read_csv("il.csv")
all_states = data.il_adi.to_list()
guessed_states = []


while len(guessed_states) < 82:
    screen.update()
    answer_state = screen.textinput(title=f"{len(guessed_states)+1}/81", prompt="What is another city's name?").upper()
    if answer_state in guessed_states:
        pass
    elif answer_state not in guessed_states:
        guessed_states.append(answer_state)
        if answer_state in all_states:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.color("blue")
            state_data = data[data.il_adi == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state, align="center", font=("Hobo Std", 8, "normal"))
            #state_data.state.item()
    if answer_state =="EXIT":
        s = turtle.Turtle()
        s.color("red")
        s.goto(0,0)
        s.write("GAME OVER!", align="center", font=("Alfa Slab One", 32, "normal"))  # state_data.state.item()
        break

screen.exitonclick()