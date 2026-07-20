from flask import Flask, render_template, abort

app = Flask(__name__)


def get_portfolio_data():
    return {
        "name": "Igfirlii Nuur Aziiza",
        "role": "Fullstack Web Developer & AI Enthusiast",
        "about": "Lulusan Teknik Informatika yang berdedikasi dalam membangun solusi perangkat lunak yang efisien. Memiliki pengalaman dalam pengembangan web fullstack serta berfokus pada bahasa pemrograman python.",
        "skills": {
            "Backend & Database": ["PHP", "MySQL", "PostgreSQL", "REST API", "Python (Flask)"],
            "Frontend": ["HTML5", "CSS3", "Tailwind CSS", "JavaScript"],
            "Tools & Others": ["Git/GitHub", "VS Code", "Postman", "Figma", "OpenCV"]
        },
        "projects": [
            {
                "title": "Sistem Penilaian Kelayakan Udang Vaname AI",
                "tech": "Python, Flask, OpenCV, KNN, PostgreSQL",
                "desc": "Sistem berbasis website untuk mendeteksi blackspot dan kualitas warna udang secara instan menggunakan teknologi Computer Vision.",
                "url": "https://igfirli-deteksi-udang-yolo.hf.space",
                "pipeline": [
                    {"step": "01", "label": "Input Gambar Udang", "sub": "upload via web"},
                    {"step": "02", "label": "Resize 640x640", "sub": "preprocessing"},
                    {"step": "03", "label": "YOLO Detection", "sub": "deteksi + remove background"},
                    {"step": "04", "label": "OpenCV Color Extraction", "sub": "HSV, CIELab, RGB"},
                    {"step": "05", "label": "SNI Scoring", "sub": "skor standar SNI"},
                ],
                "decision": {
                    "label": "WKNN Classifier",
                    "formula": "d(xi,xj)=sqrt(sum(w(xik-xjk)^2))"
                },
                "branches": [
                    {"cond": "Grade >= 7", "result": "Lolos", "type": "yes"},
                    {"cond": "Grade < 7", "result": "Reject", "type": "no"},
                ],
            },
            {
                "title": "People Detection Monitoring",
                "tech": "Python, Machine Vision",
                "desc": "Sistem pemantauan keamanan karyawan untuk area zona khusus di PT. Kutai Timber Indonesia.",
                "url": "#",
                "github": "https://github.com/igfirli06/people_detection", 
            },
            {
                "title": "Nutrisense",
                "tech": "Python, NLP, Flask, PostgreSQL, Rest API",
                "desc": "Sistem berbasis website untuk mendeteksi kandungan gizi dari makanan yang diunggah oleh pengguna menggunakan teknologi Natural Language Processing, Studi kasus Artificial Intelligence center indonesia.",
                "url": "https://igfirli-nutrisense.hf.space",
            },
            {
                "title": "Fortigate-Automation",
                "tech": "Python, Flask, REST API",
                "desc": "Sistem otomasi untuk pengelolaan konfigurasi firewall Fortigate studi kasus PT. Kutai Timber Indonesia.",
                "url": "#",
                "github": "#",  # TODO: isi link repo GitHub-nya
            }
        ]
    }


@app.route('/')
def home():
    return render_template('index.html', data=get_portfolio_data())


@app.route('/project/<int:pid>')
def project_detail(pid):
    portfolio_data = get_portfolio_data()
    projects = portfolio_data["projects"]
    if pid < 0 or pid >= len(projects):
        abort(404)

    project = dict(projects[pid])
    project["index"] = pid + 1  # untuk label "Project_1", "Project_2", dst

    return render_template('architecture.html', data=portfolio_data, project=project)


if __name__ == '__main__':
    app.run(debug=True)