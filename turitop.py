
class Event:
	def __init__(self, game, date, time, people, status):
		self.date = date
		self.time = time
		self.game = game
		self.people = people
		self.status = status

	def __str__(self):
		return vars(self)
