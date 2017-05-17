from typing import Iterable, List

from contracts.nodes.Node import Node
from contracts.parser.Instruction import Instruction


class Tree:
    def __init__(self, roots: Iterable[Node] = None):
        self.roots = [] if roots is None else list(roots)

    def __str__(self) -> str:
        result = []
        for root in self.roots:
            result.extend(root.str(0))
        return "\n".join(result)

    def flatten(self) -> Iterable[Instruction]:
        result: List[Instruction] = []
        for root in self.roots:
            result.extend(root.flatten())
        return result