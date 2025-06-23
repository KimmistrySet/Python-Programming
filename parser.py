import PyPDF2
from docx import Document


def read_pdf(file_path):
    """Read text from a PDF file."""
    text = ""
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text.strip()
    except (FileNotFoundError, PyPDF2.errors.PdfReadError, AttributeError) as e:
        return f"Failed to read PDF: {e}"


def read_word(file_path):
    """Read text from a Word document."""
    text = ""
    try:
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text.strip()
    except (FileNotFoundError, IOError) as e:
        return f"Failed to read Word document: {e}"


if __name__ == "__main__":
    pdf_file_path = "example.pdf" # Replace with your PDF file path
    word_file_path = "example.docx" # Replace with your Word file path
    pdf_text = read_pdf(pdf_file_path)
    word_text = read_word(word_file_path)
    print("PDF Text:\n", pdf_text)
    print("Word Text:\n", word_text)

