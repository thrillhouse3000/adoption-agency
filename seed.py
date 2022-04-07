from models import Pet, db
from app import app

db.drop_all()
db.create_all()

germ = Pet(name='Germ', species='Dog', img_url='https://www.guidedogs.org/wp-content/uploads/2021/11/01.11.2021_SGD1014-Edit-1980x1321.jpg', age=9, notes='A good boy')

demon = Pet(name='Demon', species='Cat', img_url='https://www.rd.com/wp-content/uploads/2021/01/GettyImages-1175550351.jpg?resize=2048,1339', age=5, notes='A bad girl')

db.session.add_all([germ, demon])
db.session.commit()