"""
things to fix:
    1. polish quiz ui
    2. integrate ai
    3. fix assets
    4. add toolkits
    5. add comments
    6. if possible, add mini text editor
"""

init:
    $ question_num = 0
    $ score = 0
    $ timer_range = 0
    $ timer_jump = 0
    $ paused_time = 0
    $ time = 12
    $ base_path = ""

    $ quiz_title = "Quiz" #for uploading quiz

    $ timeout = 12 # Sets how long in seconds the user has to make a choice
    $ timeout_label = 'wrong'

    #bkt
    $ L  = 0.1 #initial probability that the student already knew a skill
    $ T = 0.1 #pprobability that the student will learn a skill on the next practice opportunity
    $ S = 0.1 #probability that the student will answer incorrectly despite knowing a skill
    $ G = 0.3 #that the student will answer correctly despite not knowing a skill
    $ A = 0 #action
    $ mastery_threshold = 0.8


image halfblack = "#00000088"

init python:
    import json
    import random
    import subprocess
    import os

    base_path = os.getcwd()

    def get_text(quiz_notes):
        file_path = get_path(f"kodigo/game/python/docs/{quiz_notes}.txt")
        with open(file_path, 'r') as file:
            # Read the entire file contents into a string
            texts = file.read()

        return texts

    def set_bool(b):
        global bool
        bool = b

    def terminate(process):
        process.terminate()

    def get_path(relative_path):
        return os.path.join(base_path, relative_path)

    def is_subprocess_finished(process):
        return process.poll() is not None

    def get_quiz_record():
        global quiz_record #for all for now
        quiz_record = {} #put this somewhere else

        file_path = get_path(f"kodigo/game/python/quizzes/q_records.json")

        with open(file_path, 'r') as file:
            quiz_record = json.load(file)

    def set_quiz(quiz):
        global current_quiz
        current_quiz = quiz

        #put this somwhere else
        # Check if current_quiz is not already a key in the dictionary
        if current_quiz not in quiz_record["standard"]:
            # Add current_quiz as a key and initialize its value as an empty list
            quiz_record["standard"][current_quiz] = {'records': [], 'mastery': []}
            save_quiz_record()

    def set_quiz_type(type):
        global quiz_type
        quiz_type  = type

    def get_notes(quiz_notes):
        file_path = get_path(f"kodigo/game/python/docs/{quiz_notes}.txt")
        with open(file_path, 'r') as file:
            notes = file.readlines()
        return notes

    def get_quiz():
        global questions
        global options #already randomized and correct answer provided
        global answers   #letters
        global answers_word

        file_path = get_path(f"kodigo/game/python/quizzes/OS Fundamentals.json")
        with open(file_path, 'r') as file:
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

    def save_quiz_record():
        file_path = get_path(f"kodigo/game/python/quizzes/q_records.json")
        with open(file_path, "w") as json_file:
            json.dump(quiz_record, json_file)

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

    $ get_quiz_record()

    add "quiz title":
        yalign 0.2
        xalign 0.5

    imagebutton auto "images/Minigames Menu/exit_%s.png" action ShowMenu("minigame"):
        xalign 0.86
        yalign 0.04

    imagebutton auto "images/Button/standard_quiz_%s.png" action ShowMenu("standard_quizzes"):
        yalign 0.55
        xalign 0.5
    imagebutton auto "images/Button/custom_quiz_%s.png"action ShowMenu("custom_quizzes"):
        yalign 0.7
        xalign 0.5

    #$ process = subprocess.Popen(["D:/renpy-8.1.3-sdk/kodigo/game/python/python.exe", "D:/renpy-8.1.3-sdk/kodigo/game/python/MCQ.py"]) #this works
    #, creationflags=subprocess.CREATE_NO_WINDOW

    # Check if the subprocess has finished
    #while not is_subprocess_finished(process):
    #    pause 0.1

screen custom_quizzes:
    tag menu
    add "bg quiz main"

    imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("custom_quizzes"), ShowMenu("program_quiz_protocol")]:
        xalign 0.86
        yalign 0.04

    text "QU/ZZES":
        font "Copperplate Gothic Thirty-Three Regular.otf"
        size 92
        color "#FFFFFF"
        xalign 0.5
        yalign 0.15

    if len(quiz_record["custom"]) == 0:
        text "No quiz available.":
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 60
            color "#FFFFFF"
            xalign 0.25
            yalign 0.3

    imagebutton auto "images/Button/create_quiz_%s.png" action ShowMenu("create_quiz"):
        xalign 0.5
        yalign 0.8

screen create_quiz:
    tag menu
    add "bg quiz main"

    imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("create_quiz"), Jump("upload_warning")]:
        xalign 0.86
        yalign 0.04

    $ file_path = get_path(f"kodigo/game/python/docs/{quiz_title}.txt")

    if os.path.exists(file_path):
        $ notes = get_notes(quiz_title)

    text "Notes":
        font "Copperplate Gothic Thirty-Three Regular.otf"
        size 48
        color "#FFFFFF"
        xalign 0.324
        yalign 0.15

    frame:
        xalign 0.25
        yalign 0.5
        xsize 600
        ysize 600
        background "#D9D9D9"

        if os.path.exists(file_path):
            vpgrid:
                cols 1
                scrollbars "vertical"
                spacing 5
                mousewheel True

                vbox:
                    for note in notes:
                        text note style "notes_style"

    if os.path.exists(file_path):
        imagebutton auto "images/Button/summarize_%s.png" action Jump("summarize"):
            xalign 0.28
            yalign 0.85

        vbox:
            xalign 0.9
            yalign 0.4
            imagebutton auto "images/Button/add_%s.png":# action Jump("summarize"):
                xalign 0.28
                yalign 0.85

            imagebutton auto "images/Button/auto_%s.png":# action Jump("summarize"):
                xalign 0.28
                yalign 0.85
            #jump get_keywords

    vbox:
        xalign 0.737
        yalign 0.4

        text "Keywords":
                font "Copperplate Gothic Thirty-Three Regular.otf"
                size 48
                color "#FFFFFF"
                xalign 0.5
                yalign 0.5

        frame:
            xalign 0.25
            yalign 0.5
            xpadding 40
            ypadding 40
            xsize 400
            ysize 400
            background "#D9D9D9"
            yoffset 30

    hbox:
        xalign 0.690
        yalign 0.15

        text "[quiz_title]": #specify with a number later
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 60
            color "#FFFFFF"

        imagebutton auto "images/Button/edit_title_%s.png" action Jump("edit_title"):
            xoffset 40

    if not os.path.exists(file_path):
        imagebutton auto "images/Button/upload_%s.png" action Jump("upload_file"):
            xalign 0.75
            yalign 0.8
    else:
        imagebutton auto "images/Button/upload_%s.png": #no action
            xalign 0.75
            yalign 0.8

label upload_warning:
    #check if quiz_file of the same name don't exist yet then give warning
    # meaning the quiz isn't done yet
    $ file_path = f"kodigo/game/python/quizzes/{quiz_title}.json"

    if not os.path.exists(file_path):
        $ show_s("create_quiz_dull")
        show halfblack
        call screen warning

    screen warning:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 40
            ypadding 40
            xsize 450
            ysize 420
            background "#D9D9D9"

            vbox:
                xalign 0.5
                yalign 0.5

                text f"'{quiz_title}' is not yet created.":
                    font "Copperplate Gothic Thirty-Three Regular.otf"
                    size 50
                    color "#303031"
                    xalign 0.5
                    yalign 0.5
                text "Would you like to exit?":
                    font "Copperplate Gothic Thirty-Three Regular.otf"
                    size 30
                    color "#303031"
                    yoffset 10

                hbox:
                    xalign 0.5
                    yalign 0.5
                    yoffset 50
                    spacing 40

                    imagebutton auto "images/Button/yes_%s.png" action [Hide("warning"), Function(set_bool, True), Jump("warning_2")]
                    imagebutton auto "images/Button/no_%s.png" action [Hide("warning"), Function(set_bool, False), Jump("warning_2")]

    call screen custom_quizzes

label warning_2:
    $ hide_s("create_quiz_dull")
    hide halfblack

    #if player wants to exit
    if bool:
        $ file_path = f"kodigo/game/python/docs/{quiz_title}.txt"

        if os.path.exists(file_path):
            $ os.remove(file_path) # remove notes

        $ quiz_title = "Quiz" #reset

        call screen custom_quizzes with dissolve
    else:
        call screen create_quiz

label edit_title:
    $ show_s("create_quiz_dull")
    hide screen create_quiz

    python:
        old_file_path = get_path(f"kodigo/game/python/docs/{quiz_title}.txt")
        temp = renpy.input("Quiz name:", length=17)
        temp = temp.strip()
        new_file_path = get_path(f"kodigo/game/python/docs/{temp}.txt")

    screen duplicate:
        vbox:
            xalign 0.5
            yalign 0.5
            xsize 1000
            ysize 100
            spacing 5
            text "Can't have multiple quizzes with the same name.":
                font "Copperplate Gothic Thirty-Three Regular.otf"
                size 60
                color "#999999"
                xalign 0.5
                yalign 0.5
            text "Try again.":
                font "Copperplate Gothic Thirty-Three Regular.otf"
                size 60
                color "#999999"
                xalign 0.5
                yalign 0.5

    if os.path.exists(new_file_path):
        show screen duplicate
        pause 2.0
        hide screen duplicate
        $ hide_s("create_quiz_dull")
        call screen create_quiz
    elif os.path.exists(old_file_path):
        $ os.rename(old_file_path, new_file_path)

    $ quiz_title = temp
    $ hide_s("create_quiz_dull")
    call screen create_quiz

label upload_file:
    $ show_s("create_quiz_dull")
    show halfblack
    hide screen create_quiz
    $ python_path = get_path(f"kodigo/game/python/Python311/python.exe") #"C:/Users/Adrian/AppData/Local/Programs/Python/Python311/python.exe"
    $ py_path = get_path(f"kodigo/game/python/upload_file.py")
    $ process = subprocess.Popen([python_path, py_path, quiz_title], creationflags=subprocess.CREATE_NO_WINDOW)

    screen terminate_process:
        imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("terminate_process"), Function(terminate, process)]:
            xalign 0.86
            yalign 0.04

    show screen terminate_process

    #Check if the subprocess has finished
    while not is_subprocess_finished(process):
        show screen processing
        pause 0.1

    screen processing:
        text "Processing document...":
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 60
            color "#FFFFFF"
            xalign 0.5
            yalign 0.5

    hide screen processing

    hide halfblack
    $ hide_s("create_quiz_dull")
    call screen create_quiz

label summarize:
    $ show_s("create_quiz_dull")
    show halfblack
    hide screen create_quiz

    $ notes = get_text(quiz_title)
    $ python_path = get_path(f"kodigo/game/python/Python311/python.exe") #"C:/Users/Adrian/AppData/Local/Programs/Python/Python311/python.exe"
    $ py_path = get_path(f"kodigo/game/python/summarize.py")
    $ process = subprocess.Popen([python_path, py_path, quiz_title, notes], creationflags=subprocess.CREATE_NO_WINDOW)

    screen terminate_process:
        imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("terminate_process"), Function(terminate, process)]:
            xalign 0.86
            yalign 0.04

    show screen terminate_process

    #Check if the subprocess has finished
    while not is_subprocess_finished(process):
        show screen summarizing
        pause 0.1

    screen summarizing:
        text "Summarizing...":
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 60
            color "#FFFFFF"
            xalign 0.5
            yalign 0.5

    hide screen summarizing
    hide halfblack
    $ hide_s("create_quiz_dull")
    call screen create_quiz

#after the player uploads a document, follow it with this, dk if in background though
label get_keywords:
    $ show_s("create_quiz_dull")
    show halfblack
    hide screen create_quiz

    #processes heree....

    "pause"

    hide screen summarizing
    hide halfblack
    $ hide_s("create_quiz_dull")
    call screen create_quiz

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
            imagebutton auto "images/Button/status_%s.png" action [Function(set_quiz, "OS Fundamentals"), ShowMenu("quiz_status"), Function(set_quiz_type, "standard")]:
                yoffset 20
            imagebutton auto "images/Button/notes_%s.png" action [ShowMenu("display_notes"), Function(set_quiz, "OS Fundamentals"), Function(set_quiz_type, "standard")]:
                yoffset 10

screen display_notes():
    add "bg quiz main"

    $ notes = get_notes(current_quiz)

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
    justify True
    size 24
    color "#303031"

label init_quiz:
    $ hide_s("question_dull")
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

        timer 1.0 action [Hide("go"), Show("quiz_proper"), Show("countdown")]

    call screen ready with dissolve

style init_quiz_font:
    font "Copperplate Gothic Thirty-Three Regular.otf"
    size 87
    color "#FFFFFF"

screen countdown():
    if timeout_label is not None:
        bar:
            xalign 0.5
            yalign 0.85
            xsize 740
            value AnimatedValue(old_value=1.0, value=0.0, range=1.0, delay=timeout)
        timer timeout action [SetVariable("timeout", 10), SetVariable("timeout_label", None), Jump(timeout_label)]
## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True
"""
screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    $ current_time = int(time)
    image "images/Minigames Menu/timer/[current_time].png" xalign 0.85 yalign 0.85
    """

screen quiz_proper:
    tag menu
    $ timeout = time # Sets how long in seconds the user has to make a choice
    $ timeout_label = 'wrong' #sets the label that is automatically jumped to if the user makes no choice

    imagebutton auto "images/Button/pause_quiz_%s.png" action [Hide("quiz_proper"), Hide("countdown"), Show("paused_menu")]: #action pending
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

    text "A. " + options[question_num][0]:
        font "Copperplate Gothic Thirty-Three Regular.otf"
        yalign 0.4
        xalign 0.5

    imagebutton auto "images/Button/choice_%s.png" action If(answers[question_num] == 'B', Jump("right"), Jump("wrong")):
        yalign 0.5
        xalign 0.5

    text "B. " + options[question_num][1]:
        font "Copperplate Gothic Thirty-Three Regular.otf"
        yalign 0.5
        xalign 0.5

    imagebutton auto "images/Button/choice_%s.png" action If(answers[question_num] == 'C', Jump("right"), Jump("wrong")):
        yalign 0.612
        xalign 0.5

    text "C. " + options[question_num][2]:
        font "Copperplate Gothic Thirty-Three Regular.otf"
        yalign 0.6
        xalign 0.5

    imagebutton auto "images/Button/choice_%s.png" action If(answers[question_num] == 'D', Jump("right"), Jump("wrong")):
        yalign 0.712
        xalign 0.5

    text "D. " + options[question_num][3]:
        font "Copperplate Gothic Thirty-Three Regular.otf"
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
    modal True
    $ paused_time = int(time)
    $ show_s("question_dull")
    image "images/Minigames Menu/timer/[paused_time].png" xalign 0.85 yalign 0.85
    add "halfblack"

    imagebutton auto "images/Button/pause_quiz_%s.png" action [Hide("paused_menu"), ShowMenu("quiz_proper")]:
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
            imagebutton auto "images/Button/continue_quiz_%s.png" action [Hide("paused_menu"), Hide("question_dull"), ShowMenu("quiz_proper"), Show("countdown")]:
                xalign 0.5
                yalign 0.5
            imagebutton auto "images/Button/exit_quiz_%s.png" action [Hide("paused_menu"), Hide("question_dull"), ShowMenu("standard_quizzes")]:
                xalign 0.5
                yalign 0.5
                yoffset 20

label right:
    hide screen quiz_proper
    $ show_s("question_dull")
    hide screen countdown
    pause 0.5
    show halfblack
    show mc happy_uniform at left

    $ score += 1

    "Your answer is correct!"

    hide mc
    hide halfblack
    hide screen paused
    show screen countdown
    jump next_question

label wrong:
    hide screen quiz_proper
    $ show_s("question_dull")
    hide screen countdown
    pause 0.5
    show halfblack
    show mc sad_uniform at left

    $ letter = answers[question_num]
    $ answer = answers_word[question_num]

    "Your answer is wrong."
    "The correct answer is [letter]. [answer]."

    hide mc
    hide halfblack
    hide screen paused
    show screen countdown
    jump next_question

label next_question:
    $ question_num += 1

    if question_num == 15:
        $ question_num = 0
        jump results

    call screen quiz_proper

label results:
    hide screen countdown
    $ hide_s("question_dull")
    "Your score is [score]!"

    python:
        if score/15 >= 0.7:
            A = (L*(1-S)) / (L*(1-S) + (1-L)*G)
            L = A + (1-A)*T
        else:
            A = (L*S) / ((L*S) + (1-L)*(1-G))
            L = A + (1-A)*T

    $ quiz_record['standard'][current_quiz]['records'].append(score)
    #reset
    $ score = 0
    $ mastery = round(L * 100, 2)
    $ quiz_record['standard'][current_quiz]['mastery'].append(mastery)

    $ save_quiz_record()

    call screen quiz_status

#status of quiz etc
screen quiz_status:
    add "bg quiz main"

    python:
        if len(quiz_record['standard'][current_quiz]['mastery']) == 0:
            mastery = 0
        else:
            mastery = quiz_record['standard'][current_quiz]['mastery'][-1]

    imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("quiz_status"), ShowMenu("standard_quizzes")]: #don't know yet
        xalign 0.86
        yalign 0.04

    text current_quiz:
        font "Copperplate Gothic Bold Regular.ttf"
        size 50
        color "#FFFFFF"
        xalign 0.5
        yalign 0.15

    text "Mastery":
        font "Copperplate Gothic Bold Regular.ttf"
        size 40
        color "#FFFFFF"
        xalign 0.5
        yalign 0.3

    text "[mastery]%":
        font "Copperplate Gothic Bold Regular.ttf"
        size 30
        color "#FFFFFF"
        xalign 0.5
        yalign 0.38

    imagebutton auto "images/Button/retry_%s.png" action [Hide("quiz_status"), Call("init_quiz")]:
        xalign 0.5
        yalign 0.5

    imagebutton auto "images/Button/pass_attempts_%s.png" action [Hide("quiz_status"), ShowMenu("scoreboard")]:
        xalign 0.5
        yalign 0.65

screen scoreboard:
    add "bg quiz main"

    imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("scoreboard"), ShowMenu("standard_quizzes")]: #don't know yet
        xalign 0.86
        yalign 0.04

    text current_quiz:
        font "Copperplate Gothic Bold Regular.ttf"
        size 50
        color "#FFFFFF"
        xalign 0.5
        yalign 0.15

    text "Passed Attempts":
        font "Copperplate Gothic Bold Regular.ttf"
        size 40
        color "#FFFFFF"
        xalign 0.5
        yalign 0.25

    vpgrid:
        cols 1
        mousewheel True
        scrollbars "vertical"
        xalign 0.5
        yalign 0.5
        ysize 450

        vbox:
            spacing 10

            if len(quiz_record['standard'][current_quiz]['records']) == 0:
                text "No records found.":
                    font "Copperplate Gothic Thirty-Three Regular.otf"
                    size 40
                    color "#FFFFFF"
            else:
                text "SCORE               MASTERY       " style "status_style"

                for i in range(len(quiz_record['standard'][current_quiz]['records'])):
                    $ score = quiz_record['standard'][current_quiz]['records'][i]
                    $ mastery = quiz_record['standard'][current_quiz]['mastery'][i]
                    text "      [score]                       [mastery]%        " style "status_style"

    python:
        if len(quiz_record['standard'][current_quiz]['mastery']) == 0:
            mastery = 0
        else:
            mastery = quiz_record['standard'][current_quiz]['mastery'][-1]

    text "[mastery]%" style "status_style":
        xalign 0.5
        yalign 0.8
        yoffset 20

    imagebutton auto "images/Button/play_%s.png" action [Hide("scoreboard"), Jump("init_quiz")]:
        xalign 0.98
        yalign 0.98

style status_style:
    font "Copperplate Gothic Bold Regular.ttf"
    size 30
    color "#FFFFFF"

screen create_quiz_dull:
    add "bg quiz main"

    imagebutton auto "images/Minigames Menu/exit_%s.png":
        xalign 0.86
        yalign 0.04

    $ file_path = get_path(f"kodigo/game/python/docs/{quiz_title}.txt")

    if os.path.exists(file_path):
        $ notes = get_notes(quiz_title)

    text "Notes":
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 48
            color "#FFFFFF"
            xalign 0.324
            yalign 0.15

    frame:
        xalign 0.25
        yalign 0.5
        xsize 600
        ysize 600
        background "#D9D9D9"

        if os.path.exists(file_path):
            vpgrid:
                cols 1
                scrollbars "vertical"
                spacing 5

                vbox:
                    for note in notes:
                        text note style "notes_style"

    if os.path.exists(file_path):
        imagebutton auto "images/Button/summarize_%s.png":
            xalign 0.28
            yalign 0.85

    vbox:
        xalign 0.738
        yalign 0.4

        text "Keywords":
                font "Copperplate Gothic Thirty-Three Regular.otf"
                size 48
                color "#FFFFFF"
                xalign 0.5
                yalign 0.5

        frame:
            xalign 0.25
            yalign 0.5
            xpadding 40
            ypadding 40
            xsize 400
            ysize 400
            background "#D9D9D9"
            yoffset 30


    hbox:
        xalign 0.690
        yalign 0.15

        text "[quiz_title]": #specify with a number later
                font "Copperplate Gothic Thirty-Three Regular.otf"
                size 60
                color "#FFFFFF"

        imagebutton auto "images/Button/edit_title_%s.png": #action [Hide("standard_quizzes"), ShowMenu("program_quiz_protocol")]:
            xoffset 40

    imagebutton auto "images/Button/upload_%s.png": #action [Hide("standard_quizzes"), ShowMenu("program_quiz_protocol")]:
        xalign 0.75
        yalign 0.8

screen question_dull:
    imagebutton auto "images/Button/pause_quiz_%s.png":
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

    text "A. " + options[question_num][0]:
        font "Copperplate Gothic Thirty-Three Regular.otf"
        yalign 0.4
        xalign 0.5

    imagebutton auto "images/Button/choice_%s.png":
        yalign 0.5
        xalign 0.5

    text "B. " + options[question_num][1]:
        font "Copperplate Gothic Thirty-Three Regular.otf"
        yalign 0.5
        xalign 0.5

    imagebutton auto "images/Button/choice_%s.png":
        yalign 0.612
        xalign 0.5

    text "C. " + options[question_num][2]:
        font "Copperplate Gothic Thirty-Three Regular.otf"
        yalign 0.6
        xalign 0.5

    imagebutton auto "images/Button/choice_%s.png":
        yalign 0.712
        xalign 0.5

    text "D. " + options[question_num][3]:
        font "Copperplate Gothic Thirty-Three Regular.otf"
        yalign 0.7
        xalign 0.5
