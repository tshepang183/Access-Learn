class Button:
    def render(self):
        pass

class MobileButton(Button):
    def render(self):
        return "Mobile Button"

class DesktopButton(Button):
    def render(self):
        return "Desktop Button"

class UIFactory:
    def create_button(self):
        pass

class MobileFactory(UIFactory):
    def create_button(self):
        return MobileButton()

class DesktopFactory(UIFactory):
    def create_button(self):
        return DesktopButton()