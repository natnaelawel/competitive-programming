class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
      
def check_binary_search_tree_(root):
    if root == None or (root.left == None and root.right == None):
        return True
    if root: 
        isBST = _check_binary_search_tree(root)
        return isBST

def _check_binary_search_tree(curr_node):
    # if curr_node.left:
    #     if curr_node.data < curr_node.left.data:
    #         return False
    #     elif not _check_binary_search_tree(curr_node.left):
    #         return False 
    # if curr_node.right:
    #     if curr_node.data > curr_node.right.data:
    #         return False
    #     elif not _check_binary_search_tree(curr_node.right):
    #         return False 
    # return True

    if curr_node == None or (curr_node.left == None and curr_node.right == None):
        return True

    elif curr_node.left and not curr_node.right:
        return curr_node.left.data < curr_node.data and _check_binary_search_tree(curr_node.left)

    elif curr_node.right and not curr_node.left:
        return curr_node.right.data > curr_node.data and _check_binary_search_tree(curr_node.right)

    return _check_binary_search_tree(curr_node.left) and _check_binary_search_tree(curr_node.right)
    
        