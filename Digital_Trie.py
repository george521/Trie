class TrieNode:
    def __init__(self):
        self.children = [None]*256
        self.endword = False
        self.data = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def charToIndex(self,ch):
        '''function to change characters to pointers'''
        return ord(ch)

    def insert(self,res):

        current_node = self.root

        for level in range(len(res.name)):
            index = self.charToIndex(res.name[level])
            '''create node if character doesn't exist and insertion of the node to the children of the previous one'''
            if current_node.children[index]== None:
                current_node.children[index] = TrieNode()
            current_node = current_node.children[index]

        current_node.endword = True
        current_node.data.append(res)

    def find(self,name):
        current_node =self.root
        for level in range(len(name)):
            index = self.charToIndex(name[level])
            if not current_node.children[index]:
                return current_node.data
            current_node = current_node.children[index]


        return current_node.data
