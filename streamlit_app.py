import streamlit as st
import re
import random
from datetime import datetime

class MechEngBot:
    def __init__(self):
        self.knowledge_base = {
            "career": [
                "🏢 Career Opportunities in Morocco:",
                "• Automotive Industry:",
                "  - Renault-Nissan Tanger Med",
                "  - PSA Group",
                "  - Automotive suppliers (Hands & Hands, Yazaki)",
                "• Aerospace:",
                "  - GIMAS member companies",
                "  - Safran",
                "• Manufacturing & Production",
                "• Energy Sector:",
                "  - Siemens Gamesa",
                "  - OCP Group",
                "• Average Starting Salary: 6,000-12,000 MAD/month"
            ],
            
            "courses": [
                "📚 Key Courses at FST Tanger:",
                "• First Year:",
                "  - Mathematics & Physics",
                "  - Engineering Mechanics",
                "  - Technical Drawing",
                "• Second Year:",
                "  - Thermodynamics",
                "  - Materials Science",
                "  - Manufacturing Processes",
                "• Third Year:",
                "  - Machine Design",
                "  - CAD/CAM",
                "  - Fluid Mechanics",
                "  - Project Management"
            ],
            
            "skills": [
                "🛠️ Essential Skills:",
                "• Technical Skills:",
                "  - CAD Software (SOLIDWORKS, AutoCAD)",
                "  - Programming (Python, MATLAB)",
                "  - Technical Drawing",
                "• Soft Skills:",
                "  - Problem-solving",
                "  - Team collaboration",
                "  - Project management",
                "• Languages:",
                "  - French (Professional)",
                "  - English (Technical)",
                "  - Arabic (Native)"
            ],
            
            "internships": [
                "🏭 Internship Opportunities:",
                "• Major Companies in Tanger:",
                "  - Renault Tanger Med",
                "  - Siemens Gamesa",
                "  - Hands & Hands",
                "• Application Period:",
                "  - PFE: February-March",
                "  - Summer Internships: April-May",
                "• Required Documents:",
                "  - CV in French",
                "  - Cover Letter",
                "  - Academic Transcript"
            ],
            
            "universities": [
                "🎓 Top Engineering Schools in Morocco:",
                "• Public Schools:",
                "  - EMI Rabat",
                "  - ENSEM Casablanca",
                "  - FST Tanger",
                "• Private Schools:",
                "  - EMINES Ben Guerir",
                "  - EIGSICA Casablanca",
                "• Admission Requirements:",
                "  - Strong grades in Math/Physics",
                "  - Competitive entrance exam",
                "  - French proficiency"
            ]
        }
        
        self.patterns = {
            r'\b(career|job|work|salary|employment)\b': 'career',
            r'\b(course|study|subject|curriculum)\b': 'courses',
            r'\b(skill|ability|competency)\b': 'skills',
            r'\b(internship|training|practical)\b': 'internships',
            r'\b(university|school|education|college)\b': 'universities'
        }
        
        self.greetings = [
            "Marhaba! How can I help you with mechanical engineering?",
            "Hello! What would you like to know about mechanical engineering?",
            "Hi there! Ask me anything about mechanical engineering studies!"
        ]
        
        self.fallback = [
            "I'm not sure about that. Try asking about careers, courses, skills, internships, or universities.",
            "Could you rephrase that? I can help with information about mechanical engineering studies and prospects.",
            "I didn't quite understand. I'm best at answering questions about mechanical engineering careers and education."
        ]

    def respond(self, user_input):
        if any(word in user_input.lower() for word in ['hi', 'hello', 'hey', 'marhaba']):
            return random.choice(self.greetings)
        
        if any(word in user_input.lower() for word in ['bye', 'goodbye', 'exit', 'quit']):
            return "Goodbye! Good luck with your mechanical engineering studies! 👋"
        
        for pattern, topic in self.patterns.items():
            if re.search(pattern, user_input.lower()):
                return "\n".join(self.knowledge_base[topic])
        
        return random.choice(self.fallback)

def main():
    st.set_page_config(
        page_title="Mechanical Engineering Assistant",
        page_icon="🎓",
        layout="centered"
    )

    st.title("Mechanical Engineering Student Assistant")
    st.markdown("Your guide to mechanical engineering studies in Morocco 🇲🇦")

    # Initialize session state for chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.bot = MechEngBot()
        # Add welcome message
        welcome_msg = ("Welcome to the Mechanical Engineering Assistant! 🎓\n" +
                      "Ask me about:\n" +
                      "• Careers and job prospects\n" +
                      "• Courses and curriculum\n" +
                      "• Required skills\n" +
                      "• Internship opportunities\n" +
                      "• Universities and education")
        st.session_state.messages.append({"role": "assistant", "content": welcome_msg})

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask your question here..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get bot response
        response = st.session_state.bot.respond(prompt)
        
        # Add bot response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Display bot response
        with st.chat_message("assistant"):
            st.markdown(response)

if __name__ == "__main__":
    main()
