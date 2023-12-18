import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import json

def extract_titles_and_sections_from_epub(file_path):
    book = epub.read_epub(file_path)

    content_structure = []
    current_title = {"title": "", "content": []}
    current_section = {"section_header": "", "section_content": []}

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.content, 'html.parser')
            for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul']):
                if element.name == 'h2':  # Main title
                    if current_section["section_content"]:  # Save the previous section
                        current_title["content"].append(current_section)
                    if current_title["title"]:  # Save the previous title
                        content_structure.append(current_title)
                    current_title = {"title": element.get_text(strip=True), "content": []}
                    current_section = {"section_header": "", "section_content": []}
                elif element.name in ['h3', 'h4']:  # Section headers
                    if current_section["section_content"]:  # Save the previous section
                        current_title["content"].append(current_section)
                    current_section = {"section_header": element.get_text(strip=True), "section_content": []}
                else:
                    text = element.get_text(strip=True)
                    current_section["section_content"].append(text)

    if current_section["section_content"]:  # Save the last section
        current_title["content"].append(current_section)
    if current_title["title"]:  # Save the last title
        content_structure.append(current_title)

    return content_structure

content_structure = extract_titles_and_sections_from_epub('./book_name.epub')

with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(content_structure, f, ensure_ascii=False, indent=4)
