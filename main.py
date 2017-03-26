from hierarchical_clustering import get_linkage_matrix
from drawer import draw_result

DISTANCE_MATRIX = [
    [0., 5., 0.5, 2.],
    [5., 0., 1., 0.6],
    [0.5, 1., 0., 2.5],
    [2., 0.6, 2.5, 0.],
]


def main():
    linkage_matrix = get_linkage_matrix(DISTANCE_MATRIX)
    draw_result(linkage_matrix)


if __name__ == '__main__':
    main()
