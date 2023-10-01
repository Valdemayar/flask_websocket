from fastapi import FastAPI, WebSocket, WebSocketDisconnect, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()
# Websocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_text()
            print(data)
            # if data == "start":
            #     # Code to handle the start of recording
            #     print(data)
            # elif data == "stop":
            #     # Code to handle the stop of recording and receive audio file
            #     audio_data = await websocket.receive_bytes()
            #     # Process or save the audio file as needed
            #     with open('path_to_save/audio.wav', 'wb') as audio_file:
            #         adudio_file.write(audio_data)
            #     # Send a response if needed
            #     await websocket.send_text("Audio received successfully")
        except WebSocketDisconnect:
            break

# File upload endpoint
# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile = File(...)):
#     # You can use this endpoint to upload the audio file if needed
#     return {"filename": file.filename}

@app.get("/healthcheck/")
async def healthcheck():
    return {"status": "OK"}
