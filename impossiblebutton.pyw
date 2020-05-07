import math, time, _thread

import clr
clr.AddReference('System')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')
from System import *
from System.Drawing import *
from System.Windows.Forms import *


FRAMERATE = 60
DISTANCE = 100
def gameloop():
    sleep_time = 1 / FRAMERATE
    while True:
        time.sleep(sleep_time) # Frame rate

        relx = Cursor.Position.X - (form.DesktopLocation.X + button.Size.Width  // 2)
        rely = Cursor.Position.Y - (form.DesktopLocation.Y + button.Size.Height // 2)
        distance = math.sqrt(relx ** 2 + rely ** 2)
        if distance < DISTANCE:
            form.BringToFront()
            try:
                direction = math.degrees(math.atan(rely / relx))
                if relx < 0:
                    direction += 180
                elif rely < 0:
                    direction += 360
            except ZeroDivisionError:
                direction = 0
            direction += 180
            direction %= 360
            newdistance = DISTANCE - distance
            newx = math.cos(math.radians(direction)) * newdistance
            newy = math.sin(math.radians(direction)) * newdistance
            form.DesktopLocation = Point(form.DesktopLocation.X + int(newx), form.DesktopLocation.Y + int(newy))

        form.DesktopLocation = Point(
            clamp(form.DesktopLocation.X % screen_width,  50, screen_width  - 50),
            clamp(form.DesktopLocation.Y % screen_height, 50, screen_height - 50)
        )


def clamp(num, min_value, max_value):
    return max(min(num, max_value), min_value)


form = Form()
form.FormBorderStyle = 0
form.BackColor = Color.LimeGreen
form.TransparencyKey = Color.LimeGreen
form.StartPosition = 1
form.TopMost = True
form.ShowInTaskbar = False

button = Button()
button.BackColor = Color.White
button.Text = 'Click Me!'

form.Size = button.Size
form.Controls.Add(button)

def click_handler(sender, e):
    MessageBox.Show('You Win!', 'The Impossible Button', 0, 64)
    form.Close()
button.MouseClick += EventHandler(click_handler)


screen_width  = Screen.PrimaryScreen.WorkingArea.Width
screen_height = Screen.PrimaryScreen.WorkingArea.Height


_thread.start_new_thread(gameloop, ())
Application.Run(form)