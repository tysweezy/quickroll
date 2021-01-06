from random import randint
import click

dice_list = [20, 10, 6, 8]

@click.command()
@click.option('--d', type=int, default=20)
def roll(d):
    if d in dice_list:
        num_roll = randint(1, d)
        click.echo(f"Rolled: {num_roll}")
    else:
        raise Exception("Invalid dice type")


if __name__ == '__main__':
    roll()
