import pandas as pd

proteome = pd.read_csv("proteome.csv")
quant_vals = pd.read_csv("transcriptome_expression_isoform.tsv", sep='\t')

quant_vals = quant_vals.rename(columns={'Unnamed: 0': 'id_wo_ORF'})

def transform_id_quant(id):
    id = id.split('_')
    id = '_'.join(id for id in id[-2:])
    return id

quant_vals['id_wo_ORF'] = quant_vals['id_wo_ORF'].apply(lambda x: transform_id_quant(x))

def transform_id_proteome(id):
    id = id.split('.')[0]
    return id

proteome['id_wo_ORF'] = proteome['id'].apply(lambda x: transform_id_proteome(x))

proteome = pd.merge(proteome, quant_vals, on='id_wo_ORF')

proteome.drop(columns='id_wo_ORF', inplace=True)

proteome.to_csv("proteome.csv", index=False)