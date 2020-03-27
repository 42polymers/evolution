import os
import sqlite3


conn = sqlite3.connect(os.path.join(os.path.dirname(os.getcwd()), 'evo.db'))
cursor = conn.cursor()
