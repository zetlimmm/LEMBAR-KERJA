from flask import Flask, render_template
 
app = Flask(__name__)
 

app_name = "Nama aplikasiku itu Bubub"

 #1 App Route di flask "hello word"
@app.route("/")
def hello_world():
     return "selamat pagi dunia tipu-tipu"


 #2 App Route di flask
@app.route("/aplikasi/")
def aplikasi():
     return "Selamat Datang di Brader Sodara"
 
 
 #3 App Route dengan HTML 
@app.route("/about/")
def about():
    return render_template('about.html')
 
#4 App Route dengan HTML with bostrapp
@app.route("/about-bostrapp/")
def about_bostrapp():
     return render_template('about-with-bostrapp.html')

#5 App Route Dinamis
@app.route("/nama/<string:nama_mahasiswa>/")
def getnama(nama_mahasiswa):
     return "namaku itu adalah {}".format(nama_mahasiswa)

#6 App Route ID
@app.route('/user/<int:user_id>')  # Hanya menerima angka
def user_id(user_id):
     return f"User ID: {user_id}"

#7 App Route Variabel Global
@app.route('/variabel-global/')
def variabel_global():
     return f"Welcome {app_name}"

#8 App Route Dictionary Variabel
@app.route('/data/')
def data():
     user = {"Name": "Nur Alim", "Age": 18, "City": "Makassar"}
     return render_template('data.html', user=user)

if __name__ == "__main__":
     app.run()