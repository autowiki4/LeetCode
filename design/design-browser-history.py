class Node:
    def __init__(self, val = '', nxt = None, prev = None):
        self.val = val
        self.next = nxt
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        nxt_node = Node(url)
        nxt_node.prev = self.curr
        self.curr.next = nxt_node
        self.curr = nxt_node

    def back(self, steps: int) -> str:
        i = 0
        while self.curr.prev and i < steps:
            self.curr = self.curr.prev
            i += 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        i = 0
        while self.curr.next and i < steps:
            self.curr = self.curr.next
            i += 1
        return self.curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)