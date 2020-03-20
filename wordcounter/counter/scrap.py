import requests 
from bs4 import BeautifulSoup 
import operator 
from collections import Counter 

def start(url):
    word_count = {}
    clean_list =[] 
    wordlist = [] 
    source_code = requests.get(url).text 
    soup = BeautifulSoup(source_code, 'html.parser') 
    for each_text in soup.findAll('p'): 
        content = each_text.text 
        words = content.lower().split() 
        for each_word in words: 
            wordlist.append(each_word)

    for word in wordlist:
        symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '
        for i in range (0, len(symbols)):
            word = word.replace(symbols[i], '') 
        if len(word) > 0: 
            clean_list.append(word)
    common_list=['a','an','the','are','is','for','of','these','there','all',
    'and','as','to','by','in','that','there','was','true','etc','or','not','many','be','it','can','this','has','have','had','which']
    for word in clean_list:
        if word in common_list:
            pass 
        elif word in word_count: 
            word_count[word] += 1
        else: 
            word_count[word] = 1
    c = Counter(word_count) 
    top = c.most_common(10)
    return top