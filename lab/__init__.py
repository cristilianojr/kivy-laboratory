# Standart
import sys

# Kivy Application
from kivy.app import App

# Kivy Components
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.window import Window

# Kivy Graphics
from kivy.graphics import (
	Line,
	Color, 
	Rectangle,
	InstructionGroup,
)

# Kivy Properties
from kivy.properties import (
	BooleanProperty,
	ListProperty,
	NumericProperty,
	ObjectProperty,
)

# Test applications
from registered_apps import _apps as applicationList

class Component(FloatLayout):
	"""
	# Component
	
	The Component class will be responsible for the visual demonstration all
	child class.
	"""

	border: bool = BooleanProperty(False)
	"""
	# Border

	If this variable is true, the line will be drawn on the edges of the screen.
	"""

	border_width: int = NumericProperty(2)
	"""
	# Border Width
	
	This variable represents how wide the edge line will be.
	"""

	border_color: ListProperty = ListProperty([1, 1, 1, 1])
	"""
	# Border Color
	
	This variable represents the color that will be drawn.
	"""

	border_instructions: InstructionGroup = ObjectProperty(None)
	"""
	# Border Instruction Group
	
	This variable represents all properties and graphical representations of the 
	screen border.
	"""

	hover: bool = BooleanProperty(False)
	"""
	# Hover
	
	If this variable is true, the rectangle will be drawn.
	"""

	hover_color: list = ListProperty([.2, .2, 1, 1]) 
	"""
	# Hover Color
	
	This variable represents the color that will be drawn.
	"""

	hover_instructions: InstructionGroup = ObjectProperty(None)
	"""
	# Hover Instruction Group
	
	This variable represents all properties and graphical representations of hover effect.
	"""

	def __init__(self, *args, **kwargs):
		super(Component, self).__init__(*args, **kwargs)
		"""
		Calling the init parent function.
		"""

		self.border_instructions = InstructionGroup()
		self.canvas.after.add(self.border_instructions)

		self.hover_instructions = InstructionGroup()
		self.canvas.after.add(self.hover_instructions)
		"""
		Predefining all variables so that they start with the appropriate or 
		defined values.
		"""

		for prop in ['pos', 'x', 'y', 'size', 'width', 'height',
					'size_hint', 'size_hint_x', 'size_hint_y', 
					'border', 'border_width', 'border_color']:

			self.fbind(prop, self.draw_border)
		"""
		Binding the properties referent the border
		"""

		Window.bind(mouse_pos = self.draw_hover)
		"""
		Binding the properties referent the hover
		"""


	def draw_border(self, *args) -> None:
		"""
		## Draw Border

		It will draw all graphic definitions in border_instructions.
		"""

		self.border_instructions.clear()
		"""
		Resetting all graphics settings, preparing for the next frame.
		"""

		if self.border == True:
			self.border_instructions.add(Color(*self.border_color))
			self.border_instructions.add(
				Line(
					rectangle=(
						self.x, self.y, 
						self.width, self.height),
					width = self.border_width
				)
			)

	def draw_hover(self, *args) -> None:
		"""
		## Draw Hover

		It will draw all graphic definitions in hover_instructions.
		"""

		self.hover_instructions.clear()
		"""
		Resetting all graphics settings, preparing for the next frame.
		"""

		if self.hover == True and self.collide_point(*Window.mouse_pos):
			self.hover_instructions.add(Color(*self.hover_color))
			self.hover_instructions.add(
				Rectangle(
					pos = self.pos, 
					size = self.size
				)
			)


class Screen(Component):
	"""
	# Screen

	The Screen class will be responsible for the visual demonstration of the 
	component being tested.

	It should show all modifications, in real time, made to the test zone.
	"""
	pass


class TestZone(Component):
	"""
	# Test Zone

	Here are all the components that will be used to modify and test the 
	selected component. 
	"""
	pass


class AppList(Component):
	"""
	# App List

	These are all items listed in labels. 
	"""

	apps: list = ListProperty([])
	"""
	
	"""

	def __init__(self, apps: list, *args, **kwargs) -> None:
		super(AppList, self).__init__(*args, **kwargs)
		"""
		Calling the init parent function.
		"""

		self.apps: list = apps 

		self.bind(
			pos = self.build_applist,
			x = self.build_applist,
			y = self.build_applist,
			size = self.build_applist,
			width = self.build_applist,
			height = self.build_applist,
			size_hint = self.build_applist,
			size_hint_x = self.build_applist,
			size_hint_y = self.build_applist,
		)

		self.build_applist()
	

	def build_applist(self, *args) -> None:

		if self.children != []:
			for wid in self.apps:
				self.remove_widget(wid[1])
		
		total_height: int = self.y + self.height

		for ap in self.apps:
			total_height -= ap[1].height

			ap[1].size_hint = .95, None
			ap[1].pos_hint = {'center_x': .5}
			ap[1].height = 30
			ap[1].y = total_height

			self.add_widget(ap[1])





class Structure(FloatLayout):
	def __init__(self, *args, **kwargs):
		super(Structure, self).__init__(*args, **kwargs)
		"""
		Calling the init parent function.
		"""

		self.build_structure()
		"""
		Here the command responsible for building the screen component is being 
		executed.
		"""

	def build_structure(self) -> None:

		self.screen: Screen = Screen()
		self.screen.border = True
		self.screen.size_hint = .6, .5
		self.screen.pos_hint = {'top': .96, 'center_x': .5}
		self.screen.border_color = [1, 0, 0, 1]

		self.zone: TestZone = TestZone()
		self.zone.border = True
		self.zone.size_hint = .9, .4
		self.zone.pos_hint = {'center_x': .5, 'y': .04}

		self.test_buttons = Component()
		self.test_buttons.border = True
		self.test_buttons.size_hint = .31, .9
		self.test_buttons.pos_hint = {'center_y': .5, 'center_x': .5}

		self.code = Component()
		self.code.border = True
		self.code.size_hint = .31, .9
		self.code.pos_hint = {'center_y': .5, 'center_x': .82}

		self.applist: AppList = AppList(applicationList)
		self.applist.border = True
		self.applist.size_hint = .31, .9
		self.applist.pos_hint = {'center_y': .5, 'center_x': .18}

		self.zone.add_widget(self.test_buttons)
		self.zone.add_widget(self.code)
		self.zone.add_widget(self.applist)

		self.add_widget(self.screen)
		self.add_widget(self.zone)


class Manager(App):
	def build(self) -> FloatLayout:
		s = Structure()
		return s


if __name__ == '__main__':
	managerclient = Manager()
	managerclient.run()
	sys.exit(managerclient)
