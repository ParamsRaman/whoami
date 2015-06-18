""" 
Generates predictions
"""

import sys, codecs
import math
import numpy as np
from gen_features import compute_features

# Set stdout, stdin and stderr to utf-8
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
sys.stderr = codecs.getwriter('utf-8')(sys.stderr)
sys.stdin = codecs.getreader('utf-8')(sys.stdin)

def main(args):
    f_model = args[1]
    f_mapping = args[2]
    query = args[3]

    mapping = []
    lines = open(f_mapping, "r")
    for line in lines:
        mapping.append(int(line.strip()))
    lines.close()
    print "mapping: " + str(mapping)

    first_name = query.strip().split(" ")[0]
    last_name = query.strip().split(" ")[1]
    features = compute_features(first_name.lower(), last_name.lower())
    print "first_name: " + first_name + ", last_name: " + last_name
    print "features: " + features
    tokens = features.strip().split(" ")
    M = len(tokens)
    X = np.empty([M, 1])
    for ind,t in enumerate(tokens):
        X[ind][0] = float(t.split(":")[1])
   
    K = 32
    W = np.empty([K, M])
    lines = open(f_model, "r")
    counter = 0
    for line in lines:
        tokens = line.strip().split(" ")
        tokens = tokens[1:]
        for ind,t in enumerate(tokens):
            W[counter][ind] = float(t.split(":")[1])
        counter = counter + 1
    lines.close()

    print "X: " + str(X)
    print "W: " + str(W)

    XP = np.exp(np.dot(W,X))
    print "XP: " + str(XP)
    print "max: " + str(np.max(XP))
    argmax = np.argmax(XP)
    print "argmax: " + str(argmax)
    print "prediction: " + str(mapping[argmax-1])

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print "Usage: python predict.py "
        print "              <model_file>"
        print "              <mapping_file>"
        print "              <query>"
        sys.exit(0)
    main(sys.argv)
