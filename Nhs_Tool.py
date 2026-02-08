import streamlit as st

def main():
    st.set_page_config(page_title="NHS Statement Tool", layout="wide")
    st.title("🏥 NHS Supporting Statement Tool")
    st.info("Tip: Paste the entire Person Specification into the box below. No need to format it!")

    # 1. Background Information
    st.header("1. Your Background")
    depts = st.text_area("Departments & Experience:", placeholder="e.g. 5 years in Surgical Wards, 2 years in Community...")
    trainings = st.text_area("Certifications & Training:", placeholder="e.g. BLS, Level 3 Safeguarding, Cannulation...")

    # 2. Values Alignment
    st.header("2. NHS Values")
    values_input = st.text_area("Evidence of Compassion & Respect:", placeholder="Describe a time you went above and beyond for a patient...")

    # 3. The Big Evidence Box
    st.header("3. Job Requirements (Person Specification)")
    # Changed to allow free-form pasting
    skills = st.text_area("Paste ALL the job requirements/skills here:", height=300)
    
    # 4. Action Button
    if st.button("✨ Generate My Professional Statement"):
        if not skills or not depts:
            st.warning("Please fill in your Experience and the Job Requirements first!")
        else:
            st.balloons() # A little celebration for finishing!
            st.success("Statement Generated! Copy the text below:")
            
            # This structures your notes into a formal layout
            final_draft = f"""
SUPPORTING STATEMENT

PROFESSIONAL SUMMARY & EXPERIENCE:
{depts}

KEY TRAINING & COMPLIANCE:
{trainings}

VALUES & PATIENT-CENTERED CARE:
{values_input}

EVIDENCE AGAINST PERSON SPECIFICATION:
{skills}
            """
            st.text_area("Final Draft (Select All > Copy):", value=final_draft, height=400)

if __name__ == "__main__":
    main()
