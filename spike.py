from substring_intersect import *
import sys

# grab first 10 chars of each line in the file...
search_file = open(sys.argv[1], 'r')
contents = search_file.readlines()
search_file.close()
limit = 3

search_strings = [line[:10].replace('"', '').replace(',', '') for line in contents[:limit]]

print "Grabbed {} lines of file.".format(len(search_strings))

# now grab some substrings of the search_strings
substrings = [str[0:9] for str in search_strings]

print "Grabbed 7 chars in each search_string to use as substrings were searching for"

results = substring_intersect(substrings, search_strings)

'''
print 'substrings--'
print substrings

print 'search_strings--'
print search_strings
'''

print '-----------------'
print "Found {} matches".format(len(results))

print results