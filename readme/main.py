import fitz  # PyMuPDF
import questionary

def read_toc(pdf_path):
    doc = fitz.open(pdf_path)
    toc = doc.get_toc()
    doc.close()
    return toc

def extract_text_from_pages(pdf_path, start, end):
    doc = fitz.open(pdf_path)
    pages = [doc.load_page(num).get_text() for num in range(start, end)]
    doc.close()
    return pages

pdf_path = questionary.path('path to book pdf').ask()
toc = read_toc(pdf_path)

manual_choice = questionary.Choice(title="Manual Page Range", value='manual')
# title is name of section w/ indentation
# value is a tuple of start page and stop page
sec_choices = [questionary.Choice(title='   '*(sec[0]-1)+sec[1], value=(sec[2]-1,next_sec[2]-1))
               for sec,next_sec in zip(toc[:-1],toc[1:])]
choices = [manual_choice] + sec_choices


pages = questionary.select("What pages would you like to study?",choices).ask()
if pages == 'manual':
    start = questionary.text("start page").ask()
    end = questionary.text("end page").ask()
    pages = (int(start), int(end))

page_texts = extract_text_from_pages(pdf_path, pages[0], pages[1])
for page in page_texts:
    print('\n\n', page[:4096])
