class Text:
    def __init__(self, text, font, pos):
        self.text = text
        self.font = font
        self.position = pos

    def render(self, win, size):
        font = self.font.get_font(size)
        txt = font.render(self.text, True, (200, 200, 200), None)
        win.blit(txt, self.position)
