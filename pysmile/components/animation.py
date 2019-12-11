from ..component import Component
from ..events.update import UpdateEvent


class AnimationComponent(Component):
    def __init__(self, step=1, start=0, end=0, interpolate=lambda x: x, function=lambda _: None, completion=lambda: None):
        """
        Animate values
        :param start: start value
        :param end: end value
        :param interpolate: interpolation function, like y=x or y=x^2+x
        :param function: function that called every frame with progress as parameter
        :param completion: function called when animation is ended
        """
        self.step = step
        self.progress = start
        self.start = start
        self.end = end
        self.interpolate = interpolate
        self.function = function
        self.completion = completion
        self.entity = None

    def update(self, event):
        if (self.start > self.end >= self.progress + self.step) or (
                self.start <= self.end <= self.progress + self.step):
            self.function(self.interpolate(self.end))
            self.entity.remove_component(AnimationComponent)
            self.completion()
        else:
            self.progress += self.step
            self.function(self.interpolate(self.progress))

    def removed(self):
        self.entity.event_manager.unbind(UpdateEvent, self.update)

    def applied_on_entity(self, entity):
        self.entity = entity
        entity.event_manager.bind(UpdateEvent, self.update)
