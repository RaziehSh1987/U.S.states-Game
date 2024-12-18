import  turtle
import  pandas

screen=turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"  #It is so important that we must write the exact name of the image with the extension
screen.addshape(image) # add image to screen but we don't have access to image
turtle.shape(image) # set turtle with this image to  access to the image

# #find a specific coordinate with following codes
# def print_coord(x,y):
#     print(x,y)   # -180.0 165.0
# turtle.onscreenclick(print_coord) #return x,y coordinates of Turtle click on the image

guess_state=[]
datas=pandas.read_csv("50_states.csv")
states_list=list(datas.state)

while len(guess_state)<50:
    answer_state = screen.textinput(title=f"{len(guess_state)}/50Guess States correct",
                                    prompt="what's another state's name?r").title() # get all type of format of text in one format (Ohio=oHio=OHIO=..) we dont need use lower or uuper case
    if answer_state=="Exit".title():
        missed_list=[]
        for state in states_list:
            if state not in guess_state:
               missed_list.append(state)
        new_data=pandas.DataFrame(missed_list)
        new_data.to_csv("new_states_names")
        break

    if answer_state in states_list:
        guess_state.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=datas[datas.state == answer_state]  #the professor method
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

# turtle.mainloop()  #it caused that the screen isn't closed


