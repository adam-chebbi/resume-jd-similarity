def extract_keywords(text):
    """Extract keywords from text using simple heuristics."""
    words = text.split()
    return set(words)

def match_keywords(cv_keywords, jd_keywords):
    """Match and highlight keywords between CV and JD."""
    matched = cv_keywords & jd_keywords
    missing = jd_keywords - cv_keywords
    return matched, missing
