import sqlite3
import re

# Connection & Cursor for SQL commands
conn = sqlite3.connect("orgCount.sqlite")
cur = conn.cursor()

# Reset SQL Table
cur.execute('DROP TABLE IF EXISTS Counts')

# Create table
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = 'mbox.txt'
fhandle = open(fname)

# Extracting domain & adding to DB
for line in fhandle:
    if not line.startswith('From '): continue
    domain = re.search('@(\S+)', line).group(1)
    # print(str(domain))
    cur.execute('SELECT * FROM Counts WHERE org = ?', (domain,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org=?', (domain,))
conn.commit()

sqlstring = '''SELECT * FROM Counts ORDER BY count DESC'''

for row in cur.execute(sqlstring):
    print(str(row[0]), row[1])

cur.close()