import sqlite3

# define connection and cursor
connection = sqlite3.connect('side_hustles.db')
cursor = connection.cursor()

# create sidehustles table

command1 = """CREATE TABLE IF NOT EXISTS
sidehustles(sidehustle_id INTEGER PRIMARY KEY, name TEXT)"""

cursor.execute(command1)

command2 = """CREATE TABLE IF NOT EXISTS
income(income_id INTEGER PRIMARY KEY, sidehustle_id INTEGER, annual_income FLOAT,
FOREIGN KEY(sidehustle_id) REFERENCES sidehustles(sidehustle_id))"""

cursor.execute(command2)

# add to sidehustles

cursor.execute("INSERT INTO sidehustles VALUES (1, 'Scriptwriter')")
cursor.execute("INSERT INTO sidehustles VALUES (2, 'Prompt Engineer')")
cursor.execute("INSERT INTO sidehustles VALUES (3, 'Medium Content Writer')")
cursor.execute("INSERT INTO sidehustles VALUES (4, 'Graphic Designer')")
cursor.execute("INSERT INTO sidehustles VALUES (5, 'Photographer')")
cursor.execute("INSERT INTO sidehustles VALUES (6, '3D Printing')")
cursor.execute("INSERT INTO sidehustles VALUES (7, 'Virtual Bookkeeper')")
cursor.execute("INSERT INTO sidehustles VALUES (8, 'Podcast Host')")
cursor.execute("INSERT INTO sidehustles VALUES (9, 'Online Tutor')")
cursor.execute("INSERT INTO sidehustles VALUES (10, 'Voiceover Artist')")
cursor.execute("INSERT INTO sidehustles VALUES (11, 'Web Developer')")
cursor.execute("INSERT INTO sidehustles VALUES (12, 'Babysitter')")
cursor.execute("INSERT INTO sidehustles VALUES (13, 'Content Editor')")
cursor.execute("INSERT INTO sidehustles VALUES (14, 'Video Editor')")
cursor.execute("INSERT INTO sidehustles VALUES (15, 'Dog Walker')")



# add to income

cursor.execute("INSERT INTO income VALUES (51, 1, 2900.00)")
cursor.execute("INSERT INTO income VALUES (52, 2, 8600.00)")
cursor.execute("INSERT INTO income VALUES (53, 3, 1200.00)")
cursor.execute("INSERT INTO income VALUES (54, 4, 7300.00)")
cursor.execute("INSERT INTO income VALUES (55, 5, 8400.00)")
cursor.execute("INSERT INTO income VALUES (56, 6, 6000.00)")
cursor.execute("INSERT INTO income VALUES (57, 7, 10100.00)")
cursor.execute("INSERT INTO income VALUES (58, 8, 5100.00)")
cursor.execute("INSERT INTO income VALUES (59, 9, 380.00)")
cursor.execute("INSERT INTO income VALUES (60, 10, 4500.00)")
cursor.execute("INSERT INTO income VALUES (61, 10, 3600.00)")
cursor.execute("INSERT INTO income VALUES (62, 11, 580.00)")
cursor.execute("INSERT INTO income VALUES (63, 12, 840.00)")
cursor.execute("INSERT INTO income VALUES (64, 13, 1320.00)")
cursor.execute("INSERT INTO income VALUES (65, 14, 640.00)")


# print results
reuslts = cursor.fetchall()
print(results)