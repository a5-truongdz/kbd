import libevdev
import glob
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame
pygame.mixer.init()

leftClick: pygame.mixer.Sound = pygame.mixer.Sound("g502x-wireless/primary_down.wav")
leftRelease: pygame.mixer.Sound = pygame.mixer.Sound("g502x-wireless/primary_up.wav")
rightClick: pygame.mixer.Sound = pygame.mixer.Sound("g502x-wireless/secondary_down.wav")
rightRelease: pygame.mixer.Sound = pygame.mixer.Sound("g502x-wireless/secondary_up.wav")
middleClick: pygame.mixer.Sound = pygame.mixer.Sound("g502x-wireless/middle.wav")

events: list[str] = glob.glob("/dev/input/event*")
global fd
f: bool = False
for event in events:
    fd = libevdev.Device(open(event, "rb"))
    if fd.has(libevdev.EV_REL):
        print(f"Using {event}")
        f = True
        break
if not f:
    print("No mouse found.")
    exit(1)

while True:
    for event in fd.events():
        if event.matches(libevdev.BTN_LEFT):
            if event.value == 1:
                leftClick.play()
            else:
                leftRelease.play()
        if event.matches(libevdev.BTN_MIDDLE):
            middleClick.play()
        if event.matches(libevdev.BTN_RIGHT):
            if event.value == 1:
                rightClick.play()
            else:
                rightRelease.play()