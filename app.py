import streamlit as st

def load_questions(filename):
    questions = []
    with open("questions.txt", "r") as file:
        lines = file.readlines()
        current_question = None
        for line in lines:
            line = line.strip()
            if line.startswith("Question"):
                if current_question is not None:
                    questions.append(current_question)
                current_question = {"question": line}
            elif line.startswith("Answer: "):
                current_question["answer"] = line.split(": ")[1]
            else:
                current_question.setdefault("choices", []).append(line)
    if current_question is not None:
        questions.append(current_question)
    return questions

def display_question(question, question_number):
    st.write(f"Question {question_number}: {question['question']}")
    if "choices" in question:
        for i, choice in enumerate(question["choices"], start=1):
            st.write(f"{chr(64 + i)}) {choice}")

def main():
    st.title("Quiz Game")
    quiz_file = "quiz.txt"
    questions = load_questions(quiz_file)
    score = 0
    st.write("Your Score:")
    score_display = st.empty()  # Create a placeholder for the score

    for i, question in enumerate(questions, start=1):
        display_question(question, i)
        user_answer = st.text_input(f"Your answer for question {i}:", key=f"answer_{i}").strip().upper()
        if user_answer == question["answer"]:
            st.write("Correct!\n")
            score += 1
        else:
            st.write(f"Wrong! The correct answer is {question['answer']}\n")

        # Update the score as you go through the questions
        score_display.text(f"Your Score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
