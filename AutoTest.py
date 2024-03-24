import json
import subprocess

# Run the program
subprocess.run(["/bin/python3", "Challenge.py"])

# Load expected output
with open("expected_output.json", "r") as f:
    expected_output = [json.loads(line.strip()) for line in f]

# Load actual output
with open("output.json", "r") as f:
    actual_output = [json.loads(line.strip()) for line in f]


print("Expected output:")
print(expected_output)

print("Actual output:")
print(actual_output)

# Assert both outputs are equal
assert expected_output == actual_output
