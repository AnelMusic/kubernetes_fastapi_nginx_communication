from fastapi import FastAPI, Response
import httpx

import socket

app = FastAPI()
PORT = 8000

@app.get("/")
async def root():
    hello_message = f"<h1>Your API says hello from the {socket.gethostname()}</h1>"
    print(hello_message)
    return {"message": hello_message}

@app.get("/nginx")
async def nginx():
    url = 'http://nginx'  # service name works here due to Kubernetes internal DNS
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        html_content = response.text
        return Response(content=html_content, media_type="text/html")


async def fetch_todo_data():
    url = "https://jsonplaceholder.typicode.com/todos"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        todos = response.json()
        return todos

@app.get("/jsonplaceholder")
async def json_placeholder():
    todos = await fetch_todo_data()

    # Calculate basic statistics for illustration purposes
    total_todos = len(todos)
    user_ids = {todo['userId'] for todo in todos}
    unique_user_count = len(user_ids)

    # Prepare response including statistics
    stats = {
        "total_todos": total_todos,
        "unique_user_count": unique_user_count,
        "todos": todos  # Include the fetched todos as before
    }

    return stats

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
