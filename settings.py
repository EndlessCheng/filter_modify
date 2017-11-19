# -*- coding:utf-8 -*-

DEBUG = False

# A1(1-13), A2(13-23), A3(23-33), A4(33-40), A5(41-45)
# A6(45-50), A7(50-55), A8(55-61), A9(61-63), A10(64-65)
# Socket = 2 25 35 50(A7)

#
# Part 1 - Common
#


#
# Part 2 - A1-10
#
# NPC-4L ?
#

MOVE_HAND_MAX_IL = 17  # RRG

L2_MAX_IL = 7
L3_MAX_IL = 17

MAGIC_BOOTS_IL = 10  # ★★★ 10/20/-1 (15:Lv15, 20:Lv30, 25:Lv40, 30:Lv55)  ★★★

HIDE_NORMAL_MAGIC_CLASS = ' '.join([
    # '"Gloves"',
])
# '"One Hand"',

ALERT_MAGIC_BASE_TYPE = ' '.join([
    '"Iron Ring"',
    '"Rustic Sash"',
    '"Leather Belt"',
    '"Ruby Ring" "Topaz Ring" "Sapphire Ring"',
    '"Two-Stone Ring"',
    '"Amulet"',
    '"Turquoise Amulet" "Lapis Amulet" "Agate Amulet" "Onyx Amulet"',
    '"Siege Axe"',  # 59
    '"Behemoth Mace"',  # 70
])
# '"Layered Kite Shield" "Ceremonial Kite Shield"', '"Bronze Tower Shield"', '"Ezomyte Tower Shield"',
# '"Jade" "Turquoise" "Citrine" "Amber"',

HIDE_LEVELING_RARE_CLASS = ' '.join([
    # '"Bows" "Quivers" "Two Hand" "Staves"',
    # '"Shields"',  # !!!
    # '"Body Armour"',
    # '"Wands" "Daggers"',
])
# '"Claws" "One Hand"',

SHOW_FLASK_HALLOWED = True

SHOW_FLASK_LIFE = True

SSF_CRAFT_BASE_TYPE = ' '.join([
    '"Siege Axe"',  # 59
    '"Astral Plate"',  # 62
    '"Royal Burgonet" "Eternal Burgonet"',  # 65 69
])
# '"Ceremonial Kite Shield"',  # 34     '"Bronze Tower Shield"',  # 47
# '"Karui Sceptre"',  # 56, 1.65AS!!!    '"Opal Sceptre"',  # 60    '"Ezomyte Tower Shield"',  # 64
SSF_CRAFT_AMULETS_BASE_TYPE = ' '.join([  # 80+Life
    '"Jade"',
    '"Turquoise"',
])
# ' "Citrine"', '  "Amber"',

CURRENCY_WISDOM_FONT_SIZE = [40, 33, 18][0]

LINKED_CLASS = ' '.join([
    # '"Boots"',
    '"Body Armour"',
    '"Gloves"',
    '"Helmets"',
])

#
# Part 3 - Maps
# Life: 70+(Rings), 80+(Amulets, Gloves, Boots), 90+(Helmets), 90-100+(Body Armour, Shields), 125+(Belts)
#

SSF_CRAFT_BELTS_BASE_TYPE = ' '.join(['"Rustic Sash"', '"Leather Belt"'][0:])  # 125+Life

SSF_CRAFT_RINGS_BASE_TYPE = ' '.join(['"Two-Stone"'][0:])  # 70+Life

T1_RARE_BASE_TYPE = ' '.join([
    '"Astral Plate" "Glorious Plate" "Gladiator Plate"',
    '"Royal Burgonet" "Eternal Burgonet" "Ezomyte Burgonet"',

    '"Siege Axe"',
    '"Behemoth Mace"',

    # '"Archon Kite Shield"',
    # '"Ezomyte Tower Shield"',
    # '"Opal Sceptre" "Void Sceptre" "Karui Sceptre" "Vaal Sceptre"',
    # '"Fossilised Spirit Shield" "Ivory Spirit Shield" "Bone Spirit Shield"'
])
# '"Kite Shield"', '"Tower Shield"', '"Sceptre" "Fetish" "Sekhem"', '"Spirit Shield"',
# '"Crusader Gloves" "Legion Gloves" "Soldier Gloves"',
# '"Crusader Boots" "Legion Boots" "Soldier Boots" "Zealot Boots" "Riveted Boots"',

HIDE_ENDGAME_BELOW_T1_RARE_CLASS = ' '.join([
    '"Bows" "Quivers" "Two Hand" "Staves" "Shields"',
    # '"Body Armour"',
    # '"Sceptres"',
    # '"Claws" "One Hand"',
    # '"Gloves"',
    # '"Boots"',
    # '"Helmets"',
    # '"Daggers" "Wands"',
])

NEED_RGB = True

CURRENCY_ALERT_TRANSMUTATION = True
CURRENCY_PORTAL_FONT_SIZE = [40, 33, 18][0]
CURRENCY_ARMOURER_SCRAP_FONT_SIZE = [40, 33, 18][0]

ALERT_UTILITY_FLASK_BASE_TYPE = ' '.join([
    '"Silver"',
    '"Quicksilver" "Granite" "Sulphur" "Basalt"',
    '"Ruby Flask" "Sapphire Flask" "Topaz Flask" "Amethyst Flask"',
])
CURRENCY_ALERT_BLACKSMITH = True and ALERT_UTILITY_FLASK_BASE_TYPE != ''  # Trade 8 for 1 glass

ALERT_JEWEL_BASE_TYPE = ' '.join([
    '"Crimson"',
    '"Viridian"',
    '"Cobalt"',
])
CURRENCY_ALERT_AUGMENTATION = True and ALERT_JEWEL_BASE_TYPE != ''
ALERT_SMALLS_RARE = True

ALERT_LOW_MAP = True
CURRENCY_ALERT_CHANCE = True and ALERT_LOW_MAP

ALERT_LOW_CURRENCY = True

NEED_CHISEL = False

#
# Part 4 - Others
#

BBB_MAX_IL = 1  # NPC: BBB RBB        RRR RRB

SMALLS_MAX_IL = 7

RARE_BOOTS_ALERT = (MAGIC_BOOTS_IL != -1)

LEVELING_GEMS_BASE_TYPE = ' '.join([
    '"Melee Splash" "Added Fire Damage" "Maim"',
    '"Clarity" "Concentrated Effect"',
    '"Immortal" "Taken" "Multistrike"',
]) if SHOW_FLASK_HALLOWED else ''  # ALERT_SCEPTRE
#  "Orb of Storms" "Flame Dash" "Scorching Ray" "Arctic Armour" "Elemental Focus" "Channelling"

ALERT_SCEPTRE = False

if ALERT_SCEPTRE:
    SSF_CRAFT_BASE_TYPE += ' "Crystal Sceptre" '

HIDE_FLASK_MANA = not SHOW_FLASK_HALLOWED or not SHOW_FLASK_LIFE

SHOW_ENDGAME_4L = False

CHANCING_BASE_TYPE = ''
if not ALERT_LOW_CURRENCY:
    CHANCING_BASE_TYPE += ' '.join(['"Glorious Plate"', '"Ezomyte Tower Shield"'][:])

ALERT_ESSENCE_BASE_TYPE = ' ' + '"Essence of Greed" "Essence of Zeal" "Essence of Contempt"'
# "Essence of Woe"

# Ring-Amulet-Belt's T1-Life >= 44(A6), 54(A8), 64(A10)
# Resistance = 12x : Fire12-48, Lighting13-49, Cold14-50

# Essence = (1-46 12-66 30 48 68) = 12 30 47 48 67 68

# Ex >= 35(A4)
