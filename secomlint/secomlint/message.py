from secomlint.parser import Parser


class Message:
    def __init__(self, lines) -> None:
        self.raw_text = lines
        self.text = lines
        self.sections = []

    def get_sections(self):
        parser = Parser()
        self.sections = parser.collect_sections(self.text)
