class Tab:
    def __init__(self, page=str):
        self.page = page
        self.prev = None 
        self.next = None
    
    def __str__(self):
        return self.page if self.page else "None"

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Tab(None)
        self.tail = Tab(None)
        new_tab = Tab(homepage)
        self.head.next = new_tab
        self.tail.prev = new_tab
        new_tab.prev = self.head
        new_tab.next = self.tail
        self.curr = new_tab

    def visit(self, url: str) -> None:
        new_tab = Tab(url)
        curr = self.curr
        next = self.tail
        curr.next = new_tab
        next.prev = new_tab
        new_tab.prev = curr
        new_tab.next = next
        # # head <-> lc (curr) <-> google <-> tail
        # if curr and curr.next != self.tail:
        #     next = curr.next 
        #     curr.next = new_tab
        #     next.prev = new_tab
        #     new_tab.prev = curr
        #     new_tab.next = next
        # else:
        #     # head <-> lc <-> google (curr) <-> tail
        #     next = self.tail
        #     curr.next = new_tab
        #     next.prev = new_tab
        #     new_tab.next = next
        #     new_tab.prev = curr
        
        self.curr = new_tab
        
        print(f"[VISIT] Visiting {url}")
        print(f"[VISIT] Current pointer is at {self.curr.page}")

    def debug_list(self):
        node = self.head.next
        tabs = []
        while node != self.tail:
            marker = "(curr)" if node == self.curr else ""
            tabs.append(node.page + marker)
            node = node.next
        print(f"[DEBUG] Tabs: {' <-> '.join(tabs)}")

    def back(self, steps: int) -> str:
        curr = self.curr
        while curr and curr.prev != self.head and steps > 0:
            curr = curr.prev
            steps -= 1
            print(f"[B-DEBUG] At {curr.page if curr else None}, steps left: {steps}")
        self.curr = curr
        print(f"[BACK] Moved back to {self.curr.page}, Current pointer is at {self.curr.page}")
        return self.curr.page

    def forward(self, steps: int) -> str:
        curr = self.curr
        while curr and curr.next != self.tail and steps > 0:
            curr = curr.next
            steps -= 1
            print(f"[F-DEBUG] At {curr.page if curr else None}, steps left: {steps}")
        self.curr = curr
        print(f"[FORWARD] Moved forward to {self.curr.page}, Current pointer is at {self.curr.page}")
        return self.curr.page

# Your BrowserHistory object will be instantiated and called as such:
obj = BrowserHistory("leetcode.com")   # first element
obj.visit("google.com")                # second element
obj.visit("facebook.com")              # third element
obj.visit("youtube.com")               # fourth
obj.back(1)                            # fifth
obj.back(1)                            # sixth
obj.forward(1)                         # seventh
obj.visit("linkedin.com")              # eighth
obj.forward(2)                         # linkedin
obj.debug_list() 
obj.back(2)                            # google
obj.back(7)                            # eleventh