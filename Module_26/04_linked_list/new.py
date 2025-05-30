from typing import Any, Optional

class Node:

    def __init__(self, value: Optional[Any]=None, next: Optional['Node']=None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return f"Node [{str(self.value)}]"


class LinkedList:

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length = 0

    def __str__(self) -> str:
        if self.head is not None:
            currrent = self.head
            values = [str(currrent.value)]
            while currrent.next is not None:
                currrent = currrent.next
                values.append(str(currrent.value))
            return '[{values}]'.format(values=' '.join(values))
        return 'LinkedList []'

    def append(self, elem: Any) -> None:
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

        self.length += 1


    def remove(self, index) -> None:
        cur_node = self.head
        cur_index = 0
        if self.length == 0 or self.length <= index:
            raise IndexError

        if cur_node is not None:
            if index == 0:
                self.head = cur_node.next
                self.length -= 1
                return

        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1

        prev.next = cur_node.next
        self.length -= 1

    def get(self, index) -> None:
        cur_node = self.head
        cur_index = 0
        while cur_index <= index:
            if cur_index == index:
                return cur_node
            cur_index += 1
            cur_node = cur_node.next


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
