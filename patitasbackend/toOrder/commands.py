from abc import ABCMeta, abstractstaticmethod

class Command(metaclass=ABCMeta):
        @abstractstaticmethod
        def execute():
                pass

class OrderInReverse(Command):
	def __init__(self, order, queryset):
		self._order 	= order
		self._queryset 	= queryset

	def execute(self):
		self._order.starting()
		self._order.reverse(self._queryset)
		self._order.closing()


class OrderInBubble(Command):
	def __init__(self, order, queryset):
		self._order 	= order
		self._queryset 	= queryset

	def execute(self):
		self._order.starting()
		self._order.bubble(self._queryset)
		self._order.closing()
