"""Draw graph for planarity analysis."""
import os.path
from matplotlib import pyplot as plt
import networkx as nx
from typing import TextIO


def path_to(filename: str):
    """Relative path to `filename` from current 'planarity.py' file."""
    try:
        basedir = os.path.dirname(__file__)
        fullpath = os.path.join(basedir, filename)
        return fullpath
    # some environemnts (like bpython) don't define '__file__',
    # so we assume that the file is in the current directory
    except NameError:
        return filename


def read_graph(*, filename: str = path_to('links.csv')):
    """Read graph from the provided file."""
    return nx.read_edgelist(filename, delimiter=',')


def draw_graph(graph: nx.Graph):
    """Draw graph and save output using Matplotlib."""

    # nodes
    position = nx.kamada_kawai_layout(graph)
    nx.draw(graph, position, with_labels=True, node_size=1000, font_size=10)


if __name__ == '__main__':
    from argparse import ArgumentParser, FileType

    # arguments
    parser = ArgumentParser('planarity.py')
    parser.add_argument('-s', '--save', dest='output', metavar='OUTPUT',
        default=None, help='Save drawing to a file, instead of showing')

    # reading input
    args = parser.parse_args()
    graph = read_graph()

    # rendering with matplolib
    draw_graph(graph)

    # presenting output
    if args.output is not None:
        plt.savefig(args.output)
    else:
        plt.show(block=True)
