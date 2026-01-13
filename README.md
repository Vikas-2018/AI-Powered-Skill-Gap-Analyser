🧠 AI-Powered Skill Gap Analyzer

An end-to-end NLP-based application that analyzes skill gaps between resumes and job descriptions. The system extracts skills, performs semantic similarity matching using Sentence-BERT, calculates match percentage, identifies missing skills, and presents results through an interactive Streamlit dashboard with downloadable reports.

🚀 Features

Upload resumes and job descriptions (PDF, DOCX, TXT)

Extract technical and soft skills using custom NLP logic

Perform semantic skill matching using Sentence-BERT embeddings

Identify missing or mismatched skills

Calculate skill match percentage

Download CSV skill gap report

Interactive and user-friendly Streamlit dashboard

🛠️ Tech Stack

Programming Language: Python

NLP & ML: Sentence-BERT, Scikit-learn

Frontend / UI: Streamlit

Data Handling: Pandas

File Parsing: pdfplumber, docx2txt

📂 Project Structure
AI_Skill_Gap_Analyzer/

app.py              # Streamlit application
text_utils.py       # Resume & JD text extraction
skills.py           # Skill extraction and categorization
matcher.py          # Skill similarity & match percentage logic
requirements.txt    # Project dependencies

⚙️ Installation & Setup

1️⃣ Clone the Repository
git clone https://github.com/your-username/AI_Skill_Gap_Analyzer.git
cd AI_Skill_Gap_Analyzer

2️⃣ Install Dependencies
python -m pip install -r requirements.txt

3️⃣ Run the Application
python -m streamlit run app.py


The app will open automatically in your browser at:
👉 http://localhost:8501

📊 How It Works

Upload a resume and a job description

Text is extracted and preprocessed

Skills are categorized into technical and soft skills

Sentence-BERT embeddings are generated

Skills are compared using cosine similarity

Missing skills and match percentage are displayed

A CSV report can be downloaded

🎯 Use Cases

Job seekers identifying missing skills for a role

Recruiters screening resumes efficiently

Students analyzing job-readiness

HR tech and ATS-based applications

📈 Future Enhancements

LLM-based skill recommendations

PDF report generation

FastAPI backend integration

Cloud deployment (AWS / Azure)

Resume ranking for multiple candidates

👨‍💻 Author

Devi Sri Vikas Doddipatla
B.Tech – CSE (AI & ML)
📍 Andhra Pradesh, India

⭐ If you like this project

Give it a ⭐ on GitHub and feel free to fork or contribute!
