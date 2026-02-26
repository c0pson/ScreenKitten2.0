from enum import IntEnum, StrEnum

class SIZE(IntEnum):
    TITLE_BAR = 32
    SCREEN_WIDTH = 300
    SCREEN_HEIGHT = 300

class STATE(StrEnum):
    IDLE_1     = "idle_1"
    IDLE_2     = "idle_2"
    CLEANING_1 = "cleaning_1"
    CLEANING_2 = "cleaning_2"
    RUNNING_1  = "running_1"
    RUNNING_2  = "running_2"
    SLEEPING   = "sleeping"
    WALKING    = "walking"
    JUMPING    = "jumping"
    HISSING    = "hissing"
