from sqlalchemy.orm import Session
from models import ProductModel
from schemas import ProductUpdate

def update_product(db: Session, product_id: int, product_update: ProductUpdate):
   
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    
    if not product:
        return None
        
    product.name = product_update.name
    product.price = product_update.price
    
    db.commit()
    db.refresh(product)
    
    return product