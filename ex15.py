from sys import argv

script, filename = argv

#accept a parameter, return a value and give a varibale to the returned value


print "Please type your filename here:"

fileread = raw_input(">")

txt = open(fileread)

print txt.read()


print txt.close()
