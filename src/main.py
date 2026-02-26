import customtkinter as ctk
import random

from utils import get_working_area
from const import SIZE
from pet_sprite import Cat

class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.window_width_pos = 40
        self.work_width, self.work_height = get_working_area()
        self.window_height_pos = self.work_height - SIZE.SCREEN_WIDTH
        self.velocity = -1
        self.max_x_position = self.work_width - SIZE.SCREEN_WIDTH + 100
        self.geometry(
            f"{SIZE.SCREEN_WIDTH}x{SIZE.SCREEN_HEIGHT}+{self.window_width_pos}+{self.window_height_pos}"
        )
        self.overrideredirect(True)
        self.attributes("-topmost", True)
        self.cat = Cat(self)
        self.cat.pack(side=ctk.BOTTOM)
        self.after(100, self.move_window)

    def move_window(self) -> None:
        if random.random() > 0.9991:
            self.velocity *= -1
        if self.window_width_pos > self.max_x_position or self.window_width_pos < -90:
            self.velocity *= -1
        self.window_width_pos += self.velocity
        self.geometry(
            f"{SIZE.SCREEN_WIDTH}x{SIZE.SCREEN_HEIGHT}+{self.window_width_pos}+{self.window_height_pos}"
        )
        self.after(10, self.move_window)

if __name__ == "__main__":
    ctk.deactivate_automatic_dpi_awareness()
    app = App()
    app.mainloop()
