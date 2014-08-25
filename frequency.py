#!/usr/bin/python
import collections 
import sys
import re
import json

def generate_tweet_list(raw_tweet_file):
	tweet_list = []
	for line in raw_tweet_file: 
		tweet = json.loads(line) # tweet_file contains json object. json.loads() convert json object into python dictionary
		if 'text' in tweet.keys(): 
			# if the tweet contains text:
			tweet_text = str(tweet['text'].encode('utf-8')) # decode tweet from unicode, and reformatted into python string
			tweet_text_string = str.split(tweet_text) # break tweet into words
			tweet_list.append(tweet_text_string)
	# print tweet_list
	return tweet_list


def generate_regular_word_list_from_tweet_list(tweet_list): 
	regular_word_list = []
	for lis in tweet_list:
		for word in lis: 
			res = re.search(r'^[A-Za-z]*$', word)
			if res != None:
				regular_word_list.append(res.group())
	return regular_word_list

def generate_word_frequency_dict(regular_word_list):
	freq = {}
	unique_word_list = list(set(regular_word_list))
	for unique_word in unique_word_list:
	    freq[unique_word] = regular_word_list.count(unique_word) / float(len(regular_word_list))
	#print freq.keys()
	return freq

'''	counts = collections.Counter(word_list)
	length = len(word_list)
	# print length
	for word in counts.keys():
		counts[word] = float(counts[word])/length
	return counts  '''

def pretty_print(word_frequency_dict):
	for word in word_frequency_dict.keys():
		print word, word_frequency_dict[word]

def main():
	raw_tweet_file = open(sys.argv[1])
	tweet_list = generate_tweet_list(raw_tweet_file)
	#print tweet_list
	regular_word_list = generate_regular_word_list_from_tweet_list(tweet_list)
	#print regular_word_list
	word_frequency_dict = generate_word_frequency_dict(regular_word_list)
	try:
   		del word_frequency_dict['']
	except KeyError:
    		pass
	#print word_frequency_dict.keys()
	# print sum(word_frequency_dict.values())
	pretty_print(word_frequency_dict)  
	

if __name__ == '__main__':
	main()



