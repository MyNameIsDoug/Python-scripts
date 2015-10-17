#qpy:console

"""
This script was written to run on the QPython 2.7.2 app.
"""

from operator import itemgetter

"""
The script was written to process a file representing aligned dna sequences
from a number of bacterial samples, the first number, >1, >2, >3, etc, of the 
header lines indicates the sample. The same number of aligned dna segments are
represented for each bacterial sample. These are arranged in the file so that
the first segments from each sample are all aligned with each other, similarly for 
the second segments from each sample are all aligned with each other and the 
the same for the third segments from each sample, etc.
 
Sequences of dna segments are sorted according to their sample of origin and 
concatenated so that for each sample the first segment is followed by the 
second segment followed by the third segment etc. 

The input file is a text file in the fasta format. The pathway for the input 
file, to be amended as required, is specified below.
"""

with open("/mnt/sdcard/com.hipipal.qpyplus/scripts/fasta file example.txt", "r") as myfile:

    z = []
    j = -1

    for i in myfile.readlines():
        if i[0] == ">":
            if j != -1:
                z[j][1] = "".join(z[j][1].split())
            """ 
            An additional column could be appended to the array z below.
            """
            z.append([" "," ",0])
            """
            The first column of the array z is a string representing the
            headers, he second column is a string representing a dna sequence
            and the third column is an integer representing the sample.
            """
            j = j + 1
            z[j][0] = i
            z[j][2] = int(z[j][0][z[j][0].find(">")+1:z[j][0].find(":")])
            """
            Additional data can be extracted from the header
            and inserted into an additional column as another
            sort criterion by adding a line of appropriate code here. 
            """
        else:
            z[j][1] = z[j][1] + i.replace("=","")
            
    z[j][1] = "".join(z[j][1].split())
    
    """
    If additional sort criteria have been added to z they can be used by
    specifying the column with itemgetter.
    """
    z.sort(key = itemgetter(2))
    
"""
The pathways for the output files, to be amended as required, are specified 
below.

The results.txt file contains the concatenated sequences, with a separate
header for each sample.

The headers.txt file contains a list of the headers from the input file,
sorted according to the order in which their respective sequences are 
concatenated together in the results.txt file.
"""
    	
with open("/mnt/sdcard/com.hipipal.qpyplus/scripts/example results.txt", "w") as mywritefile, open("/mnt/sdcard/com.hipipal.qpyplus/scripts/example headers.txt", "w") as myheaders:

    n = len(z)
    marker = z[0][2]

    mywritefile.write(">" + str(marker) + "\n" + z[0][1])
    myheaders.write(z[0][0])

    for j in range(1,n):
        if z[j][2] == marker:
            mywritefile.write(z[j][1])
        else:
            marker = z[j][2]
            mywritefile.write("\n" + ">" + str(marker) + "\n" + z[j][1])
        myheaders.write(z[j][0])
    