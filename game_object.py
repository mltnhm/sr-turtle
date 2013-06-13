import threading

class GameObject(object):
    arena = None

    surface_name = None
    marker_info = None

    location = (0, 0)
    heading = 0

    lock = threading.RLock()

    def __init__(s, arena):
        s.arena = arena
