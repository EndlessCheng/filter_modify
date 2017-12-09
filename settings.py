# -*- coding:utf-8 -*-

DEBUG = False

TENCENT = False

# A1(1-13), A2(13-23), A3(23-33), A4(33-40), A5(41-45)
# A6(45-50), A7(50-55), A8(55-61), A9(61-63), A10(64-65)
# Socket = 2 25 35 50(A7)

#
# Part 1 - Common
#


#
# Part 2 - A1-10
#
# >>> NPC-4L <<<
#

# Use some like >>> r-g <<< in the search box
MOVE_HAND_MAX_IL = 17  # RRG

L3_MAX_IL = 17  # 头脚3L

HIDE_NORMAL_MAGIC_CLASS = ' '.join([
    # '"Gloves"',
])

# 找血
ALERT_MAGIC_BASE_TYPE = ' '.join([
    '"Iron Ring"',
    '"Rustic Sash"',
    '"Stygian Vise"',
    '"Ruby Ring" "Topaz Ring" "Sapphire Ring"',
    '"Two-Stone Ring"',
    '"Amulet"',
    '"Turquoise Amulet" "Lapis Amulet" "Agate Amulet" "Onyx Amulet"',
    '"Siege Axe"',  # 59
    '"Behemoth Mace"',  # 70
])

HIDE_LEVELING_RARE_CLASS = ' '.join([
    #'"Bows" "Quivers" "Two Hand" "Staves" "Shields"',
    # '"Body Armour"',
    # '"Wands" "Daggers"',
])

SHOW_FLASK_HALLOWED = True

SHOW_FLASK_LIFE = True

SSF_CRAFT_BASE_TYPE = ' '.join([
    '"Siege Axe"',  # 59 73
    '"Astral Plate"',  # 62
    '"Royal Burgonet" "Eternal Burgonet"',  # 65 69
    '"Tiger Hook"',  # 70
])
SSF_CRAFT_AMULETS_BASE_TYPE = ' '.join([  # 80+Life
    '"Lapis" "Agate"',
])

CURRENCY_WISDOM_FONT_SIZE = [40, 33, 18][0]

LINKED_CLASS = ' '.join([
    '"Body Armour"',
    '"Helmets"',
    '"Gloves"',
    '"Boots"',
])

#
# Part 3 - Maps
# Life: 70+(Rings), 80+(Amulets, Gloves, Boots), 90+(Helmets), 90-100+(Body Armour, Shields), 125+(Belts)
#

SSF_CRAFT_BELTS_BASE_TYPE = ' '.join(['"Rustic Sash"', '"Leather Belt"', '"Stygian Vise"'][0:])  # 125+Life

SSF_CRAFT_RINGS_BASE_TYPE = ' '.join(['"Two-Stone"'][0:])  # 70+Life

T1_RARE_BASE_TYPE = ' '.join([
    '"Astral Plate" "Glorious Plate" "Gladiator Plate"',
    '"Royal Burgonet" "Eternal Burgonet" "Ezomyte Burgonet"',
    '"Tiger Hook"',

    '"Nightmare Mace" "Pernarch" "Legion Hammer" "Tenderizer" "Dragon Mace"',
    '"Infernal Axe" "Butcher Axe" "Karui Axe" "Engraved Hatchet" "Wraith Axe"',

    '"Behemoth Mace"',
    '"Siege Axe" "Vaal Hatchet" "Runic Hatchet"',
])

HIDE_ENDGAME_BELOW_T1_RARE_CLASS = ' '.join([
    '"Bows" "Quivers" "Two Hand" "Staves" "Shields"',
    # '"Body Armour"',
    # '"Sceptres" "Claws" "One Hand"',
    # '"Boots"',
    # '"Helmets"',
    # '"Gloves"',
    # '"Daggers" "Wands"',
])

NEED_RGB = True

CURRENCY_ALERT_TRANSMUTATION = True
CURRENCY_PORTAL_FONT_SIZE = [40, 33, 18][0]
CURRENCY_ARMOURER_SCRAP_FONT_SIZE = [40, 33, 18][0]

ALERT_UTILITY_FLASK_BASE_TYPE = ' '.join([
    '"Quicksilver" "Stibnite" "Granite" "Sulphur" "Basalt"',
    '"Ruby" "Sapphire" "Topaz" "Amethyst"',
])
CURRENCY_ALERT_BLACKSMITH = True and ALERT_UTILITY_FLASK_BASE_TYPE != ''  # Trade 8 for 1 glass

ALERT_JEWEL_BASE_TYPE = ' '.join([
    '"Crimson"',
    '"Viridian"',
    '"Cobalt"',
    '"Eye"',
])
CURRENCY_ALERT_AUGMENTATION = True and ALERT_JEWEL_BASE_TYPE != ''
ALERT_SMALLS_RARE = True

CURRENCY_ALERT_CHANCE = True

ALERT_LOW_CURRENCY = True

NEED_CHISEL = False

#
# Part 4 - Others
#

L2_MAX_IL = 4
# SMALLS_MAX_IL = 7

LEVELING_GEMS_BASE_TYPE = ' '.join([
    '"Clarity" "Concentrated Effect" "Fortify"',
    '"Immortal Call" "Cast when Damage Taken" "Multistrike"',
]) if SHOW_FLASK_HALLOWED else ''  # ALERT_SCEPTRE
#  "Orb of Storms" "Flame Dash" "Scorching Ray" "Arctic Armour" "Elemental Focus" "Channelling"

HIDE_FLASK_MANA = not SHOW_FLASK_HALLOWED or not SHOW_FLASK_LIFE

SHOW_ENDGAME_4L = False

CHANCING_BASE_TYPE = ''
if not ALERT_LOW_CURRENCY:
    CHANCING_BASE_TYPE += ' '.join(['"Glorious Plate"', '"Ezomyte Tower Shield"'][:])
    # "Ebony Tower Shield" "Glorious Plate" "Gold Amulet" "Rawhide Tower Shield" "Sorcerer Boots" "Full Wyrmscale"

ALERT_ESSENCE_BASE_TYPE = ' ' + '"Essence of Greed" "Essence of Zeal" "Essence of Contempt"'
# "Essence of Woe"

IGNORE_RARE_UNDER_T2 = False

MAGIC_BOOTS_IL = -1  # ★★★ 10/-1 (15:Lv15, 20:Lv30, 25:Lv40, 30:Lv55)  ★★★
RARE_BOOTS_ALERT = (MAGIC_BOOTS_IL != -1)
BBB_MAX_IL = 1  # NPC: BBB RBB        RRR RRB
ALERT_SCEPTRE = False
if ALERT_SCEPTRE:
    SSF_CRAFT_BASE_TYPE += ' "Crystal Sceptre" '

# Ring-Amulet-Belt's T1-Life >= 44(A6), 54(A8), 64(A10)
# Resistance = 12x : Fire12-48, Lighting13-49, Cold14-50

# Essence = (1-46 12-66 30 48 68) = 12 30 47 48 67 68

# Ex >= 35(A4)
