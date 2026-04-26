class Settings:
    def __init__(self):
        self.font_size = "medium"
        self.bandwidth_mode = "normal"

    def change_font_size(self, size):
        self.font_size = size

    def enable_low_bandwidth(self):
        self.bandwidth_mode = "low"