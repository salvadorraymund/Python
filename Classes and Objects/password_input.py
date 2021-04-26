from password_checker import check_password

def friendly_check(password):
	try:
		check_password(password)
	except InvalidPasswordError as exc:
		print("Invalid password", repr(exc))

friendly_check("Helloworld")