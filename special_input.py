# no shebang in module

"""
	that's a special input
"""


def int_input(prompt):
	'''
		allow user to input integer
	'''
	while True:
		answer = raw_input(prompt)
		try:
			answer = int(answer)
			return answer
		except ValueError:
			print("That isn't a integer dude, please try again.")
		
def float_input(prompt):
	while True:
		answer = raw_input(prompt)
		try:
			answer = float(answer)
			return answer
		except ValueError:
			print("That isn't a real number dude, please try again.")