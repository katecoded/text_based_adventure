from objects.item import Item

eight_ball_list = ["It is certain.", "It it's decidedly so.", "Without a doubt.",
                   "Yes definitely.", "You may rely on it.", "As I see it, yes.",
                   "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
                   "Reply hazy, try again", "Ask again later.", "Better not tell you now.",
                   "Cannot predict now.", "Concentrate and ask again.",
                   "Don't count on it.", "My reply is no.", "My sources say no.",
                   "Outlook not so good.", "Very doubtful."]

use_dict = {
    ("magic 8-ball", None): (eight_ball_list, None, False, False),
    ("red potion", "mass of mushrooms"): (["Pouring the red potion on the mass of mushroom seems to have had an "
                                           "effect. After a few seconds, a section starts shrinking, leaving enough "
                                           "room for you to pass through."], "annex entryway", True, True),
    ("mounted telescope", "stone pedestal"): (["As you place align the telescope's legs into the small indentations "
                                               "in the pedestal, you feel a tremor. Suddenly, a section of the west "
                                               "wall starts shifting, moving downwards into the floor. Slowly, a "
                                               "passageway wide enough for a person is revealed in the stone."],
                                              "tower entrance", False, False),
    ("tube of paste", "rusty sword"): (["You apply the paste to the sword. To your astonishment, the rust simply falls "
                                        "away as if it were a layer of dust, and the sword regains the luster it had "
                                        "before."], "shiny sword", True, False),
    ("torch", "cast-iron stove"): (["Sticking the torch inside the stove causes the dry wood inside to catch aflame. "
                                    "Waiting for a couple of seconds causes the flame to grow into a sizeable fire, "
                                    "turning the stove on"], "lit cast-iron stove", True, False),
    ("empty potion bottle", "metal pan"): (["Gingerly, you dip the potion bottle into the liquid inside the pan. This "
                                            "doesn't seem particularly safe, but you don't really have any better way "
                                            "to go about it. The bottle fills with the golden liquid, producing a "
                                            "golden potion. The hotness of the bottle makes you drop the bottle, but "
                                            "thankfully it lands safely on a pile of scattered flower left over by "
                                            "the cooks."], "golden potion", False, True),
    ("blackberries", "frowning blue-haired fairy"): (["\"Thank you!\" the fairy exclaims as she hurriedly sets to work on the "
                                                      "blackberry cobbler. \"In case you haven't found it, I think I dropped "
                                                      "the key to the potion room in the pile of cookbooks. You can have it "
                                                      "for your help!\""], "busy blue-haired fairy", True, True),
    ("ghost", "annoyed stern-looking ghost"): (["\"Thank you for bringing Snoozes to me.\" says the stern-looking ghost. "
                                                "\"You know, I read in one of these potions books that combining a gem with "
                                                "a rune scroll can activate it or some "
                                                "such thing.\""], "stern-looking ghost", True, True),
    ("shiny sword", "rock"): (["While thinking: \"I've seen this in a movie!\" you stab the sword into the rock. To "
                               "you surprise, not only does the sword stick but a deep rumbling can be felt as if the "
                               "very foundations of the castle were giving way. As the rumbling subsides, you look at "
                               "the wall ahead and find that a doorway has opened up."], "mysterious door", False, False),
    ("examine", "rubble"): (["Sifting through the rubble, you notice something wooden underneath. You take a few "
                             "minutes to move the stone away, and you find a trapdoor."], "trapdoor", False, False),
    ("examine", "weapon rack"): (["On closer inspection, there are a few metal rods here that don't seem to be"
                                  "weapons of any kind. In fact, you've seen rods like these before - they look like "
                                  "the legs of a tripod. Perhaps they go to something?"], "tripod parts", False, False),
    ("examine", "potion rack"): (["After scanning the potions bottles a bit, you do find one that looks intact."],
                                 "empty potion bottle", False, False),
    ("examine", "lit cast-iron stove"): (["The contents of the pan seem to have liquefied due to the heat, and are now "
                                          "bubbling."], "metal pan", False, False),
    ("examine", "mysterious bushes"): (["As you are about to walk away, you focus on one bush in particular. You think "
                                        "the berries here looks familiar. After looking closer, you confirm that this "
                                        "one is actually a blackberry bush."], "blackberry bush", False, False),
    ("examine", "blackberry bush"): (["You poke gingerly at the blackberries, then pop one into your mouth. Yup, "
                                     "definitely blackberries. You think you can pick some."], "blackberries", False, False),
    ("examine", "stack of cookbooks"): (["Digging through the pile causes a copper key to fall "
                                        "to the floor."], "copper key", False, False),
    ("examine", "basket"): (["Looking inside the basket, you only see a single normal egg. Is that it?"], "egg", False, False)
}

hint_scroll = Item("awakened rune scroll", "Although you cannot read the runes, suddenly you feel as if you understand "
                                           "exactly what is written inside, as if the scroll itself is trying to tell "
                                           "you something: \n\'The curious wizard, seeking power divine,\n yearned "
                                           "to find order in the night sky.\n Yet as the stars did align,\n their "
                                           "haste caused their plans to go awry.\n Lost in madness\ntheir prized "
                                           "telescope in two did break\n To cure their sadness\n return to the tower "
                                           "and fix their mistake\'\n What could this mean?", True)

telescope = Item("mounted telescope", "At first glance, the telescope seems like it wouldn't have much power. Yet as "
                                      "you try and use it to see something in the distance, you realize it is capable "
                                      "of showing a great deal. Perhaps it is quite magical.", True)

gold_key = Item("golden key", "A key that seems to be made of pure gold. You think to bite it to make sure, but "
                              "decide against it. Somehow you feel it would leave teethmarks and you don't want "
                              "to damage it", True, "key")

combine_dict = {
    ("small telescope", "tripod parts"): telescope,
    ("scroll of runes", "teal gem"): hint_scroll,
    ("golden potion", "flower"): gold_key
}
