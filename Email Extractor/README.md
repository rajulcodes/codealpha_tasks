# Email Address Extractor 📧

A simple and efficient Python script to extract valid email addresses from a text file and save them to another file.

## Features

* Uses regular expressions to match standard email patterns
* Ensures unique email extraction using Python sets
* Automatically creates a sample input file if none exists
* Accepts user-defined input/output file paths
* Supports `.txt` files with UTF-8 encoding

## Technologies Used

* Python 3.x
* `re` module for regex pattern matching
* `os` module for file existence checks

## How It Works

1. The script checks if an `input_emails.txt` file exists.
2. If not, it creates a dummy file with example email addresses.
3. Prompts the user to enter input and output file names (with defaults).
4. Scans the input file for email addresses using regex.
5. Writes all unique email addresses to the specified output file.

## Running the Script

```bash
python email_extractor.py
```

## Sample Output

```
--- Email Address Extractor ---
Creating a dummy input file: input_emails.txt
Dummy input file created with example emails.
Enter the input text file name (default: input_emails.txt):
Enter the output file name (default: extracted_emails.txt):
Attempting to extract emails from: input_emails.txt
Found 4 unique email addresses.
Successfully saved extracted emails to: extracted_emails.txt
```

## Example Emails Extracted

* [test@example.com](mailto:test@example.com)
* [support@company.org](mailto:support@company.org)
* [info.contact@mail.co.uk](mailto:info.contact@mail.co.uk)
* [another.user@my-domain.info](mailto:another.user@my-domain.info)

## Customization

You can modify the regex pattern to match specific types of emails or domain constraints.

## License

MIT License

---

Automate your inbox mining with ease! 🪯
