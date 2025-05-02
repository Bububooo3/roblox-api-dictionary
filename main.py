from fastapi import FastAPI, Response
import json

app = FastAPI()


@app.get("/json-file")
async def read_json_file():
    # Read data from the JSON file
    with open("data.json", "r") as file:
        data = json.load(file)

    # Return the data as a JSON response
    return Response(content=json.dumps(data), media_type="application/json")