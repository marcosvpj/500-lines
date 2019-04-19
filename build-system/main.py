from pprint import pprint
from collections import defaultdict

incoming = {
    'tutorial.html': {'tutorial.rst'},
    'index.html': {'index.rst'},
    'api.html': {'api.rst'},
}

outgoing = {
    'tutorial.rst': {'tutorial.html'},
    'index.rst': {'index.html'},
    'api.rst': {'api.html'},
}


class Graph:
    def __init__(self):
        self._inputs_of = defaultdict(set)
        self._consequences_of = defaultdict(set)

    def add_edge(self, input_task, consequence_task):
        """ Add a edge: `consequence_task` uses the output of `input_taks`"""
        self._consequences_of[input_task].add(consequence_task)
        self._inputs_of[consequence_task].add(input_task)

    def edges(self):
        """Return all edges as `(input_task, consequence_task)` tuples"""
        return [(a, b) for a in self._consequences_of
                for b in self._consequences_of[a]]

    def imediate_consequences_of(self, input_task):
        return self._consequences_of[input_task]


g = Graph()
g.add_edge('api.rst', 'api-title')
g.add_edge('index.rst', 'index.html')
g.add_edge('tutorial.rst', 'tutorial.html')

pprint(g.edges())
pprint(g.imediate_consequences_of('api.rst'))


g = Graph()
g.add_edge('api.rst', 'api-title')
g.add_edge('api-title', 'index.html')
g.add_edge('tutorial.rst', 'tutorial-title')
g.add_edge('tutorial-title', 'index.html')
g.add_edge('index.rst', 'index.html')

pprint(g.edges())
pprint(g.imediate_consequences_of('api.rst'))
