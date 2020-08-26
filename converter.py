import pandas as pd 

spreadsheet_data = pd.read_excel('articles.xls')

bases_data = {}

for i in range(len(spreadsheet_data)) :
    str_record = ""
    row = spreadsheet_data.iloc[i]
    row = row.fillna('') 
    #base = row['source'].replace(" ","_")
    base = row['source']
    doctype = row['document_type']

    str_bib_record = f"""
        @{doctype} {{ {row['bibtex_key']},
        language = {{{row['language']}}},
        title = {{{row['title']}}},
        journal = {{{row['journal']}}},
        author = {{{row['author']}}},
        affiliation =  {{{row['affiliation']}}},
        abstract = {{{row['abstract']}}},
        volume = {{{row['volume']}}},
        year = {{{row['year']}}},
        pages = {{{row['pages']}}},
        keywords = {{{row['keywords']}}},
        publisher = {{{row['publisher']}}},
        doi = {{{row['doi']}}},
        issn = {{{row['issn']}}},
        url = {{{row['url']}}},
        note = {{{row['note']}}} }}

    """
    #print(str_record)
    if base in bases_data :
        bases_data[base] = bases_data[base] + str_bib_record
    else :
         bases_data[base] =  str_bib_record

bases_keys = bases_data.keys()

for key in bases_keys :
    with open(key+".bib", "w", encoding='utf-8') as file :
        file.write(bases_data[key])