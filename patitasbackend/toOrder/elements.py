from toOrder.controller import last_first, bubble_order

class Order:
	def starting(self):
		print("starting searching")

	def bubble(self):
		bubble_order()

	def reverse(self,queryset):
		last_first(queryset)

	def closing(self):
		print("closing searching")