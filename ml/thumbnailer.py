from pdf2image import convert_from_path
from PIL import Image
import os
import sys
from pathlib import Path

def create_pdf_thumbnail(pdf_path, output_dir="thumbnails", width=210, height=280):
    """
    Create a thumbnail from the first page of a PDF using pdf2image
    """
    print(f"Starting thumbnail creation for: {pdf_path}")
    
    try:
        # Check if PDF file exists
        if not os.path.exists(pdf_path):
            print(f"✗ PDF file not found: {pdf_path}")
            return None
        
        print(f"✓ PDF file found: {pdf_path}")
        
        # Create output directory if it doesn't exist
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        print(f"✓ Output directory ready: {output_dir}")
        
        # Convert first page to image
        print("Converting PDF first page to image...")
        pages = convert_from_path(pdf_path, first_page=1, last_page=1, dpi=150)
        
        if not pages:
            print("✗ No pages found in PDF")
            return None
            
        print(f"✓ PDF converted successfully")
        
        # Get the first page
        page = pages[0]
        print(f"✓ Original image size: {page.size}")
        
        # Resize to desired dimensions while maintaining aspect ratio
        page.thumbnail((width, height), Image.Resampling.LANCZOS)
        print(f"✓ Resized to: {page.size}")
        
        # Generate output filename using PDF name
        pdf_name = Path(pdf_path).stem
        thumbnail_path = Path(output_dir) / f"{pdf_name}.png"
        print(f"✓ Output path: {thumbnail_path}")
        
        # Save thumbnail
        print("Saving thumbnail...")
        page.save(thumbnail_path, "PNG")
        print(f"✓ Thumbnail saved successfully!")
        
        # Verify file was created
        if os.path.exists(thumbnail_path):
            file_size = os.path.getsize(thumbnail_path)
            print(f"✓ Thumbnail file created: {thumbnail_path} ({file_size} bytes)")
            return str(thumbnail_path)
        else:
            print("✗ Thumbnail file was not created")
            return None
        
    except Exception as e:
        print(f"✗ Error: {type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    print("=== PDF Thumbnail Generator ===")
    
    # Check if command line arguments are provided
    if len(sys.argv) > 1:
        # Use command line arguments
        pdf_file = sys.argv[1]
        output_dir = sys.argv[2] if len(sys.argv) > 2 else "thumbnails"
        width = int(sys.argv[3]) if len(sys.argv) > 3 else 300
        height = int(sys.argv[4]) if len(sys.argv) > 4 else 400
        
        print(f"Using command line arguments:")
        print(f"PDF file: {pdf_file}")
        print(f"Output directory: {output_dir}")
        print(f"Dimensions: {width}x{height}")
        
    else:
        # Interactive input from terminal
        print("No command line arguments provided. Using interactive mode.")
        
        # Get PDF file path
        pdf_file = input("Enter PDF file path: ").strip()
        if not pdf_file:
            print("✗ No PDF file specified. Exiting.")
            sys.exit(1)
        
        # Get output directory (optional)
        output_dir = input("Enter output directory (press Enter for 'thumbnails'): ").strip()
        if not output_dir:
            output_dir = "thumbnails"
        
        # Get dimensions (optional)
        try:
            width_input = input("Enter thumbnail width (press Enter for 300): ").strip()
            width = int(width_input) if width_input else 300
            
            height_input = input("Enter thumbnail height (press Enter for 400): ").strip()
            height = int(height_input) if height_input else 400
        except ValueError:
            print("Invalid dimensions. Using default 300x400.")
            width, height = 300, 400
    
    print(f"\nProcessing...")
    print(f"PDF: {pdf_file}")
    print(f"Output: {output_dir}")
    print(f"Size: {width}x{height}")
    print("-" * 40)
    
    # Create thumbnail
    result = create_pdf_thumbnail(pdf_file, output_dir, width, height)
    
    if result:
        print(f"\n🎉 SUCCESS!")
        print(f"Thumbnail created at: {result}")
    else:
        print(f"\n❌ FAILED to create thumbnail")
        sys.exit(1)
        
    print("\n=== End ===")
