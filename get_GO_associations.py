#! /usr/bin/python


# This script reads through the Bstricta_278_v1.2.annotation_info.txt
# (obtained from the JGI Boechera stricta assembly files+ ' ') and creates
# a file that contains the GO associations for each str(gene as well as 
# the best TAIR10 hit symbols and defline. Note that one single column
# for GO associations is created (for use in goseq - Bioconductor+ ' '),
# so each str(gene will occur multiple times.

# Usage: ./get_GO_associations.py Bstricta_278_v1.2.annotation_info.txt
# <output_file.txt>


import sys
import re



newfile = open(sys.argv[2], 'a')
with open(sys.argv[1], 'rb') as file:
    for line in file:
        line_list = line.split('\t')
        gene = str(line_list[1] + '.v1.2')
        go_terms = line_list[9]
        tair10_symbol = line_list[11]
        tair10_defline = line_list[12]
        if len(go_terms) == 0:
            newfile.write(str(gene + '\t' + "" + '\n'))
        else:
            go_split = go_terms.split(',')
            if len(go_split) == 1:
                newfile.write(str(gene + '\t' +  go_split[0] + '\n'))
            elif len(go_split) == 2:
                newfile.write(str(gene + '\t' +  go_split[0] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[1] + '\n'))
            elif len(go_split) == 3:
                newfile.write(str(gene + '\t' +  go_split[0] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[1] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[2] + '\n'))
            elif len(go_split) == 4:
                newfile.write(str(gene + '\t' +  go_split[0] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[1] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[2] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[3] + '\n'))
            elif len(go_split) == 5:
                newfile.write(str(gene + '\t' +  go_split[0] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[1] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[2] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[3] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[4] + '\n'))
            elif len(go_split) == 6:
                newfile.write(str(gene + '\t' +  go_split[0] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[1] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[2] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[3] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[4] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[5] + '\n'))
            elif len(go_split) == 7:
                newfile.write(str(gene + '\t' +  go_split[0] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[1] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[2] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[3] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[4] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[5] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[6] + '\n'))
            elif len(go_split) == 8:
                newfile.write(str(gene + '\t' +  go_split[0] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[1] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[2] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[3] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[4] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[5] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[6] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[7] + '\n'))
            elif len(go_split) == 9:
                newfile.write(str(gene + '\t' +  go_split[0] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[1] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[2] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[3] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[4] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[5] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[6] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[7] + '\n'))
                newfile.write(str(gene + '\t' +  go_split[8] + '\n'))
            else: 
                continue


            
            
  
