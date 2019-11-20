from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()



def add_product(name, price, picture_link, description):
    student_object = Student(
        name=name,
        price=price,
        picture_link = picture_link
        description=description)
    session.add(product)
    session.commit()
