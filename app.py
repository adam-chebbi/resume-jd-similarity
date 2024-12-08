from flask import Flask, request, render_template
from utils.text_extraction import extract_text_from_pdf
from utils.preprocessing import preprocess_text
from utils.similarity import calculate_similarity
from utils.insights import extract_keywords, match_keywords
from utils.visualization import generate_insights_chart
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # File Upload Handling
        cv_file = request.files['cv']
        jd_file = request.files['jd']
        
        cv_path = os.path.join(app.config["UPLOAD_FOLDER"], cv_file.filename)
        jd_path = os.path.join(app.config["UPLOAD_FOLDER"], jd_file.filename)

        cv_file.save(cv_path)
        jd_file.save(jd_path)

        # Extract text
        cv_text = extract_text_from_pdf(cv_path)
        jd_text = extract_text_from_pdf(jd_path)

        # Preprocess text
        cv_processed = preprocess_text(cv_text)
        jd_processed = preprocess_text(jd_text)

        # Calculate similarity
        similarity_score = calculate_similarity(cv_processed, jd_processed)

        # Generate insights
        cv_keywords = extract_keywords(cv_processed)
        jd_keywords = extract_keywords(jd_processed)
        matched, missing = match_keywords(cv_keywords, jd_keywords)

        # Visualization
        chart_path = generate_insights_chart(matched, missing)

        return render_template(
            "results.html",
            similarity=similarity_score,
            matched=matched,
            missing=missing,
            chart_path=chart_path
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
