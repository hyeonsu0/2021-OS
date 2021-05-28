#!/usr/bin/python3
# 2021-05-18 soo

import re
import requests
import sys
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch

es_host="127.0.0.1"
es_port="9200"

def getText(url):
	result = ""
	taglist = ['div', 'a', 'p', 'h1', 'h2', 'h3', 'h4', 'h5']
	res = requests.get(url)
	html = BeautifulSoup(res.content, "html.parser")
	for tag in taglist:
		for string in html.find_all(tag):
			result+= string.get_text()
	return result
		
def remove_word(word_list):
	result = []
	symbols = """!@#$%^&*()_-+={[}]|\;:" `'<>?/.,"""
	for word in word_list:
		for i in range(len((symbols))):
			word = word.replace(symbols[i], '')
		if len(word) > 0:
			result.append(word)
	return result

def count_word(word_list):
	word_count = {}
	for word in word_list:
		if word in word_count:
			word_count[word]+=1
		else:
			word_count[word] = 1
	return word_count

if __name__ == '__main__':
	es = Elasticsearch([{'host':es_host, 'port':es_port}], timeout=30)
	es_index = 'web'
	es_type = 'words'

	url = u'https://en.wikipedia.org/wiki/Web_crawler'
	word_list = getText(url).lower().split()
	word_list = remove_word(word_list)
	word_count = count_word(word_list)
	words = list(word_count)
	count = list(word_count.values())
	doc = {
		"url":url,
		"words":words,
		"frequencies":count
	}
	print(words[0])
	res = es.index(index=es_index, doc_type=es_type, body = doc)
	print(res)

	
