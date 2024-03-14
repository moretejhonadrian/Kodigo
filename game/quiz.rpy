init:
    $ question_num = 0
    $ score = 0
    $ timer_range = 0
    $ timer_jump = 0
    $ paused_time = 0
    $ time = 12

image halfblack = "#00000088"

init python:
    import json
    import random
    import subprocess

    def is_subprocess_finished(process):
        return process.poll() is not None

    def set_quiz(quiz):
        global current_quiz
        current_quiz = quiz

    def set_quiz_type(type):
        global quiz_type
        quiz_type  = type

    def get_notes():
        with open(f"D:/renpy-8.1.3-sdk/kodigo/game/python/docs/{current_quiz}.txt", 'r') as file:
            notes = file.readlines()
        return notes

    def get_quiz():
        global questions
        global options #already randomized and correct answer provided
        global answers   #letters
        global answers_word

        with open(f"D:/renpy-8.1.3-sdk/kodigo/game/python/quizzes/OS Fundamentals.json", 'r') as file:
            quiz = json.load(file)

        questions = []
        options = []
        answers = []
        answers_word = []

        temp_questions = quiz["Questions"]
        temp_options = quiz["Options"]
        temp_answers = []
        temp = quiz["Answers"]

        for i in range(len(temp_questions)):
            temp_answers.append(None)

        for i in range(len(temp_questions)):
            if temp_options[i] != None: #skip those for now
                temp_options[i].append(temp[i])
                random.shuffle(temp_options[i])

                index = temp_options[i].index(temp[i])

                if index == 0:
                    temp_answers[i] = 'A'
                elif index == 1:
                    temp_answers[i] = 'B'
                elif index == 2:
                    temp_answers[i] = 'C'
                else:
                    temp_answers[i] = 'D'

        max = 0
        n = len(temp_questions)
        n_list = []

        while max != 15:
            rand = random.randrange(0, n)
            if rand not in n_list and temp_options[rand] != None:
                n_list.append(rand)

                answers.append(temp_answers[rand])
                questions.append(temp_questions[rand])
                options.append(temp_options[rand])
                answers_word.append(temp[rand])
                max += 1

    def exit_quiz():
        if quiz_type == "standard":
            renpy.show_screen("standard_quizzes")

screen quiz_instructions:
    tag menu
    add "bg roomnight"

    imagebutton auto "images/Button/exit_%s.png" action ShowMenu("minigame"):
        xalign 0.97
        yalign 0.06

    frame:
        xpadding 40
        ypadding 50
        xalign 0.5
        yalign 0.6
        background "#D9D9D9"

        vbox:
            spacing 25

            text "Program Quiz Protocol":
                style "minigame_title_font"
                color "#000000"
                xalign 0.5
                yalign 0.5

            text "Objective: Engage in an academic and entertaining\n challenge about Computer Science Concepts in a quiz format.":
                color "#000000"
                font "Inter-Bold.ttf"
                size 40
            text "Gameplay:\n• Use the mouse to navigate through the quiz interface.\n• Click on your chosen answers for each multiple-choice question presented.\n• Click on buttons or tabs to access AI-generated hints or explanations.\n• Navigate between different quiz categories or user-generated quizzes by\n clicking on respective options.\n• Review your progress, check answers, and navigate through different quiz\n sections by clicking on appropriate icons/buttons.":
                color "#000000"
                font "Inter-Regular.ttf"
                size 32

            imagebutton auto "images/Button/play_%s.png" action ShowMenu("program_quiz_protocol"):
                xalign 0.5
                yalign 0.5

screen program_quiz_protocol():
    tag menu
    add "bg quiz main"

    add "quiz title":
        yalign 0.2
        xalign 0.5

    imagebutton auto "images/Minigames Menu/exit_%s.png" action ShowMenu("minigame"):
        xalign 0.86
        yalign 0.04

    imagebutton auto "images/Button/standard_quiz_%s.png" action ShowMenu("standard_quizzes"):
        yalign 0.55
        xalign 0.5
    imagebutton auto "images/Button/custom_quiz_%s.png": #tbd #action Jump("custom_quizzes"):
        yalign 0.7
        xalign 0.5


    #$ process = subprocess.Popen(["D:/renpy-8.1.3-sdk/kodigo/game/python/python.exe", "D:/renpy-8.1.3-sdk/kodigo/game/python/MCQ.py"]) #this works
    #, creationflags=subprocess.CREATE_NO_WINDOW

    # Check if the subprocess has finished
    #while not is_subprocess_finished(process):
    #    pause 0.1

screen standard_quizzes():
    $ hide_s("question_dull")
    tag menu
    add "bg quiz main"

    imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("standard_quizzes"), ShowMenu("program_quiz_protocol")]:
        xalign 0.86
        yalign 0.04

    text "QU/ZZES":
        font "Copperplate Gothic Thirty-Three Regular.otf"
        size 92
        color "#FFFFFF"
        xalign 0.5
        yalign 0.15

    frame:
        xalign 0.25
        yalign 0.36
        xpadding 40
        ypadding 40
        xsize 435
        ysize 240
        background "#D9D9D9"

        vbox:
            xalign 0.5
            yalign 0.5
            text "#1 OS Fundamentals":
                font "Copperplate Gothic Thirty-Three Regular.otf"
                size 23
                color "#000000"
                xalign 0.5
                yalign 0.5
            imagebutton auto "images/Button/quiz_play_%s.png" action [Function(set_quiz, "OS Fundamentals"), Jump("init_quiz"), Function(set_quiz_type, "standard")]:
                yoffset 20
            imagebutton auto "images/Button/notes_%s.png" action [ShowMenu("display_notes"), Function(set_quiz, "OS Fundamentals"), Function(set_quiz_type, "standard")]:
                yoffset 10

screen display_notes():
    add "bg quiz main"

    $ notes = get_notes()

    imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("display_notes"), ShowMenu("standard_quizzes")]:
        xalign 0.86
        yalign 0.04

    text current_quiz:
        font "Copperplate Gothic Bold Regular.ttf"
        size 35
        color "#FFFFFF"
        xalign 0.5
        yalign 0.15

    frame:
        xalign 0.5
        yalign 0.55
        xsize 1263
        ysize 626
        background "#D9D9D9"

        vpgrid:
            cols 1
            scrollbars "vertical"
            spacing 5
            mousewheel True

            vbox:
                for note in notes:
                    text note style "notes_style"

    imagebutton auto "images/Button/play_%s.png" action [Hide("display_notes"), Jump("init_quiz")]:
        xalign 0.98
        yalign 0.98

style notes_style:
    font "KronaOne-Regular.ttf"
    #justify True
    size 24
    color "#303031"

label init_quiz:
    with fade
    show bg quiz main

    $ time = 12
    $ question_num = 0

    $ get_quiz()

    screen ready:
        modal True
        imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("ready"), ShowMenu("standard_quizzes")]:
            xalign 0.86
            yalign 0.04

        text "READY...":
            style "init_quiz_font"
            xalign 0.5
            yalign 0.48

        timer 1.0 action [Hide("ready"), Show("one")]

    screen one:
        imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("one"), ShowMenu("standard_quizzes")]:
            xalign 0.86
            yalign 0.04

        text "1...":
            style "init_quiz_font"
            xalign 0.5
            yalign 0.48

        timer 1.0 action [Hide("one"), Show("two")]

    screen two:
        imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("two"), ShowMenu("standard_quizzes")]:
            xalign 0.86
            yalign 0.04

        text "2...":
            style "init_quiz_font"
            xalign 0.5
            yalign 0.48

        timer 1.0 action [Hide("two"), Show("three")]

    screen three:
        imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("three"), ShowMenu("standard_quizzes")]:
            xalign 0.86
            yalign 0.04

        text "3...":
            style "init_quiz_font"
            xalign 0.5
            yalign 0.48

        timer 1.0 action [Hide("three"), Show("go")]

    screen go:
        imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("go"), ShowMenu("standard_quizzes")]:
            xalign 0.86
            yalign 0.04

        text "GO!":
            style "init_quiz_font"
            xalign 0.5
            yalign 0.48

        timer 1.0 action [Hide("go"), Call("quiz_proper")]

    call screen ready with dissolve

style init_quiz_font:
    font "Copperplate Gothic Thirty-Three Regular.otf"
    size 87
    color "#FFFFFF"

label quiz_proper:
    $ timer_range = 12
    $ timer_jump = 'wrong'

    show screen countdown
    call screen question

    screen countdown:
        timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
        $ current_time = int(time)
        image "images/Minigames Menu/timer/[current_time].png" xalign 0.85 yalign 0.85

    screen question():
        $ show_s("question_dull")
<<<<<<< HEAD
        imagebutton auto "images/Button/pause_quiz_%s.png" action [Hide("question"), Hide("countdown"), Show("paused_menu")]: #action pending
=======
        imagebutton auto "images/Button/pause_quiz_%s.png" action [Hide("countdown"), Show("paused_menu")]: #action pending
>>>>>>> dd2e81a7bae36b0a6dfce12ce133b5042a8ab5b9
            xalign 0.86
            yalign 0.04

        frame:
            xalign 0.5
            yalign 0.15
            xsize 1241
            ysize 163
            background "#D9D9D9"

            $ number = question_num + 1

            text "[number]. " + questions[question_num]:
                font "Copperplate Gothic Bold Regular.ttf"
                xalign 0.5
                yalign 0.5

        style_prefix "mytext"

        imagebutton auto "images/Button/choice_%s.png" action If(answers[question_num] == 'A', Jump("right"), Jump("wrong")):
            yalign 0.39
            xalign 0.5

        textbutton "A. " + options[question_num][0]:
            action If(answers[question_num] == 'A', Jump("right"), Jump("wrong"))

            yalign 0.4
            xalign 0.5

        imagebutton auto "images/Button/choice_%s.png" action If(answers[question_num] == 'B', Jump("right"), Jump("wrong")):
            yalign 0.5
            xalign 0.5

        textbutton "B. " + options[question_num][1]:
            action If(answers[question_num] == 'B', Jump("right"), Jump("wrong"))

            yalign 0.5
            xalign 0.5

        imagebutton auto "images/Button/choice_%s.png" action If(answers[question_num] == 'C', Jump("right"), Jump("wrong")):
            yalign 0.612
            xalign 0.5

        textbutton "C. " + options[question_num][2]:
            action If(answers[question_num] == 'C', Jump("right"), Jump("wrong"))

            yalign 0.6
            xalign 0.5

        imagebutton auto "images/Button/choice_%s.png" action If(answers[question_num] == 'D', Jump("right"), Jump("wrong")):
            yalign 0.712
            xalign 0.5

        textbutton "D. " + options[question_num][3]:
            action If(answers[question_num] == 'D', Jump("right"), Jump("wrong"))

            yalign 0.7
            xalign 0.5


style mytext_button_text:
    background None
    insensitive_color "#000000"
    color "#000000"
    hover_color "#545454"
    selected_color "#000000"
    font "Copperplate Gothic Thirty-Three Regular.otf"  # Font size
    left_margin 5
    top_margin 10
    size 23

screen paused_menu():
    $ paused_time = int(time)
    image "images/Minigames Menu/timer/[paused_time].png" xalign 0.85 yalign 0.85
    add "halfblack"

    imagebutton auto "images/Button/pause_quiz_%s.png" action [Hide("paused_menu"), Jump("quiz_proper")]:
        xalign 0.86
        yalign 0.04
    frame:
        xalign 0.82
        yalign 0.136
        xsize 489
        ysize 421
        background "#757274"

        vbox:
            xalign 0.5
            yalign 0.5
            imagebutton auto "images/Button/continue_quiz_%s.png" action [Hide("paused_menu"), Jump("quiz_proper")]:
                xalign 0.5
                yalign 0.5
            imagebutton auto "images/Button/exit_quiz_%s.png" action [Hide("paused_menu"), Hide("question"), ShowMenu("standard_quizzes")]:
                xalign 0.5
                yalign 0.5
                yoffset 20


screen paused:
    image "images/Minigames Menu/timer/[paused_time].png" xalign 0.85 yalign 0.85

label right:
    hide screen countdown
    $ paused_time = int(time)
    show screen paused
    $ show_s("question_dull")
    show halfblack
    show mc happy_uniform at left

    $ score += 1

    "Your answer is correct!"

    hide mc
    hide halfblack
    hide screen paused
    jump next_question

label wrong:
    hide screen countdown
    show screen paused
    $ paused_time = int(time)
    $ show_s("question_dull")
    show halfblack
    show mc sad_uniform at left

    $ letter = answers[question_num]
    $ answer = answers_word[question_num]

    "Your answer is wrong."
    "The correct answer is [letter]. [answer]."

    hide mc
    hide halfblack
    hide screen paused
    jump next_question

label next_question:
    $ question_num += 1

    if question_num == 15:
        $ question_num = 0
        jump results

    $ time = 12
    jump quiz_proper

label results:
    hide screen countdown
    $ hide_s("question_dull")
    "Your score is [score]!"
    call screen standard_quizzes

screen question_dull:
    imagebutton auto "images/Button/pause_quiz_%s.png": #action pending
        xalign 0.86
        yalign 0.04

    frame:
        xalign 0.5
        yalign 0.15
        xsize 1241
        ysize 163
        background "#D9D9D9"

        $ number = question_num + 1

        text "[number]. " + questions[question_num]:
            font "Copperplate Gothic Bold Regular.ttf"
            xalign 0.5
            yalign 0.5

    style_prefix "mytext"

    imagebutton auto "images/Button/choice_%s.png":
        yalign 0.39
        xalign 0.5

    textbutton "A. " + options[question_num][0]:
        yalign 0.4
        xalign 0.5

    imagebutton auto "images/Button/choice_%s.png":
        yalign 0.5
        xalign 0.5

    textbutton "B. " + options[question_num][1]:
        yalign 0.5
        xalign 0.5

    imagebutton auto "images/Button/choice_%s.png":
        yalign 0.612
        xalign 0.5

    textbutton "C. " + options[question_num][2]:
        yalign 0.6
        xalign 0.5

    imagebutton auto "images/Button/choice_%s.png":
        yalign 0.712
        xalign 0.5

    textbutton "D. " + options[question_num][3]:
        yalign 0.7
        xalign 0.5
