# Kivy Components
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stencilview import StencilView

# Components
from .component import Component


class Frame(FloatLayout, Component):
    """
    # Frame
    """
    pass


class StencilFrame(FloatLayout, Component, StencilView):
    """
    # Stencil Frame
    """
    pass
