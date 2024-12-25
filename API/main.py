#####################################
# TURKISH NATURAL DISASTER CALL API # => Verison 1.2 | 
#####################################

# Import
from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.responses import HTMLResponse
from pathlib import Path
import os
import json

# Functions
def load_json(filePath: str) -> dict | list:
    """
    Load a JSON file and return its related content.

    Args:
        filePath (str): The path to the JSON file.

    Returns:
        dict | list: Parsed JSON content as a Python object.
    """
    
    with open(filePath, 'r', encoding='utf-8') as file:
        return json.load(file)

def dump_json(data: dict | list, filePath: str) -> None:
    """
    Write Python data to a JSON file.

    Args:
        data (dict or list): The data to write to the file. Must be JSON-serializable.
        filePath (str): The path to the output JSON file.

    Raises:
        TypeError: If the data is not JSON-serializable.
        IOError: If there is an issue writing to the file.
    """
    directory = os.path.dirname(filePath)
    os.makedirs(directory, exist_ok=True)
    with open(filePath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


# Algorithm Start Here
app = FastAPI()

## Access To API Systems 
@app.get("/api/turkish-natural-disaster/{x}")
async def get_info(x: str) -> dict:
    """
    This function retrieves information about Turkish natural disasters.

    Args:
        x (str): Identifier for the natural disaster.
        token (str): Token for authorization, validated by validateToken dependency.

    Returns:
        dict: Response containing the disaster information.
    """
    try:
        data = load_json("storage.json")
        return data.get(x, {"error": "Data not found."})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/turkish-natural-disaster/{x}")
async def post_info(x: str, data: dict):
    """
    This function handles POST requests to add or update information about Turkish natural disasters.

    Args:
        x (str): Identifier for the natural disaster.
        data (dict): The payload containing the information to be added or updated.

    Returns:
        dict: Response indicating success or failure of the operation.
    """
    file_path = "storage.json"
    try:
        # Load existing data
        existing_data = load_json(file_path)

        # Update or add the data
        existing_data[x] = data

        # Save the updated data
        dump_json(existing_data, file_path)

        return {"success": True, "message": "Data updated successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

##########################################
# Run command: uvicorn main:app --reload #
##########################################
