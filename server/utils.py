from config import db
from models import Franchise, Employee


def get_all_franchises():
    return db.session.query(Franchise).all()