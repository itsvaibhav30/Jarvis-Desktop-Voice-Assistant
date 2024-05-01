from flask import Flask, request, jsonify,render_template
import jarvis

app = Flask(__name__)

@app.route("/")
def landing():   
    return render_template("index.html")

# @app.route('/jarvis/time', methods=['POST'])
# def get_time():
#     from jarvis import time
    
#     # Call your time function from your Jarvis code here (e.g., time())
#     # Extract the time as a string
#     time_string = time()#"Current time is..."  # Replace with actual time retrieval
#     return jsonify({'time': time_string})

# # Similar routes for other functionalities (date, wikipedia search, etc.)

if __name__ == '__main__':
    app.run(host="0.0.0.0")