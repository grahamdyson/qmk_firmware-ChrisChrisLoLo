"""QMK Bux

World domination secret weapon.
"""
from milc import cli
from milc.subcommand import config


@cli.subcommand('QMK Bux miner.', hidden=True)
def bux(cli):
    """QMK bux
    """
    if not cli.config.user.bux:
        bux = 0
    else:
        bux = cli.config.user.bux

    cli.args.read_only = False
    config.set_config('user', 'bux', bux + 1)
    cli.save_config()

    print(f"You've been blessed by the QMK gods!\nYou have {cli.config.user.bux} QMK bux.")
