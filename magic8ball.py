import flet as ft

import random
 
def main(page: ft.Page):
 
    page.title = "Magic 8 Ball"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
 
    inputBox = ft.TextField(

        label="Ask your question",

        width=300

    )
 
    imageList = [
'https://www.nicepng.com/png/full/311-3114888_m8nyofo-magic-8-ball-you-may-rely.png',
                     'https://image.pngaaa.com/737/475737-middle.png',
                     'https://thumbs.dreamstime.com/b/magic-ball-prediction-no-isolated-white-background-148813760.jpg',
                     'https://hackster.imgix.net/uploads/attachments/1229765/_FwftWvFVPi.blob?auto=compress&w=900&h=675&fit=min&fm=jpg%27',
                     'https://cdn.britannica.com/82/191982-050-1DF10DB5/ball.jpg',
                     'https://media.istockphoto.com/id/1133544328/photo/magic-8-ball-with-prediction-404-error-isolated-on-white-background.jpg?s=612x612&w=0&k=20&c=KCf2gXstH2YeSIuiSv_Cpf-Itu3AAgUBt8HkxP4g9Ro=%27'
    ]
 
    randomImage = ft.Image(

        src="1.jpg",

        width=400,

        height=400,

    )
 
    resultText = ft.Text("")
 
    def changeImage(e):

        if inputBox.value != "":

            number = random.randint(0, 5)

            randomImage.src = imageList[number]

            resultText.value = "Number: " + str(number + 1)

        else:

            resultText.value = "Ask a question first!"

        page.update()
 
    def reset(e):

        randomImage.src = "1.jpg"

        resultText.value = ""

        inputBox.value = ""

        page.update()
 
    askButton = ft.ElevatedButton(

        content=ft.Text("ASK"),

        on_click=changeImage

    )
 
    resetButton = ft.ElevatedButton(

        content=ft.Text("RESET"),

        on_click=reset

    )
 
    page.add( inputBox, randomImage, resultText, askButton, resetButton )
 
ft.app(target=main, assets_dir="assets")
 