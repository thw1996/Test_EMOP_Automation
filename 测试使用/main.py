

def __init__(self,is_alt=False):
    super().__init__("./images/background.png")
    if is_alt:
        self.rect.y = -self.rect.height