#all the initializations are in variables_init
#friend_1 = Carlos/Carla
#friend_2 = Justin/Jasmine

init python:
    in_story = False

    def set_gender(selected_gender):
        persistent.gender = selected_gender

        if persistent.gender == "male":
            pronoun_reffered = "he"
            pronoun_belonging = "his"
        else:
            pronoun_reffered = "she"
            pronoun_belonging = "her"

        specify_characters()

    def specify_characters():
        global friend_1
        global friend_2
        if persistent.gender == "male":
            friend_1 = "Carlos"
            friend_2 = "Justin"
        else:
            friend_1 = "Carla"
            friend_2 = "Jasmine"

screen gender_choose:
    image "bg mirror1"
    imagebutton auto "male_%s.png" action Function(lambda: set_gender("male")), Jump("start_2"):
        xalign 0.17
        yalign 0.28

    imagebutton auto "female_%s.png" action Function(lambda: set_gender("female")), Jump("start_2"):
        xalign 0.84
        yalign 0.28

label start:
    with fade
    scene bg disclaimer with Pause(5)
    scene bg frontday

    n "It's been 2 long years since the pandemic wreaked havoc upon the world,
    economies were put on hold, people were confined within their homes, jobs were put on hold and so school transitioned
    from face-to-face classes to online classes."
    n "And now that the pandemic has settled down everything went back to normal,
    so did classes and for some this opened a new chapter in their lives where they get to be in a new environment and meet new people."

    scene bg calendar with Pause(5)
    scene bg alarm_clock with Pause(5)
    scene bg roomday

    show mom happy
    mom "Honey, it's time to wake up!"
    # Character is preparing to stand, looks one’s self in the mirror
    # Proceeds to choosing of name and gender

    hide mom
    show bg mirror with dissolve
    "..."

    $ mc = renpy.input("What is your name?", default="Alex", length=32).capitalize()
    $ mc = mc.strip()
    if mc == "":
        $ mc = "Alex"

    "What is your gender?"
    call screen gender_choose with dissolve

label start_2:
    scene bg room
    show mc neutral_casual
    mc "Yes, ma. I'll be there."

    scene bg table with dissolve
    show mc neutral_casual at left with dissolve
    mc "Ma, what day is it?"
    show mom neutral at right with dissolve
    mom "Well, it's Monday, honey."
    mc "No, like, what's the day of the month is it?"
    mom "Oh, it is June 14. Why? Has something come up?"
    mc "It's nothing, it just feels like there's something I need to do today."
    mc "Ah, nevermind. I'll just enjoy this time of the year, having a rest after a long year."

    # insert text messaging

    hide mc
    hide mom

    scene bg text_messaging
    greg "Yo, [mcname]! Have you seen the result?"
    mc "What result are you talking about?"
    greg "The BUCET result! It's already out. Go check it out already."
    mc "Really?! This must have been why I'm so anxious today. Fine, I'll check it out right away."

    # Checks the result
    # Maybe an email saying congrats

    mc "Gregory, I made it. I'm so happy. But I don't see your name there. Are you not qualified?"
    greg "Yeah, I kinda figured it out. Don't worry, I have a backup school so we might be seeing each other sometime during our college days."
    mc "It feels so bad being happy that I passed but you don't. I was really thinking of the places we'd go there."
    greg "Oh, cheer up [mcname]. Let's look into what we could do for the meantime."
    mc "I gotta tell this to Mommy. Let's go out later tonight to celebrate, shall we?"
    greg "Yeah, that'll be fun! I'll see you tonight, [mcname]. Bye."

    # ends the text messaging
    scene bg table with dissolve
    show mc happy_casual at left with dissolve
    show mom neutral at right with dissolve


    mom "What's this I'm hearing, honey?"
    mc "Ma, I passed the entrance exam. I'll be going to Bicol University this coming school year."
    show mom happy with dissolve
    mom "Oh honey! That's some big news. You know what this calls for. ICE CREAM!"
    mc "Yey! I've been wanting ice cream for a long time."
    mc "Mine's chocolate!"

    show mom neutral with dissolve

    mom "Slow down, we'll wait until lunch time, okay?"

    # Family Celebrating
    hide mc
    hide mom
    scene cutscene1

    n "[mcname], an incoming first year college student of Bicol University. It was [pronoun_belonging] first time being away from home and had no friends going to the new school [pronoun_reffered] enrolled in..."
    n "and now that [pronoun_reffered] has arrived [pronoun_reffered] now has to face the challenges that every freshman must face."


    jump chapter1

label chapter1:
    scene bg calendar_aug with dissolve
    scene bg calendar_aug with Pause(4)
    scene bg dormday with dissolve

    show mc happy_casual
    mc "Oh wow! This is what the prestigious BU looks like! I feel so anxious, will I ever get new friends? Oh well guess we’ll find out when classes start."

    scene bg livday
    show emil angry
    emil "Oyy you! Always sign in the log book before going in or outside the dormitory? Got it?!"
    show emil angry at right

    menu:
        "Yes sir, I’m sorry I didn’t know, won’t happen again":
            $ emil_decision = "good"
            $ points += 1
            show mc shocked_casual at left
            show emil neutral at right
            emil "Ok, sorry for raising my voice, but please do not forget when doing so, here’s the keys to your room."

        "Silence, (*proceeds to logbook*)":
            $ emil_decision = "neutral"
            show mc sad_casual at left
            emil "(*silence*)"

        "Pff! Couldn’t you be any nicer to the new guys?!":
            $ emil_decision = "bad"
            $ points -= 1
            show mc angry_casual at left
            emil "HUH! Is that how your mother taught you how to interact with others?! Anyways, here’s your key!"

    hide emil
    scene bg roomday with dissolve
    show mc confused_casual
    mc "This room is kinda messy! I guess I need to clean up first since I’m the first one to arrive."

    hide mc
    $ in_story = True
    jump dormicleaning

label chapter1_1:
    show mc happy_casual with dissolve
    mc "Whew, finally I’m done cleaning and unpacking, I guess I’ll go for a little campus tour first."

    hide mc
    scene cutscene2 with Pause(5) # campus tour

    scene bg roomaft with dissolve
    show mc happy_casual at left
    mc "Oh, hi there!"
    show friend_1 sad_casual at right
    friend_1 "Errr..."
    mc "You must be my new roommate! My name is [mcname], what’s your name?"
    friend_1 "Hello, my name is ugh... [friend_1]."
    mc "Nice to meet you [friend_1]! I’m from ..."
    $ place = renpy.input("Where are you from?", length=50)
    $ place = place.strip()
    mc "I’m from [place]. How about you?"
    friend_1 "I’m from eehhh……. My parents are actually from Goa, but I live in Naga actually."
    mc "That's nice! I think we should hang out more. I'm sure we'll be pretty close as days pass by."
    show friend_1 neutral_casual at right
    friend_1 "Uhm... Yeah, sure."
    mc "Would you like to join me later for dinner? I'd really like to have a conversation with you. You'll be my first ever friend here."
    friend_1 "Okay, I guess."

    hide mc
    hide friend_1
    scene cutscene3 # time passes by
    scene cutscene4 # mc and a femc bumped each other


    show mc shocked_casual at left
    menu:
        "I’m sorry miss, I didn’t see you there.":
            $ points += 1
            show alex confused at right
            "???" "Oh, no worries."
            $ madam_decision = "good"
        "Watch where you're going miss!":
            $ points -= 1
            show mc angry_casual at left
            show alex angry at right
            $ madam_decision = "neutral"
            "???" "Huh! Kids these days are so rude!"
            show alex angry at right:
                linear 1.0
                xalign 2.0
            $ madam_decision = "bad"

    hide alex
    hide mc
    hide friend_1

    scene cutscene5 # dinner mc and friend_1
    scene cutscene6 # next day arrives

    scene bg roomday with dissolve
    show mc sleepy_casual with dissolve
    mc "It's morning already?! I still want to sleep."
    # make this Itallic
    mc "I forgot that I still haven’t claimed my COR for ID and my uniform has not yet been sewn yet, I guess I should go to the registrar first and then go to the tailor to get my uniform tailored."
    show cutscene7 # daily routine
    hide mc
    scene bg livday
    show friend_2 admiring_casual
    jus "Good morning fellow dormer!"
    show friend_2 admiring_casual at right
    show mc neutral_casual at left

    menu:
        "Hello, good morning to you too!":
            $ points += 1
            show mc happy_casual at left
            jus "Hello! You’re new here too huh? What course are you from? I’m [friend_2] from BS Computer Science, 1st year"
            mc "I'm [mcname]! I guess were in the same program I see."

        "*Ignores*":
            jus "Quite the shy type huh, what course are you from?"
            show friend_2 happy_casual at right with dissolve
            jus "I’m [friend_2] from BS Computer Science, 1st year"
            mc "I'm [mcname]! I guess were in the same program I see."

        "Who in the world are you?":
            $ points -= 1
            show mc angry_casual at left
            show friend_2 confused_casual at right with dissolve
            jus "Woah woah, chill dude hehe."
            show friend_2 happy_casual at right with dissolve
            jus "I mean no harm just wanted to interact, I’m [friend_2] from BS Computer Science, 1st year"
            show mc neutral_casual at left with dissolve
            mc "Oh, my bad. Anyway, I'm [mcname]. I guess were in the same program I see."

    jus "Nice! By any chance do you have your COR already?"
    mc "I haven’t, I’m just about to go to the registrar to claim it."
    jus "Great! Why don’t we go there together?"
    mc "Sounds great! Let's go."

    with dissolve
    scene bg martday
    n "And there Dormmate and [mcname] goes on to go to the registrar together to claim their respective, COR just as Character came near the registrar windows, [pronoun_belonging] face turns pale as [pronoun_reffered] saw the mystery woman in the registrar’s office"
    show mc shocked_uniform at left with fade
    mc "Uhh………. Uhm………. Hi madam, I apologise for what happened last night huhu"

    if madam_decision == "good":
        madam "Hello there mister! I see that you are also from the College of Science, I also apologise for bumping into you yesterday. How may I help you?"
        show Madam_Alexandra_Happy at right with dissolve
    elif madam_decision == "bad" or madam_decision == "neutral":
        madam "Well well well, if it isn’t mister bump, no apology here, what can you do for you? (Neutral and Bad)"
        show Madam_Alexandra_Annoyed at right with dissolve

    show mc happy_uniform at left

    mc "I would like to get my COR so that if ever that our prof needs it we can show it."
    madam "Sure, however it’ll take a few minutes before we can process it."
    mc "No problem Madam, thank you!"

    hide madam_alexandra_happy
    hide mc happy_casual

    """*Waits a few minutes, character and dormate goes out*"""

    scene bg walkaft with dissolve
    show friend_2 happy_uniform at right
    jus "Now that we have already claimed the COR, where are we going now?"
    show mc happy_uniform at left
    mc "I’m going to the tailor, I haven’t had my uniform sewn yet."
    jus "Alright then, I’ll see you back to the dorm then!"
    mc "See ya!"

    scene bg tailorshop with pixellate
    show mc happy_uniform at left
    mc "Tao po! Pwede po magpatahi uniform?"
    show erin happy at right
    aling "Good morning! Surely what is it that you needed sir?"
    mc "I need a uniform po for BU, is it possible that it'd be finished at  *date* "
    aling "Sure iho! Goodbye!"
    "Grabs wallet scene"
    mc "Thank you po aling! I'll be on my way good ma'am!"
    aling "Ok iho! Take care"
    "*Character goes back to his dorm, and when he arrives at his room the door is locked and he forgot his keys. He goes and asks kuya Emil if he could borrow his keys*"

    scene bg livday with zoomin
    show mc happy_uniform at left
    mc "Kuya Emil can I borrow the keys for our room, I might’ve forgot the key inside"

    if emil_decision == "good":
        show emil happy at right with dissolve
        emil "Here you go kiddo!"
    elif emil_decision == "bad" or emil_decision == "neutral":
        show emil angry at right with dissolve
        emil "Heh! Keys are given to you to use for opening the door, not for decoration! Next time you forget your key you’ll be waiting for your roommate to come home before you open your door!"

    n "The first official day for classes in Bicol University has officially began. The students and faculties are roaming as much as before, lots of students are having a hard time navigating the campus, the sound of vehicles during rush feels like the world has reverted back to normal. And just before official lectures start, orientation for freshmen will happen."

    "*next day arrives*"

    scene bg roomday with zoomout
    show mc happy_uniform at left with dissolve
    mc "Today’s finally the day! I get to meet my new classmates, I wonder what they look like or their personality hmmm. Guess I’ll just go with Dormmate during the orientation, having a familiar face is always a good thing. Right Roommate?"
    show friend_1 sleepy_casual at right with fade
    "*snores*"
    show mc confused_uniform at left with dissolve
    mc "Nevermind HAHAHAHA dude’s deadass asleep"

    scene bg livday with fade
    "*mc proceeds outside*"
    show friend_2 happy_uniform at right with fade
    jus " Just in time character! I was waiting for you so we can go out together. "
    show mc happy_uniform at left with fade
    mc "Let's go"

    "*They proceed to the orientation hall*"

    scene bg building1 with dissolve
    n "As they arrrive in the room, [pronoun_reffered] can hear students murmuring, the place as lively as usual"
    show friend_2 shocked_uniform at left with dissolve
    jus "Sheeeesh, there are lots of students! I have no idea where we should be designated!"
    show mc shocked_uniform at right with fade
    mc "I guess we should just look for someone who we are familiar with, maybe a familiar face in the gc?"
    jus "I've never checked the GC so far LOL"
    show mc confused_uniform at right
    mc "Then were doooommmeeeedddd!!!!!!"
    "(*another student approaches, a guy with glasses with casual shirt and braces approaches*)"
    show lurs happy_casual with fade
    lurs "*bumps in character*"
    scene bg building1 with zoomin
    show lurs shocked_casual at right
    show lurs happy_casual at right
    lurs "ohhh………sorry about that sir hehe, may I ask where the section is for Computer Science?"

    menu:
        "Oh, hi there. Are you also a computer science freshman? My name is *name* and this is Dormmate!":
            $ points += 1
            show mc happy_uniform at left
            lurs "Nice to meet you both! Yes I am a freshman student of Com Sci! Thanks for having me"
            $ johnny_decision = "good"

        "*Ignores*":
            show mc neutral_uniform at left
            lurs "Oh............"
            $ johnny_decision = "neutral"

        "Watch it hobo! Are your glasses just for clout?":
            $ points -= 1
            show mc angry_uniform at left
            show lurs sad_casual at right
            lurs "I’m sorry! I’m sorry! I didn’t mean to bump into you huhu!"
            $ johnny_decision = "bad"

    hide mc at left
    hide lurs at right
    "*They proceed to the computer science section"

    scene builing1 with pixellate
    "*Orientation noise and shit*"
    scene building1 with squares
    "*orientation ends*"
    show joseyde happy at center
    j "Ok now that the orientation has ended, I highly recommend that you get to know your blockmates first to bond and create memories. Thank you everyone and have a blessed afternoon"
    "*applauses"

    scene bg fieldday with dissolve
    show mc happy_uniform at left
    mc "Where do we go now dormmate?"
    show friend_2 confused_uniform at right
    jus "I dunno, maybe let’s go talk to  some of our classmates then?"
    "*cutscene na naguusap chuchu*"
    "*encounters Johnny*"

    if johnny_decision == "good":
        hide friend_2
        show lurs happy_uniform at right
        lurs "Oh hey there fellas! It appears that we’re actually classmates! I hope to get to know you guys better!"

    elif johnny_decision == "bad" or johnny_decision == "neutral":
        hide friend_2
        show lurs sad_uniform at right
        lurs "Ahh......... hehe"

    hide lurs
    "*Johnny goes away*"
    show mc happy_uniform at left
    show friend_2 happy_uniform at right
    mc " Oh well, I just hope we get to go along with our classmates!"
    show friend_2 happy_uniform at right
    jus "Yeah, I guess I’ll be going home for the meantime."
    mc "Aight, I think I'll go with you"

    scene bg dormday with pushup
    "*[mcname] and dormmate arrives at dormitory"

    scene bg momcall with dissolve

    menu:
        "*Answer Call*":
            $ points += 1
            show mom happy at right
            mom " Hey son/daughter, you haven’t called in a while so I had to call you just to check on ya. How’s college been"
            jump mom_convo


        "*No answer*":
            $ points -= 1

label mom_convo:
    menu:
        "So far it’s been good ma! Our class haven’t officially started but so far it’s been great!":
            show mc happy_casual at left
            show mom happy at right
            mom "Oh that’s good to hear! Keep up the good work son/daughter and remember to not pressure yourself that much and just have fun alright?"

        "It’s been absolute hell! All the people here always rubs me of the wrong way!":
            show mc angry_casual at left
            show mom sad at right
            mom "I know that college is tough but don’t be like that now. There will always be something positive to look forward in tough  situations, alway remember if you ever need help we’ll be here. Take care now"

    show mc happy_casual at left with fade
    mc "Ok ma,  I better keep going now I still have to fix my things. Bye!"
    show mom happy at right
    mom " Bye *name*, mama always loves you mwa mwa"
    "*sound of phone stops*"
    scene bg dormday
    show mc happy_casual at center
    mc "I need to go fetch my uniform now since tomorrow our lectures will officially begin"

    "*Character travels to the tailor shop"

    scene bg tailorshop with pixellate
    show mc happy_casual at left with dissolve
    mc "{i}Magandang araw po! Kukuha po sana ako nung uniform kong pintahi ho nung nakaraan.{/i}"
    show erin happy at right
    aling "Well hello there iho! You’re uniform is already done, however there is one thing that is missing. I forgot to tell you that you should’ve bought your logo from the department since our store already run out of it. I sincerely apologise if I informed you way to late"
    menu:
        "No worries, Aling Erin! I’ll just buy from our department. Thank you aling! *gives money*":
            $ points += 1
            aling "I do apologise again young man for your inconvenience, I’ll just give you a discount for your troubles. Take care!"

        "*Well you could’ve told me that earlier! Now I have to pay you full for not finishing my uniform, unfair but still thanks tsk tsk *gives money*":
            $ points -= 1
            show mc angry_casual at left with dissolve
            show erin sad at right with dissolve
            aling "My apologies young man, please do not take it to hard since I'm old and have lots of customers to accommodate,I’ll just give you a discount for your troubles, i again apologize young man"

    "*character leaves  the sewing shop, while he waits for jeeps to pass by he sees his old crush Crush walking towards him without her noticing him*"
    scene bg frontday with dissolve
    show mc shocked_casual at center with ease
    mc "Oh shizz, it's Sofia!! What do I do? What do I sayyyy??????"
    menu:
        "Hi Crush! Ho.. how… how’s… what’s up? Hehe *blushes* + Crush":
            $ points += 1
            show mc blushed_casual at left with fade
            show sophia happy_uniform at right with dissolve
            crush "Oh hey there character! It’s been summer since I last saw you huh, I would love to keep the chat going but I have a class to attend so I better be going. Bye! It was nice talking to you again!"


        "*Whit whew* hey there beautiful, hehe just kidding. Sup Crush? ":
            $ points -= 1
            show mc neutral_casual at left with dissolve
            show sophia awkward_uniform at right with dissolve
            crush "Oh hehe…. character  uhhh. I still have a class to go to so I better keep going. Bye *said in an awkward manner*"

    mc "Byee! See ya around!"
    hide sophia with fade
    "*Crush walks away hurridley since she has class to attend, meanwhile character is blushed and all*"
    scene bg frontday with dissolve
    show mc blushed_casual at center with fade
    mc "UGGGHHHHHHH!!! SHE’S AS CUTE AS EVER!!! *poker face bigla* ok calm down I still have to buy some logos for my uniforms."
    "*jeepney stops, character goes inside*"

    scene bg jeep with irisin
    show mc happy_casual at left with fade
    mc "{i}Kuya bayad po{/i}"
    show mark neutral at right with fade
    mark "{i}Sa may san toh{/i}"
    mc "{i}Sa may CM lang ho{/i}"
    "The to the fare that character gave is given back"
    scene jeep with ease
    menu:
        "{i}Kuya kulang ho ang skuli, estudyante ho ako {/i}":
            $ points += 1
            show mc confused_casual at left with dissolve
            show mark happy at right with dissolve
            mark "{i}Ayy ganon ba iho? Eto pasenya ka na ah, matanda na ang mamang hehe{/i}"


        "Kuya ba’t eto lang sukli?! Ang lapit lapit nga lang ng patahian sa BU tapos sobra ka pa maningil. Estudyante pa ako kaya dapat di ganto singil niyo!":
            $ points -= 1
            show mc angry_casual at left with dissolve
            show mark sad at right with dissolve
            mark "{i}Hay nako nagkamali lang siguro ako panukli, ang bibig ng kabataan ngayon talagang antatalas ng mga dila{/i}"

    hide mark
    hide mc

    "*character arrives at BU, and goes straight to the CSC office*"

    scene bg csc with fade
    show mc happy_casual at left with fade
    mc "Good afternoon po! Are there still available logos for our uniform?"
    show mike happy_uniform at right with fade
    mike "Hello! Yes there are still some, come in and have a sit."
    hide mike
    "*character waits for a bit*"
    scene bg csc with dissolve
    show mc happy_casual at left with dissolve
    show mike happy_uniform at right with dissolve
    mike "sorry for the wait, here are your logos"
    hide mike
    show mike confused_uniform at right with dissolve
    mike "You look so familiar......."
    mike "Feels like I've seen you somewhere hmm"
    show mc neutral_casual at left with dissolve
    mc "Really? I've only been here for a few days"
    mike "Say weren't you in the freshmen orientation a few days ago?"
    hide mc
    show mc happy_casual at left with dissolve
    mc " Yes I am, you don’t happen to be a Computer Science student as well are you?"
    hide mike
    show mike happy_uniform at right with dissolve
    mike "What a coincidence I actually am! I am a third year student and it looks like you’d be calling me “senpai” eyy! Just kidding "
    menu:
        "Nice to meet you “senpai”! I look forward to working with you in the future, I better":
            $ points += 1
            show mc happy_casual at left with dissolve
            show mike happy_uniform at right with dissolve
            mike "I see! Take care my *kohai*"

        "Sheesh no need to be stingy about it hey hey hey! Anyways take care when you get home!":
            $ points -= 1
            show mc angry_casual at left with dissolve
            show mike sad_uniform at right with dissolve
            mark "Sheesh no need to be stingy about it hey hey hey! Anyways take care when you get home!"

    hide mc
    hide mike

    "*After obtaining the logos, character goes to the dorm*"

    scene bg dormaft with blinds
    show emil neutral at right with dissolve
    emil "You look kinda tired kiddo, college’s been making things tough for ya huh?"
    show mc sad_casual at left with dissolve
    mc "Tell me about it, we haven’t even started official lecture classes but it already feels like I’ve had lots of things done"
    emil "Well don’t sweat, you’ll get the hang of it soon. Wish you luck kiddo"

    menu:
        "Thanks kuya Emil! Gon need it!":
            $ points += 1
            show mc happy_casual at left with dissolve
            show emil happy at right with dissolve
            emil "Sure kiddo, best of luck"

        "I don’t need your goodluck ":
            $ points -= 1
            show mc angry_casual at left with dissolve
            show emil angry at right with dissolve
            emil "Cocky as usual"

    "*Character proceeds to his room*"

    scene bg roomaft with move
    "*Internally, the character talks to himself*"
    show mc sad_casual at center with dissolve
    mc "{b} Hays, is it really necessary that I still put a logo on this uniform? It’s not like the guard will notice me not having this already. Oh well, guess better keep doing this now{/b}"

    "*MINI GAME (IF APPLICABLE), THERE WILL BE UNIQUE DIALOGUES IF MAKAGAWA MINI GAME, IF HINDI KAYA PROCEED LANG.*"

    hide mc
    show mc neutral_casual at center with dissolve
    mc " Now that I’ve sewn these uniforms, I now need to iron the clothes so they may look presentable when going to class"

    hide mc
    "*MIGHT MINI GAME NOT SURE"
    show mc happy_casual at center with dissolve
    mc " Finally done with the chores, now I have to prepare for my classes tomorrow"

    "*INTERACTABLE PHOTOS (CAN USE IMAGE MAP feature)*"

    hide mc
    "*Next day arrives, alarm rings*"
    scene bg roomday with hpunch
    show mc sleepy_casual at center with dissolve
    mc "Uggggghhhhhhh *with hagard jwu look*……………. It’s really here the first day of classes, I just hope that the profs are nice."
    hide mc
    show mc shocked_casual at left with dissolve
    mc "Ohh [friend_1] is almost awake, I must've been very noisy"
    show friend_1 sleepy_casual at right with dissolve
    friend_1 "Uggghhhh……………. Good morning, want to go out for breakfast?"
    menu:
        "I would love to! But I need to be early for the first day so I can’t . Let’s do it next time!":
            $ points += 1
            show mc happy_casual at left with dissolve
            show friend_1 happy_casual at right with dissolve
            friend_1 "It’s alright, let’s eat next time then"
            hide friend_1
            "*[friend_1] leaves for breakfast*"

        "No thanks, I’m not interested":
            $ points -= 1
            show mc angry_casual at left with dissolve
            show friend_1 sad at right with dissolve
            friend_1 "Oh…….. Ok"
            hide friend_1
            "*[friend_1] leaves for breakfast*"

    scene bg roomday with fade
    show mc happy_casual at center with dissolve
    mc "Ok now that I have finished preparing things, time to clean myself."
    hide mc
    "*character proceeds to go to the CR*"

    scene bg crday with fade
    "*Character and Dormmate bumps into each other*"
    show friend_2 happy_casual at right with dissolve
    jus " Oh hey there character! What a coincidence you just woke up too?"
    show mc neutral_casual at left with dissolve
    mc "nah I just finished preparing my things for the first day of classes, you can never be too prepared"
    show friend_2 happy_casual at right with dissolve
    jus "You seem to be super excited rather than nervous in the first day huh"
    show mc neutral_casual at left with dissolve
    mc "of course! It’s exciting to get to know more people other than the orientation, plus i am somehow excited on how our professors look like and how they act"
    show friend_2 happy_casual at right with dissolve
    jus "Heh…. I wish I had your enthusiasm, anyways we better get going we might be late to class. Let’s go together gooing to class i am kinda nervous hehe."
    show mc neutral_casual at left with dissolve
    mc "aight then I’ll be going now as well"
    hide mc
    hide jus
    "*character goes to shower and finishes preparing, character goes to the lobby waiting for their friend*"
    scene bg dormday with pushup
    show mc angry_uniform at center with dissolve
    mc "where the hell is dormmate, were about to be late for the first day of class"
    menu:
        "*Wait for dormmate, even if you get late*":
            $ points += 1
            hide mc
            show mc neutral_uniform at center with dissolve
            mc "I guess it wouldn’t wait to wait for a bit more"
            hide mc "After a few minutes, dormmate arrives"
            show mc angry_casual at left with dissolve
            mc "What the hell have you been doing? We are almost late!"
            show friend_2 sad_uniform at right with dissolve
            jus "Sorry character *tired sighs* I had the urge to take a call of nature at the worst time, I’ve already had my clothes on but i had to take them of cause of the urge."
            hide mc
            show mc neutral_uniform at left with dissolve
            mc "you really had to sugarcoat the term for taking a poop. Anyways we better get going or madam will get mad at us, we should go for a run at it."
            hide mc
            hide friend_2
            "*runs to the room*"
            scene bg comlab with face
            "*Character and [friend_2] both just barely made it in time"
            show mc angry_uniform at left with dissolve
            mc "We barely made it in time! No thanks to you!"
            hide mc
            show mc happy_uniform at left with dissolve
            mc "Just kidding"
            show just sad_uniform at right with dissolve
            jus "You didn’t need to be so frank with it, lol. It’s what you call being clutch"
            show mc happy_uniform at left with dissolve
            mc "Clutch your face, we better find ourselves a seat now since class is about to begin"

        "Leave Dormmate":
            $ points -= 1
            hide mc
            show mc neutral_uniform
            mc " I should just go now or I’ll be late, and maybe I’ll still arrive in time"
            hide mc
            "*Character goes through the canteen knowing that [pronoun_reffered] still has some time"
            scene bg canteenday with fade
            show mc neutral_uniform at center with dissolve
            mc "mm…….. There’s still a few more minutes before time, maybe I can stop by for a little snack *nag snack sa canteen*, oh shit! It’s almost time! I might get late."
            hide mc
            "*character runs to the room*"
            scene bg comlab with fade
            show mc happy_uniform at center with dissolve
            mc "Just in time did I arrive. Now it's time to find myself a seat."
            "*after a few moments, [friend_2] arrives"
            show friend_2 angry_uniform at right with dissolve
            jus "Dude! You literally left me tsk"
            hide mc
            show mc sad_uniform at left with dissolve
            mc "You were taking too long! It was the first day I can’t afford to be late, I’m truly sorry"
            hide friend_2
            show friend_2 happy_uniform at right with dissolve
            jus " Nah I was just messing with ya, I took too long to prepare so that one’s on me"
            hide mc
            show mc neutral_uniform at left with dissolve
            mc "Ok then, go get yourself a seat already cause class will start"

    hide mc
    hide friend_2
    "*After a while, madam Michelle arrived*"
    show michelle neutral at center with dissolve
    mich " Hello class! My name is Michelle and I will be your teacher this semester for your Introduction to Computing subject, this class won’t be as easy as you guys think. That is why I expect your full cooperation so that we may be able to get along well."
    show michelle happy at center with dissolve
    mich "Now that I have introduced myself, how about you introduce yourselves this time,"
    hide mich
    show mich neutral
    hide mich
    show mich happy with fade
    "*looks around*"
    mich "alright let’s begin with you mister/miss."
    menu:
        "Hello! My name is *character name*! I am from [loc] and I am pleased to meet you too madam Michelle!":
            $ points += 1
            show mc happy_casual at left with dissolve
            show michelle happy at rght with dissolve
            mich "Nice to meet you too character! Am also looking forward that you enjoy and learn lots in this class! Ok next. "

        "Errr…….. Why did you choose to begin with me? Anyways the Name is  *character name*. Pleased to meet you ":
            $ points -= 1
            show mc confused_casual at left with dissolve
            show michelle angry at right with dissolve
            mich "Hmm, don’t you think as the teacher it is my choice whom I wanted to call to introduce themselves first. Anyways nice meeting you too, character. Ok next"


    hide mc
    hide Michelle
    "*cutscene where there students will introduce themselves*"

    scene bg comlab with fade
    show michelle happy at center with dissolve
    mich "Ok everyone, that you have finished introducing yourselves, it is time to give you a brief description of our class curriculum"
    hide Michelle
    "*press to check the curriculum* (IMAGE BUTTON)"
    show michelle happy at center with dissolve
    mich "Now that I have given you the possible topics for the class, I expect everyone to have their expectations set on how the subject will, again I look forward to this semester with everyone and class dismissed."
    hide michelle
    "*everyone goes into frenzy as the class ends"
    scene bg fieldday with move
    show friend_2 sad_uniform at right with dissolve
    jus "Yow dude, did you just see the curriculum for that subject! Just by looking at the topics it feels like it’s getting brutal"
    show mc sad_uniform at left with dissolve
    mc "Tell me about it, just reading the first topic already made my mind about to explode."
    "*Johnny walks by*"
    show lurs happy_uniform at center with dissolve
    lurs " Oh hi there fellas! The last time we saw each other was during the freshmen orientation, how ya’ll been doing?"
    menu:
        "Hello Johnny! Nice seeing you again and I see that your as lively as ever, the topics seem so hard don’t ya think? ":
            $ points += 1
            hide friend_2
            show mc happy_uniform at left with dissolve
            show lurs happy_uniform at rght with dissolve
            mich "I think that it isn’t really that hard since it’s still just the basic when it comes to computer science,I can help you when things get rough for you!"
            show mc happy_uniform at left with dissolve
            mc "I'll keep that in min. Thanks!"
        "You're the nerd that bumped me up during the freshman orientation! Not that it matters, what do you want?":
            $ points -= 1
            hide friend_2
            show mc angry_uniform at left with dissolve
            show lurs sad_uniform at right with dissolve
            mich "orry! Sorry! Huhuhuhu, i really didn’t mean to run into you that time, I just wanted to make friends, however if you find anything difficult you can always ask me for help"
            hide lurs
            "*johnny leaves*"

    scene bg fieldday with move
    show friend_2 neutral_uniform at right with dissolve
    jus "That dude's wierd, but he is cool after all"
    show mc neutral_uniform at left with dissolve
    mc "I think so too, maybe we're just being too you know"
    hide friend_2 admiring_casual
    show just sad_uniform at right with dissolve
    jus "Being too what?"
    show mc neutral_uniform at left with dissolve
    mc "Nevermind, it’s nothing you really are slow when it comes to things at times lol"
    hide friend_2
    show friend_2 happy_uniform at right with dissolve
    jus "You’re not wrong there, anyways I heard that there’s going to be an event"
    hide mc
    show mc shocked_uniform at left with dissolve
    mc "Oh really? What's your source on this said event?"
    jus " I just kinda heard our classmates talking about it earlier, maybe some of them has some knowledge about it?"
    hide mc
    show mc neutral_uniform at left with dissolve
    mc "Hmm maybe it’s just rumors tho. You know what I just met an upperclassmen we can ask for the credibility of the event"
    jus "Alright then, let's go"
    hide mc
    hide friend_2
    "*Both character and [friend_2] goes to the CSC office"
    scene bg csc with fade
    show mike neutral_uniform at right with dissolve
    mike "Hi th....... Oh haven't I seen you before"
    "*brief pause*"
    hide mike
    show mike happy_uniform at right with dissolve
    mike "Oh you're that one that once brought logos! How may I help my dearest kohai"
    menu:
        "Koninchiwa Senpai! Were just here to ask if there really is a freshmen party upcoming":
            $ points += 1
            show mc happy_uniform at left with dissolve
            show mike happy_uniform at rght with dissolve
            mike "Oh yes there certainly is, it’s this upcoming week. There are lots of stuff coming up however the big one is an upcoming concert featuring bands from our college department!"
        "Again with this weird Japanese thing, anyways we wanna know if there really is an upcoming freshman party?":
            $ points -= 1
            show mc angry_uniform at left with dissolve
            show lurs sad_uniform at right with dissolve
            mike "No need to be stingy! This is just a me thing, going back to your question it is true that there is an upcoming freshman party and the big stuff is that there is a concert where the bands comes from our department"
    hide mike
    show friend_2 confused_uniform at right with dissolve
    jus "If that’s the case, are students excused during the said event?"
    show mike happy_uniform at center with dissolve
    mike "There is a chance that students are only excused from their 5 o clock classes onwards if it is applicable to their schedule"
    hide friend_2
    show jus sad_uniform at right with dissolve
    jus " Ohh it’s look’s like there are going to be some problems with our schedule during the freshman party character"
    hide mc
    show mc neutral_uniform at left with dissolve
    mc "Seems like it. Hold on lemme check our schedule first *pulls out phone and shows schedule*"
    hide friend_2
    hide mc
    hide mike
    "*screen will show a scheduler (kahit eme eme na lang)"
    show mc neutral_uniform at left with dissolve
    show friend_2 neutral_uniform at right with dissolve
    mc "Looks like it really will affect our Basic Programming subject. Speaking of we need to get our PE uniforms as well"
    "*mike overhears them*"
    show mike happy_uniform at center with dissolve
    mike "Ohh you haven’t claimed your PE uniforms yet as well?? You must be able to get that uniform you know, given that you will need that in your PE class and soon HATAw event"
    mc "You're right, we better hurry up and get going. Thanks kuya Mike!"
    show mike happy_uniform at center with dissolve
    mike "Sure sure no problem!!"
    hide mike
    hide mc
    hide friend_2
    "*character and roommate leaves the room, and they proceed to the registar to claim their PE*"
    scene bg registar with fade
    show mc happy_uniform at left with dissolve
    mc " Hi! Manong guard where could the office for claiming the PE uniform be?"
    show emil angry at right with dissolve
    guard "Just go inside in the registrar and from their you would be able to claim your uniform."
    show mc happy_uniform at left with dissolve
    mc "Thank you po!"
    hide mc
    hide emil
    scene bg registrar with fade
    show Madam_Alexandra_Happy at right with dissolve
    madam "Here to claim your PE uniform?"
    show mc happy_uniform at left with fade
    mc "Yes ma'am hehe"
    hide madam
    show Madam_Alexandra_Happy at right with dissolve
    madam "Here you go boy, That's (n) pesos"
    show mc happy_uniform at left with dissolve
    mc "Yes Madam! Duly noted"

    hide mc
    hide madam
    "*character returns back to the dormitory*"
    scene bg roomaft with fade
    show mc happy_casual with fade
    mc "Finally got my PE uniform, now that I look at it we have a PE schedule upcoming! Better get some rest because tomorrows going to be one hell of a day!"
    "*goes to bed early*"
    scene bg roomday with fade
    show mc sleepy_casual
    mc "Ughhhh……………. Oh shit I’m latee for class!! I better get my things together and get ready."
    scene bg crday with fade
    show mc confused_casual with dissolve
    menu:
        "Roommate is that you? I’m sorry if I am being too persistent but can you go a little faster in your bath?":
            $ points += 1
            show mc happy_uniform at left with dissolve
            friend_1 "*Oh sorry bout that character, I'm almost done now"
        "Really roommate????? Are you seriously going to take too long to take a bath!!":
            $ points -= 1
            show mc angry_uniform at left with dissolve
            friend_1 "*Oh..............."
    "*[friend_1] leaves the shower"
    show friend_1 sad_casual at right with dissolve
    friend_1 "Sorry about that character"
    hide friend_1
    hide mc
    "*Character then proceeds to the bathroom*"
    scene bg roomday with fade
    "*Character finally finsihes taking a bath"
    show mc happy_pe with dissolve
    mc "Ahh I'm finally done getting ready! I wonder we're gonna do today for PE hmm"
    scene bg liveday with fade
    show friend_2 happy_pe at right with dissolve
    jus " Hey character! Are you ready for the first day of PE!"
    show mc happy_pe at left with dissolve
    mc "I sure as hell do! Let's go now"
    hide mc
    hide friend_2
    "*both of them proceeds to the oval*"
    scene bg ovalday with fade
    show devier happy with dissolve
    dev "All right class! Is everybody here?? *Good! Now before we start I am your professor Mr. Devier for this PE class! Now that you know who I am, it is your time to tell me about yourselves."
    hide Devier
    "*mini cutscene where everyone introdcues smthn like that*"
    show devier neutral at right with dissolve
    dev "And lastly we have........."
    dev "*character*"
    show mc happy_pe at left with dissolve
    mc "Hello sir! My name is *name* and I am from *place* it’s nice to meet you sir!"
    dev "You don't look so so athletic there, just kidding HAHA"
    menu:
        "Hehehe, maybe sir, tho I am somehow confident in what I can do!":
            $ points += 1
            show mc happy_uniform at left with dissolve
            show devier happy at right with dissolve
            dev "HAHAHAAHAHA! That's spirit kiddo! I love the confidence!"
        "Pfft! Don’t you understand me old man! I’ll show you what I can do!":
            $ points -= 1
            show mc angry_uniform at left with dissolve
            show devier angry at right with dissolve
            dev "ou know there’s a fine line between confidence and arrogance son!"
    hide mc
    hide dev
    show dev neutral with dissolve
    dev "Anyways let me get straight to the point"
    dev "as you all know this is the PE class, so from here on there will be lots of tiring activities to do"
    dev "Prepare yourselves as this class will not be easy"
    hide devier
    show friend_2 confused at left with dissolve
    jus "Sir, what is it that we'll be doing today?"
    show devier happy at right with dissolve
    dev "That’s a good question, let’s start off with athletics! I’ll pair you up with someone and then we can begin the exercise."
    hide devier
    "*proceeds to group up the class"
    show devier happy with dissolve
    dev "Now that you’ve seen your partner, we fetch you up to play against each other. Whoever scores the first in the finish line wins and gets additional points! Alright settle down with your pair and goodluck!"
    hide devier
    "*everyone proceeds to their partner"
    show mc happy_pe at left with dissolve
    mc "Huh I guess it’s you and me that gets partnered again here huh dormate"
    show friend_2 happy_pe at right with dissolve
    jus "HAHAHAHAHA what are the odds character! I guess this means we begin a friendly rivalry here!"
    mc "Bring it on dormmate!"
    hide mc
    hide friend_2
    show mc confused_pe at left with dissolve
    show friend_2 confused_pe at right with dissolve
    "*someone raises their hand*"
    hide mc
    hide friend_2
    show lurs confused_pe with dissolve
    lurs "Uhmm………. Sir I don’t have a partner yet."
    hide lurs
    show devier happy with dissolve
    dev "Ok then, anyone who doesn't have a partner yet?"
    "*awkward silence*"
    hide devier
    show devier neutral with dissolve
    dev "Alright it seems like everyone has been paired already, now one pair is going to have to adopt him."
    "*dev looks around*"
    show dev happy with dissolve
    dev "You there character! Take Johnny in and you three will race it out later."
    hide devier
    "*Johnny approaches character and [friend_2]"
    show lurs neutral_pe at right with dissolve
    lurs "Hi! Ahehe it’s me again, I hope you don’t mind me grouping up with you"
    menu:
        "Sure sure! I don’t mind at all! May the best man win!":
            $ points += 1
            show mc happy_pe at left with dissolve
            show friend_2 happy_pe at right with dissolve
            show lurs happy_pe at center with dissolve
            lurs "Huh, may the best man win! You to dormate"
        "HAHAHAAHAHAH loser, don’t you worry I’ll win the race in an instant WHAHAHAHA!":
            $ points -= 1
            show mc angry_pe at left with dissolve
            show friend_2 sad_pe at right with dissolve
            show lurs sad_pe at center with dissolve
            lurs "Ohh huhuhuhu"
            jus "Don't be like that character, don't mind him Johnny he can be real stingy sometimes"

    hide friend_2
    hide mc
    hide lurs
    show devier happy at right with dissolve
    dev " Alright you three get ready as you will all play together, are you ready?"
    show mc happy_pe at left with dissolve
    mc "Yes sir!"
    dev "Alright then, on your marks, get set, GOOOOOOOOO!!!!"
    #MINI GAME NA MAY RACE MAN DAA
    scene bg ovalday with fade
    show devier happy with dissolve
    dev "Well done everyone! You all seem so fit to be great at this, as expected, you surpassed my expectation there character!"
    hide devier
    show mc tired_pe with dissolve
    MC "Thank you sir *gasping for air*"
    hide mc
    show devier happy with dissolve
    dev "Ok now everyone, now that we are done with our first meeting, get some rest and prepare for your next subject. Class dismissed"
    hide devier
    "*Everyone goes away from the oval as they all prepare for their next class*"
    "*Character and dormmate go back into the dorm*"
    show mc shocked_pe at left with dissolve
    mc "Holy macaroni, I did not expect that we’d get put into the fire that quickly. *gasping*"
    show friend_2 tired_pe at right with dissolve
    jus " Tell me about it. Oh I almost forgot that the freshman party is nearing the horizon, what do you plan to do?"
    hide mc
    show mc neutral_pe at left with dissolve
    mc "nothing really much to be honest, there’s a quiz upcoming in our Intro to Computing class. So I need to review as much as I can"
    jus "You’re right I almost forgot that! Anyways I must also study hard for the upcoming quiz, it surely won’t be easy0"
    mc "Sure as hell won't be easy"
    hide mc
    hide friend_2
    "*Fast forward to the quiz day"
    scene bg dormday with fade
    "*dormmate and character sees each other in the room"
    show mc happy_uniform at left with dissolve
    mc "Are you ready for the quiz dormmate?"
    show friend_2 happy_uniform at right with dissolve
    jus "Sure as hell I am! Anyways we should get going we don’t want to be late again for this quiz"
    mc "You are really an easy goig one huh, anyways let's go"
    scene bg comlab with fade
    "*character and dormmate arrives*"
    show michelle happy with dissolve
    mich "Alright class, is everyone here now?"
    "*play audible yes*"
    mich " Good, now that you are all here please keep your phones, put your bags infornt, no cheating, and goodlcuk everyone!"
    hide michelle
    "*madam michelle hands out the tests"
    show mc shocked_uniform with dissolve
    mc " Holy guacamole! What is the hell I have no idea what these are!"
    "*MINI GAME QUIZ PLAYS*"
    "*CHAPTER 1 ends (after the choice)"
    #There will be choice where the character can cheat or finish the exam honestly
    #Based on his score/choice will chapter 2 start

return
