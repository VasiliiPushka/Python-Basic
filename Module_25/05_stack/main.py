class Stack:
    def __init__(self):
        self.__st = []
    def __str__(self):
        return '; '.join(self.__st)
        #return str(self.__st)
    def push(self, element):
        self.__st.append(element)

    def pop(self):
        if len(self.__st) == 0:
            return None
        else:
            return self.__st.pop()
class TaskManager:
    def __init__(self):
        self.task = dict()

    def __str__(self):
        display = []
        if self.task:
            for i_priority in sorted(self.task.keys()):
                display.append('{priority} {task}\n'.format(
                    priority=str(i_priority),
                    task=self.task[i_priority]
                ))
        return ''.join(display)

    def new_task(self, task, priority):
        if priority not in self.task:
            self.task[priority] = Stack()
        self.task[priority].push(task)




manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("покататься на велосипеде", 3)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)

# Результат:
# 1 отдохнуть
# 2 поесть; сдать дз
# 4 сделать уборку; помыть посуду
