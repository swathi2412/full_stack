from flask import Flask, jsonify, request
from data_processing import load_data
from flask_cors import CORS
from recommender import Recommender
from llm import understand_query, explain

app = Flask(__name__)
CORS(app)


df = load_data()
rec = Recommender(df)

@app.route("/")
def home():
    return "AI Recommendation Engine Running"

@app.route("/recommend/<int:user_id>")
def recommend(user_id):
    products = rec.recommend(user_id)

    results = []
    for p in products:
        results.append({
            "product": str(p),
            "why": explain(p, "Similar users purchased this frequently")
        })

    return jsonify({
        "user": user_id,
        "recommendations": results
    })


@app.route("/query")
def query():
    q = request.args.get("q")

    info = understand_query(q)

    if info["category"] is None:
        products = rec.trending()
    else:
        products = rec.trending()

    response = []
    for p in products:
        response.append({
            "product": str(p),
            "why": explain(p, f"Fits {info['use_case']} needs in {info['category']} category")
        })

    return jsonify({
        "query": q,
        "understood": info,
        "results": response
    })


@app.route("/coldstart")
def cold_start():
    products = rec.trending()

    return jsonify({
        "message": "New user detected — showing popular products",
        "recommendations": products
    })


if __name__ == "__main__":
    app.run(debug=True)
