# student_population = 30
# """Creating initials for the students"""
# first = ["A", "B", "C"]
# middle = ["F", "G", "H"]
# last = ["K", "L", "M"]
# students = [(a, b, c)
#             for a in first for b in middle for c in last]
# print(students)
# courses = "C01", "C02", "C03", "C04", "C05", "C06", "C07", "C08", "C09", "C10", "C11"
# print(courses)

# section = [dict((k, v)) for k in students for v in courses]

# course_students = {
#     "C01": ["RDA", "ALB", "NAC",  "EDF", "BMG", "VLJ", "IVL", "LGM", "EGN", "KSO", "EST", "VIV"],
#     "C02": ["MCA", "EDF", "SLF", "ADG", "BCG", "AAI", "RRK", "LGM", "RLM", "JGP", "LRQ", "WAR", "KLS", "DDY"],
#     "C03": ["ABC", "BBD", "GCF", "ADG", "AKL", "BCL", "MIN", "JGP", "RSQ", "DBU", "IEY", "RAW", "ESZ"],
#     "C04": ["ANA", "JCA", "CAB", "NAC", "GCF", "GLH", "VLJ", "LLM", "MAN", "PEP", "PQQ", "ERR", "SET", "MAV", "REW"],
#     "C05": ["BBC", "EDD", "HSE", "ELG", "ISH", "JEI", "EMJ", "RRK", "TPL", "RER", "EPS", "AVU", "CDW", "ELY"],
#     "C06": ["ALA", "MCA", "ABB", "BCF", "GLH", "AKL", "HGN", "RON", "JGP", "ALQ", "EPR", "ABT", "KEV", "YEZ"],
#     "C07": ["CDC", "ISH", "ABI", "DHJ", "ESM", "FBM", "RMN", "PEP", "VIR", "JLS", "LOT", "MAV", "TEX"],
#     "C08": ["AAA", "HLA", "BBD", "WRE", "ECG", "HLH", "DHJ", "RON", "TSO", "PQQ", "MBT", "REW", "BAX", "TRY", "BDZ"],
#     "C09": ["MCA", "JCA", "BCF", "EGG", "AAI", "XTK", "WIL", "CSM", "HLO", "RSP", "APR", "RER", "JET", "DBU"],
#     "C10": ["RDA", "BBB", "CLC", "ECG", "MNH", "EMJ", "JOK", "ARM", "NFM", "EGN", "RCN", "RSP", "LEQ", "YIR", "AVU"],
#     "C11": ["ADB", "WDB", "BKC", "CLC", "SDE", "UKF", "BMG", "HRH", "BTK", "LGM", "QJP", "EPS", "KLS", "BST", "YNZ"]

# }
# print(course_students)
from collections import namedtuple

Graph = namedtuple("Graph", ["nodes", "edges"])
nodes = ["C01", "C02", "C03", "C04", "C05",
         "C06", "C07", "C08", "C09", "C10", "C11"]
edges = [
    ("C01", "C02"), ("C01", "C04"), ("C01", "C10"), ("C01", "C11"),
    ("C02", "C03"), ("C02", "C05"), ("C02", "C06"), ("C02", "C09"), ("C02", "C11"),
    ("C03", "C04"), ("C03", "C06"), ("C03", "C08"), ("C03", "C09"),
    ("C04", "C06"), ("C04", "C07"), ("C04", "C08"), ("C04", "C09"),
    ("C05", "C07"), ("C05", "C09"), ("C05", "C10"), ("C05", "C11"),
    ("C06", "C08"), ("C06", "C09"),
    ("C07", "C08"),
    ("C08", "C10"),
    ("C09", "C10"),
    ("C10", "C11"),
]

nodes_matrix = range(11)


# edges_matrix = [
#     (0, 1), (0, 1), (0, 2), (0, 2), (1, 3), (2, 3), (0, 3)
# ]

edges_matrix = [
    (0, 1), (0, 3), (0, 9), (0, 10),
    (1, 2), (1, 4), (1, 5), (1, 8), (1, 10),
    (2, 3), (2, 5), (2, 7), (2, 8),
    (3, 5), (3, 6), (3, 7), (3, 8),
    (4, 6), (4, 8), (4, 9), (4, 10),
    (5, 7), (5, 8),
    (6, 7),
    (7, 9),
    (8, 9),
    (9, 10),
]

G = Graph(nodes, edges)
Graph_matrix = Graph(nodes_matrix, edges_matrix)


def adjacency_dict(graph):
    """
    Returns the adjacency list representation
    of a graph
    """
    adj = {node: [] for node in graph.nodes}
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        # in the code below, the dict created in adj is refereced via the index of the node
        adj[node1].append(node2)
        # if the code below will not be included, edges will not repeated
        adj[node2].append(node1)
    return adj


data = adjacency_dict(G)


def adjacency_matrix(graph):
    """
    Returns the adjacency matric of a graph

    Assumes that graph.nodes is equivalent to range(len(graph.nodes))
    """
    # print(len(graph.nodes))
    adj = [[0 for node in graph.nodes]for node in graph.nodes]
    # print(adj[10])
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        # print((node1, node2))
        adj[node1][node2] += 1
        adj[node2][node1] += 1
    return adj


matrix = adjacency_matrix(Graph_matrix)
# print(matrix)

color_list = ["red", "blue", "green", "yellow"]


def algorithm_g(graph, color_list):
    """
    Creates a dictionary using color_list as key and nodes_matrix as value.
    Nodes connected to another via an edge will not be under the same key
    """
    color_dict = {color: set() for color in color_list}
    adj = {node: [] for node in graph.nodes}
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        # in the code below, the dict created in adj is refereced via the index of the node
        adj[node1].append(node2)
        # if the code below will not be included, edges will not repeated
        adj[node2].append(node1)
        # return adj
    # color_dict_length = {key: len(value) for key, value in color_dict.items()}
    for k, v in adj.items():
        nodes, edges = k, v
        print(nodes, '->', edges)
        color_dict = {color: set() for color in color_list}

        #     for edge in node:
        #         if edge not in color_dict.values():
        #             for color in color_dict:
        #                 color_dict[color].append(edge)
        # return color_dict


esp = algorithm_g(G, color_list)
