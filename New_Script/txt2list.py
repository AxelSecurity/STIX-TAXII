import os

type = None

def main():
    my_list = []
    for line in open("/mnt/c/Users/aless/Desktop/Generate String Script STIX/sha256.txt"):
        x = line.strip('\r\n')
        my_list.append(x)

    print my_list





main()
