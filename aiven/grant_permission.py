"""Grants access to the postgress USER"""
from config import URI, PG_USER

import psycopg2

conn = psycopg2.connect(URI)
cur = conn.cursor()
cur.execute("GRANT CONNECT ON DATABASE defaultdb TO " + PG_USER + ";")
cur.execute("GRANT USAGE ON SCHEMA public TO " + PG_USER + ";")
