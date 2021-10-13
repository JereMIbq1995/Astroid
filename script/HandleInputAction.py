from genie_core.script.input_action import InputAction
from genie_core.cast.Body import Body
from genie_plugins.services.PygameKeyboardService import PygameKeyboardService
from genie_plugins.constants import keys
from cast.PlayerControlledTrait import PlayerControlledTrait
import pygame

VEL = 4

class HandleInputAction(InputAction):
    def __init__(self, priority, keyboard_service):
        super().__init__(priority)
        self._keyboard_service = keyboard_service
    
    def execute(self, actors, actions, clock, callback):
        clock.tick()
        # if self._keyboard_service.is_quit():
        #     callback.on_stop()
        pygame.event.pump()

        player_controlled_actors = actors.with_traits(PlayerControlledTrait)
        for actor in player_controlled_actors:
            keys_state = self._keyboard_service.get_keys_state(keys.LEFT, keys.RIGHT, keys.DOWN, keys.UP)
            if keys_state[keys.LEFT]:
                actor.get_trait(Body).set_vx(-VEL)
            if keys_state[keys.RIGHT]:
                actor.get_trait(Body).set_vx(VEL)
            if keys_state[keys.DOWN]:
                actor.get_trait(Body).set_vy(VEL)
            if keys_state[keys.UP]:
                actor.get_trait(Body).set_vy(-VEL)
            
            if not keys_state[keys.LEFT] and not keys_state[keys.RIGHT]:
                actor.get_trait(Body).set_vx(0)
            if not keys_state[keys.UP] and not keys_state[keys.DOWN]:
                actor.get_trait(Body).set_vy(0)