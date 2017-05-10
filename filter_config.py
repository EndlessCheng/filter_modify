# -*- coding:utf-8 -*-

# ##################################
POE_VERSION = ['old', 'new'][0]
# ##################################

DEBUG = False

# 'm2s' -> 's' (3 -> 1)
SKILL = ['m', 's', 'r', 'm2s'][0]  # melee spell range

# A1( 1-13), A2(13-23), A3(*23*-33), A4(33-40) N
# A1(40-44), A2(44-48), A3(*48*-54), A4(54-57) C
# A1(56-59), A2(59-63), A3(*63*-67), A4(67-70) M

# Essence = 1-46 12-66 30 48 68 = 12 30 47 48 67 68
# Socket = 2 25 35 50(A3C)
# Ex >= 35(A4N)
# Ring-Amulet-Belt's T1-Life >= 44(A2C), 54(A4C), 64(A3M)
# Resistance = 12x : Fire12-48, Lighting13-49, Cold14-50
# MS = 1 15 30 40 55

#  "Gold" (8)    Dex: "Citrine" "Jade" "Turquoise"    Int: "Agate" "Lapis" "Turquoise" (5 16)
AMULET_BASE_TYPE = ''  # + ' "Gold" '  # + ' "Citrine" "Jade" "Turquoise"  '
# "Sapphire" "Topaz" "Ruby" "Two-Stone" (8 12 16 20)
RINGS_BASE_TYPE = ''  # + ' "Two-Stone" '  # + ' "Sapphire" "Topaz" "Ruby" '
# "Rustic Sash" "Leather Belt" (1 8)
BELTS_BASE_TYPE = ''  # + ' "Leather Belt" '  # + ' "Rustic Sash" '
# "Cobalt" "Crimson" "Viridian"
ALERT_JEWEL_BASE_TYPE = '"Crimson"  '

# '>= 1' '< 1'
MAGIC_BOOTS_ITEM_LEVEL = '< 1'

HIDE_FLASK_MANA = True

HIDE_FLASK_LIFE = True

CURRENCY_ALERT_CHANCE = False
CURRENCY_ALERT_BLACKSMITH = False
CURRENCY_ALERT_TRANSMUTATION = False
CURRENCY_ALERT_AUGMENTATION = False
CURRENCY_PORTAL_SCROLL_FONT_SIZE = 30  # 33 -> 30
CURRENCY_WISDOM_SCROLL_FONT_SIZE = 18  # 33 -> 18

# 疯狂点机会石--前期别洗珠宝，留着洗73物等的Vaal Axe
CHANCE_ALERT_SORCERER_BOOTS = False

CHANCE_ALERT_VAAL_AXE = True
CHANCE_ALERT_KARUI_MAUL = False

# ' "Vortex" "Immortal Call" "Cast when Damage Taken" ' \
# ' "Added Fire Damage" "Melee Splash" "Clarity" "Sunder" '
LEVELING_GEMS_BASE_TYPE = ''  # + ' "Immortal Call" "Cast when Damage Taken" '  # + ' "Added Fire Damage" "Melee Splash" "Clarity" "Sunder" '

NEED_MAP = True

HALLOWED_MAX_ITEM_LEVEL = 41  # 50 -> 41

# >= 15  "Body Armour"
HIDE_RARES_ALL = '' + ' "Staves"  "Shields"  "Body Armour"  "Boots" "Gloves" "Helmets"  '  # + ' "Daggers" '  # + ' "Sceptres" "Wands" '  # + ' "Boots" "Gloves" "Helmets" "Body Armour" '
# >= 2
HIDE_NORMAL_MAGIC = '"Shields" ' + ' "Two Hand Maces" "Staves" ' + ' "Two Hand" "One Hand" '
# >= 2 找到高pDPS武器就隐藏所有白武器
HIDE_NORMAL = '"Two Hand Maces" "Staves" ' + ' "Two Hand" "One Hand" '

RARE_SMALL_ARMOUR_BASE_TYPE = '"Siege Helmet" "Samite Helmet" "Burgonet" "Fencer Helm" "Lacquered Helmet" "Bascinet"' \
                              ' "Gauntlets" "Sharkskin Gloves" "Shagreen Gloves" "Stealth Gloves" "Slink Gloves"' \
                              ' "Greaves" "Sharkskin Boots" "Shagreen Boots" "Stealth Boots" "Slink Boots" "Wyrmscale Boots" "Hydrascale Boots" "Dragonscale Boots" '
RARE_BODY_ARMOUR_BASE_TYPE = '"Plate" "General\'s Brigandine" "Triumphant Lamellar"'

RARE_BOOTS_ALERT = (MAGIC_BOOTS_ITEM_LEVEL == '>= 1')

HIDE_RARES_MIN_ITEM_LEVEL = 15

# RRR BBB
LINKED4_NORMAL_MAX_ITEM_LEVEL = 66  # >60的由0216负责
LINKED4_MAGIC_MAX_ITEM_LEVEL = 55  # 第三难度不再显示
LINKED4_RARE_MAX_ITEM_LEVEL = 64  # 0700隐藏了>=65的黄装
LINKED4_SIMPLE_MAX_ITEM_LEVEL = 40  # 覆盖第一难度
LINKED4_CLASS = '"Boots" "Gloves" "Helmets" "Body Armour"'

# 三小件
SMALLS_NORMAL_MAX_ITEM_LEVEL = 9  # 出监狱后     隐藏不需要的白色三小件
SMALLS_MAGIC_MAX_ITEM_LEVEL = 23  # 出瓦尔金字塔后隐藏不需要的蓝色三小件
