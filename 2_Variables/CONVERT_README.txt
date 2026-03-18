================================================================================
Converting the Variables Chapter to DOCX and PDF
================================================================================

DOCX (Word)
-----------
Run from this folder (2_Variables):

   python md_to_docx.py

Output: CHAPTER_Variables.docx

Requirements: pip install python-docx

The script reads CHAPTER_Variables.md and embeds images from the diagrams/
folder (variable_assignment.png, input_to_variable.png, data_types_overview.png,
bodmas_precedence.png, fstring_syntax.png).


PDF
---
Open CHAPTER_Variables.docx in Microsoft Word and use File > Save As > PDF.
Or open in LibreOffice Writer and use File > Export As > Export as PDF.


Diagrams
--------
diagrams/
  variable_assignment.png   - Variable as a named box; assignment
  input_to_variable.png     - User input flow into a variable
  data_types_overview.png   - int, float, str, bool
  bodmas_precedence.png     - BODMAS order of operations
  fstring_syntax.png        - f-strings: variables in { } replaced

To add more diagrams: put PNG/JPG in diagrams/, add a line in the Markdown:
  ![Description](diagrams/your_image.png)
Then run: python md_to_docx.py
