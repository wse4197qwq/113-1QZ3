class Node: #節點
    def __init__(self, item=None):
        self.data = item #儲存資料
        self.link = None #下一節點的鏈結

class Stack: #堆疊
    def __init__(self):
        self.top = None #堆疊頂端預設為空

    def add(self, item: int): #將資料加入堆疊頂端
        new_node = Node(item) #創新節點
        new_node.link = self.top #新節點的link指向堆疊頂端
        self.top = new_node #更新top為新創的節點

    def remove(self) -> int: #從堆疊移除頂端節點並取得其資料
        if self.top is None: #如果堆疊是空的
            raise Exception("STACK_EMPTY") #拋出異常
        x = self.top #取出頂端節點
        item = x.data #保存其資料
        self.top = self.top.link #更新top為下一節點
        del x #刪除頂端節點
        return item #取得被移除節點的資料

class Queue: #佇列
    def __init__(self):
        self.front = None #佇列前端預設為空
        self.rear = None #佇列後端預設為空

    def add(self, item): #將資料加入佇列後端
        new_node = Node(item) #創新節點
        if self.rear is None: #如果佇列是空的,前後端都指向新節點
            self.front = new_node
            self.rear = new_node
        else: #否則只將rear的link指向新節點,並更新rear為新節點
            self.rear.link = new_node
            self.rear = new_node

    def remove(self): #從佇列移除前端節點並取得其資料
        if self.front is None: #如果佇列是空的
            raise Exception("Queue_Empty") #拋出異常
        x = self.front #取出前端節點
        item = x.data #保存其資料
        self.front = self.front.link #更新front為下一節點
        if self.front is None: #如果佇列變成空的
            self.rear = None #將rear設為None
        del x #刪除前端節點
        return item #取得被移除節點的資料