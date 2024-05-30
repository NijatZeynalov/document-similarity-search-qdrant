import json
from flask import Flask, request, render_template, jsonify
from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

encoder = SentenceTransformer("LaBSE")

# Load data from JSON file
with open('data/data.json', 'r', encoding='utf-8') as f:
    documents = json.load(f)

client = QdrantClient(":memory:")

client.recreate_collection(
    collection_name="my_books",
    vectors_config=models.VectorParams(
        size=encoder.get_sentence_embedding_dimension(),  # Vector size is defined by used model
        distance=models.Distance.COSINE,
    ),
)
client.upload_points(
    collection_name="my_books",
    points=[
        models.PointStruct(
            id=idx, vector=encoder.encode(doc["description"]).tolist(), payload=doc
        )
        for idx, doc in enumerate(documents)
    ],
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    query_vector = encoder.encode(query).tolist()
    hits = client.search(
        collection_name="my_books",
        query_vector=query_vector,
        limit=3,
    )
    results = [
        {
            "name": hit.payload["name"],
            "description": hit.payload["description"],
            "price": hit.payload["price"],
            "image": hit.payload["image"],
            "score": hit.score
        }
        for hit in hits
    ]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port =5004)
