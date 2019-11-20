from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()



def add_product(name, price, picture_link, description):
    product_object = product(
        name=name,
        price=price,
        picture_link = picture_link,
        description = description
        )
    session.add(product)
    session.commit()

def query_product_by_id(id_number):
	Product = session.query(Product).filter_by(
		id_number=id_number).first()
	return Customer
