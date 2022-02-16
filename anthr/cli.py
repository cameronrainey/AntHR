#!/usr/bin/env python
import click
from .defaults import SERIAL, LOG

from .get_hr2 import get_hr


@click.command()
@click.option("--filename", default=None, type=str, help="Filename for the output file")
@click.option("--output_path", default=".", type=str, help="Output Directory")
def cli(filename,  output_path):
    get_hr(filename=filename, output_path=output_path)


if __name__ == "__main__":
    cli()
