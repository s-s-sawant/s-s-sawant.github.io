import csv

def generate_book_library_from_csv(csv_file, output_file):
    """Generate HTML book library content from CSV data"""
    
    # Read CSV data
    books = []
    
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    
    # Generate content
    content = '<h1>\n  Library\n</h1>\n'
    content += '    <div class="book-slider-container" id="bookSlider">\n'
    
    # Generate book slides
    for i, book in enumerate(books, 1):
        content += f'      <!-- Book {i} -->\n'
        content += '      <div class="book-slide">\n'
        content += '        <div class="book-cover-container">\n'
        content += f'          <a href="{book["book_url"]}" target="_blank" rel="noopener">\n'
        content += f'            <img class="book-cover" src="{book["cover_image"]}" alt="{book["alt_text"]}">\n'
        content += '          </a>\n'
        content += '        </div>\n'
        content += '        <div class="book-info">\n'
        content += f'          <a href="{book["book_url"]}" class="book-title" target="_blank" rel="noopener">{book["title"]}</a>\n'
        content += f'          <div class="book-author">{book["author"]}</div>\n'
        content += '        </div>\n'
        content += '      </div>\n'
        
        if i < len(books):  # Add extra line break between books except for the last one
            content += '      \n'
    
    content += '      <!-- Add more books as needed -->\n'
    content += '    \n'
    content += '</div>'
    
    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Book library content generated successfully: {output_file}")
    print(f"Generated {len(books)} book entries")

# Usage
if __name__ == "__main__":
    generate_book_library_from_csv('books.csv', 'book_library.txt')
