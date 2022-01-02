from CoinCollectingApp.flask_app.config.mysqlconnection import connectToMySQL
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
        self.user_id = data['user_id']
        self.added_at = data['added_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def createCoin(cls,data):
        q = "INSERT INTO coins (date,mintMark,denomination,gradingService,certificationNum,grade,initialCost,value, user_id) VALUES (%(date)s,%(mintMark)s,%(denomination)s,%(gradingService)s,%(certificationNum)s,%(grade)s,%(initialCost)s,%(value)s,%(user_id)s);"
        return connectToMySQL(cls.db).query_db(q,data)
    
    @classmethod
    def getAllCoins(cls):
        q = 'SELECT * FROM coins AS c LEFT JOIN users AS u ON u.id = c.user_id;'
        results = connectToMySQL(cls.db).query_db(q)
        all_coins = []
        if not results:
            return all_coins
        for coin in results:
            new_coin = cls(coin)