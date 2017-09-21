import Other
		
class Child(object):
		
	def implicit(self):
		return Other.implicit()
		
		
	def override(self):
		print "CHILD override()"
		
	def altered(self):
		print "CHILD, BEFORE altered()"
		return Other.altered()
		print "CHILD,AFTER altered9)"
		
		
		
son = Child()

son.implicit()

son.override()

son.altered()

	