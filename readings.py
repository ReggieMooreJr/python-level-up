READINGS = [
    "Read Chapter 1 - Introduction to Python",
    "Read Chapter 2 - Data Structures",
    "Watch Python Functions Tutorial",
    "Read about OOP in Python",
    "Build a simple Flask API",
    "Explore deployment options"
]

def get_rotated_readings(offset):
    """Rotate the readings list based on the offset number."""
    if not READINGS:
        return []
    offset = offset % len(READINGS)
    return READINGS[offset:] + READINGS[:offset]

