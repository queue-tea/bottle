import sqlite3
conn = sqlite3.connect('todo.db') # Warning: This file is created in the current directory
conn.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, description char(500) NOT NULL, posted DATE, due DATE, updated DATE, status bool NOT NULL)")
conn.execute("INSERT INTO todo (task, description, posted, due, updated, status) VALUES ('Finish HW3', 'Don''t procrastinate', '2018-02-20', '2018-02-28', '2018-02-20', 0)")
conn.execute("INSERT INTO todo (task, description, posted, due, updated, status) VALUES ('Buy toothpaste','To have a nicer painful smile', '2018-02-20', '2018-02-28', '2018-02-20', 1)")
conn.execute("INSERT INTO todo (task, description, posted, due, updated, status) VALUES ('Give wife a thumbs up','She''s doing a great job at being a wife', '2018-02-20', '2018-03-01', '2018-02-20', 1)")
conn.execute("INSERT INTO todo (task, description, posted, due, updated, status) VALUES ('Eat Bart Simpson''s shorts','Pairs well with BBQ sauce and red wine', '2018-02-20', '2018-02-28', '2018-02-20', 0)")
conn.execute("INSERT INTO todo (task, description, posted, due, updated, status) VALUES ('Avoid the paparazzi', 'Harold memes are on the rise', '2018-02-20', '2018-03-05', '2018-02-20', 0)")
conn.execute("INSERT INTO todo (task, description, posted, due, updated, status) VALUES ('Bake a pie for mum', 'Make sure it''s apple pie', '2018-02-20', '2018-03-03', '2018-02-20', 0)")
conn.commit()
