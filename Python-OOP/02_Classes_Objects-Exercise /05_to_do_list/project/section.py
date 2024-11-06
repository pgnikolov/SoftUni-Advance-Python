from task import Task


class Section:
    tasks = []

    def __init__(self, name: str):
        self.name = name

    def add_task(self, new_task):
        for task_ in Section.tasks:
            if new_task.name in task_.name:
                return f"Task is already in the section {self.name}"
        Section.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task_ in Section.tasks:
            if task_.name == task_name:
                task_.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        cleaned = 0
        for task_ in self.tasks:
            if task_.completed:
                self.tasks.remove(task_)
                cleaned += 1
        return f"Cleared {cleaned} tasks."

    def view_section(self):
        text = f"Section {self.name}:\n"
        for task_ in Section.tasks:
            text += f"{task_.details()}\n"
        return text
