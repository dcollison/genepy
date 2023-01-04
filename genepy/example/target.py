class Target:
    def __init__(self, x, y):
        self.position: list[float, float] = [x, y]

    def __str__(self):
        return f"x={self.position[0]}, y={self.position[1]}"
