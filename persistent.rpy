#This is for anything that must happen CONSTANTLY in game.
label monikareturn:
    python:
        try: renpy.file(config.basedir + "../(monika).chr")
        except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
    return
