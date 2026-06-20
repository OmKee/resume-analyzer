import PyPDF2

file = open("resume.pdf", "rb")
reader = PyPDF2.PdfReader(file)

resume_text = ""

for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        resume_text = resume_text + page_text

file.close()

resume_text = resume_text.lower()

job_file = open("job_description.txt", "r")
job_text = job_file.read()
job_file.close()

job_text = job_text.lower()

possible_skills = [
    "python",
    "machine learning",
    "pandas",
    "numpy",
    "sql",
    "git",
    "tensorflow",
    "docker"
]

required_skills = []

for skill in possible_skills:
    if skill in job_text:
        required_skills.append(skill)

found_skills = []
missing_skills = []

for skill in required_skills:
    if skill in resume_text:
        found_skills.append(skill)
    else:
        missing_skills.append(skill)

total = len(required_skills)

if total > 0:
    score = (len(found_skills) / total) * 100
else:
    score = 0

print("\nRESUME VS JOB MATCH\n")

print("Required Skills:")
for skill in required_skills:
    print("-", skill)

print("\nFound Skills:")
for skill in found_skills:
    print("-", skill)

print("\nMissing Skills:")
for skill in missing_skills:
    print("-", skill)

print("\nATS SCORE:", round(score, 2), "%")