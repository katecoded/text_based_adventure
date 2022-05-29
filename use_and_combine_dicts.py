from objects.item import Item

eight_ball_list = ["It is certain.", "It it's decidedly so.", "Without a doubt.",
                   "Yes definitely.", "You may rely on it.", "As I see it, yes.",
                   "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
                   "Reply hazy, try again", "Ask again later.", "Better not tell you now.",
                   "Cannot predict now.", "Concentrate and ask again.",
                   "Don't count on it.", "My reply is no.", "My sources say no.",
                   "Outlook not so good.", "Very doubtful."]

use_dict = {
    ("magic 8-ball", None): (eight_ball_list, None),
    ("red potion", "mass of mushrooms"): (["Pouring the red potion on the mass of mushroom seems to have had an "
                                           "effect. After a few seconds a section starts shrinking, leaving enough "
                                           "room for you to pass"], "annex entryway"),
    ("mounted telescope", "stone pedestal"): (["As you place align the telescope's legs into the small indentations "
                                               "in the pedestal you feel a tremor. Suddenly a section of the west "
                                               "wall starts shifting, moving downwards into the floor. Slowly, a "
                                               "a passageway wide enough for a person is revealed in the stone."],
                                              "tower entrance"),
    ("tube of paste", "rusty sword"): (["You apply the paste to the sword. To your astonishment the rust simply falls "
                                        "away as if it were a layer of dust, and the sword regains the luster it had "
                                        "before."], "shiny sword"),
    ("examine", "rubble"): (["Sifting through the rubble you notice something wooden underneath. You take a few "
                             "minutes to move the stone away, and you find a trap door."], "trapdoor"),
    ("examine", "weapon rack"): (["Actually, on closer look, there are a few metal rods here that don't seem to be"
                                  "weapons of any kind. In fact you've seen rods like these before. Some kind of "
                                  "tripod legs?"], "tripod parts"),
    ("examine", "mysterious bushes"): (["As you are about to walk away you focus on one bush in particular. You think "
                                        "the berries here looks familiar. After looking closer you confirm that this "
                                        "is actually a blackberry bush"], "blackberry bushes"),
    ("examine", "blackberry bushes"): (["You poke gingerly at the blackberries, then pop one into your mouth. Yup, "
                                        "definitely blackberries. You think you can pick some."], "blackberries")
}

hint_scroll = Item("awakened rune scroll", "Although you cannot read the runes, suddenly you feel as if you understand "
                                           "exactly what is written inside, as if the scroll itself is trying to tell "
                                           "you something: \n\'The curious wizard, seeking power divine,\n yearned "
                                           "to find order in the night sky.\n Yet as the stars did align,\n his haste  "
                                           "caused his plans to go awry.\n Lost in madness\n his prized telescope in "
                                           "two did break\n To cure his sadness\n return to the tower and fix his "
                                           "mistake \'\n What could this mean?", True)

telescope = Item("mounted telescope", "At first glance, the telescope seems like it wouldn't have much power. Yet as "
                                      "you try and use it to see something at distance you realize it is capable of "
                                      "showing great deal. Perhaps it is quite magical", True)

gold_key = Item("gold key", "A gold that seems to be made of pure gold. You think to bite it to make sure, but "
                            "decide against it. Somehow you feel it would leave teethmarks and you don't want "
                            "to damage it", True, "key")

combine_dict = {
    ("small telescope", "tripod parts"): telescope,
    ("scroll of runes", "teal gem"): hint_scroll,
    ("gold potion", "flower"): gold_key
}
