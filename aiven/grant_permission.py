import psycopg2

from config import URI, PG_USER

conn = psycopg2.connect(URI)
cur = conn.cursor()
cur.execute("GRANT CONNECT ON DATABASE defaultdb TO " + PG_USER + ";")
cur.execute("GRANT USAGE ON SCHEMA public TO " + PG_USER + ";")
