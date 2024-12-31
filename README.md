# Smart ATS (Applicant Tracking System)

Smart ATS is a web-based tool designed to evaluate resumes against job descriptions using generative AI. It provides structured feedback to help job seekers improve their resumes and enhance their chances of getting shortlisted in competitive job markets.

---

## Features
- **Resume Evaluation:** Analyze resumes and compare them with job descriptions.
- **Generative AI Integration:** Leverages Google's Gemini AI for accurate and intelligent feedback.
- **PDF Parsing:** Extracts text from uploaded PDF resumes.
- **Feedback Structure:** Outputs a JSON-formatted evaluation, including:
  - **Job Description Match (%):** The match percentage between the resume and job description.
  - **Missing Keywords:** Keywords absent from the resume but relevant to the job description.
  - **Profile Summary:** A concise summary of the resume.
- **Interactive Interface:** Built using Streamlit for a user-friendly experience.

---

## Tech Stack
- **Python**
  - Streamlit
  - PyPDF2
  - dotenv
  - google-generativeai
- **Google Generative AI (Gemini)**

---

## Prerequisites
1. Python 3.7 or higher installed on your system.
2. A valid Google Generative AI API key.

---

## Installation

1. Clone the Repository:
   ```bash
   git clone https://github.com/your-username/atsllm.git
   cd atsllm
   ```

2. Create a Virtual Environment (Optional but Recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set Up Environment Variables:
   - Create a `.env` file in the root directory.
   - Add your Google Generative AI API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

---

## Usage

1. Run the Application:
   ```bash
   streamlit run app.py
   ```

2. Open the Application in a Browser:
   - The app will launch automatically. If not, navigate to the URL displayed in the terminal (e.g., `http://localhost:8501`).

3. Interact with the Application:
   - Paste the job description into the text area.
   - Upload your resume as a PDF file.
   - Click the "Submit" button to evaluate your resume.

---

## Project Structure
```
smart-ats/
├── app.py                # Main application file
├── requirements.txt      # Dependencies
├── .env                  # Environment variables (not included in GitHub)
├── .gitignore            # Git ignore file
├── README.md             # Project documentation
```

---

## Example Output
The application generates a response in the following structure:
```json
{
  "JD Match": "85%",
  "MissingKeywords": ["Python", "Machine Learning"],
  "Profile Summary": "Experienced software engineer with expertise in AI and data analysis."
}
```

---

## Contributing
Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Create a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements
- [Streamlit](https://streamlit.io/) for the interactive UI.
- [Google Generative AI](https://cloud.google.com/genai) for the powerful AI capabilities.
- [PyPDF2](https://pypi.org/project/PyPDF2/) for PDF parsing.

