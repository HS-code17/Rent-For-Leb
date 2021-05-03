def get_int_input(self,msg: str, valid_inputs: list[int]):
		"""
		It asks the user for an integer input, and only returns if it matches the
		valid_inputs list
		"""
		while True:
		    try:
		        choice = int(input(msg))

		        if choice in valid_inputs:
		            return choice

		        print("Error: the value has to be from the given choices")

		    except ValueError:
		        print("Error: the input has to be an integer")


def valid_number(self,str_number):
		try:
			number = int(str_number)
		except:
			return False
		return number

def validate_pages(user_input_pages):
	while True:      # keep looping until we break out of the loop
		try:
			user_input_pages = int(input("Choose the number of pages you want to scrape: "))
			if user_input_pages <= 5:
				print("You chose:", user_input_pages)
			break    # exit the loop if the previous line succeeded
			else:
			print("choose a number smaller than 5")
		except ValueError:
			print("Please enter an integer!")