import csv
import re
from urllib.parse import urlparse, parse_qs

def extract_video_id(youtube_url):
    """Extract video ID from YouTube URL"""
    if 'youtu.be' in youtube_url:
        return youtube_url.split('/')[-1].split('?')[0]
    elif 'youtube.com' in youtube_url:
        parsed_url = urlparse(youtube_url)
        return parse_qs(parsed_url.query).get('v', [None])[0]
    return None

def generate_content_from_csv(csv_file, output_file):
    """Generate HTML content from CSV data"""
    
    # Read CSV data
    sections = {}
    
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            section = row['section']
            if section not in sections:
                sections[section] = []
            sections[section].append(row)
    
    # Generate content
    content = '<h1>\n    Video Gallery on Machine Learning\n</h1>\n'
    
    # Generate sections
    for section_name, videos in sections.items():
        content += f'<h2>{section_name}</h2>\n'
        
        for video in videos:
            video_id = extract_video_id(video['youtube_url'])
            if video_id:
                thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
                
                content += f'''    <div class="video-slide">
      <a href="{video['youtube_url']}" target="_blank" rel="noopener">
        <img class="video-thumb" src="{thumbnail_url}" alt="{video['alt_text']}">
        <span class="video-title">{video['title']}</span>
      </a>
    </div>
'''    
    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Content generated successfully: {output_file}")
    print("\nGenerated content:")
    print(content)

# Usage
if __name__ == "__main__":
    generate_content_from_csv('videos.csv', 'video_gallery.txt')
