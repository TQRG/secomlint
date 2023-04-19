import sys
import click
import os

from secomlint.message import Message
from secomlint.config import Config
from secomlint.ruler import Ruler
from secomlint.section import Body
from secomlint.compliance import Compliance
from secomlint.informativeness import Informativeness
from secomlint.generation import Generation
from secomlint.section import Header

from tqdm import tqdm

def read_message():
    raw_message = [line.lower() for line in sys.stdin]
    message = Message(raw_message)
    message.parse()
    return message

@click.command()
@click.option("--compliance", is_flag=True, default=False, help="Show entire compliance report.")
@click.option("--score", is_flag=True, default=False, help="Show compliance score.")
@click.option("--quiet", is_flag=True, default=False, help="Show only compliance errors and warnings.")
@click.option("--generation", is_flag=True, default=False, help="Generates the commit message based on the code changes.")
@click.option("--informativeness", is_flag=True, default=False, help="Checks how informative is the body.")
# @click.option("--body", is_flag=True, default=False, help="Show how informative the message's body is.")
@click.option("--out", help="Output file name.")
@click.option("--csv", help="Run linter over a .csv of commit messages.")
@click.option("--rules-config", help="Rule configuration file path name.")
@click.option("--openai-key", help="Rule configuration file path name.")
def main(compliance, score, quiet, generation, informativeness, out, csv, rules_config, openai_key):
    """Linter to check compliance against SECOM (https://tqrg.github.io/secom/)."""
    
    if openai_key:
        config = Config(openai_key=openai_key)
        config.save_key()
    
    # if csv:
    #     df = pd.read_csv(csv, escapechar="\\")
    #     ruler = Ruler(Config(path=config))
    #     for idx, row in tqdm(df.iterrows()):
    #         commit_msg = [line.lower() for line in row['message'].split('\n')]
    #         message = Message(commit_msg)
    #         message.get_sections()
            
    #         warnings, entities = [], []
    #         for section in message.sections:
    #             warnings += ruler.compliance(section)
    #             entities += section.entities
    #         df.at[idx, 'entities'] = str(entities)
    #         df.at[idx, 'score_com'] = compliance_score(ruler, warnings)
            
    #     df.to_csv(out,
    #                 quoting=csv.QUOTE_NONNUMERIC,
    #                 escapechar="\\",
    #                 doublequote=False,
    #                 index=False)
    #     return
    
    if generation:
        click.echo(click.style("Welcome to SECOMlint!", fg='blue'))
        click.echo("Generating your security commit message...\n")
        config = Config()
        config.read_key()
        
        if config.openai_key:
            generation = Generation(config.openai_key)
            generation.run()
            generation.print()
            generation.save()
            # generation.usage()
        else:
            click.echo("⚠️  OPENAI key is not configured.\n")
            return
    
    if compliance:
        if not sys.stdin.isatty(): 
            message = read_message()
            if message.sections:
                compliance = Compliance(path=rules_config)
                compliance.check(message)
                compliance.calculate_score()
                compliance.report(quiet, score)
        
    if informativeness:
        if not sys.stdin.isatty(): 
            message = read_message()
            if message.sections:
                informativeness = Informativeness(message)
                informativeness.check_body()
                informativeness.report(True, False)

    return


if __name__ == '__main__':
    main()
