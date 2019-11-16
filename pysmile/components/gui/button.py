import enum
from pysmile.component import Component
from pysmile.events.update import UpdateEvent
from pysmile.events.hover import HoverEvent
from pysmile.events.click import ClickEvent
from pysmile.components.animation import AnimationComponent
from pysmile.colors import Colors


class ButtonState(enum.Enum):
    Normal = 0
    Hovered = 1
    Clicked = 2


class ButtonComponent(Component):
    def __init__(self, shader, normal_color=Colors.white, hover_color=Colors.blue, click_color=Colors.green):
        self.entity = None
        self.hovering = False
        self.click = False
        self.click_position = (-1.0, -1.0)
        self.state = ButtonState.Normal
        self.normal_color = normal_color
        self.hover_color = hover_color
        self.click_color = click_color
        shader.uniform_click_pos = self.click_position
        shader.uniform_hover_color = hover_color.to_float()
        shader.uniform_click_color = click_color.to_float()
        shader.uniform_hover_progress = 0.0
        shader.uniform_click_progress = 1.0
        self.shader = shader

    def create_hover_animation(self, reverse=False):
        return AnimationComponent(step=-20 if reverse else 20,
                                  start=120 if reverse else 0,
                                  end=0 if reverse else 220,
                                  function=lambda x: self.shader.set_uniform("hover_progress", x / 100.0))

    def create_click_animation(self, reverse=False):
        return AnimationComponent(step=-2 if reverse else 10,
                                  start=120 if reverse else 0,
                                  end=0 if reverse else 120,
                                  function=lambda x: self.shader.set_uniform("click_progress", x / 100.0))

    def start_animation(self, anim):
        if self.entity.contains_component(AnimationComponent):
            self.entity.remove_component(AnimationComponent)

        self.entity.add_component(anim)

    def update(self, event):
        if self.hovering and self.state == ButtonState.Normal:
            self.start_animation(self.create_hover_animation(False))
            self.state = ButtonState.Hovered
        elif not self.hovering and self.state == ButtonState.Hovered:
            self.start_animation(self.create_hover_animation(True))
            self.state = ButtonState.Normal
        elif not self.hovering and self.state == ButtonState.Clicked:
            self.shader.uniform_click_pos = (-1.0, -1.0)
            self.shader.uniform_hover_progress = 0.0
            self.state = ButtonState.Normal
        elif self.click and not self.entity.contains_component(AnimationComponent):
            height = self.entity.scene.game.screen_size[1]
            self.shader.uniform_click_pos = (self.click_position[0], height - self.click_position[1])
            self.start_animation(self.create_click_animation(False))
            self.state = ButtonState.Clicked

        self.hovering = False
        self.click = False

    def hover_event(self, event):
        if event.entity == self.entity:
            self.hovering = True

    def click_event(self, event):
        if event.entity == self.entity and event.buttons[0]:
            self.click = True
            self.click_position = tuple([float(i) for i in event.position])

    def applied_on_entity(self, entity):
        self.entity = entity
        entity.event_manager.bind(UpdateEvent, self.update)
        entity.event_manager.bind(HoverEvent, self.hover_event)
        entity.event_manager.bind(ClickEvent, self.click_event)
