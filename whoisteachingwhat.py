#DATA FOR COURSE 6 ONLY#

# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# from pandas import DataFrame, Series

import csv, urllib2,re
from BeautifulSoup import *
with open('who-is-teaching-what.csv','rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	courses = {}
	instructors = {}
	for row in spamreader:
		#print row
		course = row[0]
		instructor = row[-3]+ " " + row[-2]
		instructor = re.sub(r'[A-Z]\. ','', instructor)
		instructor = re.sub(r'^ ','',instructor)
		if course not in courses:courses[course] = {"Instructor":[]}
		if instructor not in instructors: instructors[instructor] = [];
		courses[course]["Instructor"].append(instructor)
		instructors[instructor].append(course)
#print courses
# df = pd.read_csv("who-is-teaching-what.csv")
# for (rowindex, Series) in df.iterrows():
# 	#print Series
# 	break


def search(*all_searches):
	for search in all_searches:
		search_type = None
		if type(search) == float:
			search = str(search)
			search_type = "course"
		elif search in instructors:
			search_type = "instructor"
		elif search in courses:
			search_type = "course"
		elif search+"J" in courses:
			search_type = "course"
			search = search+"J"
		else:
			for instructor in instructors:
				first_name = instructor.split()[0]
				last_name = instructor.split()[1]
				search_words = search.split()
				for word in search_words:
					if word == last_name:
						search_type = "instructor"
						search = instructor
					elif word == first_name:
						search_type = "instructor"
						search = instructor	
		if search_type == "course":
			print search,"Instructors:"
			print courses[search]["Instructor"]
		elif search_type == "instructor":
			print "Courses taught by "+search+":"
			print instructors[search]
		if search_type == None:
			print search, "is either invalid or unnavailable this semester"
		print ""

search("6.006","6.042","Max Goldman","6.004","6.005","Tamara Broderick")