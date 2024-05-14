from PIL import Image
import pytesseract

def extract_text(image_path):
    try:
        breakpoint()
        # Open the image
        image = Image.open(image_path)
        
        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(image)
        return text
    except IOError:
        return "Error: The image file could not be opened."
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    image_path = r"C:\\Users\\vinayeswara.reddy\\Documents\\Text_Project\\Text_Extraxction\\test.jpg"
    extracted_text = extract_text(image_path)
    print("Extracted Text:\n", extracted_text)
