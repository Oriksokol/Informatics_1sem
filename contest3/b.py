class node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
class searchtree:
    def __init__(self):
        self.root = None
    def insert(self, key, value):
        if self.root is None:
            self.root = node(key, value)
            return
        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = node(key, value)
                    return
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = node(key, value)
                    return
                current = current.right
    def search(self, key):
        current = self.root
        while current is not None:
            if key == current.key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
N = int(input())
herotree = searchtree()
artifacttree = searchtree()
for _ in range(N):
    hero_name, artifact_name = input().split()
    herotree.insert(hero_name, artifact_name)
    artifacttree.insert(artifact_name, hero_name)
Q = int(input())
for _ in range(Q):
    search = input()
    result = herotree.search(search)
    if result is not None:
        print(result)
    else:
        print(artifacttree.search(search))