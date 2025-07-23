import re
import os

def extract_emails_from_file(input_filepath, output_filepath):
    """
    Extracts all valid email addresses from an input text file
    and saves them to an output text file, one email per line.

    Args:
        input_filepath (str): The path to the input text file.
        output_filepath (str): The path to the output text file where emails will be saved.
    """
    # Regular expression for matching email addresses.
    # This regex is a common pattern that covers most standard email formats.
    # It looks for:
    #   [a-zA-Z0-9._%+-]+ : one or more alphanumeric characters, dots, underscores, percents, plus, or hyphens (username)
    #   @                 : the at symbol
    #   [a-zA-Z0-9.-]+   : one or more alphanumeric characters, dots, or hyphens (domain name)
    #   \.                : a literal dot (escaped with \)
    #   [a-zA-Z]{2,}      : two or more letters (top-level domain, e.g., com, org)
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    
    found_emails = set() # Use a set to store unique email addresses

    print(f"Attempting to extract emails from: {input_filepath}")
    try:
        # Open the input file for reading
        with open(input_filepath, 'r', encoding='utf-8') as infile:
            content = infile.read() # Read the entire content of the file
            
            # Find all matches of the email pattern in the content
            matches = email_pattern.findall(content)
            
            # Add found emails to the set to ensure uniqueness
            for email in matches:
                found_emails.add(email)
        
        print(f"Found {len(found_emails)} unique email addresses.")

        # Open the output file for writing
        with open(output_filepath, 'w', encoding='utf-8') as outfile:
            if not found_emails:
                outfile.write("No email addresses found in the input file.\n")
                print("No email addresses found. Output file created but is empty.")
            else:
                # Write each unique email address to the output file, followed by a newline
                for email in sorted(list(found_emails)): # Sort for consistent output
                    outfile.write(email + '\n')
                print(f"Successfully saved extracted emails to: {output_filepath}")

    except FileNotFoundError:
        print(f"Error: The input file '{input_filepath}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to run the email extraction script.
    """
    print("--- Email Address Extractor ---")
    
    # Define default input and output file names
    default_input_file = "input_emails.txt"
    default_output_file = "extracted_emails.txt"

    # Create a dummy input file for demonstration if it doesn't exist
    if not os.path.exists(default_input_file):
        print(f"Creating a dummy input file: {default_input_file}")
        with open(default_input_file, 'w', encoding='utf-8') as f:
            f.write("Hello, my email is test@example.com. You can reach me at support@company.org.\n")
            f.write("Also, try info.contact@mail.co.uk or user123@sub.domain.net.\n")
            f.write("Invalid email: not-an-email.com and another@.com\n")
            f.write("One more: another.user@my-domain.info\n")
        print("Dummy input file created with example emails.")

    input_file = input(f"Enter the input text file name (default: {default_input_file}): ")
    if not input_file:
        input_file = default_input_file

    output_file = input(f"Enter the output file name (default: {default_output_file}): ")
    if not output_file:
        output_file = default_output_file

    extract_emails_from_file(input_file, output_file)

if __name__ == "__main__":
    main()
