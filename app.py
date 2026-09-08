import streamlit as st
from pathlib import Path
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="CampusAI - Student Support Agent", page_icon="🎓", layout="wide")

# ---------------- Knowledge Base / RAG ----------------
DATA_FILE = Path("data/college_knowledge.txt")
text = DATA_FILE.read_text(encoding="utf-8")
chunks = [c.strip() for c in text.split("\n---\n") if c.strip()]

@st.cache_resource
def build_retriever():
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(chunks)
    return vectorizer, matrix

vectorizer, matrix = build_retriever()

def retrieve(query, k=3):
    q = vectorizer.transform([query])
    scores = cosine_similarity(q, matrix)[0]
    idx = scores.argsort()[::-1][:k]
    return [(chunks[i], float(scores[i])) for i in idx if scores[i] > 0]

# ---------------- Tools ----------------
def attendance_tool(subject="overall"):
    if "overall" in subject.lower():
        return "Attendance status: 86%. Minimum required attendance: 75%."
    return f"Attendance for {subject}: 82%. Minimum required attendance: 75%."

def timetable_tool(day="today"):
    schedules = {
        "monday": "Monday: 9:00 AI & ML, 10:00 DBMS, 11:15 Cloud Computing, 2:00 Project.",
        "tuesday": "Tuesday: 9:00 Python, 10:00 Computer Networks, 11:15 AI Lab, 2:00 Project.",
        "wednesday": "Wednesday: 9:00 Software Engineering, 10:00 ML Lab, 11:15 DBMS, 2:00 Seminar.",
        "thursday": "Thursday: 9:00 Cyber Security, 10:00 AI & ML, 11:15 Project, 2:00 Aptitude.",
        "friday": "Friday: 9:00 Cloud Computing, 10:00 Python, 11:15 Project Lab, 2:00 Placement Training."
    }
    return schedules.get(day.lower(), "Please specify Monday, Tuesday, Wednesday, Thursday or Friday.")

def search_tool(query):
    results = retrieve(query)
    if not results:
        return "No matching college information was found in the knowledge base."
    return "\n\n".join([r[0] for r in results])

# ---------------- Agent ----------------
def agent(query):
    q = query.lower()

    # Tool selection / planning
    if any(x in q for x in ["attendance", "present percentage", "percentage"]):
        tool_result = attendance_tool()
        plan = "Agent plan → detect attendance request → call Attendance Tool → return result."
        return plan, tool_result, "Attendance Tool"

    if "timetable" in q or "class today" in q or "schedule" in q:
        days = ["monday","tuesday","wednesday","thursday","friday"]
        day = next((d for d in days if d in q), "today")
        tool_result = timetable_tool(day)
        plan = "Agent plan → detect timetable request → call Timetable Tool → return result."
        return plan, tool_result, "Timetable Tool"

    # RAG path
    retrieved = retrieve(query)
    plan = "Agent plan → understand question → retrieve relevant college knowledge → generate grounded answer."
    if retrieved:
        answer = retrieved[0][0]
        return plan, answer, "RAG Knowledge Search"

    return plan, ("I could not find a reliable answer in the college knowledge base. "
                  "Please ask about regulations, syllabus, fees, attendance, exams, certificates, "
                  "notices, timetable or other information included in the knowledge base."), "RAG Knowledge Search"

# ---------------- Memory ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🎓 CampusAI")
st.subheader("Agentic AI Student Support Assistant")
st.caption("RAG + Tools + Memory | IBM Agentic AI Internship Demo")

with st.sidebar:
    st.header("Agent Capabilities")
    st.success("✓ RAG Knowledge Search")
    st.success("✓ Tool Calling")
    st.success("✓ Conversation Memory")
    st.info("Demo mode: works without an API key.")
    if st.button("Clear Memory"):
        st.session_state.messages = []
        st.rerun()

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])
        if m.get("meta"):
            st.caption(m["meta"])

query = st.chat_input("Ask a college-related question...")
if query:
    st.session_state.messages.append({"role":"user", "content":query})
    with st.chat_message("user"):
        st.write(query)

    plan, answer, capability = agent(query)

    with st.chat_message("assistant"):
        st.write(answer)
        with st.expander("Agent execution"):
            st.write(plan)
            st.write(f"Capability used: **{capability}**")

    st.session_state.messages.append({
        "role":"assistant",
        "content":answer,
        "meta":f"Used: {capability}"
    })
