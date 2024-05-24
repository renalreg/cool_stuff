from cool_stuff.cool_stuff_1 import conn
from radar_models.radar2 import Diagnose
from sqlalchemy import select

session = conn.session()

query = select(Diagnose.id, Diagnose.name)

results = session.execute(query)

for result in results:
    print(result)

query = select(Diagnose.id).where(Diagnose.name == 'Cytomegalovirus infection (CMV)')

results = session.execute(query)

for result in results:
    print(f"The diagnoses you are looking for has an ID of {result[0]}")
    