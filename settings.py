class Settings:
    def __init__(self, Width, Height, fps=7):
        self.Grid_Width = Width // 20
        self.Grid_Height = Height // 20
        self.Cell_Size = 20
        self.FPS = fps
        self.WIDTH = Width
        self.HEIGHT = Height
        self.SCORE = 0
        self.color_food = (255, 0, 0)