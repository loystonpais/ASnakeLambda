import json
import subprocess
import os
from ASnake import build


def lambda_handler(event, context):
    # Get code from event
    source = event["code"]

    # Write the generated code to a temporary file
    temp_file = "/tmp/generated_code.py"
    with open(temp_file, "w") as file:
        file.write(source)

    # Execute the generated Python code using a subprocess
    try:
        result = subprocess.run(
            ["python3", temp_file],
            text=True,
            capture_output=True,
            check=True
        )
        output = result.stdout.strip()
    except subprocess.CalledProcessError as e:
        output = f"Error: {e.stderr.strip()}"

    # Return the output or error
    return {
        'statusCode': 200,
        'body': json.dumps(output)
    }
