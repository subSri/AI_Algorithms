class TreeNode:
    def __init__(self, val=None, left=None, right=None, category=None, alpha=None, beta=None):
        self.val = val
        self.left = left
        self.right = right
        self.category = category
        self.alpha = alpha
        self.beta = beta

class Minimax:
    
    def __init__(self,height,basearr):

        self.height = height
        self.basearr = basearr
    
    def buildTree(self,root,depth):
        if depth==self.height-1:
            root.val = self.basearr.pop(0)
            return
        else:
            if depth%2!=0:
                root.left = TreeNode(category="Player")
                root.right = TreeNode(category="Player")
            else:
                root.left = TreeNode(category="Computer")
                root.right = TreeNode(category="Computer")

            self.buildTree(root.left,depth+1)
            self.buildTree(root.right,depth+1)

    def printTree(self,temproot):
        if temproot:
            self.printTree(temproot.left)
            print(temproot.alpha,temproot.beta)
            self.printTree(temproot.right)

    def miniMax(self,root):
        if  (root.left == None and root.right == None):
            return root.val
        else:
            if root.category == "Player":
                root.val = max(self.miniMax(root.left),self.miniMax(root.right))
            elif root.category == "Computer":
                root.val = min(self.miniMax(root.left),self.miniMax(root.right))
            return root.val

    def alphaBeta(self,root):
        
        if root.left.val!=None and root.right.val!=None:
            if root.category == "Computer":
                root.beta = min(root.beta,root.left.val,root.right.val)
            elif root.category == "Player":
                root.alpha = max(root.alpha,root.left.val,root.right.val)
        elif root.alpha>=root.beta:
            return 
        else:
            if root.category == "Player":
                root.left.alpha = root.alpha
                root.left.beta = root.beta
                self.alphaBeta(root.left)
                root.alpha = max(root.left.alpha,root.left.beta,root.alpha)
                
                if root.alpha>=root.beta:
                    print("===================================================")
                    print("Pruned node with alpha :",root.alpha," beta :",root.beta)
                    print("===================================================")
                    return root
                # print(root.alpha,root.beta)
                root.right.alpha = root.alpha
                root.right.beta = root.beta
                self.alphaBeta(root.right)
                root.alpha = max(root.right.alpha,root.right.beta,root.alpha)
                if root.alpha>=root.beta:
                    print("===================================================")
                    print("Pruned node with alpha :",root.alpha," beta :",root.beta)
                    print("===================================================")
                    return root

            elif root.category == "Computer":
                root.left.alpha = root.alpha
                root.left.beta = root.beta
                self.alphaBeta(root.left)
                root.beta = min(root.left.alpha,root.left.beta,root.beta)
                if root.alpha>=root.beta:
                    print("===================================================")
                    print("Pruned node with alpha :",root.alpha," beta :",root.beta)
                    print("===================================================")
                    return root
                # print(root.alpha,root.beta)
                root.right.alpha = root.alpha
                root.right.beta = root.beta
                self.alphaBeta(root.right)
                root.beta = min(root.right.alpha,root.right.beta,root.beta)
                if root.alpha>=root.beta:
                    print("===================================================")
                    print("Pruned node with alpha :",root.alpha," beta :",root.beta)
                    print("===================================================")
                    return root
            return root

height = int(input("Enter the depth of tree : "))
utilval = list(map(int,input("Enter the utility values of leaf nodes space seperated : ").split()))
# (4,[-1,3,5,-5,-6,-4,2,3]) In this example pruning happens
# (5, [])
mini = Minimax(height,utilval)
root = TreeNode(category="Player")

temp = root
mini.buildTree(temp,0)
minimaxroot = temp
alphabetaroot = temp
alphabetaroot.alpha = -float("inf")
alphabetaroot.beta = float("inf")

# print("Minimax score at root is",mini.miniMax(minimaxroot))
alpbh = mini.alphaBeta(alphabetaroot)

mini.printTree(alpbh)
print("AlphaBeta value of player at root is : ",alpbh.alpha)


    