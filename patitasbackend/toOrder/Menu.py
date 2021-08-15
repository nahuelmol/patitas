from django.db import models
from toOrder.elements import Order

class Switch:
	def __init__(self):
		self._commands = {}
		self._history = []

	@property
	def history(self):
	    return self._history

	def register(self,command_name,command):
		self._commands[command_name] = command

	def execute(self,command_name,queryset):
		if command_name in self._commands.keys():
			self._history.append((time.time(),command_name))
			self._commands[command_name].execute(queryset)
		else:
			print(f"Command [{command_name}] not recognised")



if __name__ == "__main__":
	ORDER 	= Order()

	REVERSE = OrderInReverse(ORDER)
	BUBBLE 	= OrderInBubble(ORDER)

	SWITCH = Switch()
	SWITCH.register("bubble!",  BUBBLE)
	SWITCH.register("reverse!",REVERSE)
	

	SWITCH.execute("bubble!",queryset)

	print(SWITCH.history)