from config import db

class Franchise(db.Model):
    __tablename__ = 'franchises'

    id = db.Column(db.Integer, primary_key = True)
    branch_name = db.Column(db.String, unique = True)
    franchise_no = db.Column(db.Integer)
    date_opened = db.Column(db.DateTime, server_default = db.func.now())

    def __repr__(self):
        return f"Location: {self.branch_name} Inaugurated: {self.date_opened}"



class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    job = db.Column(db.String)
    hiring_date = db.Column(db.DateTime, server_default = db.func.now())

    franchise_id = db.Column(db.Integer, db.ForeignKey('franchises.id'))

    def __repr__(self):
        return f"Name: {self.name} Job: {self.job} Hired on: {self.hiring_date}"