"""Module for aircraft flights."""


class Flight:
	"""A Flight with a particular pasenger aircraft."""
	
	def __init__(self, number, aircraft):
		"""Is an Initializer for a Constructor as the
		Object is already created before it is called.
		"""
		if not number[:2].isalpha():
			raise ValueError(f"No airline code in '{number[:2]}'")
		if not number[:2].isupper():
			raise ValueError(f"Invalid aircode '{number[:2]}'")
		if not number[2:].isdigit():
			raise ValueError(f"Invalid route number '{number[2:]}'")
		self._number = number
		self._aircraft = aircraft
		rows, seats = self._aircraft.seating_plan()
		self._seating = [None,]
	
	def number(self):
		return self._number
		
	def aircraft_model(self):
		return self._aircraft.model()
		
	def airline(self):
		return self._number[:2]
		

class Aircraft:

	def __init__(self, registration, model, num_rows, num_seats_per_row):
		self._registration = registration
		self._model = model
		self._num_rows = num_rows
		self._num_seats_per_row = num_seats_per_row
		
	def registration(self):
		return self._registration
		
	def model(self):
		return self._model
		
	def seating_plan(self):
		return (range(1,self._num_rows +1),
				"ABCDEFGHJK"[:self._num_seats_per_row])