import streamlit as st
import ollama

st.set_page_config(
    page_title="EduGenius",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #f4f7fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1 {
    color: #173b68;
}

h2, h3 {
    color: #24558a;
}

div.stButton > button {
    background-color: #24558a;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 0.5rem 1rem;
}

div.stButton > button:hover {
    background-color: #173b68;
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #e8f0fa;
}

</style>
""", unsafe_allow_html=True)
st.title("🎓 EduGenius")

st.write("Welcome! Your personal learning assistant is here to help.")

st.divider()

menu = st.sidebar.selectbox(
    "Choose a feature",
    ["Home", "Ask a Question", "Generate Short Notes", "Practice Quiz","AI Flashcards","Learning Weakness Detector","Tamil + English AI Tutor","Image-Based Learning"
    ]
)
if "selected_feature" in st.session_state:
    st.session_state["feature_menu"] = st.session_state.pop(
        "selected_feature"
    )
    st.rerun()
if menu == "Home":
    st.title("🎓 EduGenius ")

    st.markdown(
        "### Your personal AI-powered learning companion"
    )

    st.write(
        "Learn concepts, generate study notes, and test your knowledge "
        "using your AI learning assistant."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🤖 **Ask AI**\n\nGet explanations for your questions.")

    with col2:
        st.info("📝 **Smart Notes**\n\nGenerate notes on different topics.")

    with col3:
        st.info("🧠 **Practice Quiz**\n\nCreate quizzes and check your score.")

    st.divider()

    st.subheader("🚀 Start Learning")

    st.write(
        "Choose a feature from the sidebar to begin your learning session."
    )
elif menu ==  "Ask a Question":
    st.subheader("💬 Ask Your AI Learning Assistant")

    question = st.text_input(
        "Enter your question",
        placeholder="Example: Explain artificial intelligence in simple English"
    )

    if st.button("Get Answer"):
        if question.strip():
            with st.spinner("AI is thinking..."):
                try:
                    import ollama

                    response = ollama.chat(
                        model="llama3.2",
                        messages=[
                            {
                                "role": "system",
                                "content": (
                                    "You are a helpful student learning assistant. "
                                    "Explain concepts in simple English. "
                                    "Use examples and short explanations suitable for students."
                                )
                            },
                            {
                                "role": "user",
                                "content": question
                            }
                        ]
                    )

                    st.success("AI Answer")
                    st.write(response["message"]["content"])

                except Exception as e:
                    st.error(
                        "Could not connect to the AI model. "
                        "Please check that Ollama is running and llama3.2 is installed."
                    )
                    st.caption(f"Technical details: {e}")
        else:
            st.warning("Please enter a question first.")

    question = st.text_input("Enter your question")

    if st.button("Get Answer", key="get_answer_button"):
        q = question.lower()

        if "python" in q:
            st.success("Python is a programming language used to build websites, software, and AI applications.")

        elif "artificial intelligence" in q or "what is ai" in q:
            st.success("Artificial Intelligence (AI) enables computers to perform tasks that usually require human intelligence.")

        elif "computer" in q:
            st.success("A computer is an electronic device that processes data and produces information.")

        else:
            st.warning("I don't have an answer for this question yet. More topics can be added later.")

elif menu == "Generate Short Notes":
    st.subheader("📝 AI Short-Notes Generator")

    topic = st.text_input(
        "Enter a topic",
        placeholder="Example: Photosynthesis"
    )

    if st.button("Generate Notes"):
        if topic.strip():
            with st.spinner("AI is preparing your notes..."):
                try:
                    import ollama

                    response = ollama.chat(
                        model="llama3.2",
                        messages=[
                            {
                                "role": "system",
                                "content": (
                                    "You are a student learning assistant. "
                                    "Create clear, accurate, easy-to-understand "
                                    "short notes for students. Include a definition, "
                                    "important points, examples, and a short summary. "
                                    "Use headings and bullet points."
                                )
                            },
                            {
                                "role": "user",
                                "content": (
                                    f"Generate short study notes for the subject {subject} "
                                    f"on the topic: {topic}"           
                                )
                            }
                        ]
                    )

                    st.markdown("### 📚 Your Study Notes")
                    notes = response["message"]["content"]

                    st.markdown("### 📚 Your Study Notes")
                    st.markdown(notes)

                    st.download_button(
    label="📥 Download Notes",
    data=notes,
    file_name=f"{topic.replace(' ', '_')}_notes.txt",
    mime="text/plain"
)

                except Exception as e:
                    st.error(
                        "Unable to generate notes. "
                        "Please check that Ollama is running."
                    )
                    st.caption(f"Technical details: {e}")
        else:
            st.warning("Please enter a topic first.")
    st.subheader("📝 Generate Short Notes")

    topic = st.selectbox(
        "Choose a topic",
        ["Python", "Artificial Intelligence", "Computer"]
    )

    if st.button("Show Notes"):
        if topic == "Python":
            st.write("""
            **Short Notes: Python**
            - Python is a high-level programming language.
            - It has simple and readable syntax.
            - It is used in AI, web development, and data science.
            """)

        elif topic == "Artificial Intelligence":
            st.write("""   
            **Short Notes: Artificial Intelligence**
            - AI enables machines to perform intelligent tasks.
            - AI is used in healthcare, education, and transportation.
            - Machine learning is a branch of AI.
            """)

        else:
            st.write("""
            **Short Notes: Computer**
            - A computer is an electronic device that processes data.
            - It accepts input, processes data, and produces output.
            - Computers are used in education, business, and science.
            """)

elif menu == "Practice Quiz":
    import json

    st.subheader("🧠 AI-Generated Practice Quiz")
    st.write("Enter a topic and let AI create your quiz!")

    
    subject = st.selectbox(
    "📚 Choose a subject",
    [
        "Computer Science",
        "General Science",
        "Mathematics",
        "Social Studies",
        "English",
        "History"
    ]
)

topic = st.text_input(
    "📝 Enter a topic",
    placeholder="Example: Photosynthesis"
)

number = st.selectbox(
        "Number of questions",
        [5, 10]
    )

if st.button("Generate Quiz"):
        if not topic.strip():
            st.warning("Please enter a topic.")
        else:
            with st.spinner("AI is creating your quiz..."):
                try:
                    import ollama

                    response = ollama.chat(
                        model="llama3.2",
                        format="json",
                        messages=[
                            {
                                "role": "system",
                                "content": (
                                    "You are an educational quiz generator. "
                                    "Create accurate multiple-choice questions. "
                                    "Return only valid JSON with this structure: "
                                    '{"questions":[{"question":"Question text",'
                                    '"options":["A","B","C","D"],'
                                    '"answer":"A"}]}. '
                                    "The answer must exactly match one of the "
                                    "four options. Do not include explanations."
                                )
                            },
                            {
                                "role": "user",
                                "content": (
                                    f"Create {number} multiple-choice questions "
                                    f"about {topic}. Use four options per question. "
                                    "Make the questions suitable for students."
                                )
                            }
                        ]
                    )

                    data = json.loads(
                        response["message"]["content"]
                    )

                    questions = data["questions"]

                    if (
                        len(questions) != number
                        or any(
                            len(q.get("options", [])) != 4
                            or q.get("answer") not in q.get("options", [])
                            or not q.get("question")
                            for q in questions
                        )
                    ):
                        st.error(
                            "The AI generated an invalid quiz. "
                            "Please try generating it again."
                        )
                    else:
                        st.session_state["ai_quiz"] = questions
                        st.session_state["quiz_topic"] = topic
                        st.session_state.pop("quiz_score", None)
                        st.rerun()

                except Exception as e:
                    st.error("Could not generate the quiz.")
                    st.caption(f"Details: {e}")

questions = st.session_state.get("ai_quiz", [])
if questions:
        st.divider()
        st.subheader(
            f"📚 Quiz: {st.session_state['quiz_topic']}"
        )

        with st.form("ai_quiz_form"):
            answers = []

            for i, q in enumerate(questions):
                st.write(
                    f"**Question {i + 1}: {q['question']}**"
                )

                selected = st.radio(
                    "Choose your answer:",
                    q["options"],
                    index=None,
                    key=f"ai_quiz_answer_{i}"
                )

                answers.append(selected)

            submitted = st.form_submit_button("Submit Quiz")

        if submitted:
            if any(answer is None for answer in answers):
                st.warning(
                    "Please answer every question before submitting."
                )
            else:
                score = sum(
                    answers[i] == questions[i]["answer"]
                    for i in range(len(questions))
                )

                st.session_state["quiz_score"] = score

        if "quiz_score" in st.session_state:
            score = st.session_state["quiz_score"]

            st.success(
                f"Your score: {score} out of {len(questions)}"
            )

            percentage = score / len(questions) * 100
            st.write(f"**Percentage: {percentage:.0f}%**")

            with st.expander("Check correct answers"):
                for i, q in enumerate(questions):
                    st.write(f"**Question {i + 1}:** {q['question']}")
                    st.write(f"Correct answer: {q['answer']}")

            if st.button("Try Another Quiz"):
                st.session_state.pop("ai_quiz", None)
                st.session_state.pop("quiz_topic", None)
                st.session_state.pop("quiz_score", None)

                for i in range(len(questions)):
                    st.session_state.pop(
                        f"ai_quiz_answer_{i}", None
                    )

                st.rerun()
elif menu == "Learning Weakness Detector":

    st.title("🧠 AI Learning Weakness Detector")

    st.write(
        "Enter your quiz results to identify topics "
        "that may need more revision."
    )

    st.info(
        "Your results are used to recommend revision topics, "
        "not to judge your ability."
    )

    number_of_topics = st.number_input(
        "How many topics do you want to analyse?",
        min_value=1,
        max_value=10,
        value=3,
        step=1
    )

    with st.form("weakness_detector_form"):

        results = []

        for i in range(int(number_of_topics)):

            st.subheader(f"Topic {i + 1}")

            topic = st.text_input(
                "Topic name",
                key=f"weak_topic_{i}",
                placeholder="Example: Photosynthesis"
            )

            total = st.number_input(
                "Total quiz questions",
                min_value=1,
                max_value=100,
                value=5,
                key=f"weak_total_{i}"
            )

            correct = st.number_input(
                "Correct answers",
                min_value=0,
                max_value=100,
                value=2,
                key=f"weak_correct_{i}"
            )

            results.append({
                "topic": topic,
                "total": total,
                "correct": correct
            })

        analyse = st.form_submit_button("Analyse My Results")

    if analyse:

        valid_results = True

        for result in results:
            if not result["topic"].strip():
                st.warning("Please enter a name for every topic.")
                valid_results = False
                break

            if result["correct"] > result["total"]:
                st.warning(
                    f"For {result['topic']}, correct answers "
                    "cannot exceed total questions."
                )
                valid_results = False
                break

        if valid_results:

            st.subheader("📊 Your Learning Analysis")

            weak_topics = []

            for result in results:

                percentage = (
                    result["correct"] / result["total"]
                ) * 100

                st.write(f"### 📚 {result['topic']}")
                st.progress(int(percentage))
                st.write(
                    f"Score: {result['correct']}/"
                    f"{result['total']} ({percentage:.0f}%)"
                )

                if percentage < 50:
                    st.error("🔴 Recommended: Review the basics.")
                    weak_topics.append(result["topic"])

                elif percentage < 75:
                    st.warning("🟡 Recommended: Revise this topic.")
                    weak_topics.append(result["topic"])

                else:
                    st.success(
                        "🟢 Good result! Continue practising "
                        "to maintain your understanding."
                    )

            st.divider()
            st.subheader("🎯 Recommended Next Steps")

            if weak_topics:

                st.write(
                    "Spend extra revision time on these topics:"
                )

                for topic in weak_topics:
                    st.write(f"- 📖 {topic}")

                st.info(
                    "Next, use Generate Short Notes to revise "
                    "these topics and Practice Quiz to test "
                    "your understanding again."
                )

            else:
                st.success(
                    "All analysed topics scored 75% or higher. "
                    "Try a more challenging quiz to continue learning."
                )
                
 
elif menu == "Tamil + English AI Tutor":
               st.header("🗣️ Tamil + English AI Tutor")
               st.write("Learn difficult topics with simple explanations and examples.")

topic = st.text_input("Enter the topic you want to learn:")

language = st.selectbox(
        "Choose your language:",
        ["English", "Tamil", "Both Tamil and English"]
    )

if st.button("Teach Me", key="tutor_button"):
        if topic.strip():
            with st.spinner("Preparing your lesson..."):
                prompt = f"""
                You are a friendly student tutor.
                Teach the topic: {topic}

                Language: {language}

                Explain in simple words.
                Give a clear definition, important points,
                and two easy examples.
                If Tamil is selected, explain in Tamil.
                If English is selected, explain in English.
                If both are selected, explain in both languages.
                """

                try:
                    response = ollama.chat(
                        model="llama3.2",
                        messages=[
                            {"role": "user", "content": prompt}
                        ]
                    )

                    st.subheader("📚 Your Lesson")
                    st.write(response["message"]["content"])

                except Exception as e:
                    st.error(f"AI Tutor error: {e}")
        else:
            st.warning("Please enter a topic first.")

elif menu == "Image-Based Learning":
    st.header("📸 Image-Based Learning")
    st.write("Upload a textbook image and let AI explain it.")

    uploaded_image = st.file_uploader(
        "Upload a textbook image",
        type=["png", "jpg", "jpeg"],
        key="vision_learning_image"
    )

    language = st.selectbox(
        "Explanation language",
        ["English", "Tamil"],
        key="vision_image_language"
    )

    question = st.text_input(
        "What would you like to understand about this image?",
        key="vision_image_question"
    )

    if uploaded_image is not None:
        st.image(uploaded_image, caption="Your uploaded image")

        if st.button("🔍 Explain Image with AI", key="explain_image"):
            with st.spinner("AI is analysing your image..."):
                try:
                    prompt = f"""
                    Explain this textbook image in {language}.
                    Student's question: {question if question else "Explain the main ideas in this image."}
                    Use simple language and examples.
                    If the image contains text, explain its important points.
                    """

                    response = ollama.chat(
                        model="llama3.2-vision",
                        messages=[
                            {
                                "role": "user",
                                "content": prompt,
                                "images": [uploaded_image.getvalue()]
                            }
                        ]
                    )

                    st.subheader("📖 AI Explanation")
                    st.write(response["message"]["content"])

                except Exception as e:
                    st.error(f"Unable to explain the image: {e}")

                   
