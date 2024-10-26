#####################################
# TURKISH NATURAL DISASTER CALL API # => Verison 0.1
#####################################

# Import
from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi_limiter.depends import RateLimiter
import os

def getInfo(x: str , datasetPath: str) -> list: # Pull info from database.
    """
    Retrieve information for the specified key from a JSON file:
        Args:
            x (str): The key to retrieve from the JSON file.
            datasetPath (str): Path to the JSON file.
        Returns:
            list: The value associated with the key if found and is a list.
        Raises:
            ValueError: If the input key is empty.
            FileNotFoundError: If the JSON file does not exist.
            KeyError: If the specified key is not found in the JSON file.
            TypeError: If the value associated with the key is not a list.
            json.JSONDecodeError: If the JSON file contains invalid JSON.
    """

    if not x:
        raise ValueError("Input key cannot be empty.")

    if not os.path.isfile(datasetPath):
        raise FileNotFoundError(f"The file '{datasetPath}' does not exist.")

    try:
        with open(datasetPath, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON format in '{datasetPath}': {e}")

    if x not in data:
        raise KeyError(f"The key '{x}' was not found in the JSON data.")

    requestedMaterial = data[x]

    if not isinstance(requestedMaterial, list):
        raise TypeError(f"The value for '{x}' must be a list, got {type(requestedMaterial).__name__} instead.")

    return requestedMaterial

        
def validateToken(x_token: str = Header(...)): # Token valitation function. (WIP didnt write the explanation in it.)
    if x_token != os.getenv("API_TOKEN"):
        raise HTTPException(status_code=401, detail="Invalid or missing API token")
    return x_token

# API Start Here
app = FastAPI()

@app.get("/api/turkish-natural-disaster/{x}", dependencies=[Depends(RateLimiter(times=5, seconds=60))]) # Main function to 
async def get_info(x: str, token: str = Depends(validateToken)):
    try:
        result = getInfo(x)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) # Bad Request Error / Input Invalid
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected internal error occurred.") # Internal Server Error / Unexpected Issue

##########################################
# Run command: uvicorn main:app --reload #
##########################################