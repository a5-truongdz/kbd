import libevdev
import glob
import os
import random

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame
pygame.mixer.init()

KEY = [libevdev.KEY_A, libevdev.KEY_B, libevdev.KEY_C, libevdev.KEY_D, libevdev.KEY_E, libevdev.KEY_F, libevdev.KEY_G, libevdev.KEY_H, libevdev.KEY_I, libevdev.KEY_J, libevdev.KEY_K, libevdev.KEY_L, libevdev.KEY_M, libevdev.KEY_N, libevdev.KEY_O, libevdev.KEY_P, libevdev.KEY_Q, libevdev.KEY_R, libevdev.KEY_S, libevdev.KEY_T, libevdev.KEY_U, libevdev.KEY_V, libevdev.KEY_W, libevdev.KEY_X, libevdev.KEY_Y, libevdev.KEY_Z, libevdev.KEY_F1, libevdev.KEY_F2, libevdev.KEY_F3, libevdev.KEY_F4, libevdev.KEY_F5, libevdev.KEY_F6, libevdev.KEY_F7, libevdev.KEY_F8, libevdev.KEY_F9, libevdev.KEY_F10, libevdev.KEY_F11, libevdev.KEY_F12, libevdev.KEY_F13, libevdev.KEY_F14, libevdev.KEY_F15, libevdev.KEY_F16, libevdev.KEY_F17, libevdev.KEY_F18, libevdev.KEY_F19, libevdev.KEY_F20, libevdev.KEY_F21, libevdev.KEY_F22, libevdev.KEY_F23, libevdev.KEY_F24, libevdev.KEY_UP, libevdev.KEY_DOWN, libevdev.KEY_LEFT, libevdev.KEY_RIGHT, libevdev.KEY_LEFTALT, libevdev.KEY_RIGHTALT, libevdev.KEY_0, libevdev.KEY_1, libevdev.KEY_2, libevdev.KEY_3, libevdev.KEY_4, libevdev.KEY_5, libevdev.KEY_6, libevdev.KEY_7, libevdev.KEY_8, libevdev.KEY_9, libevdev.KEY_MINUS, libevdev.KEY_EQUAL, libevdev.KEY_LEFTBRACE, libevdev.KEY_RIGHTBRACE, libevdev.KEY_SLASH, libevdev.KEY_SEMICOLON, libevdev.KEY_APOSTROPHE, libevdev.KEY_COMMA, libevdev.KEY_DOT, libevdev.KEY_BACKSLASH, libevdev.KEY_ESC, libevdev.KEY_SCROLLLOCK, libevdev.KEY_NUMLOCK, libevdev.KEY_INSERT, libevdev.KEY_PRINT, libevdev.KEY_SYSRQ, libevdev.KEY_HOME, libevdev.KEY_PAGEUP, libevdev.KEY_PAUSE, libevdev.KEY_PAGEDOWN, libevdev.KEY_BREAK, libevdev.KEY_END, libevdev.KEY_LEFTMETA, libevdev.KEY_GRAVE, libevdev.KEY_COMPOSE]
BACK = [libevdev.KEY_LEFTCTRL, libevdev.KEY_LEFTSHIFT, libevdev.KEY_CAPSLOCK, libevdev.KEY_TAB, libevdev.KEY_RIGHTCTRL, libevdev.KEY_RIGHTSHIFT, libevdev.KEY_BACKSPACE, libevdev.KEY_SLEEP, libevdev.KEY_BRIGHTNESSDOWN, libevdev.KEY_BRIGHTNESSUP, libevdev.KEY_SWITCHVIDEOMODE, libevdev.KEY_MAIL, libevdev.KEY_COMPUTER, libevdev.KEY_MUTE, libevdev.KEY_VOLUMEDOWN, libevdev.KEY_VOLUMEUP, libevdev.KEY_PREVIOUS, libevdev.KEY_PLAYPAUSE, libevdev.KEY_NEXT, libevdev.KEY_DELETE]

pressKey = [pygame.mixer.Sound("mx-black/press_key1.mp3"), pygame.mixer.Sound("mx-black/press_key2.mp3"), pygame.mixer.Sound("mx-black/press_key3.mp3"), pygame.mixer.Sound("mx-black/press_key4.mp3")]
pressBack = pygame.mixer.Sound("mx-black/press_back.mp3")
pressEnter = pygame.mixer.Sound("mx-black/press_enter.mp3")
pressSpace = pygame.mixer.Sound("mx-black/press_space.mp3")
releaseKey = pygame.mixer.Sound("mx-black/release_key.mp3")
releaseBack = pygame.mixer.Sound("mx-black/release_back.mp3")
releaseEnter = pygame.mixer.Sound("mx-black/release_enter.mp3")
releaseSpace = pygame.mixer.Sound("mx-black/release_space.mp3")

events = glob.glob("/dev/input/event*")
global fd
f = False
for event in events:
    fd = libevdev.Device(open(event, "rb"))
    if fd.has(libevdev.KEY_A):
        print(f"Using {event}")
        f = True
        break
if not f:
    print("No keyboard found.")
    exit(1)

while True:
    for event in fd.events():
        if event.value == 2:
            continue
        if event.code in KEY:
            if event.value == 1:
                pressKey[random.randrange(4)].play()
            else:
                releaseKey.play()
        if event.code in BACK:
            if event.value == 1:
                pressBack.play()
            else:
                releaseBack.play()
        if event.matches(libevdev.KEY_ENTER):
            if event.value == 1:
                pressEnter.play()
            else:
                releaseEnter.play()
        if event.matches(libevdev.KEY_SPACE):
            if event.value == 1:
                pressSpace.play()
            else:
                releaseSpace.play()