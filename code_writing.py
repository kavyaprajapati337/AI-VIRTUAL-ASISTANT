# using keyboard library we write code using voice commands any type of language can write code in vscode annd other ides and visual studio community
import keyboard
import time
import speech_recognition as sr
import pyttsx3
import threading
import re
import os
import subprocess
import sys
import platform
import json

from pynput.keyboard import Key, Controller
from time import sleep
from difflib import get_close_matches
from collections import defaultdict
from pathlib import Path
from datetime import datetime
import logging
import shutil
import tempfile
import webbrowser
import requests
import clipboard
import pyperclip
import win32com.client as win32
import pythoncom
import win32gui
import win32con

# code witing
def a():
    for i in range(5):
        keyboard.press(Key.a)
        keyboard.released(Key.a)
        sleep(0.1)
def b():
    for i in range(5):
        keyboard.press(Key.b)
        keyboard.released(Key.b)
        sleep(0.1)
def c():
    for i in range(5):
        keyboard.press(Key.c)
        keyboard.released(Key.c)
        sleep(0.1)
def d():
    for i in range(5):
        keyboard.press(Key.d)
        keyboard.released(Key.d)
        sleep(0.1)
def e():
    for i in range(5):
        keyboard.press(Key.e)
        keyboard.released(Key.e)
        sleep(0.1)
def f():
    for i in range(5):
        keyboard.press(Key.f)
        keyboard.released(Key.f)
        sleep(0.1)
def g():
    for i in range(5):
        keyboard.press(Key.g)
        keyboard.released(Key.g)
        sleep(0.1)
def h():
    for i in range(5):
        keyboard.press(Key.h)
        keyboard.released(Key.h)
        sleep(0.1)
def i():
    for i in range(5):
        keyboard.press(Key.j)
        keyboard.released(Key.j)
        sleep(0.1)
def j():
    for i in range(5):
        keyboard.press(Key.j)
        keyboard.released(Key.j)
        sleep(0.1)
def k():
    for i in range(5):
        keyboard.press(Key.k)
        keyboard.released(Key.k)
        sleep(0.1)
def l():
    for i in range(5):
        keyboard.press(Key.l)
        keyboard.released(Key.l)
        sleep(0.1)
def m():
    for i in range(5):
        keyboard.press(Key.m)
        keyboard.released(Key.m)
        sleep(0.1)
def n():
    for i in range(5):
        keyboard.press(Key.n)
        keyboard.released(Key.n)
        sleep(0.1)
def o():
    for i in range(5):
        keyboard.press(Key.o)
        keyboard.released(Key.o)
        sleep(0.1)
def p():
    for i in range(5):
        keyboard.press(Key.p)
        keyboard.released(Key.p)
        sleep(0.1)
def q():
    for i in range(5):
        keyboard.press(Key.q)
        keyboard.released(Key.q)
        sleep(0.1)
def r():
    for i in range(5):
        keyboard.press(Key.r)
        keyboard.released(Key.r)
        sleep(0.1)
def s():
    for i in range(5):
        keyboard.press(Key.s)
        keyboard.released(Key.s)
        sleep(0.1)
def t():
    for i in range(5):
        keyboard.press(Key.t)
        keyboard.released(Key.t)
        sleep(0.1)
def u():
    for i in range(5):
        keyboard.press(Key.u)
        keyboard.released(Key.u)
        sleep(0.1)
def v():
    for i in range(5):
        keyboard.press(Key.v)
        keyboard.released(Key.v)
        sleep(0.1)
def w():
    for i in range(5):
        keyboard.press(Key.w)
        keyboard.released(Key.w)
        sleep(0.1)
def x():
    for i in range(5):
        keyboard.press(Key.x)
        keyboard.released(Key.x)
        sleep(0.1)
def y():
    for i in range(5):
        keyboard.press(Key.y)
        keyboard.released(Key.y)
        sleep(0.1)
def z():
    for i in range(5):
        keyboard.press(Key.z)
        keyboard.released(Key.z)
        sleep(0.1)
