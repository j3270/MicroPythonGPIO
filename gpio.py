"""
simple module for interfacing with GPIO on ESP8266 running micropython
"""

from machine import Pin

def set(p):
    """set gpio high
    """
    gpo = Pin(p, Pin.OUT, value=1)

def clear(p):
    """set gpio to 0V
    """
    gpo = Pin(p, Pin.OUT, value=0)

def toggle(p):
    """toggle gpio from previous state
    """
    gpo = Pin(p, Pin.OUT)
    if(gpo.value()):
        gpo.value(0)
    else:
        gpo.value(1)

if __name__ == "__main__":
    version()
