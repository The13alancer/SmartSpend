import heapq
from datetime import datetime


class TaskManager:
    def __init__(self, pending=None, completed=None):
        self.pending = []
        self.completed = completed if completed is not None else []
        self.next_id = 1

        if pending:
            max_id = 0
            for task in pending:
                heapq.heappush(self.pending, (task["priority"], task["id"], task))
                max_id = max(max_id, task["id"])
            self.next_id = max_id + 1

        if self.completed:
            max_completed_id = max(task["id"] for task in self.completed)
            self.next_id = max(self.next_id, max_completed_id + 1)

    def add_task(self, title, priority, due_date=""):
        title = title.strip()
        due_date = due_date.strip()

        if not title:
            return False, "Task title cannot be empty."

        if not isinstance(priority, int) or priority < 1 or priority > 5:
            return False, "Priority must be an integer from 1 to 5."

        task = {
            "id": self.next_id,
            "title": title,
            "priority": priority,
            "due_date": due_date,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "pending"
        }

        heapq.heappush(self.pending, (priority, self.next_id, task))
        self.next_id += 1
        return True, f"Task '{title}' added successfully."

    def peek_next_task(self):
        if not self.pending:
            return None
        return self.pending[0][2]

    def complete_next_task(self):
        if not self.pending:
            return False, "No pending tasks."

        _, _, task = heapq.heappop(self.pending)
        task["status"] = "completed"
        self.completed.append(task)
        return True, f"Task '{task['title']}' completed."

    def list_pending_tasks(self):
        return [item[2] for item in sorted(self.pending)]

    def list_completed_tasks(self):
        return self.completed

    def export_data(self):
        return {
            "pending": [item[2] for item in self.pending],
            "completed": self.completed
        }
