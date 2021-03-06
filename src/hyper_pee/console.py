import textwrap

import click

from . import __version__, wikipedia


@click.command()
@click.option(
    "--language",
    "-l",
    default="en",
    help="language edition of wikipedia",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(language: str) -> None:
    """My hypermodern project"""
    # data = wikipedia.random_page(language=language)
    # title = data["title"]
    # extract = data["extract"]

    # click.secho(title, fg="green")
    # click.echo(textwrap.fill(extract))
    # click.echo("You are welcome!")

    page = wikipedia.random_page(language=language)

    click.secho(page.title, fg="green")
    click.echo(textwrap.fill(page.extract))
