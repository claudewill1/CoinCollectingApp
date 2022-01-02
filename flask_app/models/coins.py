from flask_app.config.mysqlconnection import connectToMySql
from flask import flash
import re

class Coin:
    db = "coinDb"
    def __init__(self,data) -> None:
        self.id = data['id']
        self.date = data['date']
        self.mintMark = data['mintMark']
        self.denomination = data["denomination"]
        self.gradingService = data['gradingService']
        self.certificationNum = data['certificationNum']
        self.grade = data['grade']
        self.initialCost = data['initialCost']
        self.value = data['value']
        self.added_at = data['added_at']
        self.updated_at = data['updated_at']