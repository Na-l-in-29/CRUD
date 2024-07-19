from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Home page"

@app.get("/numbers")
async def sub(numbers: str):
    count = {}
    values = numbers.replace(",", "")
    for elements in values:
        if elements in count:
            count[elements] += 1
        else:
            count[elements] = 1
    for key, freq in count.items():
        if freq > len(values) // 2:
            result =  key
    return result

# from fastapi import FastAPI
# from pydantic import BaseModel

# class Sub_Page(BaseModel):
#     numbers: str

#     def high(self):
#         count = {}
#         values = self.numbers.replace(",", "")
#         for element in values:
#             if element in count:
#                 count[element] += 1
#             else:
#                 count[element] = 1
#         for key, freq in count.items():
#             if freq > len(values) // 2:
#                 return key
#         return None

# app = FastAPI()

# @app.post("/sub")
# async def subpage(sub: Sub_Page):
#     result = sub.high()
#     return result
