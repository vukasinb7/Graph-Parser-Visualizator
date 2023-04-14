from django.db import models


class Graph(models.Model):
    pass
    # def add_node(self, node: Node):
    #     self.nodes.append(node)
    #
    # def add_edge(self, edge: Edge):
    #     self.edges.append(edge)


class Node(models.Model):
    is_visible = models.BooleanField(default=True)
    node_id = models.IntegerField()
    name = models.CharField(max_length=100)
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE, related_name='nodes')


class KeyVal(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='data')
    key = models.CharField(max_length=240)
    value = models.CharField(max_length=240, null=True, blank=True)


class Edge(models.Model):
    is_visible = models.BooleanField(default=True)
    first_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name="exit_edges")
    second_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name="entry_edges")
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE, related_name='edges')
