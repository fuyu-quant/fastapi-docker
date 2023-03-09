from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel, Field

# jsonの構造と同じにする
class ShopInfo(BaseModel):
    name: str
    location: str


class Item(BaseModel):
    name : str = Field(min_length=4, max_length=12)
    description: Optional[str] = None
    price : int
    tax : Optional[float] = None


class Data(BaseModel):
    shop_info: Optional[ShopInfo] = None
    items: List[Item]

app = FastAPI()

@app.post("/item/")
async def index(data: Data):
    return {"data": data}




#@app.get("/countries/")
#async def country(country_name: Optional[str] = None, country_no: Optional[int] = None):
#    return {
#        "country_name": country_name,
#        "country_no": country_no,       
#        }

 # at last, the bottom of the file/module
#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8040)