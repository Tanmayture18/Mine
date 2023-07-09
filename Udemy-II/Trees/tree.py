# Basic Tree

class TreeNode:
    def __init__(self,data,children=[]):
        self.data=data
        self.children=children

    def __str__(self,level=0):
        res=" "*level+str(self.data)+"\n"

        for i in self.children:
            res+=i.__str__(level+1)

        return res

    def addchild(self,node):
        self.children.append(node)     


tree=TreeNode('Drinks',[])
print(tree)

# Add two childs to drinks nide
tea=TreeNode('Tea',[])
coffe=TreeNode('Coffe',[])
tree.addchild(tea)
tree.addchild(coffe)
print(tree)

# Adding child to tea
green=TreeNode('Green',[])
tea.addchild(green)

print(tree)

