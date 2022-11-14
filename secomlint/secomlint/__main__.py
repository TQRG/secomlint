import click

@click.command()
def hello():
    """Simple program that greets NAME for a total of COUNT times."""
    print('hello!!!')

if __name__ == '__main__':
    hello()