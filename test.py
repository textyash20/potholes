import sqlite3
from database import db

user=db.view_previous('yash@gm.com')

print(user[::-1])
