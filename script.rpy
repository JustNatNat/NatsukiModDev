# This is used for top-level game structure.
# Should not include any actual events or scripting; only logic and calling other labels.

label deleteingname:
    $ persistent.playername = ""
    $ renpy.utter_restart()
label deleteingname2:
    $ persistent.playername = ""
    $ renpy.utter_restart()

label changename:
    $ persistent.playername = "Chris"
    jump start_main

label start:

    # Set the ID of this playthrough
    $ anticheat = persistent.anticheat

    # We'll keep track of the chapter we're on for poem response logic and other stuff
    $ chapter = 0

    #If they quit during a pause, we have to set _dismiss_pause to false again (I hate this hack)
    $ _dismiss_pause = config.developer

    # Each of the girls' names before the MC learns their name throughout ch0.
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True

    #This section detemines the "Act Structure" for the game.
    # persistent.playthrough variable marks each of the major game events (Sayori hanging, etc.)
    #Here is an example of how you might do that
    #TODO: Consider cutting this down
    if persistent.playername == "Gaster":
        $ persistent.playername = ""
        $ renpy.utter_restart()
    if persistent.playername == "Natsuki":
        $ persistent.playername = ""
        call screen dialog("You can't steal my name dummy!", ok_action=MainMenu(confirm=False))
    if persistent.playername == "Yuri":
        $ persistent.playername = ""
        call screen dialog("P-please don't do that!", ok_action=MainMenu(confirm=False))
    if persistent.playername == "Sayori":
        $ persistent.playername = ""
        call screen dialog("ERROR: Name is causing errors.", ok_action=MainMenu(confirm=False))
    if persistent.playername == "Monika":
        $ persistent.playername = ""
        call screen dialog("There can be only one.", ok_action=MainMenu(confirm=False))
    if persistent.playername == "Edgar":
        call screen dialog("I'll allow it!", ok_action=Return)
    if persistent.playername == "Zero":
        call screen dialog("Hello Zero.", ok_action=Return)
    if persistent.playername == "Frisk":
        call screen confirm("This name will make your life hell.\nAre you sure?", yes_action=Return, no_action=Jump("deleteingname"))
    if persistent.playername == "Chara":
        call screen dialog("The true name.", ok_action=Return)
    if persistent.playername == "Ralsei":
        call screen dialog("Trying to compete with Sayori for how much people\nfind you cute? Good luck.", ok_action=Return)
    if persistent.playername == "Cute":
        call screen dialog("No you're not.", ok_action=Jump("deleteingname"))
    if persistent.playername == "MC":
        call screen dialog("That's a little unoriginal, isn't it?", ok_action=Return)
    if persistent.playername == "Kris":
        call screen confirm("Wouldn't it be spelled \"Chris\"?", yes_action=Return, no_action=Jump("start_main"))
        $ persistent.playername = "Chris"
        $ renpy.utter_restart()
    if persistent.playername == "AAAAAAAAAAAA":
        call screen dialog("That's a little unoriginal, isn't it?", ok_action=Return)
    if persistent.playername == "E":
        $ persistent.playername = ""
        call screen dialog("That's not funny.", ok_action=MainMenu(confirm=False))
    if persistent.playername == "Fuck":
        $ persistent.playername = ""
        call screen dialog("That's quite rude.", ok_action=MainMenu(confirm=False))
    if persistent.playername == "Shit":
        $ persistent.playername = ""
        call screen dialog("That's quite rude.", ok_action=MainMenu(confirm=False))
    if persistent.playername == "Bacon":
        call screen confirm("Really, Bacon?", yes_action=Return, no_action=Jump("deleteingname"))
        call screen confirm("Are you sure?", yes_action=Return, no_action=Jump("deleteingname"))
        call screen confirm("Natsuki is going to call you this for the rest of the game.", yes_action=Return, no_action=Jump("deleteingname"))
        call screen confirm("Are you sure?!", yes_action=Return, no_action=Jump("deleteingname"))
        call screen dialog("...", ok_action=Return)
        call screen dialog("Alright...", ok_action=Return)
        call screen dialog("Good luck...\n\"Bacon\"...", ok_action=Return)
    if persistent.playername == "Jevil":
        call screen dialog("Why Jevil though?", ok_action=Return)
    if persistent.playername == "Link":
        call screen dialog("The Hero of Time reborn?", ok_action=Return)
    if persistent.playername == "Zelda":
        call screen dialog("Who's the princess here?!", ok_action=Return)
    if persistent.playername == "Ganondorf":
        call screen dialog("The Great King of Evil", ok_action=Return)
    if persistent.playername == "Ganon":
        call screen dialog("The Great King of Evil", ok_action=Return)
    if persistent.playername == "Jevil":
        call screen dialog("Why Jevil though?", ok_action=Return)
    if persistent.playthrough == 0:
        #Call example script
        call start_main

    #From here, we go to autoload which handles all the startup checks and sets
    jump ch30_autoload
    return

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
