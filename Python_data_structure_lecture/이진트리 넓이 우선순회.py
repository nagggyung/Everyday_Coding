class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r


    def bft(self):
        # 빈 리스트 초기화
        traversal = []
        # 큐 초기화
        q = ArrayQueue()
        
        # 루트 노드가 존재하는 경우 
        if self.root:
            q.enqueue(self.root)
            # q가 비어있지 않는동안 반복해서 순회
            while q.size():
                element = q.dequeue()
                traversal.append(element.data)
                if element.left:
                    q.enqueue(element.left)
                if element.right:
                    q.enqueue(element.right)

        return traversal

def solution(x):
    return 0