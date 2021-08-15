class OrderInReverse():
	def __init__(self, order, queryset):
		self._order 	= order
		self._queryset 	= queryset

	def execute(self):
		self._order.starting()
		self._order.reverse(self._queryset)
		self._order.closing()


class OrderInBubble():
	def __init__(self, order, queryset):
		self._order 	= order
		self._queryset 	= queryset

	def execute(self):
		self._order.starting()
		self._order.bubble(self._queryset)
		self._order.closing()