#!/usr/bin/env python
import click
from .defaults import SERIAL, LOG

from .get_hr import get_hr


@click.command()
@click.option("--filename", default=None, type=str, help="Filename for the output file")
@click.option("--serial", default=SERIAL, type=str, help="Serial device to use")
@click.option("--output_path", default=".", type=str, help="Output Directory")
@click.option("--driver", default=".", type=str, help="serial/usb")
def cli(filename, serial, output_path,driver):
    get_hr(filename=filename, serial=serial, output_path=output_path,driver=driver)


if __name__ == "__main__":
    cli()
