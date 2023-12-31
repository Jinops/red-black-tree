from rbtree_base import *
import draw_tree

class RBTreeRotate(RBTreeBase):
  def rotate_left(self, node):
    draw_tree.draw(self)
    child = node.right
    parent = node.parent

    if child.left is not None:
      child.left.parent = node

    node.right = child.left
    node.parent = child
    child.left = node
    child.parent = parent

    if parent is not None:
      if parent.left == node:
        parent.left = child
      else:
        parent.right = child
    else:
      self.root = child
    draw_tree.draw(self)

  def rotate_right(self, node):
    draw_tree.draw(self)
    child = node.left
    parent = node.parent

    if child.right is not None:
      child.right.parent = node

    node.left = child.right
    node.parent = child
    child.right = node
    child.parent = parent

    if parent is not None:
      if parent.right == node:
        parent.right = child
      else:
        parent.left = child
    else:
      self.root = child
    draw_tree.draw(self)
