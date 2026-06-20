from datetime import date, timedelta
from src.domain.descriptors.date_future import DateFuture

class Test:
    date_fin = DateFuture()

t = Test()
t.date_fin = date.today() + timedelta(days=30)   # OK
print(t.date_fin)

t.date_fin = date.today() - timedelta(days=1)     # lève ValueError