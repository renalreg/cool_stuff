from cool_stuff.cool_stuff_1 import conn

cur = conn.cursor()

query = """
    SELECT * FROM codes
"""

cur.execute(query)
results = cur.fetchall()

for result in results:
    print(f"All the info: {result}")

for result in results:
    print(f'Code: {result[2]}')