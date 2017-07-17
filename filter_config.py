# -*- coding:utf-8 -*-

DEBUG = False

NEW = False

# A1(1-13), A2(13-23), A3(23-33), A4(33-40), A5(41-45)
# A6(45-50), A7(50-55), A8(55-61), A9(61-63), A10(64-65)
# Socket = 2 25 35 50(A3C)

#
# Part 1 - Common
#

# '"Agate" "Lapis" "Turquoise"',
SSF_CRAFT_AMULETS_BASE_TYPE = ' '.join(['"Citrine" "Jade" "Turquoise"', '"Gold"', '"Amber Amulet"'][:1])  # 找80+血
SSF_CRAFT_BELTS_BASE_TYPE = ' '.join(['"Rustic Sash"', '"Leather Belt"'][:1])  # 找125+血

#
# Part 2 - Leveling
#

# 商店看看
ALERT_SWAP_SOCKET = False

SMALLS_NORMAL_MAX_IL = 9
SMALLS_MAGIC_MAX_IL = 23
HIDE_NORMAL_MAGIC_CLASS = ''  # + ' "Gloves" ' + ' "Two Hand" '

MAGIC_BOOTS_ITEM_LEVEL = {10: None, 15: '>= 15', 20: '>= 30', 30: '>= 55', -1: '< 1'}[30]

HALLOWED_MAX_ITEM_LEVEL = [50, 1][0]  # 不推荐写成隐藏的方式
SHOW_FLASK_LIFE = True

# "Elemental Focus" "Concentrated Effect" "Controlled Destruction" "Vortex" "Increased Critical Strikes"
LEVELING_GEMS_BASE_TYPE = ' '.join(
    ['"Melee Splash" "Added Fire Damage" "Firestorm"',
     '"Orb of Storms" "Clarity" "Flame Dash" "Scorching Ray" "Arctic Armour"',  # 在图书馆之前很需要的技能
     '"Increased Duration" "Blasphemy" "Fire Penetration" "Flame Golem" "Immortal" "Channelling" "Taken"',
     ][3:]) if HALLOWED_MAX_ITEM_LEVEL != 1 else ''
# LEVELING_GEMS_BASE_TYPE = '"Point Blank" "Concentrated Effect" "Physical Projectile Attack Damage" "Vortex" "Enfeeble"'

# 有两个抗性戒指找到点伤就隐藏->2
ALERT_MAGIC_SMALLS_BASE_TYPE = ' '.join(
    ['"Amulet"', '"Iron" "Ruby" "Topaz" "Sapphire"', '"Rustic Sash"', '"Two-Stone"', '"Citrine" "Jade" "Turquoise"'][
    0:])
ALERT_SCEPTRE = True
HIDE_LEVELING_RARE_CLASS = ' '.join(
    ['"Bows" "Quivers" "Two Hand Swords" "Claws" "One Hand"', '"Staves" "Two Hand"', '"Wands" "Daggers"'][:0])
CURRENCY_ALERT_BLACKSMITH = True

LINKED_CLASS = '' + ' "Gloves" "Helmets" ' + ' "Boots" ' + ' "Body Armour" '

#
# Part 3 - Endgame
# Life: 70+(Rings), 80+(Amulets, Gloves, Boots), 90+(Helmets), 100+(Body Armour, Shields), 125+(Belts)
#

CURRENCY_ALERT_TRANSMUTATION = False
CURRENCY_PORTAL_SCROLL_FONT_SIZE = [38, 33, 30, 18][1]
CURRENCY_WISDOM_SCROLL_FONT_SIZE = [38, 33, 30, 18][1]

SSF_CRAFT_RINGS_BASE_TYPE = ' '.join(['"Two-Stone"'][:])  # 找70+血

# *直接点金*
SSF_CRAFT_BASE_TYPE = ''  # + ' "Opal Sceptre" '  # + ' "Void Sceptre" ' #+ ' "Colossal Tower Shield" ' #+ ' "Astral Plate" '
# SSF_MAGIC_BASE_TYPE = ''

NEED_RGB = False

SHOW_ENDGAME_4L = True

ALERT_T1_RARE_BASE_TYPE = '' + ' "Opal Sceptre" "Void Sceptre" "Colossal Tower Shield" "Ezomyte Tower Shield" ' + ' "Astral Plate" ' + ' "Sceptre" "Fetish" "Sekhem" '
HIDE_OTHER_T1_RARES = True

# 修改T1.5，然后隐藏所有剩下的
T1_5_RARE_BASE_TYPE = '' + ' "Royal Burgonet" "Eternal Burgonet" ' + ' "Titan Gauntlets" "Crusader Gloves" ' + ' "Titan Greaves" "Crusader Boots" '
HIDE_OTHER_T1_5_RARES = False
CURRENCY_ARMOURER_SCRAP_FONT_SIZE = [38, 33, 18][1]
ALERT_LOW_CURRENCY = False

# "Two Hand Swords"  "Body Armour"  "Boots" "Gloves" "Helmets"
HIDE_ENDGAME_BELOW_T1_5_RARE_CLASS = ' '.join(
    ['"Body Armour" "Two Hand" "One Hand"',
     '"Bows" "Quivers" "Claws" "Staves" "Daggers" "Wands" "Sceptres"', ][1:])  # 0-1-0

NEED_MAP = True
CURRENCY_ALERT_CHANCE = NEED_MAP

#
# Part 4 - Others
#

RARE_BOOTS_ALERT = (MAGIC_BOOTS_ITEM_LEVEL != '< 1')

# USELESS_RARE_MAX_IL = 23


# L4_SPECIAL_NORMAL_MAX_IL = 64
# L4_SPECIAL_MAGIC_MAX_IL = 55
L4_RARE_MAX_IL = 64
# L4_MAX_IL = 40


# CHANCING_ITEM_BASE_TYPE = '"Sorcerer Boots"'

ALERT_UTILITY_FLASK_BASE_TYPE = '"Sulphur"'  # + ' "Quicksilver" "Granite" "Sulphur" "Basalt" ' + ' "Ruby Flask" "Sapphire Flask" "Topaz Flask" "Amethyst Flask" '

# "Vaal Axe" "Coronal Maul" "Harbinger Bow"
T2_BIG_WEAPON_BASE_TYPE = ''
# "Assassin\'s Garb" "Glorious Plate" "Astral Plate" "Spike-Point Arrow Quiver"
T2_BIG_ARM_BASE_TYPE = ''  # + ' "Colossal Tower Shield" "Pinnacle Tower Shield" '

# "Fencer Helm" "Lacquered Helmet" "Bascinet"
# "Sharkskin Gloves" "Shagreen Gloves" "Stealth Gloves" "Slink Gloves"
# "Sharkskin Boots" "Shagreen Boots" "Stealth Boots" "Slink Boots" "Wyrmscale Boots" "Hydrascale Boots" "Dragonscale Boots"
# ONLY_HIGHLIGHT_RARE_SMALL_ARMOUR_BASE_TYPE = '' + ' "Siege Helmet" "Samite Helmet" "Burgonet"   "Gauntlets"  "Greaves" '

# "General\'s Brigandine" "Triumphant Lamellar"
# ONLY_HIGHLIGHT_RARE_BODY_ARMOUR_BASE_TYPE = '' + ' "Plate" '

# ONLY_HIGHLIGHT_RARE_SHIELD_BASE_TYPE = ''

# >= 2
HIDE_NORMAL_CLASS = ''  # + ' "Two Hand" '

HIDE_FLASK_MANA = (HALLOWED_MAX_ITEM_LEVEL == 1) or not SHOW_FLASK_LIFE

ALERT_JEWEL_BASE_TYPE = ' '.join(['"Cobalt"', '"Crimson"', '"Viridian"'][3:])

if ALERT_SCEPTRE:
    SSF_CRAFT_BASE_TYPE += ' "Crystal Sceptre" '
    # SSF_MAGIC_BASE_TYPE += ' "Opal Sceptre" "Void Sceptre" ' + ' "Crystal Sceptre" "Abyssal Sceptre" ' + ' "Shadow Sceptre" "Lead Sceptre" "Blood Sceptre" "Royal Sceptre" "Karui Sceptre" "Tyrant\'s Sekhem" '

# Essence = (1-46 12-66 30 48 68) = 12 30 47 48 67 68


CURRENCY_ALERT_AUGMENTATION = False

# Ex >= 35(A4N)
# Ring-Amulet-Belt's T1-Life >= 44(A2C), 54(A4C), 64(A3M)
# Resistance = 12x : Fire12-48, Lighting13-49, Cold14-50
