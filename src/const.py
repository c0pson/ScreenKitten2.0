from enum import IntEnum, StrEnum
import random

class SIZE(IntEnum):
    TITLE_BAR = 32
    SCREEN_WIDTH = 300
    SCREEN_HEIGHT = 300
    CAT = 256

class STATE(StrEnum):
    IDLE_1     = "idle_1"       # 
    IDLE_2     = "idle_2"       # IDLE
    CLEANING_1 = "cleaning_1"   # 
    CLEANING_2 = "cleaning_2"   # 
    RUNNING_1  = "running_1"    
    RUNNING_2  = "running_2"
    SLEEPING   = "sleeping"     # IDLE
    PLAYING    = "playing"
    JUMPING    = "jumping"      
    HISSING    = "hissing"      # INTERACTION WITH MOUSE RANDOMLY

    @staticmethod
    def random():
        return random.choice(list(STATE))

    @staticmethod
    def idle_states():
        return [STATE.PLAYING, STATE.IDLE_1, STATE.IDLE_2, STATE.CLEANING_1, STATE.CLEANING_2, STATE.SLEEPING]
    
    @staticmethod
    def fast_states():
        return [STATE.RUNNING_1, STATE.RUNNING_2]

    @staticmethod
    def walking_states():
        return [STATE.JUMPING]
