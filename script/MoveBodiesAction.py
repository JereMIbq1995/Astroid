from genie_core.script.update_action import UpdateAction
from genie_core.cast.Body import Body

class MoveBodiesAction(UpdateAction):
    def __init__(self, priority):
        super().__init__(priority=priority)

    def execute(self, actors, actions, clock, callback):
        movable_actors = actors.with_traits(Body)
        for actor in movable_actors:
            actor.get_trait(Body).move()