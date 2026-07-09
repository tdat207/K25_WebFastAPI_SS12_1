from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import engine, get_db
import models, schemas, crud


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.put("/products/{product_id}", response_model=schemas.ProductResponse)
def update_product_api(product_id: int, product_update: schemas.ProductUpdate, db: Session = Depends(get_db)):
   
    updated_product = crud.update_product(db=db, product_id=product_id, product_update=product_update)
    
    if updated_product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        
    return updated_product