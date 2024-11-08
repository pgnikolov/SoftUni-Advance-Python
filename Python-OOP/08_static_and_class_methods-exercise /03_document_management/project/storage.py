from project.topic import Topic
from project.category import Category
from project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        for el in self.categories:
            if el.id == category_id:
                el.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        for el in self.topics:
            if el.id == topic_id:
                el.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        for el in self.documents:
            if el.id == document_id:
                el.edit(new_file_name)

    def delete_category(self, category_id):
        for el in self.categories:
            if el.id == category_id:
                self.categories.remove(el)

    def delete_topic(self, topic_id):
        for el in self.topics:
            if el.id == topic_id:
                self.topics.remove(el)

    def delete_document(self, document_id):
        for el in self.documents:
            if el.id == document_id:
                self.documents.remove(el)

    def get_document(self, document_id):
        for el in self.documents:
            if el.id == document_id:
                return f"{str(el)}"

    def __repr__(self):
        return "\n".join(str(el) for el in self.documents)
