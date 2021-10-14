def create_success_msg():
	return "Ticket Booked Successfully"

def create_failure_msg()::
	return "Ticket Booking Failed."

def send_msg(email, create_message_function):
	def send(email, msg):
		# Dummy function to send an email
		print(email, msg)
	msg = create_message_function()
	send(email, msg)