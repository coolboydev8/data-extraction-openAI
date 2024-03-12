import os
from pypdf2 import PdfReader
# Assuming liteelm library is available (replace with actual implementation)
from liteelm import completion

def create_message(content, role="system"):
  """
  Creates a dictionary object for OpenAI API messages.
  """
  return {"content": content, "role": role}

# Set the default PDF file path
file_path = "learning_context.pdf"

# Read the PDF document
reader = PdfReader(file_path)
num_pages = len(reader.pages)

# Loop through each page
for page_num in range(num_pages):
  page = reader.pages[page_num]
  page_text = page.extract_text()  # Extract text from the page

  # Define messages for OpenAI API
  system_message = create_message("I am an expert in summarizing research papers.")
  user_message = create_message(f"Can you summarize this text in less than 200 words?\n{page_text}", role="user")

  # Create list of messages
  messages = [system_message, user_message]

  # Call OpenAI API to summarize the page (replace with actual implementation)
  response = completion(os.environ.get("OPENAI_API_KEY"), messages=messages)
  
  # Print the summarized text
  try:
    summary = response.choices[0].text.strip()
    print(f"Summary of Page {page_num + 1}:\n{summary}")
  except (AttributeError, IndexError):
    print(f"Error: Failed to summarize page {page_num + 1}")

