class Task:

    def __init__(self, name: str, deu_date: str):
        self.name = name
        self.deu_date = deu_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str):
        if self.name == new_name:
            return "Name cannot be the same."
        self.name = new_name
        return self.name

    def change_due_date(self, new_date: str):
        if self.deu_date == new_date:
            return "Date cannot be the same."
        self.deu_date = new_date
        return self.deu_date

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if comment_number >= len(self.comments):
            return "Cannot find comment."
        self.comments[comment_number] = new_comment
        return f"{", ".join(self.comments)}"

    def details(self):
        return f"Name: {self.name} - Deu Date: {self.deu_date}"
