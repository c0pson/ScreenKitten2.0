import ctypes
from ctypes import wintypes

def get_working_area() -> tuple[int, int]:
    SPI_GET_WORK_AREA = 0x0030
    rect = wintypes.RECT()
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_GET_WORK_AREA, 0, ctypes.byref(rect), 0
    )
    return rect.right - rect.left, rect.bottom - rect.top
