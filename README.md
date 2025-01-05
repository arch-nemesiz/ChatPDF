# ChatPDF
# Interactive PDF Chat

This project is a Streamlit-based web application that allows users to interact with the content of their uploaded PDF documents using a conversational AI model. By leveraging LangChain, OpenAI's API, and FAISS for vector storage, the application processes PDF files, splits the text into manageable chunks, and provides an interactive chat interface for querying the document contents.

## Features

- **PDF Upload**: Users can upload multiple PDF files.
- **Text Extraction**: Extracts text from PDF files using `PyPDF2`.
- **Text Splitting**: Splits extracted text into chunks for efficient processing.
- **Embeddings and Vector Store**: Generates text embeddings using OpenAI or HuggingFace models and stores them in a FAISS vector store.
- **Conversational Interface**: Uses a conversational retrieval chain to answer user queries based on the PDF content.
- **Session Management**: Maintains conversation history within the session.

## Getting Started

### Prerequisites

- Python 3.7+
- Streamlit
- PyPDF2
- LangChain
- OpenAI API Key
- FAISS

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/interactive-pdf-chat.git
    cd interactive-pdf-chat
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Start the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Upload PDF files via the sidebar, ask questions, and interact with the content.

## Usage

- Upload one or more PDF files using the file uploader in the sidebar.
- Click on the "Process" button to load and process the files.
- Enter your queries in the text input field and receive conversational responses based on the content of your PDFs.

## File Structure

- `app.py`: Main application script.
- `htmlTemplates.py`: Contains HTML templates for styling the chat interface.
- `requirements.txt`: List of Python dependencies.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [LangChain](https://langchain.com/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [FAISS](https://github.com/facebookresearch/faiss)

## Contact

For any inquiries or issues, please contact [your-email@example.com](mailto:your-email@example.com).


