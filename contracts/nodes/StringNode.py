from typing import List

from contracts.nodes.Node import Node
from contracts.tokens import Markers


class StringNode(Node):
    def __init__(self, words: List[str], parent: 'Node' = None):
        super().__init__(Markers.STRING, parent=parent)
        self.words = words

    def __str__(self):
        return "\"%s\"" % " ".join(self.words)

    def __eq__(self, other):
        result = not super().__eq__(other)
        if result is NotImplemented:
            return result
        if isinstance(other, StringNode):
            return self.words == other.words
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def clone(self) -> 'StringNode':
        return StringNode(list(self.words))
