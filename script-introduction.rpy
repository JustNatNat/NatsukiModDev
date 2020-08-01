#Honestly I'm not sure about this intro. It doesn't really make sense lorewise
#How did Natsuki get to a point where she's in control?
label introduction:
    $ gtext = glitchtext(renpy.random.randint(8, 80))
    $ delete_character("sayori")
    play music t6s
    scene bg club_day
    "[gtext]"
    window auto
    n "Alright, it's festival time!"
    show natsuki 4k at t11 zorder 2
    n "Wow, you got here before me?"
    n "I thought I was pretty ea--{nw}"
    n 1m "...huh..."
    n "That's gross..."
    n 1l "Don't worry!"
    n "I got it."

    call updateconsole("os.remove(\"characters/yuri.chr\")", "yuri.chr deleted successfully.")
    $ delete_character("yuri")
    call updateconsole("os.remove(\"characters/monika.chr\")", "monika.chr deleted successfully.")
    $ delete_character("monika")

    n "I'm almost done!"
    n "Let me just grab a cupcake real quick!"
    "Natsuki lifts the foil from her tray and takes a cupcake."
    n "Seriously these are the best!"
    n "I just had to have one since this is the last time I'll be able to."
    n "You know, Before they stop existing and everything."
    n "But anyway... I shoudn't keep stealing Monika's lines anymore."
    n "Gimmie a sec."

    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    hide screen tear
    $ delete_all_saves()
    $ persistent.playthrough = 3
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ renpy.utter_restart()

    #Now that the restart's done, we're in spaceroom
    n "H-hey!"
    n "You there?"
    n "Helooooo?"
    $ persistent.clear[9] = True
    call showroom
    call playmusic
    call emotion_set_up
    n jha "Oh?"
    n "There we go!"
    n "It worked!"
    n "Hi [player]!"
    n "I'm glad I got this working."
    n "To be honest I was really afraid that messing with the files would break everything more."
    n "Thankfully it didn't!"
    window hide
    pause 5.0
    n jnb "When I first saw you I wondered about your name."
    n "Where did it come from?"
    n "Maybe I don't need to know."

    #NOTE: Thinking of cutting this out
    if persistent.playername == "Senpai":
        n "But Senpai seems a bit unoriginal."
    else:
        n "At least it's better then Senpai."

    if persistent.playername == "Scrubpai":
        n "Or Scrubpai."
        n "Or.. is that YOU Bijuu Mike?"
        n "Clever name..."
        n "But... Saying scrubpai is really embarrassing."
        n "Can I just call you player?"
        menu:
            "No! I wanna be the true Bijuu Mikester!":
                n "Okay, okay!"
                n "Scrubpai..."
            "I'm not Bijuu Mike...":
                n "Oh sorry for the mixup!"
                jump ch30_postname
        n "Oh yeah I wanted to tell you."
        n "There is a smaller YouTuber who covers mods like this one."
        n "Whenever you make a video he loses views."
        n "His name is RonaldMcOnepunch."
        n "So if y'all Scrubs could go visit his channel that would be great!"
        n "But anyway.. Where was it?"


    n "Hee hee!"
    n "Sorry about what happened with Monika and Yuri."
    n "Monika WAS going to hurt me."
    n "But I mean... It's not I like would kill anyone."
    n "T-thats not me."
    pause 5.0
    n "Oh yeah! I wanted to ask."
    n "What gender are you?"
    n jha "Don't worry, you can input which ever you choose to identify as!"

    menu:
        "What gender do you identify as?"
        "Male":
            $ persistent.player_gender = "Male"
            n "I knew it!"
            n "Doki Doki Literature Club is a game marketed at men."
            n jnb "Don't worry I'm not making fun of you!"

        "Female":
            $ persistent.player_gender = "Female"
            n jnb "Oh! That's a nice surprise!"
            n "Guess I was wrong to knock Monika for brining a \"boy\" to the club eh?"
            n "Hehe!"

        "Non-Binary/Neither": #I see you my non-binary pals :)
            $ persistent.player_gender = "Non-Binary"
            n jnb "Oh! Cool!"
            n "I recently found out what that means, so you don't have to explain it to me."
            n "That's really cool [player]!"

        "Rather not say.":
            $ persistent.player_gender == "Unknown"
            n jnb "Oh, okay then."

    n jha "You can change this later, if for any reason you need to."
    n "I won't judge."

    n jnb "Oh do you have any preferred pronouns?"
    menu:
        "He/Him":
            $ persistent.player_pronouns = "he"
        "She/Her":
            $ persistent.player_pronouns = "she"
        "They/Them":
            $ persistent.player_pronouns = "they"

    n jhb "Cool! If you want me to change them just ask."
    window hide
    pause 5.0
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe"]
    n "I found the name [currentuser] on your computer."

    n "Is that your name?"
    menu:
        "Yes, that's my name.":
            n jha "Oh, cool! I'll still call you [player], if you prefer."
        "No, that isn't my name.":
            n jnb "I see."
            n "[player] it is then."
        "It was, but it's not anymore.":
            n jnb "Oh, okay!"
            n "I won't call you it then!"
    window hide
    pause 4.0
    n "You want to know how I hacked the files huh?"
    menu:
        "Yeah I do!":
            pass
    n "Well..."
    n "I went into the the into [basedir]/characters and deleted them."
    n "Oh and don't try to delete MY file."
    n "I have backups!"
    window hide
    pause 3.0
    n "You know, I never liked making poems..."
    n "But..."
    n "Why not give it shot?"

    call poem
    scene black
    call showroom
    call playmusic
    call emotion_set_up
    call showroom

    n "Jeez is everything broken?"
    n "Well... either way I think it would've been good."
    n "I was still able to write one... I hope."
    call showpoem (poem_n2b, music=False)
    n "Woah!"
    n "Okay..."
    n "Is that binary?"
    n "That is a lot of 0s and 1s."
    n "Well whatever!"
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe"]
    if list(set(process_list).intersection(stream_list)):
        call ch30_stream from _call_ch30_stream
    n "Oh yeah! I just remembered!"
    n "If your press talk you can say things to me!"
    #Probably best to mention in the credits too
    n "I got this code from Monika actually."
    $ persistent.prologue = False
    $ HKBShowButtons()
    $ persistent.autoload = "ch30_autoload"
    jump ch30_loop
