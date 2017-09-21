#this one is like your script with argv
def print_two(*args):
	a1, a2 = args
	print "arg1: %r, arg2: %r" %(a1, a2)
	
#ok, that *args is actually pointless, we can just do this
def print_two_again (a1, a2):
	print "arg1: %r, arg2: %r" %(a1, a2)
	
#this takes one argument
def print_one(a1):
	print "a1: %r" %a1
	
#this one takes no argument
def print_none():
	print "I got nothing'."
	
print_two("chang","fu")
print_two_again("chang","fu")
print_one("First!")
print_none()

	