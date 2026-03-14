from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Client connected")

    try:
        while True:
            # Receive message from client
            message = await websocket.receive_text()

            # Send response back
            response = f"Server received: {message}"
            await websocket.send_text(response)

    except WebSocketDisconnect:
        print("Client disconnected")
