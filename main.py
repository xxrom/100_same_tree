# 100_same_tree
from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.__dict__)


class Solution:
    def printTree(self, node: Node, output: List[int] = []) -> List[int]:
        output.append(node.val)
        if node.left:
            self.printTree(node.left, output)
        if node.right:
            self.printTree(node.right, output)

        return output

    def isSameTree(self, node0: Node, node1: Node) -> bool:
        # If one of them None, but another exist
        if (node0 == None and node1 != None) or (node0 != None and node1 == None):
            return False

        # If both is None
        if node0 == None and node1 == None:
            return True

        # If val not equal in nodes
        if node0.val != node1.val:
            return False

        # Store the answer from deeper cheking (isSameTree)
        left = True
        right = True
        if node0.left != None or node1.left != None:
            left = self.isSameTree(node0.left, node1.left)
        if node0.right != None or node1.right != None:
            right = self.isSameTree(node0.right, node1.right)

        # True if both True =)
        return left == right and left == True


tree0 = Node(1, Node(2), Node(3, None, Node(1)))
tree1 = Node(1, Node(2), Node(3, None, Node(1)))

my = Solution()
printedTree0 = my.printTree(tree0, [])
print('tree0', printedTree0)
printedTree1 = my.printTree(tree1, [])
print('tree1', printedTree1)

answer = my.isSameTree(tree0, tree1)
print('is the same tree ? = %s' % str(answer))
