""" 
Generates libsvm dataset (with features) from csv files. Features include:
    1.
    2.
    3.
    ..
"""
import sys, codecs
import math

# Set stdout, stdin and stderr to utf-8
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
sys.stderr = codecs.getwriter('utf-8')(sys.stderr)
sys.stdin = codecs.getreader('utf-8')(sys.stdin)

def main(args):
    f_csv = args[1]
    f_train = args[2]
    print f_csv + ", " + f_train

    lines = open(f_csv, "r")
    out = open(f_train, "w")
    for line in lines:
        print "processing: " + line
        tokens = line.strip().split(",")
        first_name = tokens[1].strip()
        last_name = tokens[0].strip()
        country = tokens[2].strip()
        features = country + compute_features(first_name.lower(), last_name.lower())
        out.write(features + "\n") 
    out.close()
    lines.close()

def compute_features(first_name, last_name):
    """
    for first name, computes the following:
    1. length of string
    2. no of vowels
    3. no of consonants
    4. first letter
    5. last letter
    6-31. no of alphabet letters
    
    for last name, computes the following:
    32. length of string
    33. no of vowels
    34. no of consonants
    35. first letter
    36. last letter
    37-62. no of alphabet letters
    """
    
    #for first_name
    if first_name=="":
        result = " " + " ".join([str(i+1)+":0" for i in range(0,31)])
    else:
        result = " 1:" + str(len(first_name)) + " 2:" + str(count_vowels(first_name)) + " 3:" + str(count_conson(first_name)) + " 4:" + str(get_first(first_name)) + " 5:" + str(get_last(first_name))

        alph_count = count_alph(first_name)
        for index, count in enumerate(alph_count):
            result = result + " " + str(6+index) + ":" + str(count)

    #for last_name
    if last_name=="":
        result = " " + " ".join([str(i+1)+":0" for i in range(31,62)])
    else:
        result = " 32:" + str(len(last_name)) + " 33:" + str(count_vowels(last_name)) + " 34:" + str(count_conson(last_name)) + " 35:" + str(get_first(last_name)) + " 36:" + str(get_last(last_name))

        alph_count = count_alph(last_name)
        for index, count in enumerate(alph_count):
            result = result + " " + str(37+index) + ":" + str(count)
    

    """two_grams = get_ngrams(first_name, 2)
    for index, gram in enumerate(two_grams):
        result = result + " " + str(6+index) + ":" + gram"""

    """counter=6+len(two_grams)
    result = result + " " + str(counter+1) + ":" + str(len(last_name)) + " " + str(counter+2) + ":" + str(count_vowels(last_name)) + " " + str(counter+3) + ":" +str(count_conson(last_name)) + " " + str(counter+4) + ":" +last_name[0] + " " + str(counter+5) + ":" +last_name[-1]
    
    counter = counter+6
    two_grams = get_ngrams(last_name, 2)
    for index, gram in enumerate(two_grams):
        result = result + " " + str(counter+6+index) + ":" + gram
    """
    return result

def get_first(token):
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    return alphabets.index(token[0])

def get_last(token):
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    return alphabets.index(token[-1])

def count_alph(token):
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    alph_count = [0 for i in range(0,26)]
    for ind, t in enumerate(token):
        if t in alphabets:
            alph_count[alphabets.index(t)] = alph_count[alphabets.index(t)]+1
    #print str(alph_count)
    return alph_count

def get_ngrams(token, length):
    ngrams = []
    for i in range(0,len(token)-length+1):
        ngrams.append(token[i:i+length])
    return ngrams

def count_vowels(token):
    vowels = list("aeiou")
    number_of_vowels = sum(token.count(c) for c in vowels)
    return number_of_vowels

def count_conson(token):
    consonants = list("bcdfghjklmnpqrstvwxyz")
    number_of_consonants = sum(token.count(c) for c in consonants)
    return number_of_consonants

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "Usage: python gen_features.py "
        print "              <csv_file>"
        print "              <libsvm_train_file>"
        sys.exit(0)
    main(sys.argv)
