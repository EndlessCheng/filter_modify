# -*- coding:utf-8 -*-

DEBUG = False

# A1(1-13), A2(13-23), A3(23-33), A4(33-40), A5(41-45)
# A6(45-50), A7(50-55), A8(55-61), A9(61-63), A10(64-65)
# Socket = 2 25 35 50(A7)

#
# Part 1 - Common
#

SSF_CRAFT_BASE_TYPE = ' '.join([
    #  '"Ceremonial Kite Shield"',  # 34
    #  '"Bronze Tower Shield"',  # 47
    #  '"Opal Sceptre"',  # 60
    '"Astral Plate"',  # 62
    '"Ezomyte Tower Shield"',  # 64
])
SSF_CRAFT_AMULETS_BASE_TYPE = ' '.join([  # 80+Life
    # '"Jade" "Turquoise"',
    '"Citrine"',
    # '"Amber Amulet"'
])

CURRENCY_WISDOM_FONT_SIZE = [38, 33, 18][0]

#
# Part 2 - A1-10
#
# NPC-4L
#

ALERT_RBB = False

MAGIC_BOOTS_IL = -1  # 10/20/-1 (25:Lv40, 30:Lv55)

ALERT_MAGIC_BASE_TYPE = ' '.join([
    # '"Amulet"',
    # '"Iron"',
    # '"Rustic Sash"',
    #  '"Leather Belt"',
    '"Ruby" "Topaz" "Sapphire"',
    '"Two-Stone"',
    '"Jade" "Turquoise" "Citrine" "Amber"',
    #  '"Layered Kite Shield" "Ceremonial Kite Shield"',
    #  '"Bronze Tower Shield" "Ezomyte Tower Shield"',
])

HIDE_LEVELING_RARE_CLASS = ' '.join(
    ['"Bows" "Quivers" "Two Hand" "Staves"', '"Claws" "One Hand"', '"Wands" "Daggers"'][:0])  # 0->1->0

ALERT_SCEPTRE = False
SHOW_FLASK_HALLOWED = False

SHOW_FLASK_LIFE = False

#
# Part 3 - A11
# Life: 70+(Rings), 80+(Amulets, Gloves, Boots), 90+(Helmets), 90-100+(Body Armour, Shields), 125+(Belts)
#

HIDE_ENDGAME_BELOW_T1_RARE_CLASS = ' '.join(
    ['"Bows" "Quivers" "Two Hand" "Staves" "One Hand" "Claws" "Shields" "Sceptres"',
     '"Body Armour"', '"Daggers" "Wands"', '"Boots" "Gloves" "Helmets"'][:0])  # 1->0->2

T1_RARE_BASE_TYPE = ' '.join([
    # '"Kite Shield"',
    '"Tower Shield"',
    '"Royal Burgonet" "Eternal Burgonet" "Ezomyte Burgonet"',
    '"Titan Gauntlets" "Crusader Gloves" "Vaal Gauntlets"',
    '"Titan Greaves" "Crusader Boots" "Vaal Greaves"',
    '"Sceptre" "Fetish" "Sekhem"',
    '"Ezomyte Tower Shield"',
    '"Astral Plate" "Glorious Plate" "Gladiator Plate"',
    '"Opal Sceptre" "Void Sceptre" "Fossilised Spirit Shield" "Archon Kite Shield"',  # MORE DAMAGE PLS
])

CURRENCY_ALERT_TRANSMUTATION = True
CURRENCY_PORTAL_FONT_SIZE = [40, 33, 18][0]
CURRENCY_ARMOURER_SCRAP_FONT_SIZE = [40, 33, 18][0]
NEED_RGB = True

ALERT_UTILITY_FLASK_BASE_TYPE = ' '.join(['"Quicksilver" "Silver" "Granite" "Sulphur" "Basalt"',
                                          '"Ruby Flask" "Sapphire Flask" "Topaz Flask" "Amethyst Flask"'][0:2])
CURRENCY_ALERT_BLACKSMITH = True and ALERT_UTILITY_FLASK_BASE_TYPE != ''  # Trade 8 for 1 glass

ALERT_JEWEL_BASE_TYPE = ' '.join(['"Viridian"', '"Crimson"', '"Cobalt"'][0:])  # 0->2
CURRENCY_ALERT_AUGMENTATION = True and ALERT_JEWEL_BASE_TYPE != ''
ALERT_SMALLS_RARE = True

ALERT_LOW_MAP = True
CURRENCY_ALERT_CHANCE = True and ALERT_LOW_MAP

ALERT_LOW_CURRENCY = True

#
# Part 4 - Others
#

SMALLS_MAX_IL = 8

RARE_BOOTS_ALERT = (MAGIC_BOOTS_IL != -1)

HIDE_NORMAL_MAGIC_CLASS = ' '.join(['"Gloves"', '"One Hand"'][:0])  # AS->1, DPS->2

SSF_CRAFT_BELTS_BASE_TYPE = ' '.join(['"Rustic Sash"', '"Leather Belt"'][0:])  # 125+Life

LEVELING_GEMS_BASE_TYPE = ' '.join(
    ['"Melee Splash" "Added Fire Damage"',
     '"Orb of Storms" "Clarity" "Flame Dash" "Scorching Ray" "Arctic Armour" "Elemental Focus"',
     '"Immortal" "Channelling" "Taken"',
     ][0:]) if ALERT_SCEPTRE else ''

if ALERT_SCEPTRE:
    SSF_CRAFT_BASE_TYPE += ' "Crystal Sceptre" '

HIDE_FLASK_MANA = not SHOW_FLASK_HALLOWED or not SHOW_FLASK_LIFE

LINKED_CLASS = ' '.join(['"Boots"', '"Body Armour"', '"Gloves" "Helmets"'][1:])
SHOW_ENDGAME_4L = True

CHANCING_BASE_TYPE = ''
if not ALERT_LOW_CURRENCY:
    CHANCING_BASE_TYPE += ' '.join(['"Glorious Plate"', ][:])

SSF_CRAFT_RINGS_BASE_TYPE = ' '.join(['"Two-Stone"'][:])  # 70+Life

# Ring-Amulet-Belt's T1-Life >= 44(A6), 54(A8), 64(A10)
# Resistance = 12x : Fire12-48, Lighting13-49, Cold14-50

# Essence = (1-46 12-66 30 48 68) = 12 30 47 48 67 68

# Ex >= 35(A4)
