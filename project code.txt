from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

# -----------------------------
# Sample University Data
# -----------------------------
responses = {
    "admission": "Admissions for new students usually start in July. Students can visit the admission section of the university website for detailed information.To take admission in university there are to methods online and offline.In online method apply for the course and give an entrance test and for offline if there will be seats vacent there will be offline counseling",

    "exam": "The examination schedule is updated by the university before exams begin. Students should regularly check notices or for the exam datesheet.",

    "result": "Students can check their results through the university result portal using their roll number and the result uploaded ususlly in 3 to 4 months.",

    "sports": "Sports activities and events are updated by the sports department regularly. Multiple sports are present in the university. ",

    "notice": "All university notices are available on the notice board section of the portal .",

    "scholarship": "Scholarship information can be collected from the scholarship section or university administration office or inn your department office .",

    "library": "The university library is open during working hours for all registered students. For applying library card contact to liberarien.",

    "hostel": "Hostel rooms are allotted according to university rules. Students can contact the hostel office for more details. rooms will be fully furnished and maintained.",

    "fees": "Students can submit their fees online through the university portal or at the fee counter. For offline fee deposit student can take a fee challan from there department and fill it and can submit there fees in bank which is in university.",

    "attendance": "Students are advised to maintain proper attendance as per university guidelines.",

    "placement": "Placement activities and company visit updates are shared by the placement cell.",

    "holiday": "Holiday lists and vacation schedules are updated through official university notices.",

    "id card": "Students can apply for or collect ID cards from their department office.",

    "migration": "Migration certificate details are available in the administration section.",

    "syllabus": "Course syllabus can be downloaded from the university academic section.",

    "timetable": "Class timetables are provided by departments before the semester starts.",

    "registration": "Semester registration details are updated regularly on the university portal.",

    "documents": "Students should keep photocopies of important academic documents and passport size photograph during admission and verification.",

    "certificate": "Degree and other certificates can be collected from the examination branch after approval.",

    "reappear": "Students who want to apply for reappear exams should fill the reappear form before the last date.",

    "practical": "Practical exam dates are usually announced by departments before examinations.",

    "internship": "Internship opportunities and training information are shared by departments and placement cells.",

    "canteen": "The university canteen provides food and refreshments during working hours.",

    "wifi": "WiFi facility may be available in selected university areas for students and staff.",

    "bus": "Bus route and transport information can be collected from the transport department.",
    

}

# -----------------------------
# Function to Generate Response
# -----------------------------
def generate_response(user_query):
    user_query = user_query.lower().strip()

    # Check every keyword properly
    for keyword, answer in responses.items():
        if keyword.lower() in user_query:
            return answer

    # Extra matching for common student words
    if "food" in user_query or "canteen" in user_query:
        return responses["canteen"]

    if "transport" in user_query or "bus" in user_query:
        return responses["bus"]

    if "wifi" in user_query or "internet" in user_query:
        return responses["wifi"]

    if "hostel" in user_query or "room" in user_query:
        return responses["hostel"]

    if "fees" in user_query or "fee" in user_query:
        return responses["fees"]

    return "Sorry, I could not understand your query properly. Please try asking in a different way."


# -----------------------------
# HTML Template
# -----------------------------
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>IGU AI Student Support System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            margin: 0;
            padding: 0;
        }

        .container {
            width: 60%;
            margin: 40px auto;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.2);
        }

        h1 {
            text-align: center;
            color: #333;
        }

        textarea {
            width: 100%;
            height: 100px;
            padding: 10px;
            font-size: 16px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }

        button {
            margin-top: 10px;
            padding: 10px 20px;
            font-size: 16px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }

        .response-box {
            margin-top: 20px;
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            border-left: 5px solid #007bff;
        }

        .footer {
            text-align: center;
            margin-top: 20px;
            color: gray;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>AI-Powered Student Support System</h1>

    <form method="POST">
        <label><b>Enter Your Query:</b></label><br><br>
        <textarea name="query" placeholder="Ask about admission, exams, results, sports, notices etc..."></textarea><br>
        <button type="submit">Submit Query</button>
    </form>

    {% if user_query %}
    <div class="response-box">
        <p><b>Your Query:</b> {{ user_query }}</p>
        <p><b>System Response:</b> {{ response }}</p>
        <p><b>Time:</b> {{ time }}</p>
    </div>
    {% endif %}

    <div class="footer">
        <p>Indira Gandhi University - AI Student Support System</p>
    </div>
</div>

</body>
</html>
"""


# -----------------------------
# Main Route
# -----------------------------
@app.route('/', methods=['GET', 'POST'])
def home():
    user_query = ""
    response = ""
    current_time = ""

    if request.method == 'POST':
        user_query = request.form['query']
        response = generate_response(user_query)
        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    return render_template_string(
        html_template,
        user_query=user_query,
        response=response,
        time=current_time
    )


# -----------------------------
# Run Application
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)
