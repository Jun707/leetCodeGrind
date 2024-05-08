class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)
        
    def visit(self, url: str) -> None:
        self.curr.next=ListNode(url)
        self.curr.next.prev = self.curr
        self.curr = self.curr.next
        
    def back(self, steps: int) -> str:
        while steps>0 and self.curr.prev:
            steps -=1
            self.curr = self.curr.prev
        return self.curr.val
        

    def forward(self, steps: int) -> str:
        while steps>0 and self.curr.next:
            steps-=1
            self.curr=self.curr.next
        return self.curr.val