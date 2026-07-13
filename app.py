from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Data portofolio dinamis
    portfolio_data = {
        "name": "Igfirlii Nuur Aziiza",
        "role": "Fullstack Web Developer & AI Enthusiast",
        "about": "Mahasiswa Teknik Informatika yang berdedikasi dalam membangun solusi perangkat lunak yang efisien. Memiliki pengalaman dalam pengembangan web fullstack serta integrasi teknologi kecerdasan buatan, khususnya pada pemrosesan citra (Computer Vision) untuk industri.",
        "skills": {
            "Backend & Database": ["PHP", "MySQL", "PostgreSQL", "REST API", "Python (Flask)"],
            "Frontend": ["HTML5", "CSS3", "Tailwind CSS", "JavaScript"],
            "Tools & Others": ["Git/GitHub", "VS Code", "Postman", "Figma", "OpenCV"]
        },
        "projects": [
            {
                "title": "Sistem Penilaian Kelayakan Udang Vaname AI",
                "tech": "Python, Flask, OpenCV, KNN, PostgreSQL",
                "desc": "Sistem berbasis website untuk mendeteksi blackspot dan kualitas warna udang secara instan menggunakan teknologi Computer Vision."
            },
            {
                "title": "People Detection Monitoring",
                "tech": "Python, Machine Vision",
                "desc": "Sistem pemantauan keamanan karyawan untuk area zona khusus di PT. Kutai Timber Indonesia."
            },
            {
                "title": "Nutrisense",
                "tech": "Python, NLP, Flask, PostgreSQL",
                "desc": "Sistem berbasis website untuk mendeteksi kandungan gizi dari makanan yang diunggah oleh pengguna menggunakan teknologi Natural Language Processing, Studi kasus Artificial Intelligence center indonesia."
            },
            {
                "title": "Fortigate-Automation",
                "tech": "Python, Flask, REST API",
                "desc": "Sistem otomasi untuk pengelolaan konfigurasi firewall Fortigate studi kasus PT. Kutai Timber Indonesia."
            }
            
        ]
    }
    return render_template('index.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True)