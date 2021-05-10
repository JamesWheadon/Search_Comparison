class PositionError(Exception):
    def __init__(self, invalid_pos):
        self.message = f"{invalid_pos} is not a possible position on this graph"