from django.shortcuts import render

def last_first(all_set):
	print("Bubble ordering method applying, reversing")
	new_set = [1,2,3,4,5,6]
	cont = 0

	for i in reversed(all_set):
		new_set[cont] = i
		cont = cont + 1

	return new_set

def bubble_order():
	print("ordering in bubble")