class ClickEvent:
    """Triggered by mouse collider when click detected"""

    def __init__(self, entity, buttons, position):
        self.entity = entity
        self.buttons = buttons
        self.position = position
