"""AI-assisted implementation based on the UTS 43030 Lecture 4 practical.

Reconstructed from the activity descriptions, not the Canvas source files.
"""


class Task:
    def __init__(self, title, status="ToDo"):
        self.title = title
        self.completed = False
        self.status = status

    def mark_completed(self):
        self.completed = True
        self.status = "Done"

    def __repr__(self):
        return f"{self.title} - {self.status}"

    def __str__(self):
        return f"Task: {self.title}, Status: {self.status}"


class TaskPool:
    def __init__(self):
        self.tasks = []

    def populate(self):
        self.tasks = [
            Task("Create the repository"),
            Task("Create the project board"),
            Task("Link the issue and pull request"),
            Task("Implement the task manager"),
            Task("Run the unit tests"),
            Task("Check the automated HTML report"),
        ]
        for task in self.tasks[:3]:
            task.mark_completed()

    def add_task(self, task):
        self.tasks.append(task)

    def get_open_tasks(self):
        return [task for task in self.tasks if task.status == "ToDo"]

    def get_done_tasks(self):
        return [task for task in self.tasks if task.status == "Done"]


def main():
    pool = TaskPool()
    pool.populate()

    print("ToDo Tasks:")
    for task in pool.get_open_tasks():
        print(task.title)

    print("Done Tasks:")
    for task in pool.get_done_tasks():
        print(task.title)


if __name__ == "__main__":
    main()
