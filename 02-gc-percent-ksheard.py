#create the sequence
#count the number of Cs and Gs in the sequence using count function
#count the number of nucleotides in the sequence using length function
#divide the number of nucleotides by the number of Cs and Gs
#multiply by 100 for the percentage


flu_ns1_seq = 'GTGACAAAGACATAATGGATCCAAACACTGTGTCAAGCTTTCAGGTAGATTGCTTTCTTTGGCATGTCCGCAAACGAGTTGCAGACCAAGAACTAGGTGA'
CG = flu_ns1_seq.count('C') + flu_ns1_seq.count('G')
nukes = len(flu_ns1_seq)
GCpercentage = CG/nukes
print(GCpercentage*100)
