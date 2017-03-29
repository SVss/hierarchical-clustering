import argparse
import numpy as np
from hierarchical_clustering import get_linkage_matrix
from drawer import draw_result


BOOK_EXAMPLE = [
    [0., 5., 0.5, 2.],
    [5., 0., 1., 0.6],
    [0.5, 1., 0., 2.5],
    [2., 0.6, 2.5, 0.],
]


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--r', dest='random_size', type=int, help='generated matrix size')
    args = argparser.parse_args()

    if args.random_size is not None:
        matrix = np.random.rand(args.random_size, args.random_size)
        matrix = (matrix + matrix.T)/2
    else:
        matrix = BOOK_EXAMPLE

    linkage_matrix = get_linkage_matrix(matrix)
    draw_result(linkage_matrix)


if __name__ == '__main__':
    main()
