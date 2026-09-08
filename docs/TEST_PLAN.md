# Test Plan

| ID | Test case | Expected result |
|---|---|---|
| TC01 | Ask minimum attendance | Knowledge-base answer about 75% |
| TC02 | Ask attendance percentage | Attendance Tool is selected |
| TC03 | Ask Monday timetable | Timetable Tool is selected |
| TC04 | Ask bonafide procedure | RAG Knowledge Search is selected |
| TC05 | Ask syllabus details | RAG Knowledge Search is selected |
| TC06 | Ask unrelated question | System explains that reliable information was not found |
| TC07 | Clear Memory | Current conversation is removed |
| TC08 | Restart session | Previous session messages are not persisted |

## Acceptance criteria

- Application launches with Streamlit.
- No external API key is required for demo mode.
- All three advertised capabilities are demonstrable.
- Knowledge answers originate from the local knowledge file.
- Tool requests display the selected capability in the execution trace.
