import pdfplumber
import docx2txt

def extract_text(file):
    if file.name.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                if page.extract_text():
                    text += page.extract_text()
        return text.lower()

    elif file.name.endswith(".docx"):
        return docx2txt.process(file).lower()

    else:
        return file.read().decode("utf-8").lower()
