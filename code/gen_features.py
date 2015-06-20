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
    num_features = 0

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
        num_features = len(features.strip().split(" "))-1
    out.close()
    lines.close()
    print "num_features = " + str(num_features)

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

    for both first and last names:
    63-72. no of times freq 2grams appear
    73-82. no of times freq 3grams appear
    """
    feature_counter = 1
    result = ""
    
    #for first_name
    if first_name=="":
        result = result + " " + " ".join([str(i)+":0" for i in range(feature_counter,feature_counter+31)])
        feature_counter = feature_counter + 31
    else:
        result = result + " " + str(feature_counter) + ":" + str(len(first_name))
        feature_counter = feature_counter + 1
        result = result + " " + str(feature_counter) + ":" + str(count_vowels(first_name))
        feature_counter = feature_counter + 1
        result = result + " " + str(feature_counter) + ":" + str(count_conson(first_name))
        feature_counter = feature_counter + 1
        result = result + " " + str(feature_counter) + ":" + str(get_first(first_name))
        feature_counter = feature_counter + 1
        result = result + " " + str(feature_counter) + ":" + str(get_last(first_name))
        feature_counter = feature_counter + 1

        alph_count = count_alph(first_name)
        for index, count in enumerate(alph_count):
            result = result + " " + str(feature_counter) + ":" + str(count)
            feature_counter = feature_counter + 1
    

    #for last_name
    if last_name=="":
        result = result + " " + " ".join([str(i)+":0" for i in range(feature_counter,feature_counter+31)])
        feature_counter = feature_counter + 31
    else:
        result = result + " " + str(feature_counter) + ":" + str(len(last_name))
        feature_counter = feature_counter + 1
        result = result + " " + str(feature_counter) + ":" + str(count_vowels(last_name))
        feature_counter = feature_counter + 1
        result = result + " " + str(feature_counter) + ":" + str(count_conson(last_name))
        feature_counter = feature_counter + 1
        result = result + " " + str(feature_counter) + ":" + str(get_first(last_name))
        feature_counter = feature_counter + 1
        result = result + " " + str(feature_counter) + ":" + str(get_last(last_name))
        feature_counter = feature_counter + 1

        alph_count = count_alph(last_name)
        for index, count in enumerate(alph_count):
            result = result + " " + str(feature_counter) + ":" + str(count)
            feature_counter = feature_counter + 1
    

    #for first and last name, compute count of top10 2grams
    two_grams=["an", "ar", "ra", "na", "ma", "ri", "in", "er", "el", "ha"]
    two_grams_count = [0 for i in range(0,10)]
    tmp = get_ngrams(first_name + " " + last_name, 2)
    count = 0
    for ind, t in enumerate(tmp):
        if t in two_grams:
            two_grams_count[two_grams.index(t)] = two_grams_count[two_grams.index(t)]+1
    for ind,val in enumerate(two_grams_count):
        result = result + " " + str(feature_counter) + ":" + str(val)
        feature_counter = feature_counter + 1
    
    #for first and last name, compute count of top10 3grams
    three_grams=["ana", "ari", "mar", "ara", "and", "ina", "han", "ian", "eli", "ann"]
    three_grams_count = [0 for i in range(0,10)]
    tmp = get_ngrams(first_name + " " + last_name, 3)
    count = 0
    for ind, t in enumerate(tmp):
        if t in three_grams:
            three_grams_count[three_grams.index(t)] = three_grams_count[three_grams.index(t)]+1
    for ind,val in enumerate(three_grams_count):
        result = result + " " + str(feature_counter) + ":" + str(val)
        feature_counter = feature_counter + 1
    
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
