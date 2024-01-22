#!pip install pubchempy
#!pip install pandas
import pubchempy as pcp
import pandas as pd

# Получение PubChem CID для каждой молекулы
molecule_identifiers = [pcp.get_cids(molecule, record_type='3d')[0] for molecule in ['Aspirin', 'oleate', 'citric acid', 'tetramethylethylenediamine', 'glyoxaline-5-alanine', '(2R)-2-amino-3-sulfanylpropanoic acid', 'BSA', 'ethylene glycol', '56-84-8', '(2S)-2-aminobutanedioic acid']]

# Загрузка данных
pcp.download('CSV', 's1.csv', molecule_identifiers, operation='property/IsomericSMILES,xlogP,MolecularWeight,Complexity,TPSA', overwrite=True)

# Чтение данных из CSV файла
df = pd.read_csv('s1.csv')
print(df)


