import streamlit as st
import random
import openai
import joblib

# Load the pipeline
pipeLine = joblib.load('model_pipeline.joblib')
# Load the model pipeline
model_pipeline = joblib.load('model_pipeline.joblib')

# Category mapping
category_mapping = {
    0: 'ثقافة',
    1: 'Finance',
    2: 'Medical',
    3: 'سياسة',
    4: 'Religion',
    5: 'رياضي',
    6: 'Tech'
}

# Apply RTL CSS
st.markdown(
    """
    <style>
    body {
        direction: rtl;
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def classification_page():
    st.title("صفحة التصنيف")
    
    article = st.text_area("ادخل المقال هنا", height=150)
    
    if st.button("صنّف"):
        if article.strip():
            # Use the model pipeline to predict the category
            numeric_prediction = model_pipeline.predict([article])[0]
            category_prediction = category_mapping.get(numeric_prediction, "Unknown")
            st.write(f"الصنف المتوقع : **{category_prediction}** ")
        else:
            st.error("يرجى إدخال مقال لتصنيفه.")

def summarization_page():
    st.title("صفحة التلخيص")
    

    # Set your OpenAI API key
    openai.api_key = '####'
    # Streamlit app

    # Text input from user
    input_text = st.text_area("ادخل المقال هنا", height=200)

    # Function to generate summary using OpenAI
    def generate_summary(text):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Default model
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                {"role": "user", "content": text}
            ],
            temperature=0.7,  # Default temperature
            max_tokens=150,  # Default max tokens
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return response.choices[0].message['content'].strip()

    # Button to trigger summarization
    if st.button("لخّص"):
        if input_text:
            with st.spinner("إنشاء التلخيص"):
                summary = generate_summary(input_text)
                st.write("### الملخص ")
                st.write(summary)
        else:
            st.warning("يرجى إدخال نص لتلخيصه.")

def generate_questions(user_text):
    questions = [
        {
            "question": "ما هو اسم الكتاب الذي حصل على جائزة عربية على هامش افتتاح معرض بيروت العربي الدولي للكتاب ؟",
            "options": ["الحضارة الاسلامية", "المصحف وقراءاته", "مؤمنون بلا حدود", "عبد المجيد الشرقي"],
            "answer": "المصحف وقراءاته"
        },
        {
            "question": "من الذي حصل أشرف على تصنيف كتاب المصحف وقراءاته ؟",
            "options": ["عبد المجيد الشرقي", "النادي الثقافي العربي", "مؤسسة مؤمنون بلا حدود", "مجموعة من الباحثين"],
            "answer": "عبد المجيد الشرقي"
        },
        {
            "question": "كم عدد مجلدات كتاب المصحف وقراءاته ؟",
            "options": ["ثلاثة مجلدات", "أربعة مجلدات", "خمسة مجلدات", "ستة مجلدات"],
            "answer": "خمسة مجلدات"
        }
    ]
    return questions

def quiz_page():
    st.title("صفحة الاختبار")

    user_text = st.text_area("ادخل المقال هنا", height=150)
    
    if st.button("أنشئ الأسئلة"):
        if user_text:
            questions = generate_questions(user_text)
            st.session_state.questions = questions
            st.session_state.current_question = None
            st.session_state.score = 0
            st.session_state.asked_questions = []

    if 'questions' in st.session_state and len(st.session_state.questions) > 0:
        if st.button("اسأل"):
            if len(st.session_state.asked_questions) < len(st.session_state.questions):
                available_questions = [q for q in st.session_state.questions if q not in st.session_state.asked_questions]
                st.session_state.current_question = random.choice(available_questions)
                st.session_state.asked_questions.append(st.session_state.current_question)
            else:
                st.write("تم عرض جميع الأسئلة")

        if st.session_state.current_question:
            question = st.session_state.current_question
            st.write(f"السؤال: {question['question']}")
            user_answer = st.radio("اختر الإجابة", question['options'], key="answer")

            if st.button("سلّم الإجابة"):
                if user_answer == question['answer']:
                    st.session_state.score += 1
                st.session_state.current_question = None

        if st.button("إنهاء الاختبار"):
            st.write(f"نتيجة الاختبار {st.session_state.score} من {len(st.session_state.asked_questions)}")
            st.session_state.score = 0
            st.session_state.asked_questions = []
            st.session_state.questions = []

# Add navigation
page = st.sidebar.selectbox("اختر صفحة", ["التصنيف", "التلخيص", "الاختبار"])

if page == "التصنيف":
    classification_page()
elif page == "التلخيص":
    summarization_page()
else:
    quiz_page()
