import spacy

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    return " ".join([token.lemma_.lower() for token in nlp(text) if token.is_alpha and not token.is_stop])

def score_resume(resume_text, job_description):
    resume_keywords = set(clean_text(resume_text).split())
    jd_keywords = set(clean_text(job_description).split())

    matched_keywords = resume_keywords & jd_keywords
    score = round(len(matched_keywords) / len(jd_keywords) * 100, 2) if jd_keywords else 0

    return score, list(matched_keywords)
