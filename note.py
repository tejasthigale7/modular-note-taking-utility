from datetime import datetime

class Note:
    def __init__(self, title, content, tags):
        self.title = title
        self.content = content
        self.tags = tags
        self.timestamp = datetime.now().isoformat()

    def save(self):
        """Return dictionary representation of note"""
        return {
            "title": self.title,
            "content": self.content,
            "tags": self.tags,
            "timestamp": self.timestamp
        }

    def display(self):
        """Print formatted note"""
        print("-" * 40)
        print(f"Title     : {self.title}")
        print(f"Timestamp : {self.timestamp}")
        print(f"Tags      : {', '.join(self.tags)}")
        print(f"Content   : {self.content}")
        print("-" * 40)

    def matches_search(self, term):
        """Check if term is in title, content, or tags"""
        term = term.lower()
        return (
            term in self.title.lower()
            or term in self.content.lower()
            or term in [tag.lower() for tag in self.tags]
        )
