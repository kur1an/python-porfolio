from flask import Flask, render_template

app = Flask(__name__)

# Data for the portfolio
portfolio_data = {
    "name": "Amith Kurian Joseph",
    "contact": {
        "phone": "7510300688",
        "email": "amith.kurianj@gmail.com",
        "linkedin": "https://www.linkedin.com/in/amithkurianjoseph/",
        "github": "https://github.com/kur1an"
    },
    "skills": [
        "Dart", "C", "JavaScript", "Python", "Java", "CSS", "LaTeX",
        "Canva", "Figma", "Express.js", "Node.js", "CNN", "MongoDB",
        "Compiler", "Operating System", "Cloud Computing", "Deep Learning",
        "Ethical Hacking", "Voice Recognition"
    ],
    "soft_skills": [
        "Problem solving", "Self-learning", "Adaptability", "Leadership",
        "Analytical thinking", "Communication", "Flexibility", "Delegation",
        "Teamwork", "Influence"
    ],
    "experience": [
        {
            "role": "Cyber Security Intern",
            "company": "SkillCraft Technology",
            "date": "Jun 2024",
            "type": "Remote"
        },
        {
            "role": "Data Science Intern",
            "company": "Bharat Intern",
            "date": "Feb 2024",
            "type": "Remote"
        }
    ],
    "education": "B.Tech in Computer Science Engineering, College of Engineering Karunagappally, Kollam (2021-25)",
    "projects": [
        {
            "title": "Automatically Live Engagement Of Students During Online Meeting",
            "tech": "Python, CNN, ResNet",
            "description": "Real-time student engagement detection system for virtual classrooms using Jitsi Meet, MediaPipe, and a CNN-ResNet ensemble model."
        },
        {
            "title": "BusT: Private & Public Bus Timing App",
            "tech": "Flutter, Figma, Node.js, MongoDB",
            "description": "Streamlined commuting experiences for users across Kerala with a robust mobile app."
        },
        {
            "title": "Human Facial Recognition System",
            "tech": "Python, Deep Learning, CNN",
            "description": "Sophisticated facial recognition system using TensorFlow or PyTorch for identity verification."
        },
        {
            "title": "Home Automation System with Arduino",
            "tech": "HTML, JavaScript, Arduino IDE",
            "description": "Voice-activated device control and remote home automation system."
        }
    ],
    "certifications": [
        "Ethical Hacking and Penetration Testing (C-DAC, NOIDA, MeitY)",
        "Digital Forensics Essentials (EC-Council)",
        "Google Cloud Computing Foundations (NPTEL Online Certification)",
        "Cyber Security Cadet - Ethical Hacking (Technovalley AKS on Udemy)"
    ]
}

@app.route('/')
def home():
    return render_template('portfolio.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True)
