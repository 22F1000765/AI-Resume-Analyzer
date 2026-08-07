import re 
from app.data.skills import SKILL_ALIASES


def extract_skills(text: str) -> list[str]:
    """
    Extract normalized technical skills from resume text.
    """

    text = text.lower()

    extracted = set()

    for alias, canonical in SKILL_ALIASES.items():
        pattern = r"\b" + re.escape(alias) + r"\b"

        if re.search(pattern, text):       
            extracted.add(canonical)

    return sorted(extracted)

