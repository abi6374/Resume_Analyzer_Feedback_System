# Smart Resume AI

An intelligent resume analysis and building platform that helps job seekers create professional resumes and improve their chances of landing their dream jobs.

## Features

### Resume Analysis
- AI-powered content analysis
- ATS compatibility checking
- Detailed feedback and suggestions
- Score-based evaluation
- Keyword optimization
- Format validation

### Resume Building
- Professional templates
- Real-time editing
- Export to PDF/DOCX
- Customizable sections
- Industry-specific guidance
- Best practices suggestions

## Technology Stack

- **Frontend**: Streamlit for interactive web interface
- **AI Models**: Google Gemini and OpenRouter integration
- **PDF Processing**: Advanced OCR and text extraction
- **Database**: SQLite for data persistence
- **Document Processing**: Support for PDF and DOCX formats

## Installation

1. Clone the repository:
```bash
git clone https://github.com/abi6374/Resume_Analyzer_Feedback_System.git
cd Smart-AI-Resume-Analyzer
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the project root and add your API keys:
```
GOOGLE_API_KEY=your_google_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
DATABASE_URL=sqlite:///resume_data.db
```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to:
```
http://localhost:8501
```

3. Use the application:
   - Upload your resume (PDF or DOCX)
   - Get AI-powered analysis
   - Build a new resume
   - View analytics and insights

## Project Structure

```
smart-resume-ai/
├── app.py                 # Main application file
├── requirements.txt       # Project dependencies
├── README.md             # Project documentation
├── .env                  # Environment variables
├── .gitignore           # Git ignore file
├── utils/               # Utility modules
│   ├── ai_resume_analyzer.py
│   ├── database.py
│   ├── resume_builder.py
│   ├── resume_analyzer.py
│   └── resume_parser.py
└── style/               # CSS and styling files
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

G S ABINIVAS (abinivas8)
- Email: abinivas6374@gmail.com
- GitHub: [@abi6374](https://github.com/abi6374)
- LinkedIn: [G S ABINIVAS](https://linkedin.com/in/abinivas8)

## Acknowledgments

- Google Gemini AI for providing the AI analysis capabilities
- Streamlit for the web framework
- All contributors and users of the project

## Version History

- 1.0.0 (April 2025)
  - Initial release
  - Basic resume analysis and building features
  - AI-powered feedback system
  - PDF report generation
