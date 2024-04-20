
import fastapi
import uvicorn



app = fastapi.FastAPI()



@app.get("/")
async def read_root():
    return {"message": "Hello"}








if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

