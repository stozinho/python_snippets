from datetime import datetime 

# isoformat 
today = datetime.utcnow().isoformat()

date_for_filename = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")

