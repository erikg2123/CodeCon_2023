count = 0
possibilities = 0

class node:
    def __init__(self, parent=None, s=""):
        self.parent = parent
        self.substring = s
        self.parent_children = []
        self.children = []
        
class tree_search:
    def __init__(self, S):
        self.root = node()
        self.len_S = len(S)

    def insert(self, S, curr_node):
        global count
        global possibilities
        for i, s in enumerate(S):
            if curr_node.parent_children is None or curr_node.substring+s not in curr_node.parent_children:
                curr_node.children.append(node(curr_node, curr_node.substring+s))
                curr_node.parent_children.append(curr_node.substring + s)
                if len(curr_node.children[-1].substring) == self.len_S:
                    possibilities += 1
                    # if isPalandrome(curr_node.children[-1].substring):
                    #     count += 1
                        # print("!!!!!!!!!!!1")
                else:
                    self.insert(S[:i]+S[i+1:], curr_node.children[-1])
    # def _insert(self, S):
    #     for s in S:

def canBePalindrome(S):
    S_dict = {}
    outlier = 0
    string = ""

    for c in S:
        if c not in S_dict.keys():
            S_dict[c] = {'count': 1}
            outlier -= 1
        else:
            S_dict[c]['count'] += 1
            if S_dict[c]['count'] % 2 != 0:
                outlier -= 1
                # string = string.replace(c, '')
            else:
                outlier += 1
                string += c

    # print(outlier)
    string = string.replace(" ", "")
    if outlier == 0 or outlier == -1:
        return string
    else:
        return None


def isPalandrome(S):
    # print(S)
    string = list(S)

    while len(string) > 1:
        a = string.pop(0)
        b = string.pop(-1)
        if a != b:
            return False
    
    return True

def stringPossibilities(S):
    tree = tree_search(S)
    tree.insert(S, tree.root)
    
if __name__ == '__main__':
    # data = sys.stdin.read().splitlines()
    data = ['momoomom']

    S = data[0]
    # i = len(S) / 2
    # print(i)
    # if i - int(i) > 0:
    #     i1 = int(i-0.5)
    #     i2 = i1 + 1
    # else:
    #     i1 = int(i)
    #     i2 = i1
    # i = int(i)
    # print(i)
    # print(S[:i1])
    # print(S[i2:])
    # print(S)
    new_S = canBePalindrome(S)
    print(new_S)
    if new_S == None:
        print(0)
    else:
        stringPossibilities(new_S)
        print(possibilities)
    # print(count)
    # print(possibilities)