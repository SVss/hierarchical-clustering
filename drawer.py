from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram

def draw_result(linkage_matrix):
    dendrogram(linkage_matrix)
    plt.show()
