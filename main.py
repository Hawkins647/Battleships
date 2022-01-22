import tkinter as tk
import threading
import random
import time

# define colours
blue = "#345995"
light_blue = "#add8e6"
grid_label_font = ("Rubrik", 25)


class Battleships:
    """

    Methods
    --------------

    """

    def __init__(self, root, background_colour, foreground_colour, grid_font):
        """
        :param root: a root window to be used for the games widgets
        :param background_colour: the hex code for the background colour
        :param foreground_colour: the hex code for the foreground colour
        :param grid_font: a tuple containing the font name and size to use on the grid labels
        """
        self.root = root
        self.background_colour = background_colour
        self.foreground_colour = foreground_colour
        self.grid_font = grid_font

        # Set up tk root window
        root.title("Battleships")
        root.iconbitmap("ship_icon.ico")
        root.geometry("800x1000")
        root.config(bg=self.background_colour)

        # define widgets
        grid_frame = tk.Frame(root, bg=self.foreground_colour)
        grid_frame.pack()
        button_frame = tk.Frame(root)
        button_frame.pack()

        # define global list
        self.grid_list = []
        self.enemy_grid_list = [0 for i in range(0, 100)]

        # define the labels that go around the grid frame across the x axis
        grid_label_placeholder = tk.Label(grid_frame, text="", font=grid_label_font, bg=self.foreground_colour)
        grid_label_placeholder.grid(row=0, column=0)

        grid_label_a = tk.Label(grid_frame, text=" A ", font=grid_label_font, width=2, bg=self.foreground_colour)
        grid_label_a.grid(row=0, column=1)
        grid_label_b = tk.Label(grid_frame, text=" B ", font=grid_label_font, width=2, bg=self.foreground_colour)
        grid_label_b.grid(row=0, column=2)
        grid_label_c = tk.Label(grid_frame, text=" C ", font=grid_label_font, width=2, bg=self.foreground_colour)
        grid_label_c.grid(row=0, column=3)
        grid_label_d = tk.Label(grid_frame, text=" D ", font=grid_label_font, width=2, bg=self.foreground_colour)
        grid_label_d.grid(row=0, column=4)
        grid_label_e = tk.Label(grid_frame, text=" E ", font=grid_label_font, width=2, bg=self.foreground_colour)
        grid_label_e.grid(row=0, column=5)
        grid_label_f = tk.Label(grid_frame, text=" F ", font=grid_label_font, width=2, bg=self.foreground_colour)
        grid_label_f.grid(row=0, column=6)
        grid_label_g = tk.Label(grid_frame, text=" G ", font=grid_label_font, width=2, bg=self.foreground_colour)
        grid_label_g.grid(row=0, column=7)
        grid_label_h = tk.Label(grid_frame, text=" H ", font=grid_label_font, width=2, bg=self.foreground_colour)
        grid_label_h.grid(row=0, column=8)
        grid_label_i = tk.Label(grid_frame, text=" I ", font=grid_label_font, width=2, bg=self.foreground_colour)
        grid_label_i.grid(row=0, column=9)
        grid_label_j = tk.Label(grid_frame, text=" J ", font=grid_label_font, width=2, bg=self.foreground_colour)
        grid_label_j.grid(row=0, column=10)

        # Define the labels that go around the grid frame across the y axis
        grid_label_1 = tk.Label(grid_frame, text="1", font=grid_label_font, width=2, bg=self.foreground_colour)
        grid_label_1.grid(row=1, column=0)
        grid_label_2 = tk.Label(grid_frame, text="2", font=grid_label_font, width=2, bg=self.foreground_colour)
        grid_label_2.grid(row=2, column=0)
        grid_label_3 = tk.Label(grid_frame, text="3", font=grid_label_font, width=2, bg=self.foreground_colour)
        grid_label_3.grid(row=3, column=0)
        grid_label_4 = tk.Label(grid_frame, text="4", font=grid_label_font, width=2, bg=self.foreground_colour)
        grid_label_4.grid(row=4, column=0)
        grid_label_5 = tk.Label(grid_frame, text="5", font=grid_label_font, width=2, bg=self.foreground_colour)
        grid_label_5.grid(row=5, column=0)
        grid_label_6 = tk.Label(grid_frame, text="6", font=grid_label_font, width=2, bg=self.foreground_colour)
        grid_label_6.grid(row=6, column=0)
        grid_label_7 = tk.Label(grid_frame, text="7", font=grid_label_font, width=2, bg=self.foreground_colour)
        grid_label_7.grid(row=7, column=0)
        grid_label_8 = tk.Label(grid_frame, text="8", font=grid_label_font, width=2, bg=self.foreground_colour)
        grid_label_8.grid(row=8, column=0)
        grid_label_9 = tk.Label(grid_frame, text="9", font=grid_label_font, width=2, bg=self.foreground_colour)
        grid_label_9.grid(row=9, column=0)
        grid_label_10 = tk.Label(grid_frame, text="10", font=grid_label_font, width=2, bg=self.foreground_colour)
        grid_label_10.grid(row=10, column=0)

        # Create each individual button needed on the grid
        self.grid_button_a1 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_a1))
        self.grid_button_a1.grid(row=1, column=1)
        self.grid_button_a2 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_a2))
        self.grid_button_a2.grid(row=1, column=2)
        self.grid_button_a3 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_a3))
        self.grid_button_a3.grid(row=1, column=3)
        self.grid_button_a4 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_a4))
        self.grid_button_a4.grid(row=1, column=4)
        self.grid_button_a5 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_a5))
        self.grid_button_a5.grid(row=1, column=5)
        self.grid_button_a6 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_a6))
        self.grid_button_a6.grid(row=1, column=6)
        self.grid_button_a7 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_a7))
        self.grid_button_a7.grid(row=1, column=7)
        self.grid_button_a8 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_a8))
        self.grid_button_a8.grid(row=1, column=8)
        self.grid_button_a9 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_a9))
        self.grid_button_a9.grid(row=1, column=9)
        self.grid_button_a10 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_a10))
        self.grid_button_a10.grid(row=1, column=10)

        self.grid_button_b1 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_b1))
        self.grid_button_b1.grid(row=2, column=1)
        self.grid_button_b2 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_b2))
        self.grid_button_b2.grid(row=2, column=2)
        self.grid_button_b3 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_b3))
        self.grid_button_b3.grid(row=2, column=3)
        self.grid_button_b4 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_b4))
        self.grid_button_b4.grid(row=2, column=4)
        self.grid_button_b5 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_b5))
        self.grid_button_b5.grid(row=2, column=5)
        self.grid_button_b6 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_b6))
        self.grid_button_b6.grid(row=2, column=6)
        self.grid_button_b7 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_b7))
        self.grid_button_b7.grid(row=2, column=7)
        self.grid_button_b8 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_b8))
        self.grid_button_b8.grid(row=2, column=8)
        self.grid_button_b9 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_b9))
        self.grid_button_b9.grid(row=2, column=9)
        self.grid_button_b10 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_b10))
        self.grid_button_b10.grid(row=2, column=10)

        self.grid_button_c1 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_c1))
        self.grid_button_c1.grid(row=3, column=1)
        self.grid_button_c2 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_c2))
        self.grid_button_c2.grid(row=3, column=2)
        self.grid_button_c3 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_c3))
        self.grid_button_c3.grid(row=3, column=3)
        self.grid_button_c4 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_c4))
        self.grid_button_c4.grid(row=3,column=4)
        self.grid_button_c5 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_c5))
        self.grid_button_c5.grid(row=3, column=5)
        self.grid_button_c6 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_c6))
        self.grid_button_c6.grid(row=3, column=6)
        self.grid_button_c7 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_c7))
        self.grid_button_c7.grid(row=3, column=7)
        self.grid_button_c8 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_c8))
        self.grid_button_c8.grid(row=3, column=8)
        self.grid_button_c9 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_c9))
        self.grid_button_c9.grid(row=3, column=9)
        self.grid_button_c10 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_c10))
        self.grid_button_c10.grid(row=3, column=10)

        self.grid_button_d1 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_d1))
        self.grid_button_d1.grid(row=4, column=1)
        self.grid_button_d2 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_d2))
        self.grid_button_d2.grid(row=4, column=2)
        self.grid_button_d3 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_d3))
        self.grid_button_d3.grid(row=4, column=3)
        self.grid_button_d4 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_d4))
        self.grid_button_d4.grid(row=4,column=4)
        self.grid_button_d5 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_d5))
        self.grid_button_d5.grid(row=4, column=5)
        self.grid_button_d6 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_d6))
        self.grid_button_d6.grid(row=4, column=6)
        self.grid_button_d7 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_d7))
        self.grid_button_d7.grid(row=4, column=7)
        self.grid_button_d8 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_d8))
        self.grid_button_d8.grid(row=4, column=8)
        self.grid_button_d9 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_d9))
        self.grid_button_d9.grid(row=4, column=9)
        self.grid_button_d10 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_d10))
        self.grid_button_d10.grid(row=4, column=10)

        self.grid_button_e1 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_e1))
        self.grid_button_e1.grid(row=5, column=1)
        self.grid_button_e2 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_e2))
        self.grid_button_e2.grid(row=5, column=2)
        self.grid_button_e3 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_e3))
        self.grid_button_e3.grid(row=5, column=3)
        self.grid_button_e4 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_e4))
        self.grid_button_e4.grid(row=5,column=4)
        self.grid_button_e5 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_e5))
        self.grid_button_e5.grid(row=5, column=5)
        self.grid_button_e6 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_e6))
        self.grid_button_e6.grid(row=5, column=6)
        self.grid_button_e7 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_e7))
        self.grid_button_e7.grid(row=5, column=7)
        self.grid_button_e8 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_e8))
        self.grid_button_e8.grid(row=5, column=8)
        self.grid_button_e9 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_e9))
        self.grid_button_e9.grid(row=5, column=9)
        self.grid_button_e10 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_e10))
        self.grid_button_e10.grid(row=5, column=10)

        self.grid_button_f1 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_f1))
        self.grid_button_f1.grid(row=6, column=1)
        self.grid_button_f2 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_f2))
        self.grid_button_f2.grid(row=6, column=2)
        self.grid_button_f3 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_f3))
        self.grid_button_f3.grid(row=6, column=3)
        self.grid_button_f4 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_f4))
        self.grid_button_f4.grid(row=6,column=4)
        self.grid_button_f5 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_f5))
        self.grid_button_f5.grid(row=6, column=5)
        self.grid_button_f6 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_f6))
        self.grid_button_f6.grid(row=6, column=6)
        self.grid_button_f7 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_f7))
        self.grid_button_f7.grid(row=6, column=7)
        self.grid_button_f8 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_f8))
        self.grid_button_f8.grid(row=6, column=8)
        self.grid_button_f9 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_f9))
        self.grid_button_f9.grid(row=6, column=9)
        self.grid_button_f10 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_f10))
        self.grid_button_f10.grid(row=6, column=10)

        self.grid_button_g1 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_g1))
        self.grid_button_g1.grid(row=7, column=1)
        self.grid_button_g2 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_g2))
        self.grid_button_g2.grid(row=7, column=2)
        self.grid_button_g3 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_g3))
        self.grid_button_g3.grid(row=7, column=3)
        self.grid_button_g4 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_g4))
        self.grid_button_g4.grid(row=7,column=4)
        self.grid_button_g5 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_g5))
        self.grid_button_g5.grid(row=7, column=5)
        self.grid_button_g6 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_g6))
        self.grid_button_g6.grid(row=7, column=6)
        self.grid_button_g7 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_g7))
        self.grid_button_g7.grid(row=7, column=7)
        self.grid_button_g8 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_g8))
        self.grid_button_g8.grid(row=7, column=8)
        self.grid_button_g9 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_g9))
        self.grid_button_g9.grid(row=7, column=9)
        self.grid_button_g10 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_g10))
        self.grid_button_g10.grid(row=7, column=10)

        self.grid_button_h1 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_h1))
        self.grid_button_h1.grid(row=8, column=1)
        self.grid_button_h2 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_h2))
        self.grid_button_h2.grid(row=8, column=2)
        self.grid_button_h3 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_h3))
        self.grid_button_h3.grid(row=8, column=3)
        self.grid_button_h4 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_h4))
        self.grid_button_h4.grid(row=8,column=4)
        self.grid_button_h5 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_h5))
        self.grid_button_h5.grid(row=8, column=5)
        self.grid_button_h6 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_h6))
        self.grid_button_h6.grid(row=8, column=6)
        self.grid_button_h7 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_h7))
        self.grid_button_h7.grid(row=8, column=7)
        self.grid_button_h8 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_h8))
        self.grid_button_h8.grid(row=8, column=8)
        self.grid_button_h9 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_h9))
        self.grid_button_h9.grid(row=8, column=9)
        self.grid_button_h10 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_h10))
        self.grid_button_h10.grid(row=8, column=10)

        self.grid_button_i1 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_i1))
        self.grid_button_i1.grid(row=9, column=1)
        self.grid_button_i2 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_i2))
        self.grid_button_i2.grid(row=9, column=2)
        self.grid_button_i3 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_i3))
        self.grid_button_i3.grid(row=9, column=3)
        self.grid_button_i4 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_i4))
        self.grid_button_i4.grid(row=9,column=4)
        self.grid_button_i5 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_i5))
        self.grid_button_i5.grid(row=9, column=5)
        self.grid_button_i6 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_i6))
        self.grid_button_i6.grid(row=9, column=6)
        self.grid_button_i7 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_i7))
        self.grid_button_i7.grid(row=9, column=7)
        self.grid_button_i8 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_i8))
        self.grid_button_i8.grid(row=9, column=8)
        self.grid_button_i9 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_i9))
        self.grid_button_i9.grid(row=9, column=9)
        self.grid_button_i10 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_i10))
        self.grid_button_i10.grid(row=9, column=10)

        self.grid_button_j1 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_j1))
        self.grid_button_j1.grid(row=10, column=1)
        self.grid_button_j2 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_j2))
        self.grid_button_j2.grid(row=10, column=2)
        self.grid_button_j3 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_j3))
        self.grid_button_j3.grid(row=10, column=3)
        self.grid_button_j4 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_j4))
        self.grid_button_j4.grid(row=10,column=4)
        self.grid_button_j5 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_j5))
        self.grid_button_j5.grid(row=10, column=5)
        self.grid_button_j6 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_j6))
        self.grid_button_j6.grid(row=10, column=6)
        self.grid_button_j7 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_j7))
        self.grid_button_j7.grid(row=10, column=7)
        self.grid_button_j8 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_j8))
        self.grid_button_j8.grid(row=10, column=8)
        self.grid_button_j9 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_j9))
        self.grid_button_j9.grid(row=10, column=9)
        self.grid_button_j10 = tk.Button(grid_frame, text="", bg=self.background_colour, font=self.grid_font, width=2, command=lambda:self.handle_press(self.grid_button_j10))
        self.grid_button_j10.grid(row=10, column=10)

        self.play_game_button = tk.Button(button_frame, text="Play new game!", font=grid_label_font, command=self.play_new_game)
        self.play_game_button.grid(row=0, column=0)

        self.button_list = [self.grid_button_a1, self.grid_button_a2, self.grid_button_a3, self.grid_button_a4, self.grid_button_a5, self.grid_button_a6, self.grid_button_a7, self.grid_button_a8, self.grid_button_a9, self.grid_button_a10,
                            self.grid_button_b1, self.grid_button_b2, self.grid_button_b3, self.grid_button_b4, self.grid_button_b5, self.grid_button_b6, self.grid_button_b7, self.grid_button_b8, self.grid_button_b9, self.grid_button_b10,
                            self.grid_button_c1, self.grid_button_c2, self.grid_button_c3, self.grid_button_c4, self.grid_button_c5, self.grid_button_c6, self.grid_button_c7, self.grid_button_c8, self.grid_button_c9, self.grid_button_c10,
                            self.grid_button_d1, self.grid_button_d2, self.grid_button_d3, self.grid_button_d4, self.grid_button_d5, self.grid_button_d6, self.grid_button_d7, self.grid_button_d8, self.grid_button_d9, self.grid_button_d10,
                            self.grid_button_e1, self.grid_button_e2, self.grid_button_e3, self.grid_button_e4, self.grid_button_e5, self.grid_button_e6, self.grid_button_e7, self.grid_button_e8, self.grid_button_e9, self.grid_button_e10,
                            self.grid_button_f1, self.grid_button_f2, self.grid_button_f3, self.grid_button_f4, self.grid_button_f5, self.grid_button_f6, self.grid_button_f7, self.grid_button_f8, self.grid_button_f9, self.grid_button_f10,
                            self.grid_button_g1, self.grid_button_g2, self.grid_button_g3, self.grid_button_g4, self.grid_button_g5, self.grid_button_g6, self.grid_button_g7, self.grid_button_g8, self.grid_button_g9, self.grid_button_g10,
                            self.grid_button_h1, self.grid_button_h2, self.grid_button_a3, self.grid_button_h4, self.grid_button_h5, self.grid_button_h6, self.grid_button_h7, self.grid_button_h8, self.grid_button_h9, self.grid_button_h10,
                            self.grid_button_i1, self.grid_button_i2, self.grid_button_i3, self.grid_button_i4, self.grid_button_i5, self.grid_button_i6, self.grid_button_i7, self.grid_button_i8, self.grid_button_i9, self.grid_button_i10,
                            self.grid_button_j1, self.grid_button_j2, self.grid_button_j3, self.grid_button_j4, self.grid_button_j5, self.grid_button_j6, self.grid_button_j7, self.grid_button_j8, self.grid_button_j9, self.grid_button_j10,]

        for button in self.button_list:
            button.config(state=tk.DISABLED)

    def set_up_boat_positions(self):
        """Set up the boat positions with an element of randomness."""
        try:
            carrier_button = random.choice(self.button_list)
            carrier_button.config(text="X")
            for i in range(1, 5):
                self.button_list[self.button_list.index(carrier_button) + i].config(text="X")

            battleship_button = random.choice(self.button_list)
            battleship_button.config(text="X")
            for i in range(1, 4):
                self.button_list[self.button_list.index(battleship_button) + i].config(text="X")

            cruiser_button = random.choice(self.button_list)
            cruiser_button.config(text="X")
            for i in range(1, 3):
                self.button_list[self.button_list.index(cruiser_button) + i].config(text="X")

            submarine_button = random.choice(self.button_list)
            submarine_button.config(text="X")
            for i in range(1, 3):
                self.button_list[self.button_list.index(submarine_button) + i].config(text="X")

            destroyer_button = random.choice(self.button_list)
            destroyer_button.config(text="X")
            for i in range(1, 2):
                self.button_list[self.button_list.index(destroyer_button) + i].config(text="X")

        except IndexError:
            self.set_up_boat_positions()

    def set_up_enemy_boat_positions(self):
        """Set up the boat positions with an element of randomness and append the values to self.enemy_grid_list"""
        try:
            carrier_button = random.choice(self.button_list)
            index = self.button_list.index(carrier_button)
            for i in range(0, 5):
                self.enemy_grid_list[index + i] = 1

            battleship_button = random.choice(self.button_list)
            index = self.button_list.index(battleship_button)
            for i in range(0, 4):
                self.enemy_grid_list[index + i] = 1

            cruiser_button = random.choice(self.button_list)
            index = self.button_list.index(cruiser_button)
            for i in range(0, 3):
                self.enemy_grid_list[index + i] = 1

            submarine_button = random.choice(self.button_list)
            index = self.button_list.index(submarine_button)
            for i in range(0, 3):
                self.enemy_grid_list[index + i] = 1

            destroyer_button = random.choice(self.button_list)
            index = self.button_list.index(destroyer_button)
            for i in range(0, 2):
                self.enemy_grid_list[index + i] = 1

        except IndexError:
            self.set_up_enemy_boat_positions()

    def play_new_game(self):
        """Main game logic"""

        self.set_up_boat_positions()
        self.play_game_button.config(text="Your board!", state=tk.DISABLED)

        # create the grid_list using text values from buttons
        for button in self.button_list:
            if button.cget('text') == "X":
                self.grid_list.append(1)
            else:
                self.grid_list.append(0)

        # clear all buttons of text
        thread = threading.Thread(target=self.clear_board)
        thread.start()

        # set up enemy boat positions
        self.set_up_enemy_boat_positions()

    def handle_press(self, button):
        """Takes in a button which is used to compare it's position in the list to the user's guess.
        Take appropriate action depending on whether the user guessed correctly or incorrectly."""

        index = self.button_list.index(button)

        # if a hit was made
        if self.enemy_grid_list[index] == 1:
            button.config(state=tk.DISABLED, text="X")
            self.play_game_button.config(text="Hit!")
            # see if the user has won
            self.check_for_win()
        # if the user missed
        else:
            button.config(state=tk.DISABLED)
            self.play_game_button.config(text="Miss!")

    def check_for_win(self):
        """Check to see if there are X's on all the spaces matching with the 1's in the enemy_grid_list list.
        If so, provide a winning message to the user and restart the game."""
        temp_list = []
        for button in self.button_list:
            if button.cget('text') == "X":
                temp_list.append(1)
            else:
                temp_list.append(0)

        # if user has won
        if temp_list == self.enemy_grid_list:
            for button in self.button_list:
                button.config(state=tk.DISABLED, text="")
            self.play_game_button.config(text="You Won!")
            thread = threading.Thread(target=self.restart_game)
            thread.start()

    def restart_game(self):
        """Clear the board and all list values and reset the game."""
        time.sleep(5)
        self.play_game_button.config(text="Play new game!")
        self.enemy_grid_list = [0 for i in range(0, 100)]
        self.grid_list = []


    def clear_board(self):
        """Clear all text on the buttons"""
        time.sleep(3)
        for button in self.button_list:
            button.config(text="")

        self.play_game_button.config(text="Take a guess!")

        # activate buttons
        for button in self.button_list:
            button.config(state=tk.NORMAL)


if __name__ == "__main__":
    root = tk.Tk()
    ships = Battleships(root, blue, light_blue, grid_label_font)
    root.mainloop()
