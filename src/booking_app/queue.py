from .models import Queue


class UniqueQueue:
    def __init__(self):
        self.queue = Queue.objects

    def add(self, value):
        if not self.queue.filter(value=value).exists():
            self.queue.create(value=value)

    def pop(self):
        if self.queue.exists():
            item = self.queue.order_by('id').first()
            item_value = item.value
            item.delete()
            return item_value
        return None

    def length(self):
        return self.queue.count()

    def last(self):
        last_item = self.queue.order_by('-id').first()
        return last_item.value if last_item else None
