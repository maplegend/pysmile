class Scene:
    def __init__(self, game):
        self.entities = []
        self.game = game

    def add_entity(self, ent):
        ent.scene = self
        self.entities.append(ent)

    def remove_entity(self, ent):
        self.entities.remove(ent)

    def get_entities(self):
        return self.entities

    def get_entities_with_component(self, comp):
        return [ent for ent in self.entities if ent.contains_component(comp)]