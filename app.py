from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Remote',
  'salary': '$2700'
},
  {
  'id': 2,
  'title': 'Data Engineer',
  'location': 'Remote',
  'salary': '$6100'
},
  {
  'id': 3,
  'title': 'Data Scientist',
  'location': 'California, US',
},
  {
  'id': 4,
  'title': 'Data Security Engineer',
  'location': 'London, UK',
  'salary': '$4200'
}
]

@app.route("/")
def homepage():
  return render_template('home.html', jobs=JOBS, company_name='Glowing Umbrella')

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
