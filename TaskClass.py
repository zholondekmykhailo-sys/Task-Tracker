class Task:
    def __init__(self, name, description, status, id):
        self.name = name
        self.description = description
        self.status = status
        self.id = id
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            name = data['name'],
            description = data['description'],
            status = data['status'],
            id = data['id']
        )

    def to_dict(self):
        return{
            'name': self.name,
            'description': self.description,
            'status': self.status,
            'id': self.id
            }