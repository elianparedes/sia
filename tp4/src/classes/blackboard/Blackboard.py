import ast
import csv
import tkinter as tk
from tkinter import Canvas, Entry
import numpy as np
import pandas as pd


class Blackboard(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Blackboard")
        self.canvas_size = 200
        self.grid_size = 5
        self.cell_size = self.canvas_size / self.grid_size

        self.canvas = Canvas(self, width=self.canvas_size, height=self.canvas_size, bg='white')
        self.canvas.pack(pady=20)

        self.canvas.bind("<B1-Motion>", self.paint)      # Left click to paint
        self.canvas.bind("<Button-1>", self.paint)
        self.canvas.bind("<Button-3>", self.erase)      # Right click to erase

        self.path_entry = Entry(self, width=30)
        self.path_entry.pack(pady=10)
        self.path_entry.insert(0, 'path_to_file.txt')

        btn_save_to_file = tk.Button(self, text="Save to File", command=self.save_to_file)
        btn_save_to_file.pack(pady=10)

        btn_clear = tk.Button(self, text="Clear", command=self.clear_canvas)
        btn_clear.pack(pady=10)

        self.initialize_canvas()

    def initialize_canvas(self):
        self.matrix = -np.ones((self.grid_size, self.grid_size), dtype=int)
        self.canvas.delete("all")
        self.draw_grid()

    def draw_grid(self):
        for i in range(self.grid_size):
            self.canvas.create_line(i * self.cell_size, 0, i * self.cell_size, self.canvas_size, fill='gray')
            self.canvas.create_line(0, i * self.cell_size, self.canvas_size, i * self.cell_size, fill='gray')

    def paint(self, event):
        x = int(event.x // self.cell_size)
        y = int(event.y // self.cell_size)
        self.canvas.create_rectangle(x*self.cell_size, y*self.cell_size, (x+1)*self.cell_size, (y+1)*self.cell_size, fill='black', width=1, outline='gray')
        self.matrix[y, x] = 1

    def erase(self, event):
        x = int(event.x // self.cell_size)
        y = int(event.y // self.cell_size)
        self.canvas.create_rectangle(x*self.cell_size, y*self.cell_size, (x+1)*self.cell_size, (y+1)*self.cell_size, fill='white', width=1, outline='gray')
        self.matrix[y, x] = -1

    def clear_canvas(self):
        self.initialize_canvas()

    def save_to_file(self):
        path = self.path_entry.get()
        with open(path, 'a') as f:
            f.write(str(self.matrix.tolist()) + '\n')


if __name__ == "__main__":
    app = Blackboard()
    app.mainloop()


