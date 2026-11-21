
# Wallps — Wallpaper Platform

<p align="center">
  <a href="https://wallps.eskiba.de">
    <img src="https://img.shields.io/badge/Live%20Website-wallps.eskiba.de-2ea44f?style=for-the-badge" alt="Live Website">
  </a>
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
</p>

**Wallps** is a web application for browsing and discovering high-quality wallpapers for desktop computers, tablets, and mobile devices.

The project demonstrates practical experience in Python web development, database management, Linux server administration, Docker containerization, and production deployment.

🌐 **Live website:** [https://wallps.eskiba.de](https://wallps.eskiba.de)

---

## ✨ Features

- 🖼️ Browse a large collection of wallpapers.
- 🗂️ Explore wallpapers by categories and tags.
- 🔎 Search for wallpapers.
- 📱 Responsive interface for different devices.
- 📐 View image details, including resolution and file size.
- 📄 Navigate through the collection using pagination.

## 🛠️ Technology Stack

| Technology | Purpose |
|:---|:---|
| **Python 3.10** | Main programming language |
| **Django 4.2** | Web application framework |
| **SQLite** | Database |
| **HTML / CSS** | Frontend |
| **Docker** | Application containerization |
| **Gunicorn** | WSGI application server |
| **Nginx** | Reverse proxy and web server |
| **Debian 13** | VPS operating system |
| **Let's Encrypt / Certbot** | HTTPS certificates |
| **Git / GitHub** | Version control and source code management |
| **systemd** | Background task scheduling and service management |

## 🚀 Deployment & Infrastructure

The application is deployed on a **Linux VPS** and runs inside a Docker container.

The production environment includes:

- 🖥️ Debian 13 VPS.
- 🐳 Docker-based application deployment.
- ⚙️ Gunicorn serving the Django application.
- 🌐 Nginx configured as a reverse proxy.
- 🔒 HTTPS with Let's Encrypt SSL certificates.
- 💾 Persistent storage for the SQLite database and uploaded media.
- 📦 Automated database migrations and static file collection during container startup.
- ⏰ systemd service and timer for scheduled background tasks.

**Production URL:** [https://wallps.eskiba.de](https://wallps.eskiba.de)

## 🔄 Development & Deployment Workflow

The project follows a Git-based deployment workflow:

1. Development and testing in a local environment.
2. Version control using Git.
3. Source code management through GitHub.
4. Deployment to the VPS by pulling updates from the repository.
5. Docker image rebuild and container recreation when application code changes.

## 👨‍💻 About This Project

Wallps is an independently developed project created to improve and demonstrate my practical skills in:

- Python and Django web development.
- Database design and management.
- Linux server administration.
- Docker and application containerization.
- Web server configuration and HTTPS deployment.
- Git-based development and deployment workflows.

I handle the development, server configuration, deployment, and maintenance of the application.

The project is continuously maintained and serves as part of my technical portfolio.

---

<p align="center">
  <b>Developed by Eugen Skiba</b>
  <br>
  <a href="https://wallps.eskiba.de">Live Project</a> •
  <a href="https://github.com/Slimperist/wallps">GitHub Repository</a>
</p>
