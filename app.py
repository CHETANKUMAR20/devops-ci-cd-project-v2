from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>DevOps CI/CD Project V2</title>
        <style>
            body {
                background-color: #0f172a;
                color: #f8fafc;
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 100px;
            }
            h1 {
                font-size: 40px;
                color: #38bdf8;
            }
            h2 {
                color: #94a3b8;
            }
            .box {
                background: #1e293b;
                padding: 30px;
                border-radius: 10px;
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🚀 Welcome to My CI/CD Project</h1>
            <h2>Project Title: DevOps CI/CD Project V2</h2>
            <p>Automated Deployment using:</p>
            <p>✔ GitHub Actions</p>
            <p>✔ Amazon ECR</p>
            <p>✔ AWS Systems Manager (SSM)</p>
            <p>✔ Immutable Image Tagging (Commit SHA)</p>
            <br>
            <p><strong>Status:</strong> Production-Style Deployment Active 🔥</p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
