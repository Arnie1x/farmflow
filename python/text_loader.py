import os
import pdfplumber

class TextLoader:
    def __init__(self, output_dir="assets/converted_texts"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def pdf_to_txt(self, pdf_path, excluded_pages=[]):
        """
        Converts a PDF file to a TXT file, excluding headers, footers, and specified pages.

        Args:
            pdf_path (str): The path to the PDF file.
            excluded_pages (list): A list of page numbers (0-indexed) to exclude.

        Returns:
            str: The path to the saved TXT file.
        """
        try:
            txt_content = []
            with pdfplumber.open(pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages):
                    if page_num not in excluded_pages:
                        # Extract text from the page
                        text = page.extract_text()

                        if text:
                            # Split text into lines and clean
                            lines = text.split("\n")
                            cleaned_lines = [
                                line.strip() for line in lines
                                if len(line.strip()) > 5  # Filter out very short lines
                            ]

                            # Optionally remove header/footer lines
                            if len(cleaned_lines) > 2:
                                cleaned_lines = cleaned_lines[1:-1]  # Exclude first and last line

                            txt_content.extend(cleaned_lines)

            # Save the converted text to a .txt file
            base_filename = os.path.splitext(os.path.basename(pdf_path))[0]
            txt_path = os.path.join(self.output_dir, f"{base_filename}.txt")
            
            with open(txt_path, "w", encoding="utf-8") as txt_file:
                txt_file.write("\n".join(txt_content))

            return txt_path

        except Exception as e:
            print(f"Error processing {pdf_path}: {e}")
            return None

    def load_text(self, txt_path):
        """
        Loads a TXT file and returns its content.

        Args:
            txt_path (str): The path to the TXT file.

        Returns:
            list: A list of document content where each item is a paragraph or section.
        """
        try:
            with open(txt_path, "r", encoding="utf-8") as file:
                content = file.read()
                return [content]  # Return content as a list for compatibility with Langchain processing
        except Exception as e:
            print(f"Error loading {txt_path}: {e}")
            return []

if __name__ == "__main__":
    # Create an instance of the TextLoader class
    text_loader = TextLoader()

    # Convert a PDF to a TXT file, excluding specified pages
    excluded_pages = [0, 1, 2, 3, 4, 5, 6, 7, 70]
    converted_txt_path = text_loader.pdf_to_txt("assets/pdfs/Kenya-Rice-Cultivation-Manual.pdf", excluded_pages=excluded_pages)

    # Load the TXT file content for processing
    if converted_txt_path:
        document_content = text_loader.load_text(converted_txt_path)
        # print(document_content[:1000])  # Print the first 1000 characters for verification