import json
import os
import pprint
import re
from dataclasses import dataclass


TEST_DATA_PATH = r'./eigen_task/test_docs/'
STORED_DATA_PATH = r'./json_data/'


@dataclass
class Word:
    word: str
    count: int
    documents: list
    sentances: list
    


def get_file_paths(directory):
    files = []

    for dirpath, _, file_names in os.walk(directory):
        for f in file_names:
            if '.txt' in f:
                files.append(os.path.abspath(os.path.join(dirpath, f)))

    return files

def load_data():
    data = []

    for one_file in get_file_paths(TEST_DATA_PATH):
        with open(file=one_file, mode='r', encoding='utf-8') as f:
            data.append(
                {os.path.splitext(os.path.basename(one_file))[0]: f.read()}
            )
    
    return data

def output_data_to_json_file(file_name, data):
    with open(file=file_name, mode='w', encoding='utf-8') as f:
        json.dump(data, f)

def get_word_count(data):
    word_count = {}

    for d in data:
        for k, v in d.items():
            for word in v.split():
                if word not in word_count:
                    word_count[word] = 0
                word_count[word] += 1
    
    sorted_word_count = sorted(
        word_count.items(), 
        key=lambda x: x[1], 
        reverse=True
    )

    return sorted_word_count

def get_sentances_containing_word(data, word):
    search = r"([^.]*?" + word + r"[^.]*\.)"
    sentances = re.findall(search, data)

    return sentances

def word_in_document(documents):
    doc_map = {}

    for d in documents:
        for k, v in d.items():
            for word in v.split():
                if word not in doc_map:
                    doc_map[word] = []

                if k not in doc_map[word]:
                 doc_map[word].append(k)
    
    return doc_map
               

data = load_data()

print(word_in_document(data))


words = {
    'word': '',
    'count': '',
    'documents': '',
    'sentances': '',
}

# word_count_data = get_word_count(data)

# print(word_count_data)
