from gupb.controller import keyboard
from gupb.controller import random
from gupb.controller import claret_wolf

KEYBOARD_CONTROLLER = keyboard.KeyboardController()
CLARET_WOLF = claret_wolf.ClaretWolfController()

CONFIGURATION = {
    'arenas': [
        'island',
    ],
    'controllers': [
        KEYBOARD_CONTROLLER,
        CLARET_WOLF,
        random.RandomController("Alice"),
        random.RandomController("Bob"),
        random.RandomController("Cecilia"),
    ],
    'visualise': True,
    'show_sight': CLARET_WOLF,
    'runs_no': 1,
}
