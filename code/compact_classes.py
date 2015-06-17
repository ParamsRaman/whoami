""" This class compacts the # of classes by
    removing those classes that do not occur
"""
import sys, codecs

# Set stdout, stdin and stderr to utf-8
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
sys.stderr = codecs.getwriter('utf-8')(sys.stderr)
sys.stdin = codecs.getreader('utf-8')(sys.stdin)

def compact(args):
    mapping = []
    inputfile = args[1]
    lines = open(inputfile, 'r')
    for line in lines:
        tokens = line.strip().split(' ', 1)
        #print tokens[0] + ", " + tokens[1]
        if int(tokens[0]) not in mapping:
            mapping.append(int(tokens[0]))
    lines.close()
    mapping.sort()
    #print str(len(mapping))
    #print mapping

    lines = open(inputfile, 'r')
    for line in lines:
        tokens = line.strip().split(' ', 1)
        print str(mapping.index(int(tokens[0]))+1) + " " + tokens[1]
    lines.close()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: python compact_classes.py <input_data_file>"
        sys.exit(0)
    compact(sys.argv)
