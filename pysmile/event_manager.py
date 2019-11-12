class EventManager:
    def __init__(self):
        self.handlers = {}

    def bind(self, event, callback):
        if event in self.handlers:
            self.handlers[event].append(callback)
        else:
            self.handlers[event] = [callback]

    def unbind(self, event, callback):
        if event in self.handlers:
            self.handlers[event].remove(callback)

    def trigger_event(self, event):
        if event.__class__ not in self.handlers:
            return
        [handler(event) for handler in self.handlers[event.__class__]]
