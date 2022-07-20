import sys
import click
import linter

@click.group()
@click.version_option("0.0.1")
def main():
    """Linter for security commit messages. SECOMLINT follows the SECOM convetion (https://tqrg.github.io/secom/)."""
    pass

@main.command()
@click.argument('message', required=True)
@click.option('--all', '-a', is_flag=True, help="Print the result of all rules.")
def check(message, all):
    """Check if message follows SECOM compliance"""
    click.echo(f"💬 {message[0:150]}...\n----------------------------------------------")
    results = linter.secom(message)

    for result in results:
        if result[1] == 1:
            click.echo(f"{result[2]} " + click.style(f"[\u001b]8;;https://tqrg.github.io/secomlint/#/secomlint-rules?id={result[0].replace('_', '-')}\u001b\\{result[0]}\u001b]8;;\u001b\\]", fg="blue"))
    if all:
        for result in results:
            if result[1] == 0:
                click.echo(result[2])
    pass

if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("Wrong usage of secomlint.")
    main()