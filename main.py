import PyPDF2

file = open("resume.pdf", "rb")
reader = PyPDF2.PdfReader(file)

resume_text = ""
for page in reader.pages:
    text = page.extract_text()
    if text:
        resume_text += text

file.close()
resume_text = resume_text.lower()

job_file = open("job_description.txt", "r")
job_text = job_file.read().lower()
job_file.close()

skills = ["python", "machine learning", "pandas", "numpy", "sql", "git", "docker"]

found = []
missing = []

for skill in skills:
    if skill in job_text:
        if skill in resume_text:
            found.append(skill)
        else:
            missing.append(skill)

total = len(found) + len(missing)
score = (len(found) / total) * 100 if total > 0 else 0

print("\nRESUME ANALYSIS\n")

print("Found Skills:")
for s in found:
    print("-", s)

print("\nMissing Skills:")
for s in missing:
    print("-", s)

print("\nATS Score:", round(score, 2), "%")