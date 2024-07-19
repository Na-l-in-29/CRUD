from fastapi import FastAPI

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def swap(ptr1, ptr2):
    tmp = ptr2.data
    ptr2.data = ptr1.data
    ptr1.data = tmp

def bubbleSort1(head):
    if not head:
        return None

    swapped = True
    while swapped:
        swapped = False
        current = head
        while current.next:
            if current.data > current.next.data:
                swap(current, current.next)
                swapped = True
            current = current.next
        convertListToPythonList(head)

def convertListToPythonList(head):
    python_list = []
    current = head
    while current:
        python_list.append(current.data)
        current = current.next
    return python_list

def insertAtTheBegin(start_ref, data):
    ptr1 = Node(data)
    ptr1.next = start_ref
    return ptr1

app = FastAPI()

arr = "8 -> 9 -> 3 -> 0 -> 7"
elements = arr.split(" -> ")

start = None
for element in elements:
    start = insertAtTheBegin(start, int(element))

bubbleSort1(start)

@app.get("/sorted/ascending")
def get_sorted_ascending():
    sorted_list = convertListToPythonList(start)
    return {"sorted_ascending": sorted_list}

@app.get("/sorted/descending")
def get_sorted_descending():
    sorted_list = bubbleSort1(start)
    return {"sorted_ascending": sorted_list}



