def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "U have %d cheeses!" %cheese_count
	print "u have %d boxed of crackers!" %boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
print "We can just give the function numbers dirctly;"
cheese_and_crackers (20,30)

print "Or, we can write variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+20,5+6)

print "And we can combine the two,variables and math:"
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)

print " Now enter how many cheese do u have?"
a = raw_input(">")
my_cheese = int(a)

print " Now enter how many crackers do u have?"
b = raw_input(">")
my_crackers = int(b)

cheese_and_crackers(my_cheese,my_crackers)