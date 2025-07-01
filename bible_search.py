# Using the XML Bibles from: https://github.com/Beblia/Holy-Bible-XML-Format/tree/master 
import os
import nltk
import json
import string
from nltk.tokenize import word_tokenize, sent_tokenize
import xml.etree.ElementTree as ET

# nltk.download('punkt')  

def get_bible_results(query, bible_version):

    working_dir = os.getcwd()
    path = os.path.join(working_dir, "source", bible_version+".xml")
    
    tree = ET.parse(path)
    root = tree.getroot()

    tokens = word_tokenize(query)
    tokens = [token for token in tokens if token not in string.punctuation]

    print("Tokens:", tokens)

    final_dict = {token: {"no_hits": 0, "hits": [], "in_bible" : False} for token in tokens}

    for token in tokens:
        for testament in root:
            for book in testament:
                for chapter in book:
                    for verse in chapter:
                        if verse.text and token in word_tokenize(verse.text):
                            print(f"Stelle gefunden für Token '{token}'!")
                            data = (
                                verse.text.strip(),
                                "Testament: " + testament.attrib.get('name', ''),
                                "Buch: " + book.attrib.get('number', ''),
                                "Kapitel: " + chapter.attrib.get("number", ''),
                                "Vers: " + verse.attrib.get("number", '')
                            )
                            final_dict[token]["hits"].append(data)
                            final_dict[token]["no_hits"] += 1
                            final_dict[token]["in_bible"] = True

    return final_dict

