import sqlite3

def maxIdInt(colName,tableName):
    conn = sqlite3.connect("details.db")
    c = conn.cursor()
    c.execute(f"select max({colName}) from {tableName}")
    result = c.fetchone()
    conn.close()
    result = str(result[0])
    print("result from maxpid redit",result)
    if result == None or result == 'None':
        result = 0
    result = int(result) + 1
    return str(result)