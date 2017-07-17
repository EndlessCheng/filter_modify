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
ALERT_SWAP_SOCKET = True

SMALLS_NORMAL_MAX_IL = 9
SMALLS_MAGIC_MAX_IL = 23
HIDE_NORMAL_MAGIC_CLASS = ''  # + ' "Gloves" '  # + ' "Two Hand" '

MAGIC_BOOTS_ITEM_LEVEL = {10: None, 15: '>= 15', 20: '>= 30', 30: '>= 55', -1: '< 1'}[10]

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

LINKED_CLASS = '' + ' "Gloves" "Helmets" ' + ' "Body Armour" '  # + ' "Boots" '

#
# Part 3 - Endgame
# Life: 70+(Rings), 80+(Amulets, Gloves, Boots), 90+(Helmets), 90-100+(Body Armour, Shields), 125+(Belts)
#

CURRENCY_WISDOM_SCROLL_FONT_SIZE = [38, 33, 18][0]
CURRENCY_ALERT_TRANSMUTATION = True
CURRENCY_PORTAL_SCROLL_FONT_SIZE = [38, 33, 18][0]

SSF_CRAFT_BASE_TYPE = '' + ' "Opal Sceptre" ' + ' "Colossal Tower Shield" ' + ' "Astral Plate" '
SHOW_ENDGAME_4L = True
SSF_CRAFT_RINGS_BASE_TYPE = ' '.join(['"Two-Stone"'][:])  # 找70+血

ALERT_T1_RARE_BASE_TYPE = ' '.join(['"Opal Sceptre" "Void Sceptre" ',
                                    '"Colossal Tower Shield" "Ezomyte Tower Shield" "Girded Tower Shield" "Pinnacle Tower Shield"',
                                    '"Astral Plate" "Glorious Plate" "Gladiator Plate"',
                                    '"Sceptre" "Fetish" "Sekhem"'][:])
HIDE_OTHER_T1_RARES = True

HIDE_OTHER_T1_5_RARES = True
CURRENCY_ARMOURER_SCRAP_FONT_SIZE = [38, 33, 18][0]
ALERT_LOW_CURRENCY = True
CURRENCY_ALERT_AUGMENTATION = True
T1_5_RARE_BASE_TYPE = ' '.join(['"Royal Burgonet" "Eternal Burgonet" "Ezomyte Burgonet"',
                                '"Titan Gauntlets" "Crusader Gloves" "Vaal Gauntlets"',
                                '"Titan Greaves" "Crusader Boots" "Vaal Greaves"'][:])

HIDE_ENDGAME_BELOW_T1_5_RARE_CLASS = ' '.join(
    ['"Bows" "Quivers" "Claws" "Staves" "Daggers" "Wands" "Two Hand" "One Hand"',
     '"Body Armour"', '"Boots" "Gloves" "Helmets"'][:0])

NEED_RGB = False

ALERT_UTILITY_FLASK_BASE_TYPE = '' + ' "Quicksilver" "Granite" "Sulphur" "Basalt" ' + ' "Ruby Flask" "Sapphire Flask" "Topaz Flask" "Amethyst Flask" '

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
# HIDE_NORMAL_CLASS = ''  # + ' "Two Hand" '

HIDE_FLASK_MANA = (HALLOWED_MAX_ITEM_LEVEL == 1) or not SHOW_FLASK_LIFE

ALERT_JEWEL_BASE_TYPE = ' '.join(['"Cobalt"', '"Crimson"', '"Viridian"'][:])

if ALERT_SCEPTRE:
    SSF_CRAFT_BASE_TYPE += ' "Crystal Sceptre" '

# Essence = (1-46 12-66 30 48 68) = 12 30 47 48 67 68

# Ex >= 35(A4N)
# Ring-Amulet-Belt's T1-Life >= 44(A2C), 54(A4C), 64(A3M)
# Resistance = 12x : Fire12-48, Lighting13-49, Cold14-50
