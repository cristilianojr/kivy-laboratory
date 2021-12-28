from components import *


def test_Component(**kwargs) -> Component:
    comp = Component()
    comp.background = True
    comp.border = True

    return comp

def test_IButton(**kwargs) -> IButton:
    bt = IButton()
    bt.source = r'imgs\Kivy_logo.png'
    bt.background = True
    bt.border = True
    bt.hover = True
    bt.press_anim = True
    
    return bt


apps: dict = {
    'Component': test_Component,
    'IButton': test_IButton,
}