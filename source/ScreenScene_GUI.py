import datetime
import customtkinter
from customtkinter import *
from tkinter import font
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkinter as tk
import math


def seconds_to_hours(seconds):
    hours = seconds // 3600
    minute = round((seconds % 3600) / 60, 1)
    return f"{hours} Hour {minute} Minutes"


app = customtkinter.CTk()
app.title("Screen_Time_Summary")
app.iconbitmap("icon.ico")

try:
    with open(f"{str(datetime.datetime.today().date())}.txt", "r") as file:
        app_data = eval(file.read())

    with open(f"{str(datetime.datetime.today().date())}-hour.txt", "r") as file:
        data = eval(file.read())

except Exception as e:
    app_data = {'brave.exe': 0, 'pycharm64.exe': 0, 'python3.12.exe': 0, 'explorer.exe': 0, 'ScreenClippingHost.exe': 0,
                'chrome.exe': 0, 'ShellExperienceHost.exe': 0}
    data = {16: 1800, 17: 1800, 18: 3600, 19: 1800, 20: 1800, 21: 0, 22: 0}

sorted_app_data = sorted(app_data, key=app_data.get, reverse=True)
goal_list = ['pycharm64.exe', 'code.exe']
total_goal = 0
total_time = 0

for exes in data:
    total_time += int(data[exes])

for exes in goal_list:
    total_goal += app_data.get(exes, 0)

app.geometry("450x750")
app.resizable(False, False)
app.configure(fg_color="#B6BBC4")

frame = CTkFrame(app, width=200, height=80, corner_radius=10, fg_color="#31304D")
frame.place(x=15, y=70)
frame_2 = CTkFrame(app, width=200, height=80, corner_radius=10, fg_color="#31304D")
frame_2.place(x=230, y=70)

underline_label = CTkLabel(app, text="-------", font=("Small Fonts", 25, "bold"), bg_color="transparent",
                           text_color="#31304D")
underline_label.place(x=18, y=40)

summary_label = CTkLabel(app, text="Summary", font=("Small Fonts", 25), text_color="#31304D")
summary_label.pack(anchor="w", padx=15, pady=(30, 0))

code_label = CTkLabel(app, text="Project goal", font=("Fixedsys", 17, "normal"), text_color="#B6BBC4",
                      bg_color="#31304D")
code_label.place(x=30, y=75)
# print(total_goal/7200)
code_time = CTkLabel(app, text=seconds_to_hours(total_goal), font=("Small Fonts", 18, "normal"), text_color="#F0ECE5",
                     bg_color="#31304D")
code_time.place(x=30, y=105)

code_goal = CTkLabel(app, text=f"{round((total_goal / 7200) * 100)}%", font=("Fixedsys", 18, "normal"),
                     text_color="#F0ECE5", bg_color="#31304D")
code_goal.place(x=180, y=75)

code_label = CTkLabel(app, text="Project goal", font=("Fixedsys", 17, "normal"), text_color="#B6BBC4",
                      bg_color="#31304D")
code_label.place(x=30, y=75)

limit_time = CTkLabel(app, text=seconds_to_hours(total_time), font=("Small Fonts", 18, "normal"), text_color="#F0ECE5",
                      bg_color="#31304D")
limit_time.place(x=250, y=105)

limit_label = CTkLabel(app, text="Time limit", font=("Fixedsys", 17, "normal"), text_color="#B6BBC4",
                       bg_color="#31304D")
limit_label.place(x=250, y=75)

limit_goal = CTkLabel(app, text=f"{round((total_time / 21600) * 100)}%", font=("Fixedsys", 18, "normal"),
                      text_color="#F0ECE5", bg_color="#31304D")
limit_goal.place(x=390, y=75)
print((total_time / 21600) * 100)

hour_indicator = CTkFrame(app, width=440, height=150, bg_color="transparent", fg_color="transparent")
hour_indicator.place(x=30, y=200)

am_hours = [x for x in range(1, 25)]

screen_time_label = CTkLabel(app, text="Daily_Screen_Time", font=("Small Fonts", 25, "normal"), text_color="#31304D")
screen_time_label.place(x=15, y=165)

minute_label = CTkLabel(app, text="Min", font=("Fixedsys", 5, "normal"), text_color="#31304D")
minute_label.place(x=5, y=200)

minute_seperator = CTkFrame(app, width=1, height=170, bg_color="#4d4d66", fg_color="#4d4d66")
minute_seperator.place(x=30, y=210)

minute_label30 = CTkLabel(app, text="30", font=("Fixedsys", 5, "normal"), text_color="#31304D")
minute_label30.place(x=5, y=289)

minute_label60 = CTkLabel(app, text="60", font=("Fixedsys", 5, "normal"), text_color="#31304D")
minute_label60.place(x=5, y=362)

minute_label15 = CTkLabel(app, text="15", font=("Fixedsys", 5, "normal"), text_color="#31304D")
minute_label15.place(x=5, y=253)

minute_label45 = CTkLabel(app, text="45", font=("Fixedsys", 5, "normal"), text_color="#31304D")
minute_label45.place(x=5, y=325)

minute_line30 = CTkFrame(app, width=400, height=1, bg_color="#4d4d66", fg_color="#4d4d66")
minute_line30.place(x=30, y=303)

minute_line15 = CTkFrame(app, width=400, height=1, bg_color="#4d4d66", fg_color="#4d4d66")
minute_line15.place(x=30, y=265)

minute_line60 = CTkFrame(app, width=400, height=1, bg_color="#4d4d66", fg_color="#4d4d66")
minute_line60.place(x=30, y=378)

minute_line45 = CTkFrame(app, width=400, height=1, bg_color="#4d4d66", fg_color="#4d4d66")
minute_line45.place(x=30, y=340)

for time in am_hours:
    height = data.get(time, 0)
    hour = CTkLabel(hour_indicator, text=str(time), font=("Fixedsys", 5, "normal"), text_color="#31304D")
    hour.grid_configure(row=0, column=am_hours.index(time), padx=(7, 0))
    time_frame = CTkFrame(hour_indicator, width=9, height=(height / 3600) * 150, bg_color="#31304D", fg_color="#31304D")
    time_frame.grid_configure(row=1, column=am_hours.index(time), sticky="n", padx=(7, 0))

app_time_label = CTkLabel(app, text="App_Usage", font=("Small Fonts", 25, "normal"), text_color="#31304D")
app_time_label.place(x=15, y=395)

app_time_frame = CTkFrame(app, height=400, width=420, bg_color="transparent", fg_color="transparent")
app_time_frame.place(x=10, y=430)

column = 0
row = 0
for apps in sorted_app_data:
    if sorted_app_data[4] == apps:
        column = 1
        row = 0

    if sorted_app_data.index(apps)<7:
        app_frame = CTkFrame(app_time_frame, height=70, width=200, corner_radius=10, fg_color="#31304D")
        app_label_canvas = CTkCanvas(app_frame, width=150, height=30, bg="#31304D", highlightthickness=0)
        app_label_canvas.place(x=13, y=6)
        app_label = CTkLabel(app_label_canvas, text=apps, font=("Fixedsys", 16, "normal"), text_color="#B6BBC4")
        app_label.place(x=0, y=0)
        app_time = CTkLabel(app_frame, text=seconds_to_hours(app_data[apps]), font=("Small Fonts", 16, "normal"),
                        text_color="white")
        app_time.place(x=10, y=30)
        app_percent = CTkLabel(app_frame, text=f"{round((app_data[apps] / total_time) * 100)}%",
                           font=("Fixedsys", 16, "normal"), anchor="e")
        app_percent.place(x=170, y=6)
        app_frame.grid_configure(column=column, row=row, padx=10, pady=5)
        row += 1

app.mainloop()
