'''
3408. Design Task Manager
Medium
Topics
premium lock iconCompanies

There is a task management system that allows users to manage their tasks, each associated with a priority. The system should efficiently handle adding, modifying, executing, and removing tasks.

Implement the TaskManager class:

    TaskManager(vector<vector<int>>& tasks) initializes the task manager with a list of user-task-priority triples. Each element in the input list is of the form [userId, taskId, priority], which adds a task to the specified user with the given priority.

    void add(int userId, int taskId, int priority) adds a task with the specified taskId and priority to the user with userId. It is guaranteed that taskId does not exist in the system.

    void edit(int taskId, int newPriority) updates the priority of the existing taskId to newPriority. It is guaranteed that taskId exists in the system.

    void rmv(int taskId) removes the task identified by taskId from the system. It is guaranteed that taskId exists in the system.

    int execTop() executes the task with the highest priority across all users. If there are multiple tasks with the same highest priority, execute the one with the highest taskId. After executing, the taskId is removed from the system. Return the userId associated with the executed task. If no tasks are available, return -1.

Note that a user may be assigned multiple tasks.

Constraints:
    1 <= tasks.length <= 105
    0 <= userId <= 105
    0 <= taskId <= 105
    0 <= priority <= 109
    0 <= newPriority <= 109
    At most 2 * 105 calls will be made in total to add, edit, rmv, and execTop methods.
    The input is generated such that taskId will be valid.

'''


# Note that this question sucks because there is only one user per task, it does not mention that at all...only in the discussion section did I learn this
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_map = {}
        self.task_pq = [] # Have a priority queue so we don't have to loop through the entire map everytime (was previously failing to do time limit)
        for user, task, priority in tasks:
            self.task_map[task] = (priority, user)
            bisect.insort(self.task_pq, (priority, task))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = (priority, userId)
        bisect.insort(self.task_pq, (priority, taskId))

    def edit(self, taskId: int, newPriority: int) -> None: 
        old_priority, user_id = self.task_map[taskId]
        # Bisect left just returns an index
        index = bisect.bisect_left(self.task_pq, (old_priority, taskId))
        self.task_pq.pop(index)
        self.task_map[taskId] = (newPriority, user_id)
        bisect.insort(self.task_pq, (newPriority, taskId))

    def rmv(self, taskId: int) -> None:
        priority, user_id = self.task_map[taskId]
        index = bisect.bisect_left(self.task_pq, (priority, taskId))
        self.task_pq.pop(index)
        del self.task_map[taskId]

    def execTop(self) -> int:
        if not self.task_pq:
            return -1
        _, top_task = self.task_pq.pop()
        user_id = self.task_map[top_task][1]
        del self.task_map[top_task]
        return user_id
 

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
