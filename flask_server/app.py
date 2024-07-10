from flask import Flask, request, jsonify
from main import recommend_song  # Import your recommendation function

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    song_name = data.get('song')
    recommendations = recommend_song(song_name)  # Call your recommendation function
    print(f"Returning recommendations: {recommendations}")
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
