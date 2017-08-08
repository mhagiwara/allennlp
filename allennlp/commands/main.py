from typing import Sequence
import argparse

import allennlp.commands.serve as serve
import allennlp.commands.bulk as bulk
import allennlp.commands.train as train

def main(raw_args: Sequence[str]) -> None:
    parser = argparse.ArgumentParser(description="Run AllenNLP", usage='%(prog)s [command]')
    subparsers = parser.add_subparsers(title='Commands', metavar='')

    # Add sub-commands
    bulk.add_subparser(subparsers)
    train.add_subparser(subparsers)
    serve.add_subparser(subparsers)

    args = parser.parse_args(raw_args)

    # If a subparser is triggered, it adds its work as `args.func`.
    # So if no such attribute has been added, no subparser was triggered,
    # so give the user some help.
    if 'func' in dir(args):
        args.func(args)
    else:
        parser.print_help()