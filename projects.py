import uuid


class Project:
    projects=[]

    def __init__(self, owner_id,title, details, total_target, start_date, end_date):
        self.owner_id=owner_id
        self.title = title
        self.details = details
        self.total_target = total_target
        self.start_date = start_date
        self.end_date = end_date


