import os
import csv
from datetime import datetime

def log_interaction(session_id: str, query: str, response: str, is_crisis: bool):
    """Log the user interaction to a CSV file."""
    log_file = 'interactions_log.csv'
    file_exists = os.path.isfile(log_file)
    
    with open(log_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write header if file does not exist
        if not file_exists:
            writer.writerow(['timestamp', 'session_id', 'query', 'response', 'crisis_flag'])
        
        # Write the interaction data
        writer.writerow([datetime.now().isoformat(), session_id, query, response, str(is_crisis)])