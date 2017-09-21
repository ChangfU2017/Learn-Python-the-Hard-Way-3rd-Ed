##Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
## dog is a Animal
class Dog (Animal):
	
	def __init__(self,name)"
	##dog has a __init_ takes self and name parameter
	self.name = name
	
##cat is a animal
Class Cat(Animal):

	def __init__(self,name)"
	##cat has a __init__ takes self and name parameter
	self.name = name
	
##person is an object
clss Person(object):

	def __init__(self, name)
		##person has a __init__ takes self and name parameter
		self.name = name
		
		#person ahs a pet of some kind
		self.pet = 	None
		
##employee is a person
class Employee (Person):
	def __init__(self,name,salary):
	##
	super(Emplyee,self).__init__(name)
	##
	self.salary= salary
	
##fish is an object
class Fish(object):
	pass

##salmon is a fish
class Salmon(Fish):
	pass
	
##halibut is a fish
class Halibut(Fish):
	pass
	
	
##rover is a dog
rover = Dog("Rover")

##satan is a cat
satan = Cat("Satan")

##mary is a person
mary = Person("Mary")

##mary has a pet named satan
mary.pet = satan

##frank is a emplyee has 120000 salary
frank = Employee("Frank",120000)

##frank has a pet called rover
frank.pet = rover

##flipper is a fish
Flipper = Fish()

##cros is a salmon
crouse = Salmon()

##harry is halibut
harry = Halibut()





	

