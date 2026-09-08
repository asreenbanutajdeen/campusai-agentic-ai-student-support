# CampusAI – Agentic AI Student Support Assistant

## Fast 2-hour IBM Agentic AI Internship project

This project demonstrates the three capabilities required by the selected use case:
- RAG: retrieves answers from a college knowledge base
- Tools: attendance and timetable tools
- Memory: keeps the current conversation in Streamlit session state

## Run

1. Install Python 3.10+.
2. Open terminal in this folder.
3. Run:
   `pip install -r requirements.txt`
4. Run:
   `streamlit run app.py`
5. Open the browser URL shown by Streamlit.

## Demo questions
- What is the minimum attendance requirement?
- What is my attendance percentage?
- Give me Monday timetable.
- How do I apply for a bonafide certificate?
- What does the syllabus include?
- What should I prepare for placements?

## Architecture
Student → Streamlit UI → Agent Planner → (RAG Search / Attendance Tool / Timetable Tool) → Grounded Response → Conversation Memory

## Important
This is a demo knowledge base. Replace data/college_knowledge.txt with your own college regulations, syllabus, FAQs and notices for a real deployment.
