import os
from app.models import Document, db  # Import db and Document model
from app.file_parsers import read_txt, read_pdf, read_docx, read_xlsx  # Ensure these functions exist

def parse_file(file_path):
    """
    Parse a file based on its extension and return the content as a list of paragraphs.
    """
    file_extension = file_path.lower()
    if file_extension.endswith(".txt"):
        return read_txt(file_path)
    elif file_extension.endswith(".pdf"):
        return read_pdf(file_path)
    elif file_extension.endswith(".docx"):
        return read_docx(file_path)
    elif file_extension.endswith(".xlsx"):
        return read_xlsx(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path}")

DATA_FOLDER = "data"

def save_documents_to_db():
    """
    Save the content of all files in the data folder into the Document database table.
    """
    try:
        # Clear the "documents" table
        Document.query.delete()  # This will delete all existing rows in the table
        db.session.commit()  # Commit changes (table is cleared)

        # Process files and save their content
        for file in os.listdir(DATA_FOLDER):
            file_path = os.path.join(DATA_FOLDER, file)
            if file.lower().endswith((".txt", ".pdf", ".docx", ".xlsx")):
                paragraphs = parse_file(file_path)  # Parse file into paragraphs
                content = "\n".join(paragraphs)  # Join paragraphs into one content string
                document = Document(name=file, content=content)  # Create a Document object
                db.session.add(document)  # Add to the session

        # Commit the changes after processing all files
        db.session.commit()  # Save all added documents to the database
    
    except Exception as e:
        # Rollback the session in case of any errors
        db.session.rollback()  # This ensures the session is rolled back in case of error
        print(f"Error saving documents to the database: {e}")

