#!/usr/bin/python
import sys
import json

def calculate_sentiment_score(text, scores):
	count = 0
	for single_word in text:
		#print single_word
		if single_word in scores.keys():
			count = count + scores[single_word]
		#	print scores[single_word]
	print count
			
def generate_sentiment_word_dict(sent_file): # this output is actually a dictionary
	score_list = {} 
	for line in sent_file:  
		term, score  = line.split("\t") # sent_file is .txt file separated by \t tab 
		score_list[term] = int(score)
	return score_list

def main():
	sent_file = open(sys.argv[1], 'r') # define argv[1] to be sentiment file
	tweet_file = open(sys.argv[2], 'r') # define argv[2] to be tweet file	
	score_list = generate_sentiment_word_dict(sent_file)

	for line in tweet_file: 
		tweet = json.loads(line) # tweet_file contains json object. json.loads() convert json object into python dictionary
		if 'text' in tweet.keys(): 
			# if the tweet contains text:
			tweet_text = str(tweet['text'].encode('utf-8')) # decode tweet from unicode, and reformatted into python string
			tweet_text_string = str.split(tweet_text) # break tweet into words
			calculate_sentiment_score(tweet_text_string, score_list) 
		else:
			# if the tweet doesn't contain text: 
			print 0

	
if __name__ == '__main__':
    main()
