import docx

def getText(filename):
    doc = docx.Document(filename)
    fulltext = []
    for para in doc.paragraphs:
        fulltext.append(para.text)
    return '\n'.join(fulltext)

print(getText('C:\\Users\\3azzouz\\mypythonscripts\\demo.docx'))
