"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Matt Hummel.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # -------------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # -------------------------------------------------------------------------

    window = tkinter.Tk()


    # -------------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # -------------------------------------------------------------------------

    frame = ttk.Frame(window)
    frame.grid()


    # -------------------------------------------------------------------------
    # DONE: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # -------------------------------------------------------------------------

    button = ttk.Button(frame)
    button['command'] = lambda: print('Hello')
    button.grid(row=0,column=0)

    box = ttk.Entry(frame)
    box.grid(row=0,column = 1)

    button2 = ttk.Button(frame)
    button2['command'] = lambda: printstuff(box)
    button2.grid(row=1,column=1)

    box2 = ttk.Entry(frame)
    box2.grid(row=0,column=2)

    button3 = ttk.Button(frame)
    button3['command'] = lambda: print2(box,box2)
    button3.grid(row = 1,column=2)

    button4 = ttk.Button(frame,text = 'I move')
    button4['command'] = lambda: button4.grid(row = 4, column = 2)
    button4.grid(row = 2, column = 0)

    window.mainloop()


    # -------------------------------------------------------------------------
    # DONE: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # DONE: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # -------------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    # -------------------------------------------------------------------------
    # DONE: 8. As time permits, do other interesting GUI things!
    # -------------------------------------------------------------------------

def printstuff(box):

    if(box.get() == 'OK'):
        print('Hello')
    else:
        print('Goodbye')

def print2(box,box2):

    n = int(box2.get())
    for k in range(n):
        print(box.get())


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
