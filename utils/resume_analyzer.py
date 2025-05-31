"""
Resume Analyzer Module
"""
import re
import io
import PyPDF2
from docx import Document
import fitz  # PyMuPDF
import pandas as pd
import numpy as np
from typing import Union, Dict, List, Any

class ResumeAnalyzer:
    def __init__(self):
        """Initialize the ResumeAnalyzer"""
        self.sections = {
            'education': ['education', 'academic', 'university', 'college', 'school'],
            'experience': ['experience', 'employment', 'work', 'job'],
            'skills': ['skills', 'technical skills', 'competencies', 'expertise'],
            'projects': ['projects', 'portfolio', 'achievements'],
            'summary': ['summary', 'profile', 'objective', 'about']
        }

    def extract_text_from_pdf(self, file) -> str:
        """Extract text from PDF file"""
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            raise Exception(f"Error extracting text from PDF: {str(e)}")

    def extract_text_from_docx(self, file) -> str:
        """Extract text from DOCX file"""
        try:
            doc = Document(file)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            return text
        except Exception as e:
            raise Exception(f"Error extracting text from DOCX: {str(e)}")

    def analyze_resume(self, resume_data: Dict[str, Any], job_requirements: Dict[str, Any] = None) -> Dict[str, Any]:
        """Analyze resume and return results"""
        try:
            text = resume_data.get('raw_text', '')
            if not text:
                return {'error': 'No text content found in resume'}

            # Basic analysis
            analysis = {
                'document_type': 'resume',
                'ats_score': self._calculate_ats_score(text),
                'format_score': self._calculate_format_score(text),
                'section_score': self._calculate_section_score(text),
                'keyword_match': self._analyze_keyword_match(text, job_requirements),
                'suggestions': self._generate_suggestions(text)
            }

            return analysis
        except Exception as e:
            return {'error': f'Error analyzing resume: {str(e)}'}

    def _calculate_ats_score(self, text: str) -> int:
        """Calculate ATS compatibility score"""
        score = 100
        # Check for common ATS issues
        if len(text) < 100:
            score -= 20
        if not re.search(r'\b(experience|education|skills)\b', text.lower()):
            score -= 15
        if re.search(r'[^\x00-\x7F]', text):  # Non-ASCII characters
            score -= 10
        return max(0, score)

    def _calculate_format_score(self, text: str) -> int:
        """Calculate format score"""
        score = 100
        # Check formatting elements
        if not re.search(r'\n{2,}', text):  # No double line breaks
            score -= 10
        if not re.search(r'[A-Z][a-z]+', text):  # No proper capitalization
            score -= 10
        return max(0, score)

    def _calculate_section_score(self, text: str) -> int:
        """Calculate section completeness score"""
        score = 100
        found_sections = 0
        for section_keywords in self.sections.values():
            if any(keyword in text.lower() for keyword in section_keywords):
                found_sections += 1
        score = (found_sections / len(self.sections)) * 100
        return int(score)

    def _analyze_keyword_match(self, text: str, job_requirements: Dict[str, Any] = None) -> Dict[str, Any]:
        """Analyze keyword match with job requirements"""
        if not job_requirements:
            return {'score': 0, 'missing_skills': []}

        required_skills = job_requirements.get('required_skills', [])
        found_skills = []
        missing_skills = []

        for skill in required_skills:
            if re.search(r'\b' + re.escape(skill.lower()) + r'\b', text.lower()):
                found_skills.append(skill)
            else:
                missing_skills.append(skill)

        score = int((len(found_skills) / len(required_skills)) * 100) if required_skills else 0
        return {
            'score': score,
            'found_skills': found_skills,
            'missing_skills': missing_skills
        }

    def _generate_suggestions(self, text: str) -> List[str]:
        """Generate improvement suggestions"""
        suggestions = []
        
        # Check for common issues
        if len(text) < 200:
            suggestions.append("Resume appears too short. Consider adding more details about your experience and skills.")
        
        if not re.search(r'\b(experience|work|job)\b', text.lower()):
            suggestions.append("No work experience section found. Add your professional experience.")
        
        if not re.search(r'\b(education|university|college|school)\b', text.lower()):
            suggestions.append("No education section found. Add your educational background.")
        
        if not re.search(r'\b(skills|expertise|competencies)\b', text.lower()):
            suggestions.append("No skills section found. List your technical and soft skills.")
        
        return suggestions

    def detect_document_type(self, text):
        text = text.lower()
        scores = {}
        
        # Calculate score for each document type
        for doc_type, keywords in self.document_types.items():
            matches = sum(1 for keyword in keywords if keyword in text)
            density = matches / len(keywords)
            frequency = matches / (len(text.split()) + 1)  # Add 1 to avoid division by zero
            scores[doc_type] = (density * 0.7) + (frequency * 0.3)
        
        # Get the highest scoring document type
        best_match = max(scores.items(), key=lambda x: x[1])
        
        # Only return a document type if the score is significant
        return best_match[0] if best_match[1] > 0.15 else 'unknown'
        
    def calculate_keyword_match(self, resume_text, required_skills):
        resume_text = resume_text.lower()
        found_skills = []
        missing_skills = []
        
        for skill in required_skills:
            skill_lower = skill.lower()
            # Check for exact match
            if skill_lower in resume_text:
                found_skills.append(skill)
            # Check for partial matches (e.g., "Python" in "Python programming")
            elif any(skill_lower in phrase for phrase in resume_text.split('.')):
                found_skills.append(skill)
            else:
                missing_skills.append(skill)
                
        match_score = (len(found_skills) / len(required_skills)) * 100 if required_skills else 0
        
        return {
            'score': match_score,
            'found_skills': found_skills,
            'missing_skills': missing_skills
        }
        
    def check_resume_sections(self, text):
        text = text.lower()
        section_scores = {}
        
        for section, keywords in self.essential_sections.items():
            found = sum(1 for keyword in keywords if keyword in text)
            section_scores[section] = min(25, (found / len(keywords)) * 25)
            
        return sum(section_scores.values())
        
    def check_formatting(self, text):
        lines = text.split('\n')
        score = 100
        deductions = []
        
        # Check for minimum content
        if len(text) < 300:
            score -= 30
            deductions.append("Resume is too short")
            
        # Check for section headers
        if not any(line.isupper() for line in lines):
            score -= 20
            deductions.append("No clear section headers found")
            
        # Check for bullet points
        if not any(line.strip().startswith(('•', '-', '*')) for line in lines):
            score -= 20
            deductions.append("No bullet points found")
            
        # Check for consistent spacing
        if any(len(line.strip()) == 0 and len(next_line.strip()) == 0 
               for line, next_line in zip(lines[:-1], lines[1:])):
            score -= 15
            deductions.append("Inconsistent spacing between sections")
            
        # Check for contact information format
        contact_patterns = [
            r'\b[\w\.-]+@[\w\.-]+\.\w+\b',  # email
            r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',  # phone
            r'linkedin\.com/\w+',  # LinkedIn
        ]
        if not any(re.search(pattern, text) for pattern in contact_patterns):
            score -= 15
            deductions.append("Missing or improperly formatted contact information")
            
        return max(0, score), deductions
        
    def extract_text_from_file(self, file: Union[bytes, io.BytesIO], file_type: str) -> str:
        """Unified method to extract text from different file types"""
        try:
            if file_type.lower() == 'pdf':
                return self.extract_text_from_pdf(file)
            elif file_type.lower() in ['docx', 'doc']:
                return self.extract_text_from_docx(file)
            else:
                raise ValueError(f"Unsupported file type: {file_type}")
        except Exception as e:
            raise Exception(f"Error extracting text from file: {str(e)}")

    def extract_personal_info(self, text):
        """Extract personal information from resume text"""
        email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
        phone_pattern = r'(\+\d{1,3}[-.]?)?\s*\(?\d{3}\)?[-.]?\s*\d{3}[-.]?\s*\d{4}'
        linkedin_pattern = r'linkedin\.com/in/[\w-]+'
        
        email = re.search(email_pattern, text)
        phone = re.search(phone_pattern, text)
        linkedin = re.search(linkedin_pattern, text)
        
        return {
            'email': email.group(0) if email else '',
            'phone': phone.group(0) if phone else '',
            'linkedin': linkedin.group(0) if linkedin else ''
        }

    def extract_education(self, text):
        """Extract education information from resume text"""
        education = []
        lines = text.split('\n')
        education_keywords = [
            'education', 'academic', 'qualification', 'degree', 'university', 'college',
            'school', 'institute', 'certification', 'diploma', 'bachelor', 'master',
            'phd', 'b.tech', 'm.tech', 'b.e', 'm.e', 'b.sc', 'm.sc','bca', 'mca', 'b.com',
            'm.com', 'b.cs-it', 'imca', 'bba', 'mba', 'honors', 'scholarship'
        ]
        in_education_section = False
        current_entry = []

        for line in lines:
            line = line.strip()
            # Check for section header
            if any(keyword.lower() in line.lower() for keyword in education_keywords):
                if not any(keyword.lower() == line.lower() for keyword in education_keywords):
                    # This line contains education info, not just a header
                    current_entry.append(line)
                in_education_section = True
                continue
            
            if in_education_section:
                # Check if we've hit another section
                if line and any(keyword.lower() in line.lower() for keyword in self.document_types['resume']):
                    if not any(edu_key.lower() in line.lower() for edu_key in education_keywords):
                        in_education_section = False
                        if current_entry:
                            education.append(' '.join(current_entry))
                            current_entry = []
                        continue
                
                if line:
                    current_entry.append(line)
                elif current_entry:  # Empty line and we have content
                    education.append(' '.join(current_entry))
                    current_entry = []
        
        if current_entry:
            education.append(' '.join(current_entry))
        
        return education

    def extract_experience(self, text):
        """Extract work experience information from resume text"""
        experience = []
        lines = text.split('\n')
        experience_keywords = [
            'experience', 'employment', 'work history', 'professional experience',
            'work experience', 'career history', 'professional background',
            'employment history', 'job history', 'positions held', 'experience',
            'job title', 'job responsibilities', 'job description', 'job summary'
        ]
        in_experience_section = False
        current_entry = []

        for line in lines:
            line = line.strip()
            # Check for section header
            if any(keyword.lower() in line.lower() for keyword in experience_keywords):
                if not any(keyword.lower() == line.lower() for keyword in experience_keywords):
                    # This line contains experience info, not just a header
                    current_entry.append(line)
                in_experience_section = True
                continue
            
            if in_experience_section:
                # Check if we've hit another section
                if line and any(keyword.lower() in line.lower() for keyword in self.document_types['resume']):
                    if not any(exp_key.lower() in line.lower() for exp_key in experience_keywords):
                        in_experience_section = False
                        if current_entry:
                            experience.append(' '.join(current_entry))
                            current_entry = []
                        continue
                
                if line:
                    current_entry.append(line)
                elif current_entry:  # Empty line and we have content
                    experience.append(' '.join(current_entry))
                    current_entry = []
        
        if current_entry:
            experience.append(' '.join(current_entry))
        
        return experience

    def extract_projects(self, text):
        """Extract project information from resume text"""
        projects = []
        lines = text.split('\n')
        project_keywords = [
            'projects', 'personal projects', 'academic projects', 'key projects',
            'major projects', 'professional projects', 'project experience',
            'relevant projects', 'featured projects','latest projects',
            'top projects'
        ]
        in_project_section = False
        current_entry = []

        for line in lines:
            line = line.strip()
            # Check for section header
            if any(keyword.lower() in line.lower() for keyword in project_keywords):
                if not any(keyword.lower() == line.lower() for keyword in project_keywords):
                    # This line contains project info, not just a header
                    current_entry.append(line)
                in_project_section = True
                continue
            
            if in_project_section:
                # Check if we've hit another section
                if line and any(keyword.lower() in line.lower() for keyword in self.document_types['resume']):
                    if not any(proj_key.lower() in line.lower() for proj_key in project_keywords):
                        in_project_section = False
                        if current_entry:
                            projects.append(' '.join(current_entry))
                            current_entry = []
                        continue
                
                if line:
                    current_entry.append(line)
                elif current_entry:  # Empty line and we have content
                    projects.append(' '.join(current_entry))
                    current_entry = []
        
        if current_entry:
            projects.append(' '.join(current_entry))
        
        return projects

    def extract_skills(self, text):
        """Extract skills from resume text"""
        skills = set()
        lines = text.split('\n')
        in_skills_section = False
        
        for line in lines:
            line = line.strip().lower()
            if 'skills' in line:
                in_skills_section = True
                continue
                
            if in_skills_section:
                if any(section in line for section in ['experience', 'education', 'work']):
                    break
                    
                # Extract skills from the line
                potential_skills = [s.strip() for s in line.split(',')]
                skills.update(s for s in potential_skills if len(s) > 2)
        
        return list(skills)

    def extract_summary(self, text):
        """Extract summary/objective from resume text"""
        lines = text.split('\n')
        summary = []
        
        # Look for summary in first few lines
        for line in lines[:5]:
            if line.strip() and not any(keyword in line.lower() for keyword in ['experience', 'education', 'skills']):
                summary.append(line.strip())
                
        return ' '.join(summary)