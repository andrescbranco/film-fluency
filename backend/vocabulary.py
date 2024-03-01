import pandas as pd

spanish = './backend/assets/Spanish 5000.txt'
portuguese = './backend/assets/Portuguese 5000.txt'
french = './backend/assets/French 5000.txt'
japanese = './backend/assets/Japanese 5000.txt'

def spanish_vocab(spanish):
    column_names = ['Rank', 'Word', 'Part of Speech', 'English Translation', 'Phrase', 'English Phrase', 'Frequency', 'Column8']

    df_es = pd.read_csv(spanish, sep='\t', header=None, skiprows=3, names=column_names)

    df_es = df_es.iloc[:, :-2]

    df_es =df_es.head(5000)

    csv_file_path = './backend/assets/Spanish 5000.csv'
    df_es.to_csv(csv_file_path, index=False)

    print(df_es.head())

def portuguese_and_french_vocab(portuguese,french):

    column_names = ['Rank', 'Word', 'Part of Speech', 'English Translation', 'Phrase', 'English Phrase', 'Frequency', 'Column8']

    df_pt = pd.read_csv(portuguese, sep='\t', header=None, skiprows=3, names=column_names)
    df_fr = pd.read_csv(french, sep='\t', header=None, skiprows=3, names=column_names)

    df_pt = df_pt.iloc[:, :-1]
    df_pt['Frequency'] = df_pt['Frequency'].apply(lambda x: x.split('|')[0].strip())

    df_fr = df_fr.iloc[:, :-1]
    df_fr['Frequency'] = df_fr['Frequency'].apply(lambda x: x.split('|')[0].strip())

    df_pt =df_pt.head(5000)
    df_fr=df_fr.head(5000)

    csv_file_path = './backend/assets/French 5000.csv'
    csv_file_path_2 = './backend/assets/Portuguese 5000.csv'
    df_fr.to_csv(csv_file_path, index=False)
    df_pt.to_csv(csv_file_path_2, index=False)


def japanese_vocab(japanese):

    column_names = ['Kanji','Word', 'Part of Speech','English Translation', 'Phrase', 'English Phrase', 'Englsh Phrase', 'Frequency', 'Column8', 'x']

    df_jp = pd.read_csv(japanese, sep='\t', header=None, skiprows=3, names=column_names)

    df_jp = df_jp.iloc[:, :-4]

    df_jp =df_jp.head(5000)

    csv_file_path = './backend/assets/Japanese 5000.csv'
    df_jp.to_csv(csv_file_path, index=True)




# portuguese_and_french_vocab(portuguese, french)
# spanish_vocab(spanish)
# japanese_vocab(japanese)