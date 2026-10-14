from datetime import datetime, timezone
import os
import socket

from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template(
        "index.html",
        app_env=os.getenv("APP_ENV", "development"),
        hostname=socket.gethostname(),
    )


@app.get("/health")
def health():
    return jsonify(
        status="ok",
        environment=os.getenv("APP_ENV", "development"),
        timestamp=datetime.now(timezone.utc).isoformat(),
    )


@app.get("/api/info")
def info():
    return jsonify(
        project="Lab Loan Tracker",
        course="Cloud Computing",
        code="PTI 2802",
        meeting=3,
        milestone="M03",
        deployment="VPS Ubuntu Server 24.04",
    )


@app.get("/api/devices")
def devices():
    return jsonify(devices=[
        {"id": 1, "name": "Proyektor Epson EB-X06", "status": "tersedia"},
        {"id": 2, "name": "Laptop Lab 01", "status": "dipinjam"},
        {"id": 3, "name": "Router MikroTik hAP", "status": "tersedia"},
    ])
