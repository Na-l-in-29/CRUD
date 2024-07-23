from fastapi import FastAPI
from pydantic import BaseModel

class Sub_Page(BaseModel):
    heading : str | None = "Sub page heading 0"
    description : str |None = "description of sub page 0"
    footer : str | None = "footer of subpage 0"
    page_no : int = 0
    page_dimension : float = 16.9

new_dict = {}

app = FastAPI()
# 
@app.get("/")
async def home():
    return new_dict

@app.post("/sub")
async def subpage(sub : Sub_Page):
    if new_dict.get(sub.page_no):
        sub_copy = dict(sub)
        new_dict[sub.page_no] = sub_copy
        return "subpage updated"
    else:
        new_dict[sub.page_no] = sub
        return "sub page created"
# @app.put("/sub/put")
# async def put(sub : Sub_Page):
#         if new_dict.get(sub.page_no):
#             new_dict[sub.page_no] = sub
#             return "subpage updated"
#         else:
#              return "sub page can't update"
@app.put("/sub1/{page_no}")
async def put(page_no : int,sub : Sub_Page):
        print(new_dict.get(page_no))
        if new_dict.get(page_no):
            new_dict[page_no] = sub
            return "subpage updated"
        else:
             return "sub page can't update"
        
@app.delete("/sub2/{page_no}")
async def delete(page_no : int, sub : Sub_Page):
    if new_dict.get(page_no):
        del new_dict[page_no]
        return "Sucessfully deleted"
    else:
        return "Sub page can't delete"
        
@app.patch("/sub3/{page_no}")
async def patched(page_no : int, sub : Sub_Page):
    if new_dict.get(page_no):
        sub_copy = dict(sub)
        for key, value in sub_copy.items():
            new_dict[page_no][key] = sub_copy[key]
        return new_dict
    else:
        return "can't update"