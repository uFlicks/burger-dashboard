#!/bin/bash

echo "=== Job Started at $(date) ==="

# Activate the virtual environment
source /venv/bin/activate

# Run the scripts
python etl_script/extract_data.py
streamlit run etl_script/dashbord.py --server.port=5000


