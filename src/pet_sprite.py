import customtkinter as ctk
from PIL import Image, ImageOps
import os
from copy import deepcopy

from const import STATE

class Cat(ctk.CTkLabel):
    def __init__(self, master) -> None:
        super().__init__(master, text="")
        self.cat_actions: dict[str, tuple[int, list[ctk.CTkImage]]] = {
            STATE.IDLE_1     : (4, []),
            STATE.IDLE_2     : (4, []),
            STATE.CLEANING_1 : (4, []),
            STATE.CLEANING_2 : (4, []),
            STATE.RUNNING_1  : (8, []),
            STATE.RUNNING_2  : (8, []),
            STATE.SLEEPING   : (4, []),
            STATE.WALKING    : (6, []),
            STATE.JUMPING    : (7, []),
            STATE.HISSING    : (8, []),
        }
        self.cat_actions_reversed: dict[str, tuple[int, list[ctk.CTkImage]]] = {
            STATE.IDLE_1     : (4, []),
            STATE.IDLE_2     : (4, []),
            STATE.CLEANING_1 : (4, []),
            STATE.CLEANING_2 : (4, []),
            STATE.RUNNING_1  : (8, []),
            STATE.RUNNING_2  : (8, []),
            STATE.SLEEPING   : (4, []),
            STATE.WALKING    : (6, []),
            STATE.JUMPING    : (7, []),
            STATE.HISSING    : (8, []),
        }
        self.load_sprites()
        self.configure(
            require_redraw=True,
            image=self.get_sprite(STATE.WALKING, 0)
        )
        self.animate(STATE.RUNNING_1)

    def load_sprites(self) -> None:
        sprites = Image.open(os.path.join("assets", "Cat_Sprite_Sheet.png"))
        for i, (state, (frame_count, frames)) in enumerate(self.cat_actions.items()):
            row = i*32
            for frame in range(frame_count):
                sprite = sprites.crop((frame * 32, row, frame * 32 + 32, row + 32))
                sprite = sprite.resize((256, 256), Image.Resampling.NEAREST)
                sprite_reversed = ImageOps.mirror(sprite)
                frames.append(ctk.CTkImage(sprite, sprite, sprite.size))
                self.cat_actions_reversed[state][1].append(ctk.CTkImage(sprite_reversed, sprite_reversed, sprite_reversed.size))

    def get_sprite(self, state: STATE, frame: int) -> ctk.CTkImage:
        if self.master.velocity == -1:
            return self.cat_actions_reversed[state][1][frame]
        if self.master.velocity == 1:
            return self.cat_actions[state][1][frame]

    def animate(self, state: STATE, frame: int=0) -> None:
        if frame > self.cat_actions[state][0]-1:
            frame = 0
        self.configure(
            require_redraw=True,
            image=self.get_sprite(state, frame)
        )
        self.after(125, lambda: self.animate(state, frame+1))
