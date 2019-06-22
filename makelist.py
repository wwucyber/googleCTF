import sh
from sh import bash
import sys

listencoded = [];
lineOfencoded = [];
code = [];
encoded = "";
line = "";
i = 0;
j = 0;

print ( "running");

with open('list-cities.txt') as input_file:
    with open('codes.cvs', 'w') as output_file:
        for i, line in enumerate(input_file):
            line = line.rstrip()
            if line:
                #print (line);
                #encoded = ""+ (sh.phantomjs("run.js", line));
                j = 0;
                for lineOfencoded in (sh.phantomjs("run.js", line, _iter="out")):
                    #print (j);
                    listencoded.append(lineOfencoded);
                    j += 1;
                encoded = listencoded[0].rstrip();
                listencoded[:] = [];
                #listencoded = encoded.read().isplitlines()
                #print (encoded);
                code = encoded.split('"', 4 )
                #print (code[3]);
                output = line + "," + code[3].rstrip() + "\n";
                #print (output);
                output_file.write(output)
#{"message":"1010140125015013450"}
print ( "done");
