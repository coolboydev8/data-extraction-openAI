# PDF Summarizer

This Python script extracts text from a PDF document and then uses an AI model (OpenAI's GPT-3) to summarize each page. The summarized text is then printed out.

## Prerequisites

- Python 3.x
- `pypdf2` library (`pip install pypdf2`)
- OpenAI API key
- `liteelm` library (replace with actual implementation)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your_username/pdf-summarizer.git
   cd pdf-summarizer
   ```

2. Install the required Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key as an environment variable. You can do this by exporting it in your shell configuration file (e.g., `.bashrc`, `.bash_profile`, or `.zshrc`):

   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```

## Usage

1. Place your PDF document in the same directory as the script or specify the path to your PDF file in the `file_path` variable within the script.

2. Run the script:

   ```bash
   python pdf_summarizer.py
   ```

3. The script will extract text from each page of the PDF, send it to the OpenAI API for summarization, and print the summarized text.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
