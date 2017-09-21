from sys import argv

script, filename = argv

print " Here is your modified file"

txt = open(filename)

print txt.read()
