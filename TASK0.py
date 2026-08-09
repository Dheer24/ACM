import re
from datetime import datetime

def transform_logs(input_text: str) -> str:
    # 1. Mask sensitive data (Emails)
    # Matches standard email structures
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    text = re.sub(email_pattern, '[HIDDEN]', input_text)
    
    # 2. Add a fun flag (Error Highlighting)
    # \b ensures we only match the exact word "ERROR"
    text = re.sub(r'\bERROR\b', '🚨 ERROR', text)
    
    # 3. Normalize timestamps
    # Matches DD/MM/YYYY HH:MM
    date_pattern = r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}'
    
    def format_date(match) -> str:
        date_str = match.group(0)
        try:
            # Parse the string into a datetime object
            dt = datetime.strptime(date_str, '%d/%m/%Y %H:%M')
            
            # Logic for ordinal suffixes (st, nd, rd, th)
            day = dt.day
            if 11 <= day <= 13:
                suffix = 'th'
            else:
                suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
            
            # Format the month, year, and time (stripping leading zero from hour if present)
            time_str = dt.strftime("%I:%M %p").lstrip('0')
            month_year_str = dt.strftime("%B %Y")
            
            return f"{day}{suffix} {month_year_str}, {time_str}"
            
        except ValueError:
            # Fallback: if the date is invalid (e.g., 99/99/2025), return it unchanged
            return date_str

    # Pass the formatting function as the replacement argument
    text = re.sub(date_pattern, format_date, text)
    
    return text

# --- Testing the function ---
raw_log = "User john@mail.com logged in at 23/08/2025 14:05. ERROR: session timeout."
print("Input: ", raw_log)
print("Output:", transform_logs(raw_log))
