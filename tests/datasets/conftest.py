import sys
from pathlib import Path

# Get the directory two levels up
parent_directory = Path(__file__).resolve().parents[2]

# Add it to the system path
sys.path.insert(0, str(parent_directory))