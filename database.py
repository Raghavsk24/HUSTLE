import sqlite3

# define connection and cursor
connection = sqlite3.connect('side_hustles.db')
cursor = connection.cursor()

# create sidehustles table
command1 = """CREATE TABLE IF NOT EXISTS
sidehustles(sidehustle_id INTEGER PRIMARY KEY, name TEXT)"""

cursor.execute(command1)

# create income table
command2 = """CREATE TABLE IF NOT EXISTS
income(income_id INTEGER PRIMARY KEY, sidehustle_id INTEGER, annual_income FLOAT,
FOREIGN KEY(sidehustle_id) REFERENCES sidehustles(sidehustle_id))"""

cursor.execute(command2)

# create time commitment table
command3 = """CREATE TABLE IF NOT EXISTS
time_commitment(time_commitment_id INTEGER PRIMARY KEY, sidehustle_id INTEGER, min_commitment INTEGER, max_commitment INTEGER,
FOREIGN KEY(sidehustle_id) REFERENCES sidehustles(sidehustle_id))"""

cursor.execute(command3)

# create employment type table
command4 = """CREATE TABLE IF NOT EXISTS
employment_type(employment_type_id INTEGER PRIMARY KEY, sidehustle_id INTEGER, employment_type_name TEXT,
FOREIGN KEY(sidehustle_id) REFERENCES sidehustles(sidehustle_id))"""

cursor.execute(command4)

# create category table
command5 = """CREATE TABLE IF NOT EXISTS
category(category_id INTEGER PRIMARY KEY, sidehustle_id INTEGER, category_name TEXT,
FOREIGN KEY(sidehustle_id) REFERENCES sidehustles(sidehustle_id))"""

cursor.execute(command5)

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
cursor.execute("INSERT INTO time_commitment VALUES (101, 1, 5, 20)")
cursor.execute("INSERT INTO time_commitment VALUES (102, 2, 1, 6)")
cursor.execute("INSERT INTO time_commitment VALUES (103, 3, 2, 5)")
cursor.execute("INSERT INTO time_commitment VALUES (104, 4, 5, 20)")
cursor.execute("INSERT INTO time_commitment VALUES (105, 5, 10, 20)")
cursor.execute("INSERT INTO time_commitment VALUES (106, 6, 5, 30)")
cursor.execute("INSERT INTO time_commitment VALUES (107, 7, 1, 10)")
cursor.execute("INSERT INTO time_commitment VALUES (108, 8, 5, 15)")
cursor.execute("INSERT INTO time_commitment VALUES (109, 9, 5, 20)")
cursor.execute("INSERT INTO time_commitment VALUES (110, 10, 1, 5)")
cursor.execute("INSERT INTO time_commitment VALUES (111, 11, 1, 5)")
cursor.execute("INSERT INTO time_commitment VALUES (112, 12, 10, 30)")
cursor.execute("INSERT INTO time_commitment VALUES (113, 13, 1, 5)")
cursor.execute("INSERT INTO time_commitment VALUES (114, 14, 1, 5)")
cursor.execute("INSERT INTO time_commitment VALUES (115, 15, 5, 20)")
cursor.execute("INSERT INTO time_commitment VALUES (116, 16, 1, 5)")

# add to employment type
cursor.execute("INSERT INTO employment_type VALUES (1, 1, 'Freelance Services')")
cursor.execute("INSERT INTO employment_type VALUES (2, 2, 'Freelance Services')")
cursor.execute("INSERT INTO employment_type VALUES (3, 3, 'Self-employed')")
cursor.execute("INSERT INTO employment_type VALUES (4, 4, 'Freelance Services')")
cursor.execute("INSERT INTO employment_type VALUES (5, 5, 'Freelance Services')")
cursor.execute("INSERT INTO employment_type VALUES (6, 6, 'Self-employed')")
cursor.execute("INSERT INTO employment_type VALUES (7, 7, 'Business Venture')")
cursor.execute("INSERT INTO employment_type VALUES (8, 8, 'Freelance Services')")
cursor.execute("INSERT INTO employment_type VALUES (9, 9, 'Self-employed')")
cursor.execute("INSERT INTO employment_type VALUES (10, 10, 'Freelance Services')")
cursor.execute("INSERT INTO employment_type VALUES (11, 11, 'Freelance Services')")
cursor.execute("INSERT INTO employment_type VALUES (12, 12, 'Freelance Services')")
cursor.execute("INSERT INTO employment_type VALUES (13, 13, 'Self-employed')")
cursor.execute("INSERT INTO employment_type VALUES (14, 14, 'Freelance Services')")
cursor.execute("INSERT INTO employment_type VALUES (15, 15, 'Freelance Services')")
cursor.execute("INSERT INTO employment_type VALUES (16, 16, 'Self-employed')")

# add to category
cursor.execute("INSERT INTO category VALUES (1, 1, 'Content & Media')")
cursor.execute("INSERT INTO category VALUES (2, 2, 'Technical')")
cursor.execute("INSERT INTO category VALUES (3, 3, 'Content & Media')")
cursor.execute("INSERT INTO category VALUES (4, 4, 'Content & Media')")
cursor.execute("INSERT INTO category VALUES (5, 5, 'Content & Media')")
cursor.execute("INSERT INTO category VALUES (6, 6, 'Content & Media')")
cursor.execute("INSERT INTO category VALUES (7, 7, 'Technical')")
cursor.execute("INSERT INTO category VALUES (8, 8, 'Technical')")
cursor.execute("INSERT INTO category VALUES (9, 9, 'Content & Media')")
cursor.execute("INSERT INTO category VALUES (10, 10, 'Customer Service')")
cursor.execute("INSERT INTO category VALUES (11, 11, 'Content & Media')")
cursor.execute("INSERT INTO category VALUES (12, 12, 'Technical')")
cursor.execute("INSERT INTO category VALUES (13, 13, 'Customer Service')")
cursor.execute("INSERT INTO category VALUES (14, 14, 'Content & Media')")
cursor.execute("INSERT INTO category VALUES (15, 15, 'Content & Media')")
cursor.execute("INSERT INTO category VALUES (16, 16, 'Customer Service')")

connection.commit()
connection.close()
