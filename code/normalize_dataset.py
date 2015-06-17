import sys, codecs, numpy as np

# Set stdout, stdin and stderr to utf-8
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
sys.stderr = codecs.getwriter('utf-8')(sys.stderr)
sys.stdin = codecs.getreader('utf-8')(sys.stdin)

def normalize(args):
    mapping = []
    inputfile = args[1]
    N = int(args[2])
    M = int(args[3])
    X = np.empty([N, M]);
   
    count = 0
    lines = open(inputfile, 'r')
    for line in lines:
        tokens = line.strip().split(' ')
        features = tokens[1:]
        for f in features:
            pair = f.split(':')
            findex = int(pair[0])-1
            fvalue = float(pair[1])
            X[count][findex] = fvalue
        count = count + 1
    lines.close()
   
    for i in range(0,M):
        mean = np.mean(X[:, i])
        std = np.std(X[:, i])
        #print "old column: "
        #print X[:, i]
        #print "mean: " + str(mean) + ", std: " + str(std)
        #print ""
        
        #print "std: " + str(std)
        if std != 0:
            X[:, i] = (X[:, i] - mean)/std
        else:
            X[:, i] = (X[:, i] - mean)
            #print "special case: " + str(X[:,i])
        
        #print "new column: "
        #print X[:, i]
        #print "mean: " + str(mean) + ", std: " + str(std)
        #print ""
        #print ""
    
    lines = open(inputfile, 'r')
    count = 0
    for line in lines:
        result = ""
        tokens = line.strip().split(' ')
        result = result + tokens[0]
        features = tokens[1:]
        for f in features:
            pair = f.split(':')
            findex = int(pair[0])-1
            result = result + " " + pair[0] + ":" + str(X[count][findex])
        count = count + 1
        print result
    lines.close()


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print "Usage: python normalize_dataset.py <input_data_file> <N> <M> > <output_file>"
        sys.exit(0)
    normalize(sys.argv)
