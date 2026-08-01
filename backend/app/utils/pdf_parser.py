import fitz


def extract_text_from_pdf(file_path: str) -> str:
    document = fitz.open(file_path)

    extracted_text = ""

    for page in document:
        extracted_text += page.get_text()

    document.close()
    
    return extracted_text.strip()

def detect_sections(text: str):
    """
    Parse extracted resume text into structured sections.
    Returns a dictionary where each key is a resume section
    and the value is a list of lines belonging to that section.
    """

    # Step 1: Split the resume into individual lines
    lines = text.splitlines()

    # Step 2: No section detected initially
    current_section = None

    # Step 3: Initialize all supported sections
    sections = {
        "Summary": [],
        "Education": [],
        "Experience": [],
        "Projects": [],
        "Skills": [],
        "Certifications": [],
        "Unknown": []
    }

    # Step 4: Define alternative headings for each section
    section_keywords = {
        "Summary": [
            "summary",
            "professional summary",
            "profile",
            "objective"
        ],
        "Education": [
            "education",
            "academics",
            "academic qualifications"
        ],
        "Experience": [
            "experience",
            "work experience",
            "professional experience",
            "employment",
            "internship"
        ],
        "Projects": [
            "projects",
            "personal projects",
            "academic projects"
        ],
        "Skills": [
            "skills",
            "technical skills",
            "core skills",
            "technologies"
        ],
        "Certifications": [
            "certifications",
            "certificates",
            "courses"
        ]
    }

    # Step 5: Process every line
    for line in lines:

        # Remove leading/trailing spaces
        clean_line = line.strip()

        # Ignore blank lines
        if not clean_line:
            continue

        found_section = False

        # Check if the current line is a section heading
        for section, keywords in section_keywords.items():

            for keyword in keywords:

                if clean_line.lower() == keyword.lower():

                    current_section = section
                    found_section = True
                    break

            if found_section:
                break

        # Skip adding the heading itself
        if found_section:
            continue

        # Add content to the detected section
        if current_section:
            sections[current_section].append(clean_line)
        else:
            # Content before the first heading
            sections["Unknown"].append(clean_line)

    # Remove empty sections before returning
    return {
        section: content
        for section, content in sections.items()
        if content
    }