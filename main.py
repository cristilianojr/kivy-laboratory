# Standart 
import sys

# Kivy APP
from kivy.app import App
from kivy.uix.widget import Widget


class ManagerComponents(App):
	pass

def run(component: Widget) -> None:

	def build_component(component: Widget) -> Widget:
		return component

	manager = ManagerComponents()
	manager.build = lambda: build_component(component)
	manager.run()
	sys.exit(manager)
