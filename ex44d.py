class Parent (object):

	def override(self):
		print "PARENT override()"
		
	def implicit(self):
		print "PARENT implicit()"
		
	def altered(self):
		print "PARENT altered()"
		
class Child (Parent):

	def override(self):
		print "CHILD override()"
		
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child,self).altered()
		print "CHILD, AFTER PARENT altered()"
		
dad = Parent()
son = Child()

dad.implicit()
#PARENT implicit
son.implicit()
#PARENT implicit

dad.override()
#PARENT override
son.override()
#CHILD override

dad.altered()
#PARENT altered
son.altered()
#CHILD BEFORE
#PARENT altered
#CHILD AFTER