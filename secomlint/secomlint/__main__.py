import sys

import click

@click.command()
def main():
    """Simple program that greets NAME for a total of COUNT times."""
    commit_msg = [line for line in sys.stdin]
    print(''.join(commit_msg))


if __name__ == '__main__':
    main()