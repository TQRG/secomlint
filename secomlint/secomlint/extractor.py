import spacy
import os


class Extractor:
    def __init__(self) -> None:
        self.engine = spacy.load("en_core_web_lg")
        self.engine.remove_pipe("ner")
        self.engine.add_pipe("entity_ruler").from_disk(
            f"{os.path.dirname(os.path.abspath(__file__))}/entities/patterns.jsonl")

    def entities(self, lines):
        return [(ent.text, ent.label_, ent.ent_id_)
                for ent in self.engine('\n'.join(lines)).ents]
