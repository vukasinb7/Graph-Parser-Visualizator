import json

from app_core.models import Graph, Node, Edge, KeyVal


class JsonParser:
    def __init__(self):
        self.graph = Graph()
        self.id_counter = 0
        self.node_map = {}

    def _is_tail_node(self, node_dict):
        for key in node_dict.keys():
            if isinstance(node_dict[key], dict) or isinstance(node_dict[key], list):
                return False
        return True

    def _get_attributes(self, node_dict):
        attributes = {}
        for key in node_dict.keys():
            if isinstance(node_dict[key], str):
                attributes[key] = node_dict[key]
        return attributes

    def _insert_node(self, name, data):
        node = Node(node_id=self.id_counter, name=name, graph=self.graph)
        node.save()
        for key in data.keys():
            node_data = KeyVal(node=node, key=key, value=data[key])
            node_data.save()
        self.id_counter += 1
        return node

    def create_graph(self, json_tuple, tail_node=False):
        key, value = json_tuple

        if 'references' in value.keys() and value['references'] in self.node_map.keys():
            current_node = self.node_map[value['references']]
        elif 'id' in value.keys() and value['id'] in self.node_map.keys():
            current_node = self.node_map[value['id']]
        else:
            data = self._get_attributes(value)
            current_node = self._insert_node(key, data)

        if tail_node:
            return current_node
        else:
            for key in value.keys():
                if isinstance(value[key], dict):
                    child_node = self.create_graph((key, value[key]), self._is_tail_node(value[key]))
                    edge = Edge(first_node=current_node, second_node=child_node, graph=self.graph)
                    edge.save()
                elif isinstance(value[key], list):
                    for node_dict in value[key]:
                        child_node = self.create_graph((key, node_dict), self._is_tail_node(node_dict))
                        edge = Edge(first_node=current_node, second_node=child_node, graph=self.graph)
                        edge.save()
            return current_node

    def create_node_map(self, json_tuple):
        key, value = json_tuple
        if isinstance(value, dict):
            if "id" in value.keys():
                data = self._get_attributes(value)
                node = self._insert_node(key, data)
                self.node_map[data['id']] = node
            for key in value.keys():
                if isinstance(value[key], dict) or isinstance(value[key], list):
                    self.create_node_map((key, value[key]))
        elif isinstance(value, list):
            for item in value:
                self.create_node_map((key, item))

    def load_graph(self, file_name):
        self.reset_graph()
        self.graph.save()

        f = open("upload/" + file_name)
        json_dict = json.load(f)
        print(json_dict)

        for key in json_dict.keys():
            self.create_node_map((key, json_dict[key]))
        print(self.node_map)
        for key in json_dict.keys():
            self.create_graph((key, json_dict[key]))
        self.graph.save()

    def reset_graph(self):
        Graph.objects.all().delete()
        self.graph = Graph()
        self.id_counter = 0
        self.node_map = {}
