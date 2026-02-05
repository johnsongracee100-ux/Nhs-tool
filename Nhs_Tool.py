import streamlit as st
import re

def count_words(text):
    return len(text.split()) if text else 0

def main():
    st.set_page_config(page_title="NHS Interview Guarantee Tool", layout="wide")
    
    st.title("🏥 NHS Supporting Statement: Interview Guarantee Edition")
    st.markdown("---")

    # --- SIDEBAR: PROGRESS & KEYWORDS ---
    st.sidebar.header("🎯 Score Optimizer")
    keywords = ["Patient Safety", "Compassion", "Governance", "Equality", "Safeguarding", "Multi-disciplinary", "Accountability", "Confidentiality"]
    
    # --- INPUT SECTIONS ---
    col1, col2 = st.columns(2)
    with col1:
        st.header("1. Professional Context")
        dept_input = st.text_area("Departments Worked In:", placeholder="e.g. A&E, Community, Elderly Care...")
        training_input = st.text_area("Key Trainings:", placeholder="e.g. BLS, Safeguarding Level 3...")

    with col2:
        st.header("2. NHS Values Check")
        st.caption("Recruiters score you on how you reflect these values.")
        values_input = st.text_area("How do you show Compassion & Respect?", 
                                   placeholder="Give a brief example of patient-centered care...")

    st.header("3. Essential Criteria (Person Specification)")
    st.info("Paste your Job Description criteria here. The tool will create a STAR box for each.")
    skills_input = st.text_area("List Skills (one per line):", height=100)
    criteria_list = [c.strip() for c in skills_input.split('\n') if c.strip()]
    
    all_text = dept_input + training_input + values_input
    user_responses = {}

    if criteria_list:
        st.divider()
        st.subheader("4. Evidence Builder (The STAR Method)")
        [attachment_0](attachment)
        for i, crit in enumerate(criteria_list):
            st.write(f"### Requirement: {crit}")
            resp = st.text_area(
                "Your STAR Evidence:", 
                key=f"crit_{i}",
                placeholder="SITUATION: Where were you?\nTASK: What was the goal?\nACTION: What did YOU do?\nRESULT: What was the outcome?"
            )
            user_responses[crit] = resp
            all_text += " " + resp
            st.caption(f"Word count for this section: {count_words(resp)}")

    # --- KEYWORD TRACKER ---
    for word in keywords:
        if re.search(word, all_text, re.IGNORECASE):
            st.sidebar.write(f"✅ **{word}**")
        else:
            st.sidebar.write(f"❌ {word}")

    total_sum = count_words(all_text)
    st.sidebar.divider()
    st.sidebar.metric("Total Word Count", f"{total_sum} / 1500")

    # --- ACTION BUTTONS ---
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🚀 Generate Final Statement"):
            if total_sum > 1500:
                st.error(f"Too long! You are at {total_sum} words. Please trim {total_sum - 1500} words.")
            else:
                final_text = f"# Supporting Information\n\n## Introduction\nI have a strong background in {dept_input}, supported by training in {training_input}.\n\n"
                final_text += f"## Alignment with NHS Values\n{values_input}\n\n"
                for crit, response in user_responses.items():
                    final_text += f"## {crit}\n{response}\n\n"
                
                st.success("Statement Generated!")
                st.text_area("Copy/Paste this:", final_text, height=400)
    
    with col_b:
        # Save Progress Logic
        raw_data = f"DEPT:{dept_input}\nTRAIN:{training_input}\nVALUES:{values_input}\nSKILLS:{skills_input}"
        st.download_button("💾 Save Progress (Draft)", raw_data, file_name="statement_draft.txt")

if __name__ == "__main__":
    main()
