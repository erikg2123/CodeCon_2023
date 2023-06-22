import time
start_time = time.time()

data = 250

conversion = 7
tries = 3
kick = 2
explored = 10000

class node():
    def __init__(self, root=None, count=[0, 0, 0], score=0):
        self.root = root
        self.count = count
        self.score = score
        self.left = None
        self.middle = None
        self.right = None

class trinary_search_tree():
    def __init__(self):
        self.root = node()

        conversion_score = self.root.score + conversion

        count_conversion = self.root.count.copy()
        count_conversion[0] += 1

        # if self.root.left == None and conversion_score <= data:
        #     self.root.left = node(self.root, count_conversion, conversion_score)
            # explored.append(count_conversion)
    
    def right(self, curr_node):
        global explored
        tries_score = curr_node.score + tries
        kick_score = curr_node.score + kick

        count_conversion = curr_node.count.copy()
        count_conversion[0] += 1

        count_tries = curr_node.count.copy()
        count_tries[1] += 1

        count_kick = curr_node.count.copy()
        count_kick[2] += 1
        
        if curr_node.right == None and kick_score <= data and count_kick[2] < explored:
            new_count = curr_node.count.copy()
            new_count[2] += 1
            curr_node.right = node(curr_node, new_count, curr_node.score+kick)
            # explored.append(new_count)
            self.right(curr_node.right)

        if curr_node.middle == None and tries_score <= data and count_tries[2] < explored:
            new_count = curr_node.count.copy()
            new_count[1] += 1
            curr_node.middle = node(curr_node, new_count, curr_node.score+tries)
            # explored.append(new_count)
            self.right(curr_node.middle)

        if curr_node.score == data:
            explored = curr_node.count[2] - 2
            print(curr_node.count[0], curr_node.count[1], curr_node.count[2])
    
    def left(self, curr_node):
        global explored
        conversion_score = curr_node.score + conversion
        count_conversion = curr_node.count.copy()
        count_conversion[0] += 1

        while curr_node.left == None and conversion_score <= data:
            curr_node.left = node(curr_node, count_conversion, conversion_score)
            # explored.append(count_conversion)
            if curr_node.left.score == data:
                print(curr_node.count[0], curr_node.count[1], curr_node.count[2])
                break
            else:
                explored = 1000000000
                self.right(curr_node.left)
                print("--- %s seconds ---" % (time.time() - start_time))
            curr_node = curr_node.left

            conversion_score = curr_node.score + conversion

            count_conversion = curr_node.count.copy()
            count_conversion[0] += 1

    def _left(self, curr_node):
        print("")


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
    tree.left(tree.root)


print("--- %s seconds ---" % (time.time() - start_time))