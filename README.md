# SkillSight - Placement Skill Matcher & Readiness Analyser

SkillSight is an intelligent web platform designed to evaluate students' placement readiness, detect skill gaps, and provide actionable improvement roadmaps. Built with a modern **React** frontend and a robust **Django REST Framework** backend, it streamlines resume analysis and career preparation.

---

## 🌟 Key Features

- **Automated Resume Parsing**: Upload resumes (PDF) to automatically extract text and recognize key technical competencies.
- **Skill Gap Detection & Scoring**: Matches candidate skills against target industry roles (Frontend, Backend, Full Stack, Data Analyst, AI/ML) and computes a Readiness Score (0-100).
- **Personalized Recommendations**: Provides targeted step-by-step improvement roadmaps and customized study recommendations based on missing skills.
- **Skill Assessment & Tests**: Interactive MCQ assessments to validate technical proficiency.
- **Authentication & User Profiles**: Secure account registration, login, and user profile management powered by Django Token Authentication.
- **Responsive Modern UI**: Interactive dashboard featuring light/dark mode support and intuitive workflows.

---

## 🛠️ Tech Stack

### Frontend
- **React.js** (v19)
- **React Router DOM** (v7)
- **Axios**
- **Framer Motion**

### Backend
- **Python** & **Django** (v6+)
- **Django REST Framework (DRF)**
- **Token Authentication** (`rest_framework.authtoken`)
- **PyPDF2** (PDF text extraction)
- **django-cors-headers**
- **SQLite3**

---

## 🚀 Getting Started

### Prerequisites
- [Node.js](https://nodejs.org/) (v16 or higher)
- [Python](https://www.python.org/) (v3.10 or higher)
- `git`

---

### 1. Clone the Repository
```bash
git clone https://github.com/shashihere/SkillSight-Placement-Skill-Matcher-Readiness-Analyser.git
cd SkillSight-Placement-Skill-Matcher-Readiness-Analyser
```

---

### 2. Backend Setup (Django)

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   - **Windows:**
     ```powershell
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **macOS / Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the Django development server:
   ```bash
   python manage.py runserver 5000
   ```
   *The backend API will run at `http://127.0.0.1:5000`.*

---

### 3. Frontend Setup (React)

1. Open a new terminal and navigate to the `client` directory:
   ```bash
   cd client
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```
   *The frontend application will be accessible at `http://localhost:3000`.*

---

## 📡 API Endpoints Overview

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Health check / Server root |
| `POST` | `/analyze` | Extracts text from Base64-encoded PDF |
| `POST` | `/api/upload` | Multipart resume upload & skill gap analysis |
| `POST` | `/api/suggestions` | Generates rule-based improvement plan |
| `POST` | `/api/auth/register` | User signup & token generation |
| `POST` | `/api/auth/login` | User login & token authentication |

---

## 👤 Author

- **Shashi Prabha** - [GitHub Profile](https://github.com/shashihere)
- Repository: [SkillSight-Placement-Skill-Matcher-Readiness-Analyser](https://github.com/shashihere/SkillSight-Placement-Skill-Matcher-Readiness-Analyser)
