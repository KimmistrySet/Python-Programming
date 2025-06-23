import re


def find_patterns(text):
    """
    Regular expression pattern for email addresses.
    """
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    # Regular expression pattern for phone numbers.
    phone_pattern = r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b"

    found_emails = re.findall(email_pattern, text)
    found_phones = re.findall(phone_pattern, text)

    return found_emails, found_phones


if __name__ == "__main__":
    sample_text = """
    Please contact us at support@example.com or call us at 123-456-7890.
    You can also reach out to info@example.org or 987.654.3210.
    Thank you for contacting us!
    """
    emails, phones = find_patterns(sample_text)
    print("Emails found:", emails)
    for email in emails:
        print("Email:", email)
    print("Phone numbers found:", phones)
    for phone in phones:
        print("Phone:", phone)