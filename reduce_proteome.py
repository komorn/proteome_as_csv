from Bio import SeqIO

proteome_cdhit_path = 'transcriptome_clst.pep'
transcriptome_path = 'transcriptome.fasta'
transcriptome_reduced_path = 'transcriptome_clst.fasta'

### Extract headers from proteome_cdhit ###
headers = []

with open(proteome_cdhit_path, 'r') as proteome:
    for record in SeqIO.parse(proteome, "fasta"):
        headers.append(record.id)


headers_short = [item.split('_') for item in headers]
headers_short = ['_'.join(sublist[6:]) for sublist in headers_short]
headers_short = [item.split('.')[0] for item in headers_short]


#search headers in transcriptome.fasta
with open(transcriptome_path, 'r') as transcriptome, open(transcriptome_reduced_path, 'w') as transcriptome_reduced:
    for record in SeqIO.parse(transcriptome, 'fasta'):
        id_short = record.id.split('_')
        id_short = '_'.join(id_short[6:]) 
        if id_short in headers_short:
            SeqIO.write(record, transcriptome_reduced, 'fasta-2line')
