import pymysql


class Database():
    def __init__(self):
        self.db = pymysql.connect(host = '192.168.0.50',
                     port = 3306,
                     user='matrix_hhw',
                     passwd = 'matrix_hhw',
                     db = 'matrix_hhw',
                     charset = 'utf8')
        
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)



    def execute(self, query, args={}):
        self.cursor.execute(query, args)


    def excuteOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row


    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row


    def commit(self):
        self.db.commit()

