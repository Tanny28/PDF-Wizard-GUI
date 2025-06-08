import tkinter as tk
from tkinter import filedialog, messagebox
import os
from pdf_utils import merge_pdfs, split_pdf

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

class PDFWizardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📄 PDF Wizard – Merge & Split")
        self.root.geometry("500x350")
        self.root.resizable(False, False)

        # File lists
        self.merge_files = []
        self.split_file = ""

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="PDF Merge & Split Tool", font=("Arial", 16)).pack(pady=10)

        # Merge Frame
        merge_frame = tk.LabelFrame(self.root, text="Merge PDFs")
        merge_frame.pack(padx=10, pady=5, fill="x")

        tk.Button(merge_frame, text="Select PDFs", command=self.select_merge_files).pack(pady=5)
        tk.Button(merge_frame, text="Merge & Save", command=self.merge_pdfs).pack()

        # Split Frame
        split_frame = tk.LabelFrame(self.root, text="Split PDF")
        split_frame.pack(padx=10, pady=5, fill="x")

        tk.Button(split_frame, text="Select PDF", command=self.select_split_file).pack(pady=5)
        tk.Button(split_frame, text="Split & Save", command=self.split_pdf).pack()

        # Output message
        self.status_label = tk.Label(self.root, text="", fg="green")
        self.status_label.pack(pady=10)

        # Clear + Exit
        tk.Button(self.root, text="Clear", command=self.clear_all).pack(side="left", padx=20, pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(side="right", padx=20, pady=10)

    def select_merge_files(self):
        files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        if files:
            self.merge_files = files
            self.status_label.config(text=f"{len(files)} PDFs selected for merge")

    def select_split_file(self):
        file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file:
            self.split_file = file
            self.status_label.config(text="1 PDF selected for split")

    def merge_pdfs(self):
        if not self.merge_files:
            messagebox.showwarning("No Files", "Please select PDF files to merge.")
            return
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF File", "*.pdf")])
        if output_path:
            result = merge_pdfs(self.merge_files, output_path)
            self.status_label.config(text=result)

    def split_pdf(self):
        if not self.split_file:
            messagebox.showwarning("No File", "Please select a PDF to split.")
            return
        output_dir = filedialog.askdirectory()
        if output_dir:
            result = split_pdf(self.split_file, output_dir)
            self.status_label.config(text=result)

    def clear_all(self):
        self.merge_files = []
        self.split_file = ""
        self.status_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFWizardApp(root)
    root.mainloop()
