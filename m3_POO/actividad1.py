import sqlite3

class Point:

   def __init__(self, x, y):
        self.x, self.y = x, y
        
   def __conform__(self, protocol):
        if protocol is sqlite3.PrepareProtocol:  
            return "%f;%f" % (self.x, self.y)

con = sqlite3.connect(":memory:")

cur = con.cursor()

p = Point(5.2, -3.5)

cur.execute("select ?", (p,))

print(cur.fetchone()[0])