
import sys, codecs
import math

# Set stdout, stdin and stderr to utf-8
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
sys.stderr = codecs.getwriter('utf-8')(sys.stderr)
sys.stdin = codecs.getreader('utf-8')(sys.stdin)

def main(args):
    f_input = args[1]
    N = int(args[2])

    lines = open(f_input, "r")
    result = {}
    for line in lines:
        tmp = get_ngrams(line.strip().lower(), N)
        for t in tmp:
            if t not in result:
                result[t]=1
            else:
                count = result[t]
                result[t] = count+1
    lines.close()

    for w in sorted(result, key=result.get, reverse=True):
        print w + "=>" + str(result[w])

    #for k,v in result.items():
    #    print k + "=>" + str(v)
    print "Total Length: " + str(len(result))

def get_ngrams(token, length):
    ngrams = []
    for i in range(0,len(token)-length+1):
        ngrams.append(token[i:i+length])
    return ngrams

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "Usage: python gen_top_ngrams.py "
        print "              <long_list>"
        print "              <n (ngram length)>"
        sys.exit(0)
    main(sys.argv)
