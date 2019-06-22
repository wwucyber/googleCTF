import sh
from sh import bash
import sys

listencoded = [];
encoded = "";
line = "";
i = 0;
j = 0;

with open('list-cities.txt') as input_file:
    for i, line in enumerate(input_file):
        line = line.rstrip()
        if line:
            print (line);
            #encoded = ""+ (sh.phantomjs("run.js", line));
            j = 0;
            for line in (sh.phantomjs("run.js", line, _iter="out")): # tail("-f", "/var/log/some_log_file.log", _iter=True):
                #print (j);
                listencoded.append(line);
                j += 1;
            print ( listencoded[0].rstrip())
            #listencoded = encoded.read().isplitlines()
            #print (encoded[0]);
