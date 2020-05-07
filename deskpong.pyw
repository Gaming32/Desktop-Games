import random, time

import clr
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')
from System.Drawing import *
from System.Windows.Forms import *


def create_windows():
    paddles[0] = Form()
    paddles[0].FormBorderStyle = 0
    paddles[0].BackColor = Color.Black
    paddles[0].InitialPosition = Point(paddlex, paddley)
    paddles[0].ShowInTaskbar = False
    paddles[0].Show()
    paddles[0].DesktopLocation = Point(paddlex, paddley)
    paddles[0].Size = Size(paddlew, paddleh)

    paddles[1] = Form()
    paddles[1].FormBorderStyle = 0
    paddles[1].BackColor = Color.Black
    paddles[1].ShowInTaskbar = False
    paddles[1].Show()
    paddles[1].DesktopLocation = Point(screen_width - paddlex - paddleh, paddley)
    paddles[1].Size = Size(paddlew, paddleh)


def reset():
    Cursor.Position = Point(screen_width // 2, random.randint(*reset_cursor_range))
    cursor_velocity[:] = [random.choice((1, -1)), random.randint(-1, 1)]


screen_width = Screen.PrimaryScreen.WorkingArea.Right - Screen.PrimaryScreen.WorkingArea.Left
screen_height = Screen.PrimaryScreen.WorkingArea.Bottom - Screen.PrimaryScreen.WorkingArea.Top
screen_size = (screen_width, screen_height)

reset_screen_variation = screen_height / 5.3
reset_cursor_range = (int(screen_height / 2 - reset_screen_variation), int(screen_height / 2 + reset_screen_variation))
paddlex = int(screen_width / (318 / 3.0))
paddleh = int(screen_height / 4.24)
paddley = int(screen_height / 2 - paddleh / 2)
paddlew = int(screen_width / 63.6)

print(reset_screen_variation, reset_cursor_range)
print(paddlex, paddley)
print(paddlew, paddleh)

cursor_velocity = [0, 0]
score = [0, 0]
paddles = [None, None]

reset()
create_windows()

Application.Run(Form())

VELOCITY_RATIO = 15
def get_actual_velocity(*vals):
    if len(vals) == 1 and isinstance(vals[0], (list, tuple)):
        return type(vals[0])(get_actual_velocity(*vals[0]))
    return tuple(val * VELOCITY_RATIO for val in vals)

FRAMERATE = 60
wait_time = 1.0 / FRAMERATE

while True:
    Cursor.Position = Point.Subtract(Cursor.Position, Size(*get_actual_velocity(cursor_velocity)))
    if Cursor.Position.Y <= 15:
        cursor_velocity[1] = -1
    elif Cursor.Position.Y >= screen_height - 15:
        cursor_velocity[1] = 1
    time.sleep(wait_time)