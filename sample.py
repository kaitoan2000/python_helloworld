import redis
class savetoRedis:
    db  = redis.StrictRedis (
        host='localhost',
        port=6379,
        db=0) 

    def __init__(self, name, age):        
        self.name = name        
        self.age = age        

    def save(self):        
	self.db.set('Name', '%s') % self.name
	self.db.get('Name')

sv1 = savetoRedis("nhan",1)
print sv1.save()
