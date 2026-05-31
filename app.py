from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

responses = {
    "admission": "Admissions for new students usually start in July. Students can visit the admission section of the university website for detailed information. To take admission in university there are two methods online and offline.",

    "exam": "The examination schedule is updated by the university before exams begin.",

    "result": "Students can check their results through the university result portal using their roll number.",

    "sports": "Sports activities and events are updated by the sports department regularly.",

    "notice": "All university notices are available on the notice board section of the portal.",

    "scholarship": "Scholarship information can be collected from the scholarship section.",

    "library": "The university library is open during working hours for all registered students.",

    "hostel": "Hostel rooms are allotted according to university rules.",

    "fees": "Students can submit their fees online through the university portal.",

    "attendance": "Students are advised to maintain proper attendance.",

    "placement": "Placement activities and company visit updates are shared by the placement cell.",

    "holiday": "Holiday lists and vacation schedules are updated through official notices.",

    "id card": "Students can collect ID cards from their department office.",

    "syllabus": "Course syllabus can be downloaded from the academic section.",

    "timetable": "Class timetables are provided before semester starts.",

    "bus": "Bus route and transport information can be collected from the transport department."
}


def generate_response(user_query):
    user_query = user_query.lower().strip()

    for keyword, answer in responses.items():
        if keyword in user_query:
            return answer

    return "Sorry, I could not understand your query. Please try again."


html_template = """
<!DOCTYPE html>
<html>
<head>
<title>IGU AI Student Support System</title>

<style>

body{
font-family:Arial,sans-serif;
background:#f2f2f2;
margin:0;
padding:0;
}

.container{
width:65%;
margin:30px auto;
background:white;
padding:25px;
border-radius:15px;
box-shadow:0px 0px 15px rgba(0,0,0,0.2);
}

.logo{
text-align:center;
}

.logo img{
width:140px;
margin-bottom:10px;
}

h1{
text-align:center;
color:#ff5a1f;
}

textarea{
width:100%;
height:100px;
padding:10px;
font-size:16px;
border-radius:8px;
border:1px solid #ccc;
}

button{
padding:12px 25px;
font-size:16px;
background:#ff5a1f;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
margin-top:10px;
}

button:hover{
opacity:0.9;
}

.response-box{
margin-top:20px;
padding:15px;
background:#f8f9fa;
border-left:5px solid #ff5a1f;
border-radius:5px;
}

.footer{
text-align:center;
margin-top:20px;
color:gray;
}

</style>
</head>

<body>

<div class="container">

<div class="logo">
<img src="{{ url_for('static', filename='logo.png') }}">
</div>

<h1>AI Powered Student Support System</h1>

<form method="POST">

<label><b>Enter Your Query</b></label>
<br><br>

<textarea
name="query"
placeholder="Ask about admission, exams, fees, hostel, results..."></textarea>

<br>

<button type="submit">Submit Query</button>

</form>

{% if user_query %}

<div class="response-box">

<p><b>Your Query:</b> {{user_query}}</p>

<p><b>Response:</b> {{response}}</p>

<p><b>Time:</b> {{time}}</p>

</div>

{% endif %}

<div class="footer">
<p>Indira Gandhi University AI Support System</p>
</div>

</div>

</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def home():

    user_query=""
    response=""
    current_time=""

    if request.method=="POST":
        user_query=request.form["query"]
        response=generate_response(user_query)
        current_time=datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    return render_template_string(
        html_template,
        user_query=user_query,
        response=response,
        time=current_time
    )

if __name__=="__main__":
    app.run(debug=True)