# CampusAI Demo Script

## 1. Introduction
“This is CampusAI, an Agentic AI Student Support Assistant developed for the TNSDC–IBM Agentic AI Internship. It demonstrates RAG-style retrieval, tool calling and conversation memory.”

## 2. Knowledge Retrieval
Ask:
`What is the minimum attendance requirement?`

Explain that the application searches the local college knowledge base using TF-IDF similarity and returns the most relevant grounded content.

## 3. Attendance Tool
Ask:
`What is my attendance percentage?`

Explain that the agent detects an attendance intent and invokes the Attendance Tool.

## 4. Timetable Tool
Ask:
`Give me Monday timetable.`

Explain that the agent detects the timetable intent and invokes the Timetable Tool.

## 5. Memory
Continue the conversation and point out that previous user/assistant messages remain visible in the active Streamlit session.

## 6. Closing
“The prototype shows how one student-support interface can route different requests to different capabilities while keeping the conversation visible to the user.”
