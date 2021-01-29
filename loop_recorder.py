import time
import mouse
import keyboard
import queue
import pyautogui
import boxes_on_screen
import json


def record_loop(dictionary):
    i = 1
    while True:
        i += 1
        keyboard.wait('insert')
        l = []
        print('recording')
        mouse.hook(l.append)
        keyboard.wait('print screen')
        mouse.unhook(l.append)
        dictionary.update({'{}'.format(str(i)),l})

def record_loop_json(file):
    i = 1
    while True:
        i += 1
        keyboard.wait('insert')
        l = []
        print('recording')
        mouse.hook(l.append)
        keyboard.wait('print screen')
        mouse.unhook(l.append)
        with open(file, 'a+', encoding='utf/8') as f:
            json.dump(l)


def mouse_position():
            actual = pyautogui.position()
            return actual.x, actual.y
# print(help(pyautogui.position()))


def inside_box(x1,y1,x2,y2):
    print('box: ({0},{1}), ({2},{3})'.format(x1,y1,x2,y2))
    while True:
        (x,y) = mouse_position()
        h = False
        if x1 < x < x2 and y1 < y < y2:
            h = True
        yield h
print(boxes_on_screen.dict['search'])

if __name__ == '__main__':
    # for h in inside_box(*boxes_on_screen.dict['search']):
    #     print(h)
    record_loop_json('trajectories.json')