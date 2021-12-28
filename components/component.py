# Kivy Components
from kivy.uix.widget import Widget
from kivy.core.window import Window

# Kivy Porperties
from kivy.properties import (
	NumericProperty,
	ListProperty,
	BooleanProperty,
	ObjectProperty,
)

# Kivy Graphics
from kivy.graphics import (
	Line, Color,
	RoundedRectangle,
	InstructionGroup,
)


class Component(Widget):
	"""
	# Components

	This is the basis for all subcomponents of the application.
	"""

	radius: list = ListProperty([10, 10, 10, 10])
	"""
	## Radius

	Represents the curvature that the edges will have.
	"""

	background: bool = BooleanProperty(False)
	"""
	## Background

	Indicates when the background should be drawn. If true, it will be drawn. 
	"""
	background_color: list = ListProperty([.15, .15, .15, 1])
	"""
	## Backgrond Color

	Represents the background color that will be drawn. 
	"""
	_background_instructions: InstructionGroup = ObjectProperty(None)
	"""
	## Background Graphic Instruction Group
	
	"""

	border: bool = BooleanProperty(False)
	"""
	## Border
	
	"""
	border_width: int = NumericProperty(1)
	"""
	## Border width
	
	"""
	border_color: list = ListProperty([1, 1, 1, 1])
	""" 
	## Border Color
	
	Represents the border color that will be drawn. 
	"""
	_border_instructions: InstructionGroup = ObjectProperty(None)
	"""
	## Border Graphic Instruction group
	
	"""
	
	hover: bool = BooleanProperty(False)
	"""
	## Hover
	
	"""
	hover_color: list = ListProperty([.2, .2, 1, .5])
	"""
	## Hover Color
	
	Represents the hover color that will be drawn. 
	"""
	_hover_instructions: InstructionGroup = ObjectProperty(None)
	"""
	## Hover Graphic Instruction group
	
	"""
	
	def __init__(self, **kwargs):
		super(Component, self).__init__(**kwargs)
		"""
		Calling the init parent function.
		"""

		self._background_instructions = InstructionGroup()
		self.canvas.before.add(self._background_instructions)

		self._border_instructions = InstructionGroup()
		self.canvas.after.add(self._border_instructions)

		self._hover_instructions = InstructionGroup()
		self.canvas.after.add(self._hover_instructions)

		"""
		Adding the background, border and hover effect instructions on the respective canvas layer. 
		"""

		basic_properties: list = [
			'pos', 'x', 'y',
			'size', 'width', 'height',
			'size_hint', 'size_hint_x', 'size_hint_y',
			'radius', 
		]

		background_properties: list = [
			'background', 'background_color',
		]

		border_properties: list = [
			'border', 'border_width', 'border_color',
		]

		self.__bind_properties(self.do_background, *basic_properties, *background_properties)
		self.__bind_properties(self.do_border, *basic_properties, *border_properties)
		Window.bind(mouse_pos = self.do_hover)
	
	def __bind_properties(self, func, *args) -> None:
		"""
		## 
		"""
		for prop in args:
			self.fbind(prop, func)

	def do_background(self, *args) -> None:
		"""
		## Do Background
		"""
		self._background_instructions.clear()

		if self.background == True:
			self._background_instructions.add(
				Color(*self.background_color)
			)
			self._background_instructions.add(
				RoundedRectangle(
					pos = self.pos,
					size = self.size,
					radius = self.radius,
				)
			)

	def do_border(self, *args) -> None:
		"""
		## Do Border
		"""
		self._border_instructions.clear()

		if self.border == True:
			self._border_instructions.add(
				Color(*self.border_color)
			)
			self._border_instructions.add(
				Line(
					rounded_rectangle = (
						self.x, self.y,
						self.width, self.height,
						*self.radius,
					),
					width = self.border_width,
				)
			)

	def do_hover(self, *args) -> None:
		"""
		## Do Hover
		"""
		self._hover_instructions.clear()

		if self.hover == True and self.collide_point(*Window.mouse_pos):
			self._hover_instructions.add(
				Color(*self.hover_color)
			)
			self._hover_instructions.add(
				RoundedRectangle(
					pos = self.pos,
					size = self.size,
					radius = self.radius,
				)
			)
		