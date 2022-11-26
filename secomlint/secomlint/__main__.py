import sys
import click
import csv

import pandas as pd

from secomlint.message import Message
from secomlint.config import Config
from secomlint.ruler import Ruler
from secomlint.section import Body

from tqdm import tqdm


def compliance_score(ruler, warnings):
    no_rules = len(ruler.rules)
    rules_not_in_compliance = sum(
        [warning.result for warning in warnings])
    return ((no_rules - rules_not_in_compliance) / no_rules) * 100


def get_symbol(result, wtype, sep="  "):
    if result == 0:
        return f"✅{sep}"
    if wtype == 1:
        return f"❌{sep}"
    else:
        return f"🟡{sep}"
    

def print_summary(ruler, warnings, alerts, problems, print_score=False):
    color = 'green' if alerts == 0 and problems == 0 else 'yellow'
    summary = f"\nfound {problems} problem(s), {alerts} warning(s);"
    if print_score:
        score = compliance_score(ruler, warnings)
        secom_link = f"[\u001b]8;;https://tqrg.github.io/secom\u001b\\SECOM\u001b]8;;\u001b\\]"
        click.echo(
            click.style(
                (summary
                 + f" 🎯 Commit message is {score:.2f}% in compliance with {secom_link} convention."),
                fg=color,
                bold=True))
    else:
        click.echo(
            click.style(summary, fg=color, bold=True))


def print_body_analysis(message):
    body_section = [
        section for section in message.sections if type(section) == Body]
    if len(body_section) == 1:
        secwords, count = [], 0
        for entity in body_section[0].entities:
            entity_list = list(entity)
            if entity_list[1] == 'SECWORD':
                secwords.append(entity_list[0])
                count += 1
        if secwords:
            click.echo(
                """👍 Good to go! Extractor found the following security related words in the message's body:""")
            for word in secwords:
                click.echo(click.style(f"   - {word}", fg="green"))
        else:
            click.echo(
                """🧐 The message's body is not informative enough. Try improving the message's body by adding more security related words!""")
    else:
        click.echo(
            """❌ The message's body is missing! Don't forget the what, why and how structure.""")


@click.command()
@click.option("--no-compliance", is_flag=True, default=False, help="Show missing compliance.")
@click.option("--from-file", help="Run linter over a .csv of commit messages.")
@click.option("--out", help="Output file name.")
@click.option("--is-body-informative", is_flag=True, default=False, help="Checks body for security information.")
@click.option("--score", is_flag=True, default=False, help="Show compliance score.")
@click.option("--config", help="Rule configuration file path name.")
def main(no_compliance, from_file, out, is_body_informative, score, config):
    """Linter to check compliance against SECOM (https://tqrg.github.io/secom/)."""
    
    if from_file:
        df = pd.read_csv(from_file, escapechar="\\")
        ruler = Ruler(Config(path=config))
        for idx, row in tqdm(df.iterrows()):
            commit_msg = [line.lower() for line in row['message'].split('\n')]
            message = Message(commit_msg)
            message.get_sections()
            
            warnings, entities = [], []
            for section in message.sections:
                warnings += ruler.compliance(section)
                entities += section.entities
            df.at[idx, 'entities'] = str(entities)
            df.at[idx, 'score_com'] = compliance_score(ruler, warnings)
            
        df.to_csv(out,
                    quoting=csv.QUOTE_NONNUMERIC,
                    escapechar="\\",
                    doublequote=False,
                    index=False)
        return
    
    if not sys.stdin.isatty():
        commit_msg = [line.lower() for line in sys.stdin]
        if commit_msg:
            message = Message(commit_msg)
            message.get_sections()
            if len(message.text) > 0:
                config_ = Config(path=config)
            else:
                # TODO: raise error saying it couldn't
                # get sections or msg is empty
                return

            ruler = Ruler(config_)
            warnings = []
            for section in message.sections:
                warnings += ruler.compliance(section)

            alerts, problems = 0, 0

            # TODO: order it by (result == 1, type == 1),
            # (result == 1, type == 0), (result == 0)
            for warning in warnings:
                if warning.result == 1 and warning.type == 1:
                    click.echo(get_symbol(warning.result, warning.type)
                               + warning.message + ' ' +
                               click.style(warning.link, fg="blue"))
                    problems += 1
            for warning in warnings:
                if warning.result == 1 and warning.type == 0:
                    click.echo(get_symbol(warning.result, warning.type)
                               + warning.message + ' ' +
                               click.style(warning.link, fg="blue"))
                    alerts += 1
            if not no_compliance:
                for warning in warnings:
                    if warning.result == 0:
                        click.echo(get_symbol(warning.result, warning.type)
                                   + warning.message + ' ' +
                                   click.style(warning.link, fg="blue"))

            print_summary(ruler, warnings, alerts, problems, print_score=score)

            if is_body_informative:
                print_body_analysis(message)

    return


if __name__ == '__main__':
    main()
