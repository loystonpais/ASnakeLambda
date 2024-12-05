import json
import subprocess
import os
from ASnake import build

def lambda_handler(event, context):

    try:

        body = event["body"]

        # Check if "code" key is in the event body
        if "code" not in body:
            return {
                'statusCode': 400,
                'body': json.dumps("Error: 'code' key not found in event body.")
            }
        
        # Convert body to json
        body = json.loads(body)

        # Get code from event body
        asnake_source = body["code"]

        # Build the source code using the ASnake library
        source = build(asnake_source)

        # Write the generated code to a temporary file
        temp_file = "/tmp/transpiled.py"
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
    except Exception as e:
        # Server exceptions
        return {
            'statusCode': 500,
            'body': json.dumps(f"Server Error: {str(e)}")
        }
