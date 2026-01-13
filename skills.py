TECHNICAL_SKILLS = [
    "python", "java", "c++", "machine learning", "deep learning",
    "data science", "sql", "nlp", "tensorflow", "pytorch",
    "html", "css", "javascript", "streamlit", "flask",
    "opencv", "git", "github", "linux"
]

SOFT_SKILLS = [
    "communication", "teamwork", "problem solving",
    "leadership", "adaptability", "critical thinking"
]

def extract_skills(text):
    tech = set()
    soft = set()

    for skill in TECHNICAL_SKILLS:
        if skill in text:
            tech.add(skill)

    for skill in SOFT_SKILLS:
        if skill in text:
            soft.add(skill)

    return list(tech), list(soft)
