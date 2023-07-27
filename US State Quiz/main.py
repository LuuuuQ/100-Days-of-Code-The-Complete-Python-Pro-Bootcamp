import turtle
import pandas
from states_text import Text

screen = turtle.Screen()
screen.title("U.S States Quiz")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
x_list = data.x.to_list()
y_list = data.y.to_list()

text = Text()


points = 0
correct_guesses = []
to_learn = []

while points != 51:
    title_answer = screen.textinput(title=f"Guess the State {points}/50", prompt="What's another state's name").title()

    if title_answer == "Exit":
        break

    if title_answer in state_list and title_answer not in correct_guesses:
        correct_guesses.append(title_answer)
        state_index = state_list.index(title_answer)
        x_value = (x_list[state_index])
        y_value = (y_list[state_index])

        text.texting(title_answer, x_value, y_value)
        points += 1
        print(correct_guesses)

for item in state_list:
    if item in correct_guesses:
        pass
    else:
        to_learn.append(item)

my_data = pandas.DataFrame(to_learn)
my_data.to_csv("to learn.csv")


