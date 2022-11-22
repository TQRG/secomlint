"""This module abstracts the different sections of a commit message."""

class Section:
    def __init__(self) -> None:
        self.lines = []
        self.entities = []
        self.tag = None

    def set_lines(self, lines):
        self.lines = lines

    def set_entities(self, entities):
        self.entities = entities

    def set_tag(self, tag):
        self.tag = tag

    def append_line(self, line):
        self.lines += [line]


class Header(Section):
    def __init__(self, lines=None, entities=None) -> None:
        super().__init__()
        super().set_lines(lines)
        super().set_entities(entities)


class Body(Section):
    def __init__(self, lines=None, entities=None) -> None:
        super().__init__()
        super().set_lines(lines)
        super().set_entities(entities)


class Metadata(Section):
    def __init__(self, lines=None, tag=None, entities=None) -> None:
        super().__init__()
        super().set_lines(lines)
        super().set_entities(entities)
        super().set_tag(tag)


class Contact(Section):
    def __init__(self, lines=None, tag=None, entities=None) -> None:
        super().__init__()
        super().set_lines(lines)
        super().set_entities(entities)
        super().set_tag(tag)


class Bugtracker(Section):
    def __init__(self, lines=None, tag=None, entities=None) -> None:
        super().__init__()
        super().set_lines(lines)
        super().set_entities(entities)
        super().set_tag(tag)

    def add_line(self, line):
        super().append_line(line)
