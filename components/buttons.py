# Component
from .component import Component

# Kivy Components
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window

# Kivy Properties
from kivy.properties import (
    BooleanProperty,
    ObjectProperty,
    ListProperty,
)

# Kivy Graphics
from kivy.graphics import (
    Color, RoundedRectangle,
    InstructionGroup,
)


class CustomButton(ButtonBehavior, Component):
    """
    # Custom Button

    This is the class that will serve as the basis for all buttons created. 
    """

    press_anim: bool = BooleanProperty(False)
    """
    ## Press Animation

    If true, the effect will be activated. 
    """
    _press_anim_instructions: InstructionGroup = ObjectProperty(None)
    """
    ## Press Animation Graphic Instruction Group
    """

    release_anim: bool = BooleanProperty(False)
    """
    ## Release Animation

    If true, the effect will be activated. 
    """
    _release_anim_instructions: InstructionGroup = ObjectProperty(None)
    """
    ## Release Animation Graphic Instruction Group
    """

    activate_color: list = ListProperty([1, 1, 1, .5])
    """
    ## Activate Color
    """

    def __init__(self, **kwargs):
        super(CustomButton, self).__init__(**kwargs)
        """
		Calling the init parent function.
		"""

        self._press_anim_instructions = InstructionGroup()
        self.canvas.after.add(self._press_anim_instructions)

        self._release_anim_instructions = InstructionGroup()
        self.canvas.after.add(self._release_anim_instructions)

        self.bind(
            on_press=self.do_press_anim,
            on_touch_move=self.do_press_anim,
            on_touch_up=self.do_release_anim,
        )
        """
        Binding Properties
        """

    def do_press_anim(self, *args) -> None:
        """
        ## Do Press Animation
        """
        self._press_anim_instructions.clear()

        if self.press_anim == True and self.collide_point(*Window.mouse_pos):
            self._press_anim_instructions.add(
                Color(*self.activate_color)
            )
            self._press_anim_instructions.add(
                RoundedRectangle(
                    pos=self.pos,
                    size=self.size,
                    radius=self.radius,
                )
            )

    def do_release_anim(self, *args) -> None:
        """
        ## Do Press Animation
        """
        self._press_anim_instructions.clear()


class IButton(CustomButton, Image):
    """
    # IButton -> Image Button 
    """
    pass


class TButton(CustomButton, Label):
    """
    # TButton -> Text Button 
    """
    pass
