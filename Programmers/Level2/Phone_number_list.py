

def solution(phone_book):

	phone_book.sort()

	for phone_number_index in range(len(phone_book) - 1):
		for the_other_phone_number_index in range(phone_number_index + 1, len(phone_book)):
			if phone_book[the_other_phone_number_index].startswith(phone_book[phone_number_index]):
				return False

	return True
