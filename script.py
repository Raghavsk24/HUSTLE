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

command3 = """CREATE TABLE IF NOT EXISTS
timeCommitment(timeCommitment_id INTEGER PRIMARY KEY, sidehustle_id INTEGER, min_commitment INTEGER, max_commitment INTEGER,
FOREIGN KEY(sidehustle_id) REFERENCES sidehustles(sidehustle_id))"""

cursor.execute(command3)

# add to sidehustles

cursor.execute("INSERT INTO sidehustles VALUES (1, 'Scriptwriter')")
cursor.execute("INSERT INTO sidehustles VALUES (2, 'Prompt Engineer')")
cursor.execute("INSERT INTO sidehustles VALUES (3, 'Medium Content Writer')")
cursor.execute("INSERT INTO sidehustles VALUES (4, 'Graphic Designer')")
cursor.execute("INSERT INTO sidehustles VALUES (5, 'Animator')")
cursor.execute("INSERT INTO sidehustles VALUES (6, 'Photographer')")
cursor.execute("INSERT INTO sidehustles VALUES (7, '3D Printing')")
cursor.execute("INSERT INTO sidehustles VALUES (8, 'Virtual Bookkeeper')")
cursor.execute("INSERT INTO sidehustles VALUES (9, 'Podcast Host')")
cursor.execute("INSERT INTO sidehustles VALUES (10, 'Online Tutor')")
cursor.execute("INSERT INTO sidehustles VALUES (11, 'Voiceover Artist')")
cursor.execute("INSERT INTO sidehustles VALUES (12, 'Web Developer')")
cursor.execute("INSERT INTO sidehustles VALUES (13, 'Babysitter')")
cursor.execute("INSERT INTO sidehustles VALUES (14, 'Content Editor')")
cursor.execute("INSERT INTO sidehustles VALUES (15, 'Video Editor')")
cursor.execute("INSERT INTO sidehustles VALUES (16, 'Dog Walker')")

# add to income

cursor.execute("INSERT INTO income VALUES (51, 1, 2900.00)")
cursor.execute("INSERT INTO income VALUES (52, 2, 8600.00)")
cursor.execute("INSERT INTO income VALUES (53, 3, 1200.00)")
cursor.execute("INSERT INTO income VALUES (54, 4, 7300.00)")
cursor.execute("INSERT INTO income VALUES (55, 5, 8400.00)")
cursor.execute("INSERT INTO income VALUES (56, 6, 6000.00)")
cursor.execute("INSERT INTO income VALUES (57, 7, 15600.00)")
cursor.execute("INSERT INTO income VALUES (58, 8, 10100.00)")
cursor.execute("INSERT INTO income VALUES (59, 9, 5100.00)")
cursor.execute("INSERT INTO income VALUES (60, 10, 380.00)")
cursor.execute("INSERT INTO income VALUES (61, 11, 4500.00)")
cursor.execute("INSERT INTO income VALUES (62, 12, 3600.00)")
cursor.execute("INSERT INTO income VALUES (63, 13, 580.00)")
cursor.execute("INSERT INTO income VALUES (64, 14, 840.00)")
cursor.execute("INSERT INTO income VALUES (65, 15, 1320.00)")
cursor.execute("INSERT INTO income VALUES (66, 16, 640.00)")

# add to time commitment

cursor.execute("INSERT INTO timeCommitment VALUES (101, 1, 5, 20)")
cursor.execute("INSERT INTO timeCommitment VALUES (102, 2, 1, 6)")
cursor.execute("INSERT INTO timeCommitment VALUES (103, 3, 2, 5)")
cursor.execute("INSERT INTO timeCommitment VALUES (104, 4, 5, 20)")
cursor.execute("INSERT INTO timeCommitment VALUES (105, 5, 10, 20)")
cursor.execute("INSERT INTO timeCommitment VALUES (106, 6, 5, 30)")
cursor.execute("INSERT INTO timeCommitment VALUES (107, 7, 1, 10)")
cursor.execute("INSERT INTO timeCommitment VALUES (108, 8, 5, 15)")
cursor.execute("INSERT INTO timeCommitment VALUES (109, 9, 5, 20)")
cursor.execute("INSERT INTO timeCommitment VALUES (110, 10, 1, 5)")
cursor.execute("INSERT INTO timeCommitment VALUES (111, 11, 1, 5)")
cursor.execute("INSERT INTO timeCommitment VALUES (112, 12, 10, 30)")
cursor.execute("INSERT INTO timeCommitment VALUES (113, 13, 1, 5)")
cursor.execute("INSERT INTO timeCommitment VALUES (114, 14, 1, 5)")
cursor.execute("INSERT INTO timeCommitment VALUES (115, 15, 5, 20)")
cursor.execute("INSERT INTO timeCommitment VALUES (116, 16, 1, 5)")


