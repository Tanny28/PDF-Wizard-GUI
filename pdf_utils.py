import os
from PyPDF2 import PdfMerger, PdfReader
import logging

os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename="logs/wizard.log", level=logging.INFO)

def merge_pdfs(file_paths, output_path):
    try:
        merger = PdfMerger()
        for path in file_paths:
            merger.append(path)
        merger.write(output_path)
        merger.close()
        logging.info(f"Merged {len(file_paths)} files into {output_path}")
        return f"✅ Merged into {output_path}"
    except Exception as e:
        logging.error(f"Merge failed: {str(e)}")
        return f"❌ Merge failed: {str(e)}"

def split_pdf(file_path, output_dir):
    try:
        os.makedirs(output_dir, exist_ok=True)
        reader = PdfReader(file_path)
        for i, _ in enumerate(reader.pages):
            merger = PdfMerger()
            merger.append(file_path, pages=(i, i+1))
            output_file = os.path.join(output_dir, f"page_{i+1}.pdf")
            merger.write(output_file)
            merger.close()
        logging.info(f"Split {file_path} into {len(reader.pages)} pages")
        return f"✅ Split into {len(reader.pages)} pages at {output_dir}"
    except Exception as e:
        logging.error(f"Split failed: {str(e)}")
        return f"❌ Split failed: {str(e)}"
