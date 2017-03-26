from itertools import combinations


def pairs(iterable):
    return combinations(iterable, 2)


def get_linkage_matrix(distance_matrix):
    def distance(cluster1, cluster2):
        return min([distance_matrix[x][y] for x in cluster1 for y in cluster2])

    current_cluster_index = len(distance_matrix)
    result = []
    forest = [(i, [i]) for i in range(current_cluster_index)]
    while len(forest) > 1:
        uniting_clusters, new_distance = min((((a, b), distance(a[1], b[1])) for a, b in pairs(forest)), key=lambda x: x[1])
        new_cluster_items = uniting_clusters[0][1] + uniting_clusters[1][1]
        forest = [x for x in forest if x not in uniting_clusters]
        forest.append((current_cluster_index, new_cluster_items))
        current_cluster_index += 1
        result.append([uniting_clusters[0][0], uniting_clusters[1][0], new_distance, len(new_cluster_items)])
    return result
