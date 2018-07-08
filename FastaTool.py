# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 13:02:57 2018

@author: Muzi
"""

import sys

fin_fasta=sys.argv[1]
n=int(sys.argv[2])
m=int(sys.argv[3])
fout_fasta=sys.argv[4]
#fin_list=sys.argv[2]


def extract_seq_by_id(fin_fasta, fin_list, fout_fasta):
    fasta_in=open(fin_fasta, 'r')
    ids=open(fin_list, 'r')
    fasta_out=open(fout_fasta, 'w')
    id_list=[]
    for line in ids:
        id_list.append(line.strip())
    for line in fasta_in:
        if line.startswith('>'):
            seq_id=line.strip().split(' ')[0][1:]
        if seq_id in id_list:
            fasta_out.write(line)
    fasta_in.close()
    ids.close()
    fasta_out.close()

def extract_seq_by_number(fin_fasta, n, m, fout_fasta):
    fasta_in=open(fin_fasta, 'r')
    fasta_out=open(fout_fasta, 'w')
    count=0
    for line in fasta_in:
        if line.startswith('>'):
            count=count+1
        if count>=n and count<=m:
            fasta_out.write(line)
        if count>m:
            break
    fasta_in.close()
    fasta_out.close()
        
#extract_seq_by_id(fin_fasta, fin_list, fout_fasta)
extract_seq_by_number(fin_fasta, n, m, fout_fasta)
