## Project Overview
This project is a Streamlit application designed for Arabic text analysis, including text classification, summarization, and quiz generation. It aims to provide users with tools to understand and process Arabic texts more effectively, leveraging machine learning models and OpenAI's language model for various text processing tasks.

## Features
Text Classification: Classify Arabic articles into categories such as Culture, Finance, Medical, Politics, Religion, Sports, and Tech using a pre-trained machine learning model.
Text Summarization: Generate concise summaries of Arabic articles using OpenAI's GPT-3.5 Turbo model.
Quiz Generation: Create interactive quizzes based on input text to help reinforce learning and understanding.

## Goals
Ease of Use: Provide a user-friendly interface for Arabic text analysis tasks.
Accuracy: Use reliable machine learning models for text classification and summarization to ensure accurate results.
Interactive Learning: Engage users with dynamic quizzes generated from input texts.

## Installation
Prerequisites
Python 3.7 or higher
Streamlit
Joblib
OpenAI API key

## Usage
## Text Classification
Navigate to the التصنيف page using the sidebar.
Enter the Arabic article text in the text area provided.
Click the صنّف button to get the predicted category of the article.
## Text Summarization
Go to the التلخيص page using the sidebar.
Enter the text you want to summarize in the text area.
Press the لخّص button to generate a summary of the input text.
## Quiz Generation
Access the الاختبار page via the sidebar.
Input text in the provided text area to generate questions.
Click أنشئ الأسئلة to create a set of questions based on the input.
Use the اسأل button to display a question, and select an answer from the options.
Submit your answer with سلّم الإجابة to check if it is correct.
Use إنهاء الاختبار to view your final score and reset the quiz.
## Architecture
## Text Classification Architecture
Utilizes a pre-trained machine learning model loaded using Joblib.
Classifies input text into one of seven categories: Culture, Finance, Medical, Politics, Religion, Sports, and Tech.
## Text Summarization Architecture
Leverages OpenAI's GPT-3.5 Turbo model to generate summaries.
Sends text inputs to the API and retrieves summarized text, with adjustable parameters such as temperature and max tokens.
## Quiz Generation Architecture
Generates quiz questions from predefined templates.
Randomly selects questions and options to create an interactive quiz experience.      
## DEMO

https://github.com/user-attachments/assets/5fe48caa-ddee-4428-a187-b67ec118e81d

