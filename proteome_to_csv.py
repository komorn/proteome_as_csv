from Bio import SeqIO
import csv

input_file = "transcriptome.pep"
output_file = "proteome.csv"

with open(output_file, 'w', newline='') as csvfile:
    fieldnames = ['id', 'orf_type', 'orientation', 'orf_score', 'sequence', 'length', 'blastp', 'blastp_e-value', 'pfam', 'pfam_e-value']

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for record in SeqIO.parse(input_file, 'fasta'):
        header_parts = record.description.split(' ')
        sequence_id = record.id  # g4311_i1.p1
        sequence_id = sequence_id.split('_')
        sequence_id = '_'.join(id for id in sequence_id[-2:])
        orf_type = header_parts[4].split(':')[1]  
        orientation = header_parts[5].split(',')[0] 
        orf_score = header_parts[5].split(',')[1].split('=')[1]
        
        sequence = str(record.seq)
        length = header_parts[6].split(':')[1]

        if len(header_parts[5].split(',')) >= 3:
            blastp = header_parts[5].split(',')[2]
            blastp_evalue = header_parts[5].split(',')[2].split('|')[-1]
        if len(header_parts[5].split(',')) >= 4:
            pfam = header_parts[5].split(',')[-1].split('|')[1]
            pfam_evalue = header_parts[5].split(',')[-1].split('|')[-1]

        writer.writerow({
            'id': sequence_id,
            'orf_type': orf_type,
            'orientation': orientation,
            'orf_score': orf_score,
            'sequence': sequence,
            'length': length,
            'blastp': blastp,
            'blastp_e-value': blastp_evalue,
            'pfam': pfam,
            'pfam_e-value': pfam_evalue
        })