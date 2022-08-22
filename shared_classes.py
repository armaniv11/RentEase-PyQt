import sqlite3
class SharedClasses:
    partyDict = {}

      
    #defining constructor  
    def __init__(self):  
        self.loadPartyAndId()

    def loadPartyAndId(self):
        conn = sqlite3.connect("details.db")
        c = conn.cursor()
        c.execute("SELECT partyname,partyid from newparty")
        pmList = c.fetchall()
        conn.close()
        for k,v in pmList:
            print(k,v)
            self.partyDict[k]=v
        #     if k !='CASH' and k != 'BANK':
        return self.partyDict