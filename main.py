from tkinter import *
from tkinter import ttk
from datetime import datetime as dt
from datetime import timedelta as tdelta
import time as t
import os

def loadTimes():
    times = []

    f = open('clocked_times.txt')
    lines = f.readlines()

    for l in lines:
        times.append(l)


def clockTime(clockIn):
    f = open('clocked_times.txt', 'a+')
    
    #append strings based on clocking in or out, thse will be stripped later on load
    if clockIn:
        f.write('I|'+ str(t.time()) + '\n')
        timing = True
    else:
        f.write('O|'+ str(t.time()) + '\n')
        timing = False
    
    f.close()

def wipeTimes():
    os.remove('clocked_times.txt')

def getClockedTime():
    return "This is a total"

def main():
    running = True
    timing = False

    while running:
        i = input('> ')

        match i:
            case "clock":
                if not timing:
                    clockTime(True)
                    timing = True
                    print("Clocked In - " + str(dt.now()))
                else:
                    clockTime(False)
                    timing = False
                    print("Clocked Out - " + str(dt.now()))
            case "wipe":
                wipeTimes()
            case "total":
                print("Total time clocked: " + getClockedTime())
            case "exit":
                if timing:
                    clockTime(False)
                    print("Clocked Out from Exit - " + str(dt.now()))
                running = False
            case _:
                print("Please enter valid command")

    print("Bye")

if __name__ == "__main__":
    main()

