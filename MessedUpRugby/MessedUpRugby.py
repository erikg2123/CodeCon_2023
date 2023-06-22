data = 44

conversion = 7
tries = 3
kick = 2
counts = []
explored = []

class node():
    def __init__(self, root=None, count=[0, 0, 0], score=0, binary=False):
        self.root = root
        self.count = count
        self.score = score
        self.left = None
        self.middle = None
        self.right = None
        self.binary = binary

class trinary_search_tree():
    def __init__(self):
        self.root = node()

        conversion_score = data - conversion
        tries_score = self.root.score + tries
        kick_score = self.root.score + kick

        count_conversion = self.root.count.copy()
        count_conversion[0] += 1

        count_tries = self.root.count.copy()
        count_tries[1] += 1

        count_kick = self.root.count.copy()
        count_kick[2] += 1

        if self.root.left == None and data-conversion_score >= 0:
            new_count = self.root.count.copy()
            new_count[0] += 1
            self.root.left = node(self.root, new_count, data-conversion_score)
            explored.append(new_count)

        # if self.root.middle == None and tries_score <= data:
        #     new_count = self.root.count.copy()
        #     new_count[0] += 1
        #     self.root.left = node(self.root, new_count, self.root.score+conversion)
        #     explored.append(new_count)

        # if self.root.left == None and kick_score <= data:
        #     new_count = self.root.count.copy()
        #     new_count[0] += 1
        #     self.root.left = node(self.root, new_count, self.root.score+conversion)
        #     explored.append(new_count)
    
    def right(self, curr_node):
        conversion_score = curr_node.score + conversion
        tries_score = curr_node.score + tries
        kick_score = curr_node.score + kick

        count_conversion = curr_node.count.copy()
        count_conversion[0] += 1

        count_tries = curr_node.count.copy()
        count_tries[1] += 1

        count_kick = curr_node.count.copy()
        count_kick[2] += 1
        
        if curr_node.right == None and kick_score <= data and count_kick not in explored:
            new_count = curr_node.count.copy()
            new_count[2] += 1
            curr_node.right = node(curr_node, new_count, curr_node.score+kick)
            explored.append(new_count)
            self.right(curr_node.right)

        if curr_node.middle == None and tries_score <= data and count_tries not in explored:
            new_count = curr_node.count.copy()
            new_count[1] += 1
            curr_node.middle = node(curr_node, new_count, curr_node.score+tries)
            explored.append(new_count)
            self.right(curr_node.middle)

        if curr_node.score == data:
            print(curr_node.count[0], curr_node.count[1], curr_node.count[2])
    
    def middle(self, curr_node):
        conversion_score = curr_node.score + conversion
        tries_score = curr_node.score + tries
        kick_score = curr_node.score + kick

        count_conversion = curr_node.count.copy()
        count_conversion[0] += 1

        count_tries = curr_node.count.copy()
        count_tries[1] += 1

        count_kick = curr_node.count.copy()
        count_kick[2] += 1
        
        # if curr_node.right == None and kick_score <= data and count_kick not in explored:
        #     new_count = curr_node.count.copy()
        #     new_count[2] += 1
        #     curr_node.right = node(curr_node, new_count, curr_node.score+kick)
        #     explored.append(new_count)
        #     self.middle(curr_node.right)

        if curr_node.middle == None and tries_score <= data and count_tries not in explored:
            new_count = curr_node.count.copy()
            new_count[1] += 1
            curr_node.middle = node(curr_node, new_count, curr_node.score+tries)
            explored.append(new_count)
            self.middle(curr_node.middle)

        if curr_node.left == None and conversion_score <= data and count_conversion not in explored:
            new_count = curr_node.count.copy()
            new_count[0] += 1
            curr_node.left = node(curr_node, new_count, curr_node.score+conversion)
            explored.append(new_count)
            self.middle(curr_node.left)

        if curr_node.score == data:
            print(curr_node.count[0], curr_node.count[1], curr_node.count[2])
    
    def left(self, curr_node):
        conversion_score = curr_node.score - conversion
        tries_score = curr_node.score - tries
        kick_score = curr_node.score - kick

        count_conversion = curr_node.count.copy()
        count_conversion[0] += 1

        count_tries = curr_node.count.copy()
        count_tries[1] += 1

        count_kick = curr_node.count.copy()
        count_kick[2] += 1

        if curr_node.left == None and data-conversion_score >= 0 and count_conversion not in explored:
            new_count = curr_node.count.copy()
            new_count[0] += 1
            curr_node.left = node(curr_node, new_count, curr_node.score+conversion)
            explored.append(new_count)
            self.left(curr_node.left)

        if curr_node.middle == None and data-tries_score >= 0 and count_tries not in explored:
            new_count = curr_node.count.copy()
            new_count[1] += 1
            curr_node.middle = node(curr_node, new_count, curr_node.score+tries)
            explored.append(new_count)
            self.left(curr_node.middle)
        
        if curr_node.right == None and data-kick_score >= 0 and count_kick not in explored:
            new_count = curr_node.count.copy()
            new_count[2] += 1
            curr_node.right = node(curr_node, new_count, curr_node.score+kick)
            explored.append(new_count)
            self.left(curr_node.right)

        if curr_node.score == data:
            print(curr_node.count[0], curr_node.count[1], curr_node.count[2])


    def print_tree(self, curr_node):
        if curr_node.right != None:
            self.print_tree(curr_node.right)

        if curr_node.middle != None:
            self.print_tree(curr_node.middle)

        if curr_node.left != None:
            self.print_tree(curr_node.left)
        
        if curr_node.score == data:
            print(curr_node.count[0], curr_node.count[1], curr_node.count[2])



tree = trinary_search_tree()

if data < 2:
    print(0, 0, 0)
else:
    tree.right(tree.root)
    if tree.root.left != None:
        tree.left(tree.root.left)