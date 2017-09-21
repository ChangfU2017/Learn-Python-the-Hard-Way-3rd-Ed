print "Let's practice everything."
print 'you \'d need to know \'bout escape with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovel world
with logic so firmly planted
cannot discern \n the needs of lovel
nor comprehend passion from intuition
and requires an explannation
\n\twhere there is none.
"""

print "________________"
print poem
print "_______________"


five = 10-2+3-6
print "This should be five: %s" %five

def secret_formula(started):
	jelly_beans = started*500
	jars = jelly_beans/1000
	crates = jars/100
	return jelly_beans, jars, crates
	
	
start_point = 10000
beans, jars, crates = secret_formula(start_point)
	
print "With a starting point of : %d " %start_point
print "We'd have %d beans, %d jars and %d crates." % (beans, jars, crates)

start_point = start_point/10

print "We cna also do that this way:"
print "We'd have %d beans, %d jars and %d crates." %secret_formula(start_point)