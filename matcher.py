from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def find_skill_gap(resume_skills, jd_skills):
    if not resume_skills or not jd_skills:
        return []

    resume_emb = model.encode(resume_skills)
    jd_emb = model.encode(jd_skills)

    sim = cosine_similarity(jd_emb, resume_emb)

    missing = []
    for i, row in enumerate(sim):
        if max(row) < 0.6:
            missing.append(jd_skills[i])

    return missing


def calculate_match_percentage(resume_skills, jd_skills, missing_skills):
    if not jd_skills:
        return 0
    matched = len(jd_skills) - len(missing_skills)
    return round((matched / len(jd_skills)) * 100, 2)
