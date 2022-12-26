from fastapi import FastAPI, status
from typing import Optional

app = FastAPI()

items = {

    'phone_1': {'model': 'iphone1', 'made in': 'USA'},
    'phone_2': {'model': 'iphone2', 'made in': 'USA'},
    'phone_3': {'model': 'iphone3', 'made in': 'USA'},
    'phone_4': {'model': 'iphone4', 'made in': 'USA'},
    'phone_5': {'model': 'iphone5', 'made in': 'USA'},

}


@app.get('/')
async def oll_items(vew_items: Optional[str] = None):
    return {vew_items: items}


@app.post('/ad_item/')
async def add_item(item_name: str, item_description: str, ):
    id = 0
    if len(items) > 0:
        for item in items:
            x = int(item.split('_')[-1])
            if x > id:
                id = x
    items[f"phone_{id + 1}"] = {'mopdel': item_name, 'made in': item_description}
    return items[f'phone_{id + 1}']


@app.put('/update_item/')
async def updete_item(item_name, item_model, item_made_in):
    info = {'model': item_model, 'made in': item_made_in}
    items[item_name] = info
    return info


@app.delete('/delete_item/' , status_code=204)
async def delete_item(item_name):
    del items[item_name]
    return "HTTP_204_NO_CONTENT",
