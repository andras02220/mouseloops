import pyautogui


def show_mouse_position():
    while 1:
        actual = pyautogui.position()
        print(actual.x, actual.y)

if __name__ == "__main__":
    show_mouse_position()