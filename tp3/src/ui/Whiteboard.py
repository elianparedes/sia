import tkinter as tk

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 700
GRID_WIDTH = 5 
GRID_HEIGHT = 7
GRID_SPACING_X = CANVAS_WIDTH // GRID_WIDTH 
GRID_SPACING_Y = CANVAS_HEIGHT // GRID_HEIGHT
PIXEL_SIZE_X = CANVAS_WIDTH // GRID_WIDTH 
PIXEL_SIZE_Y = CANVAS_HEIGHT // GRID_HEIGHT

class Whiteboard:
    def __init__(self, on_recognize):
        self.matrix = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        root = tk.Tk()

        self.root = root
        self.on_recognize = on_recognize
        self.root.title("Number Recognition")

        self.canvas = tk.Canvas(root, bg="white", width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<Button-3>", self.show_context_menu)

        self.prev_x, self.prev_y = None, None
        self.draw_grid()

        self.context_menu = tk.Menu(root, tearoff=0)
        self.context_menu.add_command(label="Delete", command=self.delete_selected)

        self.selected_item = None

        self.clear_button = tk.Button(root, text="Clear", command=self.clear_canvas)
        self.action_button = tk.Button(root, text="Recognize", command=self.execute_recognize)

        self.clear_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.action_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def start_draw(self, event):
        self.prev_x, self.prev_y = event.x, event.y
        self.draw(event)

    def draw(self, event):
        x, y = event.x, event.y

        if x < 0 or x > CANVAS_WIDTH or y < 0 or y > CANVAS_HEIGHT:
            return
        
        col = x // GRID_SPACING_X
        row = y // GRID_SPACING_Y
        self.matrix[row][col] = 1

        if self.prev_x and self.prev_y:
            col1, row1 = self.prev_x // GRID_SPACING_X, self.prev_y // GRID_SPACING_Y
            col2, row2 = col, row
            rect = self.canvas.create_rectangle(
                col1 * GRID_SPACING_X,
                row1 * GRID_SPACING_Y,
                (col2 + 1) * GRID_SPACING_X,
                (row2 + 1) * GRID_SPACING_Y,
                fill="black",
                outline="black",
            )
            self.prev_x, self.prev_y = x, y

            self.canvas.tag_bind(rect, "<Button-3>", lambda event, item=rect: self.show_context_menu(event, item))
        else:
            self.draw_single_pixel(event)

    def draw_single_pixel(self, event):
        x, y = event.x, event.y
        col, row = x // GRID_SPACING_X, y // GRID_SPACING_Y
        rect = self.canvas.create_rectangle(
            col * GRID_SPACING_X,
            row * GRID_SPACING_Y,
            (col + 1) * GRID_SPACING_X,
            (row + 1) * GRID_SPACING_Y,
            fill="black",
            outline="black",
        )

    def show_context_menu(self, event, item=None):
        self.context_menu.post(event.x_root, event.y_root)
        self.selected_item = item

    def delete_selected(self):
        if self.selected_item:
            self.canvas.delete(self.selected_item)
            self.selected_item = None

    def clear_canvas(self):
        all_items = self.canvas.find_all()
        for item in all_items:
            if item not in self.grid_lines:
                self.canvas.delete(item)
        self.matrix = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    def execute_recognize(self):
        if self.on_recognize is None:
            return
        
        matrix = [[cell for cell in row] for row in self.matrix]
        self.on_recognize(matrix)
        pass

    def draw_grid(self):
        self.grid_lines = []
        for col in range(1, GRID_WIDTH):
            x = col * GRID_SPACING_X
            line = self.canvas.create_line(x, 0, x, CANVAS_HEIGHT, fill="gray")
            self.grid_lines.append(line)
        for row in range(1, GRID_HEIGHT):
            y = row * GRID_SPACING_Y
            line = self.canvas.create_line(0, y, CANVAS_WIDTH, y, fill="gray")
            self.grid_lines.append(line)

    def show(self):
        self.root.mainloop()
    
