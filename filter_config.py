# -*- coding:utf-8 -*-

DEBUG = False

# A1(1-13), A2(13-23), A3(23-33), A4(33-40), A5(41-45)
# A6(45-50), A7(50-55), A8(55-61), A9(61-63), A10(64-65)
# Socket = 2 25 35 50(A7)

#
# Part 1 - Common
#

SSF_CRAFT_AMULETS_BASE_TYPE = ' '.join(['"Jade" "Turquoise"', '"Citrine"', '"Amber Amulet"'][2:])  # 80+Life
CURRENCY_WISDOM_FONT_SIZE = [38, 33, 18][1]

#
# Part 2 - A1-10
# Set all = True when new
# NPC-4L
#

ALERT_RRG = False
ALERT_RBB = False

MAGIC_BOOTS_IL = -1  # 10/20/30/-1

HIDE_NORMAL_MAGIC_CLASS = ' '.join(['"Gloves"', '"One Hand"'][:0])  # AS->1, DPS->2

# +Dex->1, +Phy&Res->2/3, +Life&Res belt->4, +Life&Res Rings->5, +Life&Res Amulet->6
ALERT_MAGIC_SMALLS_BASE_TYPE = ' '.join(
    ['"Amulet"', '"Iron" "Ruby" "Topaz" "Sapphire"', '"Rustic Sash"', '"Leather Belt"',
     '"Two-Stone"', '"Jade" "Turquoise" "Citrine" "Amber"'][4:])

HIDE_LEVELING_RARE_CLASS = ' '.join(
    ['"Bows" "Quivers" "Two Hand" "Staves"', '"Claws" "One Hand"', '"Wands" "Daggers"'][:2])

ALERT_SCEPTRE = False
SHOW_FLASK_HALLOWED = False

SHOW_FLASK_LIFE = False



#
# Part 3 - A11
# Life: 70+(Rings), 80+(Amulets, Gloves, Boots), 90+(Helmets), 90-100+(Body Armour, Shields), 125+(Belts)
#

CURRENCY_ALERT_TRANSMUTATION = True
CURRENCY_PORTAL_FONT_SIZE = [40, 33, 18][0]
CURRENCY_ARMOURER_SCRAP_FONT_SIZE = [40, 33, 18][0]

SSF_CRAFT_BASE_TYPE = ' '.join(['"Opal Sceptre"', '"Astral Plate"', '"Ezomyte Tower Shield"'][1:3])
SSF_CRAFT_RINGS_BASE_TYPE = ' '.join(['"Two-Stone"'][:])  # 70+Life

T1_RARE_BASE_TYPE = ' '.join(['"Opal Sceptre" "Void Sceptre" ',
                              # '"Colossal Tower Shield" "Ezomyte Tower Shield" "Girded Tower Shield" "Pinnacle Tower Shield"',
                              '"Astral Plate" "Glorious Plate" "Gladiator Plate"',
                              '"Sceptre" "Fetish" "Sekhem"',
                              '"Tower Shield"'][:4])
SHOW_OTHER_T1_RARES = True

HIDE_ENDGAME_BELOW_T1_RARE_CLASS = ' '.join(
    ['"Bows" "Quivers" "Two Hand" "Staves" "One Hand" "Claws"', '"Daggers" "Wands"',
     '"Body Armour"', '"Boots" "Gloves" "Helmets" "Shields" "Sceptres"'][:1])  # default = [:1]

T2_RARE_BASE_TYPE = ' '.join(['"Royal Burgonet" "Eternal Burgonet" "Ezomyte Burgonet"',
                              '"Titan Gauntlets" "Crusader Gloves" "Vaal Gauntlets"',
                              '"Titan Greaves" "Crusader Boots" "Vaal Greaves"'][:])
SHOW_OTHER_T2_RARES = True

NEED_RGB = True

ALERT_UTILITY_FLASK_BASE_TYPE = ' '.join(['"Quicksilver" "Silver" "Granite" "Sulphur" "Basalt"',
                                          '"Ruby Flask" "Sapphire Flask" "Topaz Flask" "Amethyst Flask"'][0:2])
CURRENCY_ALERT_BLACKSMITH = True and ALERT_UTILITY_FLASK_BASE_TYPE != ''  # Trade 8 for 1 glass

ALERT_JEWEL_BASE_TYPE = ' '.join(['"Viridian"', '"Crimson"', '"Cobalt"'][0:])  # 0->2
CURRENCY_ALERT_AUGMENTATION = True and ALERT_JEWEL_BASE_TYPE != ''  # Jewel
ALERT_SMALLS_RARE = True

ALERT_LOW_MAP = True
CURRENCY_ALERT_CHANCE = True and ALERT_LOW_MAP

ALERT_LOW_CURRENCY = True

#
# Part 4 - Others
#

SMALLS_MAX_IL = 8

RARE_BOOTS_ALERT = (MAGIC_BOOTS_IL != -1)

SSF_CRAFT_BELTS_BASE_TYPE = ' '.join(['"Rustic Sash"', '"Leather Belt"'][0:])  # 125+Life

LEVELING_GEMS_BASE_TYPE = ' '.join(
    ['"Melee Splash" "Added Fire Damage"',
     '"Orb of Storms" "Clarity" "Flame Dash" "Scorching Ray" "Arctic Armour" "Elemental Focus"',
     '"Vortex" "Increased Duration" "Blasphemy" "Immortal" "Channelling" "Taken"',
     ][0:]) if ALERT_SCEPTRE else ''

if ALERT_SCEPTRE:
    SSF_CRAFT_BASE_TYPE += ' "Crystal Sceptre" '

HIDE_FLASK_MANA = not SHOW_FLASK_HALLOWED or not SHOW_FLASK_LIFE

LINKED_CLASS = ' '.join(['"Boots"', '"Body Armour"', '"Gloves" "Helmets"'][1:])
SHOW_ENDGAME_4L = True

CHANCING_BASE_TYPE = ''
if not ALERT_LOW_CURRENCY:
    CHANCING_BASE_TYPE += ' '.join(['"Glorious Plate"', ][:])

# Ring-Amulet-Belt's T1-Life >= 44(A6), 54(A8), 64(A10)
# Resistance = 12x : Fire12-48, Lighting13-49, Cold14-50

# Essence = (1-46 12-66 30 48 68) = 12 30 47 48 67 68

# Ex >= 35(A4)
