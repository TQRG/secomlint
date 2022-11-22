import spacy
import os


class Extractor:
    def __init__(self) -> None:
        self.nlp = spacy.load("en_core_web_lg")
        self.nlp.remove_pipe("ner")
        self.nlp.add_pipe("entity_ruler").from_disk(
            f"{os.path.dirname(os.path.abspath(__file__))}/entities/patterns.jsonl")

    def extract_entities(self, lines):
        return [(ent.text, ent.label_, ent.ent_id_)
                for ent in self.nlp('\n'.join(lines)).ents]
