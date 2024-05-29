 # Document Similarity Search with qdrant

This project provides a web application to perform real-time document (book) similarity searches using a pre-trained sentence transformer model. The application is built using Flask for the backend and plain HTML/CSS/JavaScript for the frontend. It leverages the Qdrant vector search engine to handle document embedding and similarity queries.

## Features

- Real-time document similarity search as you type
- Displays document name, description, price, and image
- Uses a pre-trained Sentence Transformer model for encoding
- JSON-based document storage
- Demonstrates integration with Qdrant vector search engine

## Getting Started

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/nijatzeynalov/document-similarity-search.git
    cd document-similarity-search
    ```

2. Install the required Python packages:
    ```sh
    pip install flask qdrant-client sentence-transformers
    ```

3. Start the Flask application:
    ```sh
    python app.py
    ```

4. Open your web browser and navigate to `http://127.0.0.1:5000/`.

5. Enter a query in the search box. The application will display the most similar documents in real-time, showing the document name, description, price, and image.


# Demonstration
As a demonstration, we are using a dataset of books. Each book has attributes like name, description, price, and an image URL. The application showcases how Qdrant can be used to find similar books based on the provided description.

# Benefits of Using Qdrant
High Performance: Qdrant is optimized for handling large datasets and high-dimensional vectors, providing fast and accurate similarity searches.
Ease of Use: Qdrant’s API is straightforward, making it easy to integrate with machine learning models and applications.
Flexibility: Qdrant supports various distance metrics and can be configured to suit different types of similarity searches.

