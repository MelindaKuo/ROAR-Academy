import PyPDF2
file_handle = open("Sense-and-Sensibility-by-Jane-Austen.pdf", 'rb')
pdf_reader = PyPDF2.PdfReader(file_handle)
page_number = len(pdf_reader.pages)

for page in range(page_number):
    page_object = pdf_reader.pages[page]
    page_text = page_object.extract_text()

    file_handle.close()

    lines = page_text.split("\n")
    freq = dict()

    for line in lines:
        words = line.split()
        for word in words:
            if word.isalpha():
            
                if word in freq:
                    freq[word]+=1
                else:
                    freq[word] = 1


print(freq)

