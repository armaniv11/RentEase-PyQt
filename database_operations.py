import sqlite3


class DatabaseOperations:
    
    def selectRentFromParty(partyId):
        conn = sqlite3.connect("details.db")
        c = conn.cursor()
        c.execute("SELECT partyname,rent from newparty where partyid = ?",(partyId,))
        result = c.fetchone()
        print(f"{result} printing rent")
        conn.close()
        rentInfo = {"partyName":result[0],"rent":result[1]}
        return rentInfo
    
    def findPidFromName(name):
        conn = sqlite3.connect("details.db")
        c = conn.cursor()
        c.execute("SELECT partyid from newparty where partyname = ?",(name,))
        result = c.fetchone()
        print(result)
        conn.close()
        return result[0]

