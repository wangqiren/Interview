import pdfplumber

with pdfplumber.open('C:/Users/10601/Desktop/Java研发工程师-王启人 .pdf') as pdf:
    text = ''
    for page in pdf.pages:
        t = page.extract_text()
        if t:
            text += t
        text += '\n\n--- PAGE BREAK ---\n\n'
    print(text)
