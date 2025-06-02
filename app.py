"""
Smart Resume AI - Main Application
"""
import streamlit as st

# Set page config at the very beginning
st.set_page_config(
    page_title="Smart Resume AI",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

import os
from datetime import datetime
from utils.resume_analyzer import ResumeAnalyzer
from utils.ai_resume_analyzer import AIResumeAnalyzer
from utils.resume_builder import ResumeBuilder
import pandas as pd

# Load environment variables from Streamlit secrets
try:
    # Get API keys from Streamlit secrets
    google_api_key = st.secrets["api_keys"]["GOOGLE_API_KEY"]
    openrouter_api_key = st.secrets["api_keys"]["OPENROUTER_API_KEY"]
    database_url = st.secrets["database"]["DATABASE_URL"]
    
    # Set environment variables
    os.environ["GOOGLE_API_KEY"] = google_api_key
    os.environ["OPENROUTER_API_KEY"] = openrouter_api_key
    os.environ["DATABASE_URL"] = database_url
    
except Exception as e:
    st.error(f"Error loading secrets: {str(e)}")
    st.info("Please make sure you have set up your secrets.toml file with the required API keys.")
    # Set default values if secrets loading fails
    os.environ["GOOGLE_API_KEY"] = "your_google_api_key_here"
    os.environ["OPENROUTER_API_KEY"] = "your_openrouter_api_key_here"
    os.environ["DATABASE_URL"] = "sqlite:///resume_data.db"

class ResumeApp:
    def __init__(self):
        """Initialize the Resume App"""
        self.resume_analyzer = ResumeAnalyzer()
        
        # Initialize AI analyzer with error handling
        try:
            self.ai_analyzer = AIResumeAnalyzer()
            if not self.ai_analyzer:
                st.error("Failed to initialize AI analyzer. Please check your API keys.")
                self.ai_analyzer = None
        except Exception as e:
            st.error(f"Error initializing AI analyzer: {str(e)}")
            st.info("Please make sure you have set up your secrets.toml file with the required API keys.")
            self.ai_analyzer = None
        
        self.resume_builder = ResumeBuilder()
        
        # Initialize session state
        if 'current_page' not in st.session_state:
            st.session_state.current_page = 'Home'
        if 'form_data' not in st.session_state:
            st.session_state.form_data = {}
        if 'is_admin' not in st.session_state:
            st.session_state.is_admin = False
        if 'resume_data' not in st.session_state:
            st.session_state.resume_data = None
        if 'ai_analysis_stats' not in st.session_state:
            st.session_state.ai_analysis_stats = None

    def main(self):
        """Main application entry point"""
        # Sidebar navigation
        with st.sidebar:
            st.title("Smart Resume AI")
            
            # Navigation buttons
            pages = {
                'Home': '🏠',
                'Resume Analyzer': '📊',
                'Resume Builder': '📝',
                'Dashboard': '📈',
                'About': 'ℹ️'
            }
            
            for page, icon in pages.items():
                if st.button(f"{icon} {page}", use_container_width=True):
                    st.session_state.current_page = page

        # Main content area
        if st.session_state.current_page == 'Home':
            self.show_home()
        elif st.session_state.current_page == 'Resume Analyzer':
            self.show_analyzer()
        elif st.session_state.current_page == 'Resume Builder':
            self.show_builder()
        elif st.session_state.current_page == 'Dashboard':
            self.show_dashboard()
        elif st.session_state.current_page == 'About':
            self.show_about()

    def show_home(self):
        """Display home page"""
        st.title("Welcome to Smart Resume AI")
        st.write("""
        Smart Resume AI is your intelligent resume analysis and building assistant. 
        Our platform helps you create professional resumes and provides detailed analysis 
        to improve your chances of landing your dream job.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Resume Analysis")
            st.write("""
            - Get detailed feedback on your resume
            - Check ATS compatibility
            - Receive improvement suggestions
            - Analyze keyword matches
            """)
            if st.button("Start Analysis", use_container_width=True):
                st.session_state.current_page = 'Resume Analyzer'
        
        with col2:
            st.subheader("Resume Builder")
            st.write("""
            - Create professional resumes
            - Choose from multiple templates
            - Easy-to-use interface
            - Export to PDF
            """)
            if st.button("Build Resume", use_container_width=True):
                st.session_state.current_page = 'Resume Builder'

    def show_analyzer(self):
        """Display resume analyzer page"""
        st.header("Resume Analyzer")
        
        if self.ai_analyzer is None:
            st.error("AI Analyzer is not available. Please check your API key configuration.")
            st.info("Make sure you have set up your secrets.toml file with the required API keys.")
            return
            
        uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=['pdf', 'docx'])
        
        if uploaded_file is not None:
            # Save the uploaded file temporarily
            temp_path = os.path.join("temp", uploaded_file.name)
            os.makedirs("temp", exist_ok=True)
            
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getvalue())
            
            # Get job role
            job_role = st.text_input("Enter the job role you're applying for", "Software Developer")
            
            # Get model choice
            model = st.selectbox(
                "Select AI Model",
                ["Google Gemini", "OpenRouter"],
                index=0
            )
            
            # Initialize session state for analysis results if not exists
            if 'analysis_result' not in st.session_state:
                st.session_state.analysis_result = None
            if 'candidate_name' not in st.session_state:
                st.session_state.candidate_name = None
            
            if st.button("Get AI Analysis"):
                with st.spinner("Analyzing your resume..."):
                    try:
                        # Initialize analyzer
                        analyzer = AIResumeAnalyzer()
                        
                        # Extract text from resume
                        if uploaded_file.name.endswith('.pdf'):
                            resume_text = analyzer.extract_text_from_pdf(uploaded_file)
                        else:
                            resume_text = analyzer.extract_text_from_docx(uploaded_file)
                        
                        if not resume_text:
                            st.error("Could not extract text from the resume. Please ensure the file is not corrupted.")
                            return
                        
                        # Analyze resume
                        analysis_result = analyzer.analyze_resume(
                            resume_text=resume_text,
                            job_role=job_role,
                            model=model
                        )
                        
                        if analysis_result and not analysis_result.get('error'):
                            # Store results in session state
                            st.session_state.analysis_result = analysis_result
                            st.session_state.candidate_name = os.path.splitext(uploaded_file.name)[0]
                            st.session_state.ai_analysis_stats = analysis_result
                            
                            # Display results
                            st.subheader("AI Analysis Results")
                            
                            # Display scores
                            col1, col2 = st.columns(2)
                            with col1:
                                st.metric("Resume Score", f"{analysis_result.get('score', 0)}%")
                            with col2:
                                st.metric("ATS Score", f"{analysis_result.get('ats_score', 0)}%")
                            
                            # Display strengths and weaknesses
                            st.subheader("Key Strengths")
                            for strength in analysis_result.get('strengths', []):
                                st.write(f"✅ {strength}")
                            
                            st.subheader("Areas for Improvement")
                            for weakness in analysis_result.get('weaknesses', []):
                                st.write(f"⚠️ {weakness}")
                            
                            # Display detailed analysis
                            st.subheader("Detailed Analysis")
                            st.write(analysis_result.get('full_response', ''))
                            
                            # Add PDF report generation
                            st.subheader("Download Analysis Report")
                            if st.button("Generate PDF Report"):
                                with st.spinner("Generating PDF report..."):
                                    try:
                                        # Generate PDF report
                                        pdf_bytes = analyzer.generate_pdf_report(
                                            analysis_result=st.session_state.analysis_result,
                                            candidate_name=st.session_state.candidate_name,
                                            job_role=job_role
                                        )
                                        
                                        if pdf_bytes:
                                            # Create download button
                                            st.download_button(
                                                label="Download PDF Report",
                                                data=pdf_bytes.getvalue(),
                                                file_name=f"{st.session_state.candidate_name}_Analysis_Report.pdf",
                                                mime="application/pdf"
                                            )
                                            st.success("PDF report generated successfully!")
                                        else:
                                            st.error("Failed to generate PDF report. Please try again.")
                                    except Exception as e:
                                        st.error(f"Error generating PDF report: {str(e)}")
                                        import traceback
                                        st.code(traceback.format_exc())
                        else:
                            error_msg = analysis_result.get('error', 'Unknown error occurred')
                            st.error(f"Error analyzing resume: {error_msg}")
                            
                    except Exception as e:
                        st.error(f"Error analyzing resume: {str(e)}")
                    finally:
                        # Clean up temporary file
                        if os.path.exists(temp_path):
                            os.remove(temp_path)
            
            # Display results if they exist in session state
            elif st.session_state.analysis_result:
                st.subheader("AI Analysis Results")
                
                # Display scores
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Resume Score", f"{st.session_state.analysis_result.get('score', 0)}%")
                with col2:
                    st.metric("ATS Score", f"{st.session_state.analysis_result.get('ats_score', 0)}%")
                
                # Display strengths and weaknesses
                st.subheader("Key Strengths")
                for strength in st.session_state.analysis_result.get('strengths', []):
                    st.write(f"✅ {strength}")
                
                st.subheader("Areas for Improvement")
                for weakness in st.session_state.analysis_result.get('weaknesses', []):
                    st.write(f"⚠️ {weakness}")
                
                # Display detailed analysis
                st.subheader("Detailed Analysis")
                st.write(st.session_state.analysis_result.get('full_response', ''))
                
                # Add PDF report generation
                st.subheader("Download Analysis Report")
                if st.button("Generate PDF Report"):
                    with st.spinner("Generating PDF report..."):
                        try:
                            # Generate PDF report
                            pdf_bytes = self.ai_analyzer.generate_pdf_report(
                                analysis_result=st.session_state.analysis_result,
                                candidate_name=st.session_state.candidate_name,
                                job_role=job_role
                            )
                            
                            if pdf_bytes:
                                # Create download button
                                st.download_button(
                                    label="Download PDF Report",
                                    data=pdf_bytes.getvalue(),
                                    file_name=f"{st.session_state.candidate_name}_Analysis_Report.pdf",
                                    mime="application/pdf"
                                )
                                st.success("PDF report generated successfully!")
                            else:
                                st.error("Failed to generate PDF report. Please try again.")
                        except Exception as e:
                            st.error(f"Error generating PDF report: {str(e)}")
                            import traceback
                            st.code(traceback.format_exc())

    def show_builder(self):
        """Display resume builder page"""
        st.title("Resume Builder")
        
        # Template selection
        template = st.selectbox(
            "Choose a template",
            ["Modern", "Professional", "Minimal", "Creative"]
        )
        
        # Personal Information
        st.subheader("Personal Information")
        col1, col2 = st.columns(2)
        
        with col1:
            full_name = st.text_input("Full Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone")
        
        with col2:
            location = st.text_input("Location")
            linkedin = st.text_input("LinkedIn Profile")
            portfolio = st.text_input("Portfolio Website")
        
        # Professional Summary
        st.subheader("Professional Summary")
        summary = st.text_area("Write a brief summary of your professional background")
        
        # Experience
        st.subheader("Work Experience")
        experience = []
        
        num_experiences = st.number_input("Number of experiences", min_value=1, max_value=10, value=1)
        
        for i in range(num_experiences):
            st.write(f"Experience {i+1}")
            col1, col2 = st.columns(2)
            
            with col1:
                company = st.text_input(f"Company {i+1}")
                position = st.text_input(f"Position {i+1}")
            
            with col2:
                start_date = st.date_input(f"Start Date {i+1}")
                end_date = st.date_input(f"End Date {i+1}")
            
            description = st.text_area(f"Description {i+1}")
            
            if company and position:
                experience.append({
                    'company': company,
                    'position': position,
                    'start_date': start_date.strftime("%B %Y"),
                    'end_date': end_date.strftime("%B %Y"),
                    'description': description
                })
        
        # Education
        st.subheader("Education")
        education = []
        
        num_education = st.number_input("Number of education entries", min_value=1, max_value=5, value=1)
        
        for i in range(num_education):
            st.write(f"Education {i+1}")
            col1, col2 = st.columns(2)
            
            with col1:
                school = st.text_input(f"School {i+1}")
                degree = st.text_input(f"Degree {i+1}")
            
            with col2:
                field = st.text_input(f"Field of Study {i+1}")
                graduation_date = st.date_input(f"Graduation Date {i+1}")
                gpa = st.text_input(f"GPA {i+1}")
            
            if school and degree:
                education.append({
                    'school': school,
                    'degree': degree,
                    'field': field,
                    'graduation_date': graduation_date.strftime("%B %Y"),
                    'gpa': gpa
                })
        
        # Skills
        st.subheader("Skills")
        skills = {}
        
        technical_skills = st.text_area("Technical Skills (comma-separated)")
        soft_skills = st.text_area("Soft Skills (comma-separated)")
        languages = st.text_area("Languages (comma-separated)")
        tools = st.text_area("Tools & Technologies (comma-separated)")
        
        if technical_skills:
            skills['technical'] = [s.strip() for s in technical_skills.split(',')]
        if soft_skills:
            skills['soft'] = [s.strip() for s in soft_skills.split(',')]
        if languages:
            skills['languages'] = [s.strip() for s in languages.split(',')]
        if tools:
            skills['tools'] = [s.strip() for s in tools.split(',')]
        
        # Generate Resume
        if st.button("Generate Resume"):
            resume_data = {
                'template': template,
                'personal_info': {
                    'full_name': full_name,
                    'email': email,
                    'phone': phone,
                    'location': location,
                    'linkedin': linkedin,
                    'portfolio': portfolio
                },
                'summary': summary,
                'experience': experience,
                'education': education,
                'skills': skills
            }
            
            try:
                # Generate resume
                resume_bytes = self.resume_builder.generate_resume(resume_data)
                
                if resume_bytes:
                    # Download button
                    st.download_button(
                        "Download Resume",
                        resume_bytes,
                        file_name=f"{full_name.replace(' ', '_')}_Resume.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
                else:
                    st.error("Error generating resume")
            
            except Exception as e:
                st.error(f"Error generating resume: {str(e)}")

    def show_dashboard(self):
        """Display dashboard page"""
        st.title("Dashboard")
        
        try:
            # Get AI analysis statistics
            stats = self.ai_analyzer.get_ai_analysis_statistics()
            
            if stats and stats.get('total_analyses', 0) > 0:
                # Overall Statistics
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric("Total Resumes Analyzed", stats['total_analyses'])
                    st.metric("Average Resume Score", f"{stats['average_score']:.1f}%")
                
                with col2:
                    # Model Usage Distribution
                    st.subheader("Model Usage")
                    if stats['model_usage']:
                        model_data = pd.DataFrame({
                            'Model': list(stats['model_usage'].keys()),
                            'Count': list(stats['model_usage'].values())
                        })
                        st.bar_chart(model_data.set_index('Model'))
                    else:
                        st.info("No model usage data available")
                
                # Job Role Distribution
                st.subheader("Job Role Distribution")
                if stats['job_roles']:
                    role_data = pd.DataFrame({
                        'Role': list(stats['job_roles'].keys()),
                        'Count': list(stats['job_roles'].values())
                    })
                    st.bar_chart(role_data.set_index('Role'))
                else:
                    st.info("No job role data available")
                
                # Recent Analyses
                st.subheader("Recent Analyses")
                recent_analyses = self.ai_analyzer.get_recent_analyses(limit=5)
                if recent_analyses:
                    for analysis in recent_analyses:
                        with st.expander(f"Analysis from {analysis['created_at']}"):
                            st.write(f"Job Role: {analysis['job_role']}")
                            st.write(f"Resume Score: {analysis['resume_score']}%")
                            st.write(f"Model Used: {analysis['model_used']}")
                else:
                    st.info("No recent analyses available")
            else:
                st.info("No analysis data available yet. Start analyzing resumes to see statistics.")
                
        except Exception as e:
            st.error(f"Error loading dashboard data: {str(e)}")
            import traceback
            st.code(traceback.format_exc())

    def show_about(self):
        """Display about page"""
        st.title("About Smart Resume AI")
        
        # Introduction
        st.write("""
        Smart Resume AI is an intelligent resume analysis and building platform that helps 
        job seekers create professional resumes and improve their chances of landing their 
        dream jobs. This innovative tool combines the power of artificial intelligence with 
        industry best practices to provide comprehensive resume analysis and optimization.
        """)
        
        # Features Section
        st.subheader("Key Features")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("""
            **Resume Analysis**
            - AI-powered content analysis
            - ATS compatibility checking
            - Detailed feedback and suggestions
            - Score-based evaluation
            - Keyword optimization
            - Format validation
            """)
            
        with col2:
            st.write("""
            **Resume Building**
            - Professional templates
            - Real-time editing
            - Export to PDF/DOCX
            - Customizable sections
            - Industry-specific guidance
            - Best practices suggestions
            """)
        
        # Technology Stack
        st.subheader("Technology Stack")
        st.write("""
        Built with cutting-edge technologies:
        - **Frontend**: Streamlit for interactive web interface
        - **AI Models**: Google Gemini and OpenRouter integration
        - **PDF Processing**: Advanced OCR and text extraction
        - **Database**: SQLite for data persistence
        - **Document Processing**: Support for PDF and DOCX formats
        """)
        
        # Creator Information
        st.subheader("About the Creator")
        st.write("""
        Smart Resume AI was developed by G S ABINIVAS (abinivas8), a passionate developer focused on creating 
        innovative solutions that make a real difference in people's lives. This project was 
        born from the understanding that job seekers need better tools to navigate the 
        competitive job market.
        """)
        
        # Mission and Vision
        st.subheader("Our Mission")
        st.write("""
        To empower job seekers with intelligent tools that help them present their best selves 
        to potential employers. We believe that everyone deserves access to professional 
        resume analysis and building tools, regardless of their background or resources.
        """)
        
        # Contact Information
        st.subheader("Contact & Support")
        st.write("""
        For any questions, feedback, or support:
        - **Email**: abinivas6374@gmail.com
        - **GitHub**: [Smart Resume AI Repository](https://github.com/abi6374)
        - **LinkedIn**: [G S ABINIVAS](https://linkedin.com/in/abinivas8)
        """)
        
        # Version Information
        st.subheader("Version Information")
        st.write("""
        Current Version: 1.0.0
        Last Updated: April 2025
        
        We are constantly working to improve Smart Resume AI with new features and 
        enhancements. Your feedback helps us make the platform better for everyone.
        """)
        
        # Footer
        st.markdown("---")
        st.write("""
        <div style='text-align: center'>
            <p>© 2025 Smart Resume AI. All rights reserved.</p>
            <p>Made with ❤️ by ABINIVAS (abinivas8)</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    app = ResumeApp()
    app.main()
