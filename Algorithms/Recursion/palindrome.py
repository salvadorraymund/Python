# Non-recursive
def is_palindrome(word):
    """Return True if word is a palindrome; False if not."""
    return word == word[::-1]


print(is_palindrome("civic"))

# Recursive
def palindrome(word):
	if len(word) <= 1:
		return True
	else:
		return word[0] == word[-1] and is_palindrome(word[1:-1])

print(palindrome("foo"))
