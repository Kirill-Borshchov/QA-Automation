import tkinter as tk
import random
import time

window = tk.Tk()
window.title("Reaction Check")
window.geometry("720x640")

title_label = tk.Label(
    text="REACTION CHECK",
    foreground="white",
    background="black",
    width=100,
    height=2
)

frame_1 = tk.Frame(
    height=50
)

info_label = tk.Label(
    text="Hurry up and click on the 'Click' button when the background color turns red.",
    foreground="black",
    width=100,
    height=2
)

frame_2 = tk.Frame(
    height=50
)

button_colors = ["white", "blue", "yellow", "green", "red", "orange", "pink", "purple", "violet", "gray", "brown"]

start_time = time.time()
current_color = "white"
previous_color_index = 0
red_clicked = False
missed_clicks_count = 0


def handle_start_event():
    button.config(text='Click me', background=button_colors[0], foreground="black", command=handle_click_event)

    result_label.config(text="")
    missed_clicks_label.config(text="")
    global missed_clicks_count
    missed_clicks_count = 0

    start_clicking_process()


initial_button_config = {
    "text": "START",
    "bg": "blue",
    "fg": "yellow",
    "width": 30,
    "height": 3,
    "command": handle_start_event
}

button = tk.Button(cnf=initial_button_config)

frame_3 = tk.Frame(
    height=50
)

result_label = tk.Label(
    foreground="black",
    width=100,
    height=2
)

frame_4 = tk.Frame(
    height=25
)

missed_clicks_label = tk.Label(
    foreground="black",
    width=100,
    height=2
)


def start_clicking_process():
    global red_clicked
    if red_clicked:
        red_clicked = False
        return


    global start_time
    start_time = time.time()

    if button["state"] == "disabled":
        button["state"] = "normal"


    global previous_color_index

    color_index = random.randint(0, len(button_colors) - 1)
    while color_index == previous_color_index:
        color_index = random.randint(0, len(button_colors) - 1)

    color = button_colors[color_index]
    button.config(background=color)
    global current_color
    current_color = color
    previous_color_index = color_index


    if not red_clicked:
        window.after(random.randint(300, 900), start_clicking_process)
    else:
        red_clicked = False


def handle_click_event():
    click_time = time.time()
    global missed_clicks_count
    if current_color != "red":
        missed_clicks_count += 1
        if button["state"] == "normal":
            button["state"] = "disabled"
    else:
        result_label.config(text="Red color was clicked in " + str(round(click_time - start_time, 3)) + " seconds")
        missed_clicks_label.config(text="Missed clicks: " + str(missed_clicks_count))

        global red_clicked
        red_clicked = True
        button.config(initial_button_config)


for c in window.children:
    window.children[c].pack()

window.mainloop()