import click

from secomlint.section import Body

class Informativeness:
    def __init__(self, message) -> None:
        self.entities = {}
        for section in message.sections:
            if not section.entities:
                continue
            if type(section).__name__ not in self.entities.keys():
                self.entities[type(section).__name__] = section.entities
            else:
                self.entities[type(section).__name__] += section.entities
        self.body = [section for section in message.sections if type(
            section) == Body][0]
        self.body_secwords = None
        self.prioritization = None
        self.detection = None
        self.assessment = None
        self.level = None

    def calculate_level(self):
        entities = []
        for key in self.entities.keys():
            entities += self.entities[key]
        # TODO: Apply rules to calculate 
        # informativeness levels
        
    def check_body(self):
        if 'Body' in self.entities.keys():
            self.body_secwords = set(
            [entity[0] for entity in self.entities['Body'] if entity[1] == 'SECWORD'])            
            
    def triage_systems(self):
        self.assessment = False
        self.prioritization = False
        self.detection = False
        for key in self.entities.keys():
            if 'CWEID' in str(self.entities[key]):
                self.assessment = True
            if 'SEVERITY' in str(self.entities[key]):
                self.prioritization = True
        

    def report(self, body, triage):
        if body:
            if self.body_secwords:
                click.echo(
                    """👍 Good to go! Extractor found the following security-related words in the message's body:""")
                for word in self.body_secwords:
                    click.echo(click.style(f"   - {word}", fg="green"))
            else:
                click.echo(
                    """🧐 The message's body is not informative enough. Try improving the message's body by adding more security related words!""")

        if triage:
            click.echo(f"Detection (D): {self.detection}")
            click.echo(f"Assessment (A): {self.assessment}")
            click.echo(f"Prioritization (P): {self.prioritization}")