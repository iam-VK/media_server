#!/bin/bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt

# mysql -u groot -p search_engine < DB_DUMP.sql