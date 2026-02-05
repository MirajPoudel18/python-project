#Task Management System build using classes

from datetime import datetime

class Task:
    def __init__(self, task_id, title, description, priority, due_date, category):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.category = category
        self.status = "Pending"
        self.created_at = datetime.now()
        self.completed_at = None
    
    def mark_complete(self):
        self.status = "Completed"
        self.completed_at = datetime.now()
        print(f"✓ Task '{self.title}' marked as complete!")
    
    def mark_in_progress(self):
        self.status = "In Progress"
        print(f"⟳ Task '{self.title}' is now in progress!")
    
    def update_priority(self, new_priority):
        old_priority = self.priority
        self.priority = new_priority
        print(f"Priority changed from {old_priority} to {new_priority}")
    
    def update_due_date(self, new_date):
        self.due_date = new_date
        print(f"Due date updated to {new_date}")
    
    def is_overdue(self):
        if self.status == "Completed":
            return False
        
        if isinstance(self.due_date, str):
            due = datetime.strptime(self.due_date, "%Y-%m-%d")
        else:
            due = self.due_date
        
        return datetime.now() > due
    
    def __str__(self):
        overdue = " [OVERDUE!]" if self.is_overdue() else ""
        return (f"[{self.task_id}] {self.title}{overdue}\n"
                f"  Priority: {self.priority} | Status: {self.status}\n"
                f"  Category: {self.category} | Due: {self.due_date}\n"
                f"  Description: {self.description}")
    
    def __repr__(self):
        return f"Task({self.task_id}, {self.title}, {self.priority})"


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
    
    def add_task(self, title, description, priority, due_date, category):
        task = Task(self.next_id, title, description, priority, due_date, category)
        self.tasks.append(task)
        self.next_id += 1
        print(f"✓ Task '{title}' added successfully! (ID: {task.task_id})")
        return task
    
    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print(f"✓ Task '{task.title}' deleted!")
                return True
        print(f"✗ Task with ID {task_id} not found!")
        return False
    
    def get_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None
    
    def mark_task_complete(self, task_id):
        task = self.get_task(task_id)
        if task:
            task.mark_complete()
        else:
            print(f"✗ Task with ID {task_id} not found!")
    
    def filter_by_status(self, status):
        filtered = [task for task in self.tasks if task.status == status]
        return filtered
    
    def filter_by_priority(self, priority):
        filtered = [task for task in self.tasks if task.priority == priority]
        return filtered
    
    def filter_by_category(self, category):
        filtered = [task for task in self.tasks if task.category == category]
        return filtered
    
    def get_overdue_tasks(self):
        overdue = [task for task in self.tasks if task.is_overdue()]
        return overdue
    
    def sort_by_priority(self):
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        sorted_tasks = sorted(self.tasks, key=lambda task: priority_order[task.priority])
        return sorted_tasks
    
    def sort_by_due_date(self):
        sorted_tasks = sorted(self.tasks, 
                            key=lambda task: datetime.strptime(task.due_date, "%Y-%m-%d") 
                            if isinstance(task.due_date, str) else task.due_date)
        return sorted_tasks
    
    def sort_by_status(self):
        status_order = {"Pending": 1, "In Progress": 2, "Completed": 3}
        sorted_tasks = sorted(self.tasks, key=lambda task: status_order[task.status])
        return sorted_tasks
    
    def display_all_tasks(self):
        if not self.tasks:
            print("\nNo tasks available!")
            return
        
        print("\n" + "="*60)
        print("ALL TASKS")
        print("="*60)
        for task in self.tasks:
            print(task)
            print("-"*60)
    
    def display_tasks(self, task_list, title="TASKS"):
        if not task_list:
            print(f"\nNo tasks found in '{title}'!")
            return
        
        print("\n" + "="*60)
        print(title)
        print("="*60)
        for task in task_list:
            print(task)
            print("-"*60)
    
    def get_statistics(self):
        total = len(self.tasks)
        completed = len(self.filter_by_status("Completed"))
        pending = len(self.filter_by_status("Pending"))
        in_progress = len(self.filter_by_status("In Progress"))
        overdue = len(self.get_overdue_tasks())
        
        print("\n" + "="*60)
        print("TASK STATISTICS")
        print("="*60)
        print(f"Total Tasks: {total}")
        print(f"Completed: {completed}")
        print(f"In Progress: {in_progress}")
        print(f"Pending: {pending}")
        print(f"Overdue: {overdue}")
        print("="*60)


manager = TaskManager()

manager.add_task("Finish Python project", "Complete the task management system", 
                 "High", "2026-02-10", "Work")
manager.add_task("Buy groceries", "Milk, eggs, bread", 
                 "Medium", "2026-02-06", "Personal")
manager.add_task("Gym workout", "Chest and triceps day", 
                 "Low", "2026-02-07", "Health")
manager.add_task("Client meeting", "Discuss Q1 results", 
                 "High", "2026-02-05", "Work")
manager.add_task("Read book", "Finish chapter 5", 
                 "Low", "2026-02-08", "Personal")

manager.display_all_tasks()

manager.mark_task_complete(1)

task = manager.get_task(2)
task.mark_in_progress()

work_tasks = manager.filter_by_category("Work")
manager.display_tasks(work_tasks, "WORK TASKS")

high_priority = manager.filter_by_priority("High")
manager.display_tasks(high_priority, "HIGH PRIORITY TASKS")

pending = manager.filter_by_status("Pending")
manager.display_tasks(pending, "PENDING TASKS")

sorted_by_date = manager.sort_by_due_date()
manager.display_tasks(sorted_by_date, "TASKS SORTED BY DUE DATE")

overdue = manager.get_overdue_tasks()
manager.display_tasks(overdue, "OVERDUE TASKS")

manager.get_statistics()

manager.delete_task(3)