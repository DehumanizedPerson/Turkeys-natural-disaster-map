#####################################
# TURKISH NATURAL DISASTER CALL API # => Version 0.1 | github @kaganerkan
#####################################

# Imports
from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi_limiter.depends import RateLimiter
import os

# Function Definitions

def getInfo(x: str, datasetPath: str) -> list:
    """
    Retrieve information for the specified key from a JSON file.

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

    # Check for empty input key
    if not x:
        raise ValueError("Input key cannot be empty.")

    # Verify dataset file exists
    if not os.path.isfile(datasetPath):
        raise FileNotFoundError(f"The file '{datasetPath}' does not exist.")

    # Attempt to load JSON data
    try:
        with open(datasetPath, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON format in '{datasetPath}': {e}")

    # Check if key exists in data
    if x not in data:
        raise KeyError(f"The key '{x}' was not found in the JSON data.")

    # Validate data type of the key's value
    requestedMaterial = data[x]
    if not isinstance(requestedMaterial, list):
        raise TypeError(f"The value for '{x}' must be a list, got {type(requestedMaterial).__name__} instead.")

    return requestedMaterial


def validateToken(x_token: str = Header(...)):
    """
    Token validation function to authenticate requests.

    Args:
        x_token (str): The token provided in the request header.

    Raises:
        HTTPException: If the token is invalid or missing.

    Returns:
        str: The validated token.
    """
    if x_token != os.getenv("API_TOKEN"):
        raise HTTPException(status_code=401, detail="Invalid or missing API token")
    return x_token

# API Instance Initialization
app = FastAPI()

# Main Endpoint Definition

@app.get("/api/turkish-natural-disaster/{x}", dependencies=[Depends(RateLimiter(times=5, seconds=60))])
async def get_info(x: str, token: str = Depends(validateToken)):
    """
    Fetch natural disaster data based on the specified key.

    Args:
        x (str): The specific key or category of information to retrieve.
        token (str): The validated API token, provided through dependency injection.

    Raises:
        HTTPException: Various HTTP exceptions based on possible errors during data retrieval.

    Returns:
        list: A list of relevant data related to the requested key.
    """
    try:
        result = getInfo(x)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected internal error occurred.")

##########################################
# Run command: uvicorn main:app --reload #
##########################################
