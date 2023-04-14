def find_root_nodes(graph):
    root_nodes = []
    nodes = graph.nodes.all()
    global_traversed_nodes = set()
    for node in nodes:
        traversed_nodes = set()
        traverse_nodes(node, global_traversed_nodes, traversed_nodes, True)

    for node in nodes:
        if node not in global_traversed_nodes:
            root_nodes.append(node)

    return root_nodes


def traverse_nodes(node, global_traversed_nodes, traversed_nodes, is_first=False):
    if node in traversed_nodes or node in global_traversed_nodes:
        return

    if not is_first:
        global_traversed_nodes.add(node)
    traversed_nodes.add(node)

    for edge in node.exit_edges.all():
        traverse_nodes(edge.second_node, global_traversed_nodes, traversed_nodes)
