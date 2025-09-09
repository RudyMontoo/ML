from fastapi import FastAPI
app=FastAPI()
@app.get("/hello")
def hello():
    return "Hello Rudra"



@app.get("/")
def hello():
    return "Hello"

food_item={
    'indian' : ["Samosa","Dosa"],
    'american' : ["Hot dog","Apple pie"],
    'italian':["Pizza","pasta"]
}

@app.get("/get_items/{cuisine}")
def get_items(cuisine):
    return food_item.get(cuisine)