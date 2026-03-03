from IPython.display import HTML
import json


class MCQ:
    """A class to hold the definitions of a multiple choice quiz."""

    div_counter = 0  # class based counter for divs to avoid id collision on the images to be moved around if multiple quizzes

    def __init__(
        self, question: str, option_dict: dict, check_selected_only=True
    ) -> str:
        """creates a html/ javascript multiple choice quiz

        Args:
            question (str): A string based question that the multiple choice options will refer to
            option_dict (dict): A list of dictionary items showing the options, if they are correct and any optional feedback
            check_selected_only (bool, optional): A boolean flag as to whether only ticked items should be marked or all items. Defaults to True.

        Returns:
            str: html/javascript combination for rendering the quiz
        """
        self.question = json.dumps(question)
        self.options = json.dumps(option_dict)
        self.CSO = json.dumps(check_selected_only)
        MCQ.div_counter += 1

    def quiz(self):
        quiz = f"quiz-container-{MCQ.div_counter}"
        html = f"""
        <style>
        #{quiz} {{
            font-family: Arial, sans-serif;
        }}

        .form-check {{
            margin-bottom: 10px;
            padding: 10px;
            border-radius: 5px;
        }}

        .is-correct {{
            border: 2px solid #198754;
            background-color: #d1e7dd;
            color: #0f5132;
        }}

        .is-incorrect {{
            border: 2px solid #dc3545;
            background-color: #f8d7da;
            color: #842029;
        }}

        .feedback {{
            margin-top: 5px;
            font-size: 14px;
        }}

        .correct {{
            color: #198754;
        }}

        .incorrect {{
            color: #dc3545;
        }}

        .quiz-button {{
            margin-top: 15px;
            padding: 8px 15px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }}

        .quiz-button:hover {{
            background-color: #0056b3;
        }}
        </style>

        <div id="{quiz}"></div>

        <script>
        (function() {{
        const quizQuestion = {self.question};
        const quizData = {self.options};
        const CHECK_SELECTED_ONLY = {self.CSO};

        const container = document.getElementById('{quiz}');
        const form = document.createElement('form');
        form.id = 'quizForm';

        const intro = document.createElement('div');
        intro.innerHTML = quizQuestion;
        container.appendChild(intro);

        quizData.forEach((item, index) => {{
            const formCheck = document.createElement('div');
            formCheck.className = 'form-check';

            const input = document.createElement('input');
            input.className = 'form-check-input';
            input.type = 'checkbox';
            input.name = `{quiz}-answer-${{index}}`;
            input.id = `{quiz}-answer-${{index}}`;
            input.dataset.correct = item.correct;

            const label = document.createElement('label');
            label.className = 'form-check-label';
            label.htmlFor = `{quiz}-answer-${{index}}`;
            label.textContent = item.text;

            const feedback = document.createElement('div');
            feedback.className = 'feedback';
            feedback.id = `{quiz}-feedback-${{index}}`;

            formCheck.appendChild(input);
            formCheck.appendChild(label);
            formCheck.appendChild(feedback);
            form.appendChild(formCheck);
        }});

        const button = document.createElement('button');
        button.type = 'submit';
        button.className = 'quiz-button';
        button.textContent = 'Check Answers';
        form.appendChild(button);

        container.appendChild(form);

        form.addEventListener('submit', function (e) {{
            e.preventDefault();

            form.querySelectorAll('.form-check').forEach(div => {{
            div.classList.remove('is-correct', 'is-incorrect');
            }});

            quizData.forEach((item, index) => {{
            const checkbox = document.querySelector(`#{quiz}-answer-${{index}}`);
            const feedback = document.querySelector(`#{quiz}-feedback-${{index}}`);
            const parent = checkbox.closest('.form-check');

            const isChecked = checkbox.checked;
            const isCorrect = checkbox.dataset.correct === "true";
            if (CHECK_SELECTED_ONLY) {{ 
            if (isChecked) {{ 
                let message = isCorrect === isChecked ? "✅ Correct" : "❌ Incorrect";

                if (isCorrect === isChecked && item.feedbackCorrect) {{
                message += ` — ${{item.feedbackCorrect}}`;
                }} else if (isCorrect !== isChecked && item.feedbackIncorrect) {{
                message += ` — ${{item.feedbackIncorrect}}`;
                }}

                feedback.textContent = message;
                parent.classList.add(isCorrect === isChecked ? 'is-correct' : 'is-incorrect');
            }} else {{
                feedback.textContent = '';
            }}
            }} else {{ 
            let message = isCorrect === isChecked ? "✅ Correct" : "❌ Incorrect";

            if (isCorrect === isChecked && item.feedbackCorrect) {{
                message += ` — ${{item.feedbackCorrect}}`;
            }} else if (isCorrect !== isChecked && item.feedbackIncorrect) {{
                message += ` — ${{item.feedbackIncorrect}}`;
            }}

            feedback.textContent = message;
            parent.classList.add(isCorrect === isChecked ? 'is-correct' : 'is-incorrect');
            }}
            }});
        }});
        }})();
        </script>
        """
        return HTML(html)


def mcq_1():
    """Creates a simple mcq question.  The question text is defined and then the options_dict is defined as a list of dictionary
    objects. For each option provide a text for the option and a boolean value to the correct field indicating if the answer is correct
    There are optional feedbackCorrect and feedbackIncorrect fields that can be defined for feedback displayed on submission.
    When we create the quiz we can also pass an optional third boolean argument as to whether to mark only options that are ticked as true (default)
    or show feedback on all options

    Returns:
        HTML:HTML rendering of the quiz
    """

    question = "<p><strong>Select the correct answers about the Python Language (more than one answer may be correct)</strong><p>"

    options_dict = [
        {
            "text": "Python is the fastest coding language",
            "correct": False,
            "feedbackIncorrect": "Python is not the fastest — precompiled languages like C or Rust are generally faster.",
        },
        {
            "text": "Python is a great language to start with",
            "correct": True,
            "feedbackCorrect": "Yes! Python's simple syntax makes it a great first language.",
        },
        {
            "text": "Python was developed in the 1980s",
            "correct": True,
            "feedbackCorrect": "Correct — Python was conceived in the late 1980s by Guido van Rossum.",
        },
    ]

    quiz = MCQ(question, options_dict)
    return quiz.quiz()


def mcq_2():
    """Creates a simple mcq question.  The question text is defined and then the options_dict is defined as a list of dictionary
    objects. In this case we have defined some code for inspection. use the syntax below so your code displays correctly with indentation.
    For each option provide a text for the option and a boolean value to the correct field indicating if the answer is correct
    There are optional feedbackCorrect and feedbackIncorrect fields that can be defined for feedback displayed on submission.
    When we create the quiz we can also pass an optional third boolean argument as to whether to mark only options that are ticked as true (default)
    or show feedback on all options

    Returns:
    HTML:HTML rendering of the quiz
    """

    question = """
<p>Analyse the following code and select the two correct answers
<pre>
<code>
for i in range(10):
    if i % 2 == 1:
        print(f"{i} is odd")
    else:
        print(f"{i} is even")
</code></pre></p>
"""

    options_dict = [
        {
            "text": "in the for loop i takes on integers between 1 and 10",
            "correct": False,
            "feedbackIncorrect": "Remember the default start for the range object is 0 and the stop position is NOT included",
        },
        {
            "text": "in the for loop i takes on integers between 0 and 9",
            "correct": True,
            "feedbackCorrect": "Yes! The range objects default start is 0 and stop is not included",
        },
        {
            "text": "The % operator shows the remainder after division",
            "correct": True,
            "feedbackCorrect": "Correct in this code we look at the remainder after division by 2 - an odd number will always have remainder 1",
        },
    ]

    quiz = MCQ(question, options_dict, True)
    return quiz.quiz()
