import xml.etree.ElementTree as ET

from app_core.models import Graph, Node, Edge, KeyVal


class XmlParser:
    def __init__(self):
        self.graph = Graph()
        self.id_counter = 0
        self.node_map = {}

    def create_graph(self, current_tag, tail_node=False):

        if 'references' in current_tag.attrib and current_tag.attrib['references'] in self.node_map.keys():
            current_node = self.node_map[current_tag.attrib['references']]
        elif 'id' in current_tag.attrib and current_tag.attrib['id'] in self.node_map.keys():
            current_node = self.node_map[current_tag.attrib['id']]
        else:
            data = current_tag.attrib
            if current_tag.text and current_tag.text.strip().replace("\n", " ") != "":
                data['value'] = current_tag.text.strip().replace("\n", " ")
            current_node = Node(node_id=self.id_counter, name=current_tag.tag, graph=self.graph)
            current_node.save()
            for key in data.keys():
                nodeData = KeyVal(node=current_node, key=key, value=data[key])
                nodeData.save()
            self.id_counter += 1

        if tail_node:
            return current_node
        else:
            for child_tag in current_tag:
                if len(list(child_tag)) == 0:
                    child_node = self.create_graph(child_tag, True)
                else:
                    child_node = self.create_graph(child_tag)
                edge = Edge(first_node=current_node, second_node=child_node, graph=self.graph)
                edge.save()
            return current_node

    def create_node_map(self, rootTag):
        if "id" not in rootTag.attrib:
            rootTag.attrib['id'] = "rootTag"
        for current_tag in rootTag.iter():
            if "id" in current_tag.attrib:
                data = current_tag.attrib
                if current_tag.text and current_tag.text.strip().replace("\n", " ") != "":
                    data['value'] = current_tag.text.strip().replace("\n", " ")
                node = Node(node_id=self.id_counter, name=current_tag.tag, graph=self.graph)
                node.save()
                for key in data.keys():
                    nodeData = KeyVal(node=node, key=key, value=data[key])
                    nodeData.save()
                self.id_counter += 1
                self.node_map[current_tag.attrib['id']] = node

    def load_graph(self, file_name):
        self.reset_graph()
        self.graph.save()

        rootTag = ET.parse("upload/" + file_name).getroot()
        self.create_node_map(rootTag)
        self.create_graph(rootTag)

        self.graph.save()

    def reset_graph(self):
        Graph.objects.all().delete()
        self.graph = Graph()
        self.id_counter = 0
        self.node_map = {}
