# -*- coding:utf-8 -*-

DEBUG = False

# A1( 1-13), A2(13-23), A3(23-33), A4(33-40), A 5(41-45)
# A6(45-50), A7(50-55), A8(55-61), A9(61-63), A10(64-65)

# Socket = 2 25 35 50(A3C)
# Ex >= 35(A4N)
# Ring-Amulet-Belt's T1-Life >= 44(A2C), 54(A4C), 64(A3M)
# Resistance = 12x : Fire12-48, Lighting13-49, Cold14-50

#
# 第一部分：1-64
#

# Tips: 4L 跑鞋点蜕变
MAGIC_BOOTS_ITEM_LEVEL = {10: None, 15: '>= 15', 20: '>= 30', 30: '>= 55', -1: '< 1'}[10]

SSF_CRAFT_AMULETS_BASE_TYPE = ' '.join(['"Agate" "Lapis" "Turquoise"', '"Citrine" "Jade" "Turquoise"', '"Gold"'][:-1])
SSF_CRAFT_BELTS_BASE_TYPE = ' '.join(['"Rustic Sash"', '"Leather Belt"'][0:])

ALERT_MAGIC_SMALLS_BASE_TYPE = ' '.join(['"Rustic Sash"', '"Ruby" "Topaz" "Sapphire"', '"Two-Stone"', '"Amulet"'][0:])

CURRENCY_ALERT_BLACKSMITH = True
CURRENCY_ALERT_TRANSMUTATION = True
CURRENCY_PORTAL_SCROLL_FONT_SIZE = [33, 30, 18][0]
CURRENCY_WISDOM_SCROLL_FONT_SIZE = [33, 18][0]
CURRENCY_ARMOURER_SCRAP_FONT_SIZE = [33, 18][0]

HALLOWED_MAX_ITEM_LEVEL = [50, 1][0]  # 不推荐写成隐藏的方式
HIDE_FLASK_LIFE = False
HIDE_NORMAL_MAGIC_CLASS = ''  # + ' "Two Hand" '
LEVELING_GEMS_BASE_TYPE = ' '.join(
    ['"Melee Splash" "Added Fire Damage" "Firestorm"',
     '"Orb of Storms" "Clarity" "Scorching Ray" "Arctic Armour" "Blasphemy"',
     '"Cast when Damage Taken" "Immortal Call" "Increased Duration"'][0:]) if HALLOWED_MAX_ITEM_LEVEL != 1 else ''

HIDE_LEVELING_RARE_CLASS = ' '.join(
    ['"Bows" "Quivers" "One Hand" "Claws" "Two Hand Swords" "Staves"', '"Two Hand"'][:0])

#
# 第二部分：65+
#

NEED_MAP = True

NEED_RGB = True

CURRENCY_ALERT_AUGMENTATION = True
CURRENCY_ALERT_CHANCE = True

# TODO: add socket color?
SHOW_ENDGAME_4L = True

# "Hubris Circlet" "Vaal Regalia"  "Astral Plate"  "Opal Sceptre" "Void Sceptre"
# *直接点金*
SSF_CRAFT_BASE_TYPE = '' + ' "Opal Sceptre" "Void Sceptre" ' + ' "Astral Plate" ' + ' "Crystal Sceptre" '
SSF_MAGIC_BASE_TYPE = '' + ' "Opal Sceptre" "Void Sceptre" ' + ' "Crystal Sceptre" "Abyssal Sceptre" ' + ' "Shadow Sceptre" "Lead Sceptre" "Blood Sceptre" "Royal Sceptre" "Karui Sceptre" "Tyrant\'s Sekhem" '

ALERT_T1_RARE_BASE_TYPE = ''  # + ' "Vaal Regalia" '

ALERT_T2_RARE_BASE_TYPE = '' + ' "Astral Plate" "Opal Sceptre" "Void Sceptre" "Opal Wand" "Tornado Wand" "Prophecy Wand" '
ALERT_RARE_BASE_TYPE = ALERT_T1_RARE_BASE_TYPE + ALERT_T2_RARE_BASE_TYPE + SSF_MAGIC_BASE_TYPE

# "Two Hand Swords"  "Body Armour"  "Boots" "Gloves" "Helmets"
HIDE_ENDGAME_BELOW_T2_RARE_CLASS = ' '.join(
    ['"Bows" "Quivers" "One Hand" "Claws" "Two Hand" "Staves"', '"Shields"', '"Sceptres"', '"Wands"', '"Daggers"'][:5])

#
# 第三部分：（大致）固定内容
#

RARE_BOOTS_ALERT = (MAGIC_BOOTS_ITEM_LEVEL != '< 1')

SMALLS_NORMAL_MAX_IL = 9
SMALLS_MAGIC_MAX_IL = 23
# USELESS_RARE_MAX_IL = 23
# "Sapphire" "Topaz" "Ruby" "Two-Stone" (8 12 16 20)
SSF_CRAFT_RINGS_BASE_TYPE = '' + ' "Two-Stone" '

# L4_SPECIAL_NORMAL_MAX_IL = 64
# L4_SPECIAL_MAGIC_MAX_IL = 55
L4_RARE_MAX_IL = 64
# L4_MAX_IL = 40
LINKED_CLASS = '' + ' "Gloves" "Helmets" ' + ' "Boots" ' + ' "Body Armour" '

# CHANCING_ITEM_BASE_TYPE = '"Sorcerer Boots"'

# "Ruby Flask" "Sapphire Flask" "Topaz Flask" "Amethyst Flask"
ALERT_UTILITY_FLASK_BASE_TYPE = '' + ' "Quicksilver" "Bismuth" "Stibnite" "Silver" "Granite" "Sulphur" "Basalt" '

# "Vaal Axe" "Coronal Maul" "Harbinger Bow"
T2_BIG_WEAPON_BASE_TYPE = ''
# "Assassin\'s Garb" "Glorious Plate" "Astral Plate" "Spike-Point Arrow Quiver"
T2_BIG_ARM_BASE_TYPE = '' + ' "Colossal Tower Shield" "Pinnacle Tower Shield" '

# "Fencer Helm" "Lacquered Helmet" "Bascinet"
# "Sharkskin Gloves" "Shagreen Gloves" "Stealth Gloves" "Slink Gloves"
# "Sharkskin Boots" "Shagreen Boots" "Stealth Boots" "Slink Boots" "Wyrmscale Boots" "Hydrascale Boots" "Dragonscale Boots"
# ONLY_HIGHLIGHT_RARE_SMALL_ARMOUR_BASE_TYPE = '' + ' "Siege Helmet" "Samite Helmet" "Burgonet"   "Gauntlets"  "Greaves" '

# "General\'s Brigandine" "Triumphant Lamellar"
# ONLY_HIGHLIGHT_RARE_BODY_ARMOUR_BASE_TYPE = '' + ' "Plate" '

# ONLY_HIGHLIGHT_RARE_SHIELD_BASE_TYPE = ''

# >= 2
HIDE_NORMAL_CLASS = ''  # + ' "Two Hand" '

HIDE_FLASK_MANA = (HALLOWED_MAX_ITEM_LEVEL == 1) or HIDE_FLASK_LIFE

ALERT_JEWEL_BASE_TYPE = ' '.join(['"Cobalt"', '"Crimson"', '"Viridian"'][:])

# Essence = (1-46 12-66 30 48 68) = 12 30 47 48 67 68
