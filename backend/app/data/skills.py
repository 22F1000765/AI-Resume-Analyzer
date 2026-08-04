"""
Centralized technical skills dataset.

This module contains categorized technical skills that are used
throughout the application for resume analysis.
"""

TECHNICAL_SKILLS = {
    "programming_languages": [
        "Python",
        "Java",
        "C",
        "C++",
        "JavaScript",
        "TypeScript",
        "SQL",
        "Go",
        "Rust",
        "PHP",
    ],

    "frontend": [
        "HTML",
        "CSS",
        "React",
        "Vue.js",
        "Angular",
        "Tailwind CSS",
        "Bootstrap",
    ],

    "backend": [
        "FastAPI",
        "Flask",
        "Django",
        "Node.js",
        "Express.js",
        "Spring Boot",
    ],

    "databases": [
        "PostgreSQL",
        "MySQL",
        "SQLite",
        "MongoDB",
        "Redis",
    ],

    "cloud_devops": [
        "Docker",
        "Kubernetes",
        "AWS",
        "Azure",
        "GCP",
        "GitHub Actions",
    ],

    "ai_ml": [
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch",
        "Scikit-learn",
        "Pandas",
        "NumPy",
    ],

    "tools": [
        "Git",
        "GitHub",
        "Postman",
        "Swagger",
        "VS Code",
    ],
}
SKILL_ALIASES = {
    # Programming Languages
    "python": "Python",
    "java": "Java",
    "javascript": "JavaScript",
    "js": "JavaScript",
    "typescript": "TypeScript",
    "ts": "TypeScript",
    "c++": "C++",
    "c": "C",
    "sql": "SQL",

    # Frontend
    "react": "React",
    "vue": "Vue.js",
    "vuejs": "Vue.js",
    "vue.js": "Vue.js",
    "tailwind": "Tailwind CSS",

    # Backend
    "fastapi": "FastAPI",
    "flask": "Flask",
    "django": "Django",
    "node": "Node.js",
    "nodejs": "Node.js",
    "node.js": "Node.js",
    "express": "Express.js",
    "expressjs": "Express.js",

    # Databases
    "postgres": "PostgreSQL",
    "postgresql": "PostgreSQL",
    "mysql": "MySQL",
    "sqlite": "SQLite",
    "mongodb": "MongoDB",

    # Cloud & DevOps
    "docker": "Docker",
    "kubernetes": "Kubernetes",
    "aws": "AWS",
    "azure": "Azure",
    "gcp": "GCP",

    # AI / ML
    "machine learning": "Machine Learning",
    "deep learning": "Deep Learning",
    "tensorflow": "TensorFlow",
    "pytorch": "PyTorch",
    "sklearn": "Scikit-learn",
    "scikit learn": "Scikit-learn",
    "numpy": "NumPy",
    "pandas": "Pandas",

    # Tools
    "git": "Git",
    "github": "GitHub",
    "git hub": "GitHub",
    "postman": "Postman",
    "swagger": "Swagger",
    "vscode": "VS Code",
    "vs code": "VS Code",
}