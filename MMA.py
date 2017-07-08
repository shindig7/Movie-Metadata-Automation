#!/usr/bin/env python
import json
import requests
from os import *
import re

p = 'E:\\Movies\\Test'
chdir(p)

def main():
    movies = []
    collections = []

    file_list = listdir(p)
    print file_list

    for fil in file_list:
    	if isCollection(fil):
	    collections.append(fil)
	else:
	    movies.append(fil)

    print '\n'
    for f in map(collectionManager, collections):
        movies += f
    search_terms = map(searchTerm, movies)
    print search_terms
	

def isCollection(folder):
    title = re.findall(r'\(\d{4}\)', folder)
    if title:
    	return False 
    else:
	return True

def collectionManager(collection):
    col_movies = listdir(p + '\\' + collection)
    return col_movies


def searchTerm(file_name):
    spl_file = file_name.split(' ')
    spl_search = [f for f in spl_file if '[' not in f and ']' not in f]
    term = ' '.join(spl_search)
    return term

main()
