import spacy
import json
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "text_output.json")

with open(file_path, "r") as file:
    data = json.load(file)

nlp = spacy.load("en_core_web_sm")

