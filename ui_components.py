import streamlit as st

def apply_modern_styles():
    """Apply modern styles to the application"""
    st.markdown("""
    <style>
        /* Modern UI Components */
        .stApp {
            background: linear-gradient(135deg, #f6f9fc 0%, #eef2f7 100%);
        }

        /* Header styles */
        .main-header {
            background: linear-gradient(135deg, #FF6B6B 0%, #FF8E8E 100%);
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            box-shadow: 0 10px 20px rgba(255,107,107,0.2);
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .main-header h1 {
            color: white;
            font-size: 2.5rem;
            font-weight: 600;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }

        .main-header p {
            color: rgba(255,255,255,0.9);
            font-size: 1.2rem;
            margin-top: 1rem;
        }

        /* Card styles */
        .feature-card {
            background: white;
            border-radius: 15px;
            padding: 2rem;
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
            margin-bottom: 1.5rem;
        }

        .feature-card:hover {
            transform: translateY(-5px);
        }

        .feature-card h2 {
            color: #FF6B6B;
            font-size: 1.8rem;
            margin-bottom: 1rem;
        }

        /* Button styles */
        .stButton>button {
            background: linear-gradient(135deg, #FF6B6B 0%, #FF8E8E 100%);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.8rem 1.5rem;
            font-weight: bold;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(255,107,107,0.3);
        }

        /* Input styles */
        .stTextInput>div>div>input {
            border-radius: 10px;
            border: 2px solid #e0e0e0;
            padding: 0.8rem;
            transition: all 0.3s ease;
        }

        .stTextInput>div>div>input:focus {
            border-color: #FF6B6B;
            box-shadow: 0 0 0 2px rgba(255,107,107,0.2);
        }

        /* Select box styles */
        .stSelectbox>div>div>select {
            border-radius: 10px;
            border: 2px solid #e0e0e0;
            padding: 0.8rem;
            transition: all 0.3s ease;
        }

        .stSelectbox>div>div>select:focus {
            border-color: #FF6B6B;
            box-shadow: 0 0 0 2px rgba(255,107,107,0.2);
        }

        /* File uploader styles */
        .stFileUploader>div>div>button {
            background: linear-gradient(135deg, #FF6B6B 0%, #FF8E8E 100%);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.8rem 1.5rem;
            font-weight: bold;
            transition: all 0.3s ease;
        }

        .stFileUploader>div>div>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(255,107,107,0.3);
        }

        /* Footer styles */
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background: linear-gradient(135deg, #FF6B6B 0%, #FF8E8E 100%);
            color: white;
            text-align: center;
            padding: 1rem;
            font-weight: bold;
            box-shadow: 0 -5px 15px rgba(0,0,0,0.1);
            z-index: 1000;
        }

        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }

        ::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb {
            background: #FF6B6B;
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #FF8E8E;
        }
    </style>
    """, unsafe_allow_html=True)

def hero_section():
    """Render the hero section with your name"""
    st.markdown("""
    <div class="main-header">
        <h1>Smart Resume AI</h1>
        <p>Powered by Advanced AI Technology</p>
        <p style="font-size: 1rem; margin-top: 2rem;">Created by ABINIVAS</p>
    </div>
    """, unsafe_allow_html=True)

def feature_card(title, description, icon):
    """Render a feature card with modern styling"""
    st.markdown(f"""
    <div class="feature-card">
        <h2>{icon} {title}</h2>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)

def about_section():
    """Render the about section with your name"""
    st.markdown("""
    <div class="feature-card">
        <h2>About Smart Resume AI</h2>
        <p>Smart Resume AI is an advanced resume analysis and optimization tool that helps job seekers create ATS-friendly resumes and improve their chances of landing interviews.</p>
        <p style="margin-top: 1rem; font-style: italic;">Developed with ❤️ by ABINIVAS</p>
    </div>
    """, unsafe_allow_html=True)

def page_header(title, subtitle=None):
    """Render a consistent page header with gradient background"""
    st.markdown(
        f'''
        <div class="page-header">
            <h1 class="header-title">{title}</h1>
            {f'<p class="header-subtitle">{subtitle}</p>' if subtitle else ''}
        </div>
        ''',
        unsafe_allow_html=True
    )

def hero_section(title, subtitle=None, description=None):
    """Render a modern hero section with gradient background and animations"""
    # If description is provided but subtitle is not, use description as subtitle
    if description and not subtitle:
        subtitle = description
        description = None
    
    st.markdown(
        f'''
        <div class="page-header hero-header">
            <h1 class="header-title">{title}</h1>
            {f'<div class="header-subtitle">{subtitle}</div>' if subtitle else ''}
            {f'<p class="header-description">{description}</p>' if description else ''}
        </div>
        ''',
        unsafe_allow_html=True
    )

def feature_card(icon, title, description):
    """Render a modern feature card with hover effects"""
    st.markdown(f"""
        <div class="card feature-card">
            <div class="feature-icon icon-pulse">
                <i class="{icon}"></i>
            </div>
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
    """, unsafe_allow_html=True)

def about_section(content, image_path=None, social_links=None):
    """Render a modern about section with profile image and social links"""
    st.markdown("""
        <div class="glass-card about-section">
            <div class="profile-section">
    """, unsafe_allow_html=True)
    
    # Profile Image
    if image_path:
        st.image(image_path, use_column_width=False, width=200)
    
    # Image Upload
    uploaded_file = st.file_uploader("Upload profile picture", type=['png', 'jpg', 'jpeg'])
    if uploaded_file is not None:
        st.image(uploaded_file, use_column_width=False, width=200)
    
    # Social Links
    if social_links:
        st.markdown('<div class="social-links">', unsafe_allow_html=True)
        for platform, url in social_links.items():
            st.markdown(f'<a href="{url}" target="_blank" class="social-link"><i class="fab fa-{platform.lower()}"></i></a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # About Content
    st.markdown(f"""
            </div>
            <div class="about-content">{content}</div>
        </div>
    """, unsafe_allow_html=True)

def metric_card(label, value, delta=None, icon=None):
    """Render a modern metric card with animations"""
    icon_html = f'<i class="{icon}"></i>' if icon else ''
    delta_html = f'<div class="metric-delta">{delta}</div>' if delta else ''
    
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-header">
                {icon_html}
                <div class="metric-label">{label}</div>
            </div>
            <div class="metric-value">{value}</div>
            {delta_html}
        </div>
    """, unsafe_allow_html=True)

def template_card(title, description, image_url=None):
    """Render a modern template card with glassmorphism effect"""
    image_html = f'<img src="{image_url}" class="template-image" />' if image_url else ''
    
    st.markdown(f"""
        <div class="glass-card template-card">
            {image_html}
            <h3>{title}</h3>
            <p>{description}</p>
            <div class="card-overlay"></div>
        </div>
    """, unsafe_allow_html=True)

def feedback_card(name, feedback, rating):
    """Render a modern feedback card with rating stars"""
    stars = "⭐" * int(rating)
    
    st.markdown(f"""
        <div class="card feedback-card">
            <div class="feedback-header">
                <div class="feedback-name">{name}</div>
                <div class="feedback-rating">{stars}</div>
            </div>
            <p class="feedback-text">{feedback}</p>
        </div>
    """, unsafe_allow_html=True)

def loading_spinner(message="Loading..."):
    """Show a modern loading spinner with message"""
    st.markdown(f"""
        <div class="loading-container">
            <div class="loading-spinner"></div>
            <p class="loading-message">{message}</p>
        </div>
    """, unsafe_allow_html=True)

def progress_bar(value, max_value, label=None):
    """Render a modern animated progress bar"""
    percentage = (value / max_value) * 100
    label_html = f'<div class="progress-label">{label}</div>' if label else ''
    
    st.markdown(f"""
        <div class="progress-container">
            {label_html}
            <div class="progress-bar">
                <div class="progress-fill" style="width: {percentage}%"></div>
            </div>
            <div class="progress-value">{percentage:.1f}%</div>
        </div>
    """, unsafe_allow_html=True)

def tooltip(content, tooltip_text):
    """Render content with a modern tooltip"""
    st.markdown(f"""
        <div class="tooltip" data-tooltip="{tooltip_text}">
            {content}
        </div>
    """, unsafe_allow_html=True)

def data_table(data, headers):
    """Render a modern data table with hover effects"""
    header_row = "".join([f"<th>{header}</th>" for header in headers])
    rows = ""
    for row in data:
        cells = "".join([f"<td>{cell}</td>" for cell in row])
        rows += f"<tr>{cells}</tr>"
    
    st.markdown(f"""
        <div class="table-container">
            <table class="modern-table">
                <thead>
                    <tr>{header_row}</tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>
            </table>
        </div>
    """, unsafe_allow_html=True)

def grid_layout(*elements):
    """Create a responsive grid layout"""
    st.markdown("""
        <div class="grid">
            {}
        </div>
    """.format("".join(elements)), unsafe_allow_html=True)

def about_section(title, description, team_members=None):
    st.markdown(f"""
        <div class="about-section">
            <h2>{title}</h2>
            <p class="about-description">{description}</p>
            {generate_team_section(team_members) if team_members else ''}
        </div>
        <style>
            .about-section {{
                background: linear-gradient(135deg, #2D2D2D 0%, #1E1E1E 100%);
                border-radius: 20px;
                padding: 3rem 2rem;
                margin: 2rem 0;
                position: relative;
                overflow: hidden;
            }}
            
            .about-section::before {{
                content: '';
                position: absolute;
                top: -50%;
                left: -50%;
                width: 200%;
                height: 200%;
                background: radial-gradient(circle, rgba(0,180,219,0.1) 0%, transparent 70%);
                animation: rotate 20s linear infinite;
            }}
            
            .about-section h2 {{
                color: #E0E0E0;
                margin-bottom: 1.5rem;
                font-size: 2rem;
            }}
            
            .about-description {{
                color: #B0B0B0;
                line-height: 1.6;
                font-size: 1.1rem;
                max-width: 800px;
                margin-bottom: 2rem;
            }}
            
            .team-section {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 1.5rem;
                margin-top: 2rem;
            }}
            
            .team-member {{
                background: #2D2D2D;
                border-radius: 15px;
                padding: 1.5rem;
                text-align: center;
                border: 1px solid #3D3D3D;
                transition: all 0.3s ease;
            }}
            
            .team-member:hover {{
                transform: translateY(-5px);
                border-color: #00B4DB;
            }}
            
            .team-member img {{
                width: 120px;
                height: 120px;
                border-radius: 50%;
                margin-bottom: 1rem;
            }}
            
            .team-member h3 {{
                color: #E0E0E0;
                margin-bottom: 0.5rem;
            }}
            
            .team-member p {{
                color: #B0B0B0;
            }}
        </style>
    """, unsafe_allow_html=True)

def generate_team_section(team_members):
    if not team_members:
        return ""
    
    team_html = '<div class="team-section">'
    for member in team_members:
        team_html += f"""
            <div class="team-member">
                <img src="{member['image']}" alt="{member['name']}">
                <h3>{member['name']}</h3>
                <p>{member['role']}</p>
            </div>
        """
    team_html += '</div>'
    return team_html

def render_feedback(feedback_data):
    """Render feedback with modern styling"""
    if not feedback_data:
        return
    
    feedback_html = """
    <div class="feedback-section">
        <h3 class="feedback-header">Resume Analysis Feedback</h3>
        <div class="feedback-content">
    """
    
    for category, items in feedback_data.items():
        if items:  # Only show categories with feedback
            for item in items:
                feedback_html += f"""
                <div class="feedback-item">
                    <div class="feedback-category">{category}</div>
                    <div class="feedback-description">{item}</div>
                </div>
                """
    
    feedback_html += """
        </div>
    </div>
    """
    
    st.markdown(feedback_html, unsafe_allow_html=True)

def render_analytics_section(resume_uploaded=False, metrics=None):
    """Render the analytics section of the dashboard"""
    if not metrics:
        metrics = {
            'views': 0,
            'downloads': 0,
            'score': 'N/A'
        }
    
    # Views Card
    st.markdown("""
        <div style='background: rgba(0, 20, 30, 0.3); border-radius: 15px; padding: 2rem; text-align: center; margin-bottom: 1rem;'>
            <div style='color: #00bfa5; font-size: 2.5rem; margin-bottom: 1rem;'>
                <i class='fas fa-eye'></i>
            </div>
            <h2 style='color: white; font-size: 1.5rem; margin-bottom: 1rem;'>Resume Views</h2>
            <p style='color: #00bfa5; font-size: 2.5rem; font-weight: bold; margin: 0;'>{}</p>
        </div>
    """.format(metrics['views']), unsafe_allow_html=True)
    
    # Downloads Card
    st.markdown("""
        <div style='background: rgba(0, 20, 30, 0.3); border-radius: 15px; padding: 2rem; text-align: center; margin-bottom: 1rem;'>
            <div style='color: #00bfa5; font-size: 2.5rem; margin-bottom: 1rem;'>
                <i class='fas fa-download'></i>
            </div>
            <h2 style='color: white; font-size: 1.5rem; margin-bottom: 1rem;'>Downloads</h2>
            <p style='color: #00bfa5; font-size: 2.5rem; font-weight: bold; margin: 0;'>{}</p>
        </div>
    """.format(metrics['downloads']), unsafe_allow_html=True)
    
    # Profile Score Card
    st.markdown("""
        <div style='background: rgba(0, 20, 30, 0.3); border-radius: 15px; padding: 2rem; text-align: center; margin-bottom: 1rem;'>
            <div style='color: #00bfa5; font-size: 2.5rem; margin-bottom: 1rem;'>
                <i class='fas fa-chart-line'></i>
            </div>
            <h2 style='color: white; font-size: 1.5rem; margin-bottom: 1rem;'>Profile Score</h2>
            <p style='color: #00bfa5; font-size: 2.5rem; font-weight: bold; margin: 0;'>{}</p>
        </div>
    """.format(metrics['score']), unsafe_allow_html=True)

def render_activity_section(resume_uploaded=False):
    """Render the recent activity section"""
    st.markdown("""
        <div style='background: rgba(0, 20, 30, 0.3); border-radius: 15px; padding: 2rem; height: 100%;'>
            <h2 style='color: white; font-size: 1.5rem; margin-bottom: 1.5rem;'>
                <i class='fas fa-history' style='color: #00bfa5; margin-right: 0.5rem;'></i> Recent Activity
            </h2>
    """, unsafe_allow_html=True)
    
    if resume_uploaded:
        st.markdown("""
            <div style='color: #ddd;'>
                <p style='margin: 0.8rem 0; font-size: 1.1rem;'>• Resume uploaded and analyzed</p>
                <p style='margin: 0.8rem 0; font-size: 1.1rem;'>• Generated optimization suggestions</p>
                <p style='margin: 0.8rem 0; font-size: 1.1rem;'>• Updated profile score</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style='text-align: center; padding: 2rem; color: #666;'>
                <i class='fas fa-upload' style='font-size: 2.5rem; color: #00bfa5; margin-bottom: 1rem;'></i>
                <p style='margin: 0; font-size: 1.1rem;'>Upload your resume to see activity</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

def render_suggestions_section(resume_uploaded=False):
    """Render the suggestions section"""
    st.markdown("""
        <div style='background: rgba(0, 20, 30, 0.3); border-radius: 15px; padding: 2rem; height: 100%;'>
            <h2 style='color: white; font-size: 1.5rem; margin-bottom: 1.5rem;'>
                <i class='fas fa-lightbulb' style='color: #00bfa5; margin-right: 0.5rem;'></i> Suggestions
            </h2>
    """, unsafe_allow_html=True)
    
    if resume_uploaded:
        st.markdown("""
            <div style='color: #ddd;'>
                <p style='margin: 0.8rem 0; font-size: 1.1rem;'>• Add more quantifiable achievements</p>
                <p style='margin: 0.8rem 0; font-size: 1.1rem;'>• Include relevant keywords</p>
                <p style='margin: 0.8rem 0; font-size: 1.1rem;'>• Optimize formatting</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style='text-align: center; padding: 2rem; color: #666;'>
                <i class='fas fa-file-alt' style='font-size: 2.5rem; color: #00bfa5; margin-bottom: 1rem;'></i>
                <p style='margin: 0; font-size: 1.1rem;'>Upload your resume to get suggestions</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)