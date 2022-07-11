# singleton design pattern

class DB:
    __connection = None

    @classmethod
    def connect(cls):
        if not cls.__connection:
            print('Establishing connection...')
            cls.__connection = ...
        return cls.__connection

      
if __name__ == '__main__':
    connection1 = DB.connect()
    connection2 = DB.connect()
