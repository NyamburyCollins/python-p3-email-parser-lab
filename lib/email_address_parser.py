# your code goes here!
import re
class EmailAddressParser:
    def __init__(self, emails):
        self.emails = emails

    def parse(self):
        # Split emails using both commas and spaces as separators
        split_emails = re.split(r'[, ]+', self.emails)
        
        # Filter valid emails using regex pattern
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        valid_emails = [email for email in split_emails if re.match(email_pattern, email)]
        
        # Remove duplicates and sort alphabetically
        unique_emails = list(set(valid_emails))
        unique_emails.sort()
        
        return unique_emails