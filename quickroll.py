#!/usr/bin/python3

from random import randint
import click

# dice_list = [20, 10, 6]

@click.command()
@click.option('--d', type=int, default=20)
def roll(d):
    if d == 20:
        num_roll = randint(1, 20)
        click.echo(f'rolled: {num_roll}')
    else:
        raise Exception("Invalid dice type")


if __name__ == '__main__':
    roll()
