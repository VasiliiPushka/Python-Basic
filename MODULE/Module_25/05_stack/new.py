class TaskManager:

    def __init__(self):
        self.task = dict()


    def __str__(self):
        display = []
        if self.task:
            for i_priority in sorted(self.task.keys()):
                display.append(f"{str(i_priority)} "
                               f"{self.task[i_priority]}\n")

        return ''.join(display)

    def new_task(self, task:str, priority:int):
        if priority not in self.task:
            self.task[priority] = Stack()
        self.task[priority].push(task)


class Stack:

    def __init__(self):
        self.__st = []

    def __str__(self):
        return f"{self.__st}"

    def push(self, element):
        self.__st.append(element)

    def pop(self):
        if len(self.__st) == 0:
            return None
        return self.__st.pop()

manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)




# my_st = Stack()
# for i in range(5):
#     my_st.push(i)
# print(my_st)
#
# for _ in range(33):
#     my_st.pop()
# print(my_st)






