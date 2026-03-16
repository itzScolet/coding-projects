import flet as ft
import random
 
def main(page: ft.Page):
 
    page.title = "Cartoon Trivia"
 
    hint_used = False
    answered = False
    question_number = 0
    score = 0
 
    option1 = None
    option2 = None
    option3 = None
    option4 = None
    next_button = None
 
    questions = [
 
    [
    "Which cartoon features Finn and Jake?",
    ["Adventure Time","images/adventuretimes.png"],
    ["Gumball","images/gumball.png"],
    ["Samurai Jack","images/Samurai Jack's.png"],
    ["Teen Titans Go","images/teentitansgo.png"],
    "Adventure Time"
    ],
 
    [
    "Which cartoon has a mysterious glowing train?",
    ["Infinity Train","images/infinitytrain.png"],
    ["Gumball","images/gumball.png"],
    ["Ben 10","images/Ben 10.png"],
    ["Adventure Time","images/adventuretimes.png"],
    "Infinity Train"
    ],
 
    [
    "Which cartoon features a boy with an alien watch?",
    ["Ben 10","images/Ben 10.png"],
    ["Gumball","images/gumball.png"],
    ["Samurai Jack","images/Samurai Jack's.png"],
    ["Teen Titans Go","images/teentitansgo.png"],
    "Ben 10"
    ],
 
    [
    "Which cartoon follows a samurai fighting Aku?",
    ["Samurai Jack","images/Samurai Jack's.png"],
    ["Adventure Time","images/adventuretimes.png"],
    ["Ben 10","images/Ben 10.png"],
    ["Gumball","images/gumball.png"],
    "Samurai Jack"
    ],
 
    [
    "Which cartoon has a blue cat named Gumball?",
    ["Gumball","images/gumball.png"],
    ["Ben 10","images/Ben 10.png"],
    ["Adventure Time","images/adventuretimes.png"],
    ["Teen Titans Go","images/teentitansgo.png"],
    "Gumball"
    ],
 
    [
    "Which cartoon has Raven and Beast Boy?",
    ["Teen Titans Go","images/teentitansgo.png"],
    ["Ben 10","images/Ben 10.png"],
    ["Adventure Time","images/adventuretimes.png"],
    ["Gumball","images/gumball.png"],
    "Teen Titans Go"
    ],
 
    [
    "Which cartoon includes Bugs Bunny?",
    ["Looney Tunes","images/Looney Tunes.png"],
    ["Tom and Jerry","images/tomyjerry.png"],
    ["Scooby Doo","images/scoobydooo.png"],
    ["Gumball","images/gumball.png"],
    "Looney Tunes"
    ],
 
    [
    "Which cartoon has a dog solving mysteries?",
    ["Scooby Doo","images/scoobydooo.png"],
    ["Ben 10","images/Ben 10.png"],
    ["Gumball","images/gumball.png"],
    ["Adventure Time","images/adventuretimes.png"],
    "Scooby Doo"
 
    ],
    [
    "Which cartoon has a team of superheroes including Robin, Starfire, Raven, Beast Boy, and Cyborg?",
    ["Teen Titans","images/teentitans.png"],
    ["Ben 10","images/Ben 10.png"],
    ["The Amazing World of Gumball","images/gumball.png"],
    ["Scooby Doo","images/scoobydooo.jpeg"],
    "Teen Titans"
    
    ],
    [
    "Which cartoon features Tom chasing Jerry?",
    ["Tom and Jerry","images/tomyjerry.png"],
    ["Looney Tunes","images/Looney Tunes.png"],
    ["Scooby Doo","images/scoobydoo.png"],
    ["Ben 10","images/Ben 10.png"],
    "Tom and Jerry"
    ]
 
    ]
 
    def welcome(e):
        random.shuffle(questions)
        page.controls.clear()
 
        page.add(
            ft.Text("Cartoon Trivia", size=34, weight="bold"),
            ft.ElevatedButton("Start Quiz", on_click=show_question)
        )
 
        page.update()
 
    def use_hint(e):
        nonlocal hint_used
 
        if hint_used or answered:
            return
 
        correct = questions[question_number][5]
 
        wrong_buttons = []
 
        for btn in [option1, option2, option3, option4]:
            if btn and btn.visible and btn.data != correct:
                wrong_buttons.append(btn)
 
        remove = random.sample(wrong_buttons, min(2, len(wrong_buttons)))
 
        for btn in remove:
            btn.visible = False
 
        hint_used = True
        page.update()
 
    def answer(e):
        nonlocal score, answered
 
        if answered:
            return
 
        answered = True
 
        selected = e.control.data
        correct = questions[question_number][5]
 
        
        correct_image = None
        for i in range(1,5):
            if questions[question_number][i][0] == correct:
                correct_image = questions[question_number][i][1]
 
        if selected == correct:
            score += 1
            result_text = ft.Text(" Correct!", size=20, color="green")
        else:
            result_text = ft.Text(f" Wrong! Correct answer: {correct}", size=20, color="red")
 
        result_image = ft.Image(src=correct_image, width=150)
 
        page.add(result_text, result_image)
 
        if next_button:
            next_button.disabled = False
 
        page.update()
 
    def next_question(e):
        nonlocal question_number
 
        question_number += 1
 
        if question_number >= len(questions):
            results(None)
        else:
            show_question(None)
 
    def show_question(e):
        nonlocal option1, option2, option3, option4, hint_used, answered, next_button
 
        hint_used = False
        answered = False
 
        page.controls.clear()
 
        q = ft.Text(questions[question_number][0], size=22)
 
        img1 = ft.Image(src=questions[question_number][1][1], width=120)
        img2 = ft.Image(src=questions[question_number][2][1], width=120)
        img3 = ft.Image(src=questions[question_number][3][1], width=120)
        img4 = ft.Image(src=questions[question_number][4][1], width=120)
 
        option1 = ft.ElevatedButton(questions[question_number][1][0], data=questions[question_number][1][0], on_click=answer)
        option2 = ft.ElevatedButton(questions[question_number][2][0], data=questions[question_number][2][0], on_click=answer)
        option3 = ft.ElevatedButton(questions[question_number][3][0], data=questions[question_number][3][0], on_click=answer)
        option4 = ft.ElevatedButton(questions[question_number][4][0], data=questions[question_number][4][0], on_click=answer)
 
        col1 = ft.Column([img1, option1])
        col2 = ft.Column([img2, option2])
        col3 = ft.Column([img3, option3])
        col4 = ft.Column([img4, option4])
 
        hint_button = ft.ElevatedButton("Hint", on_click=use_hint)
        next_button = ft.ElevatedButton("Next", disabled=True, on_click=next_question)
 
        page.add(
            q,
            ft.Row([col1, col2]),
            ft.Row([col3, col4]),
            hint_button,
            next_button
        )
 
        page.update()
 
    def results(e):
        page.controls.clear()
 
        page.add(
            ft.Text("Quiz Finished!", size=30),
            ft.Text(f"Final Score: {score} / {len(questions)}", size=24),
            ft.ElevatedButton("Restart Quiz", on_click=restart)
        )
 
        page.update()
 
    def restart(e):
        nonlocal question_number, score
 
        question_number = 0
        score = 0
        welcome(None)
 
    welcome(None)
 
ft.app(target=main, assets_dir = "assets")