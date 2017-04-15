# -*- coding:utf-8 -*-

DEBUG = False

# A1( 1-13), A2(13-23), A3(23-33), A4(33-40) N
# A1(40-44), A2(44-48), A3(48-54), A4(54-57) C
# A1(56-59), A2(59-63), A3(63-67), A4(67-70) M
# Socket = 2 25 35 50(A3C)
# Essence = 1-46 12-66 30 48 68
# Ex >= 35(A4N)

# Dex: "Citrine" "Jade" "Turquoise"  Int: "Agate" "Lapis" "Turquoise" (5 16)
AMULET_BASE_TYPE = '' + '"Agate" "Turquoise"'  # + '"Lapis"'
# "Sapphire" "Topaz" "Ruby" "Two-Stone" (8 12 16 20)
RINGS_BASE_TYPE = '' + '"Two-Stone"'  # + '"Ruby" "Sapphire" "Topaz"'
# "Rustic Sash" "Leather Belt" (1 8)
BELTS_BASE_TYPE = ''  # + '"Rustic Sash"'

# 1 15 30 40 55
# '>= 1'  '>= 15'  '< 2'
MAGIC_BOOTS_ITEM_LEVEL = '< 2'

HIDE_FLASK_MANA = True
HIDE_FLASK_LIFE = False

CURRENCY_ALERT_CHANCE = True
CURRENCY_ALERT_BLACKSMITH = True
CURRENCY_ALERT_TRANSMUTATION = True
CURRENCY_ALERT_AUGMENTATION = True
CURRENCY_PORTAL_SCROLL_FONT_SIZE = 33  # 30
CURRENCY_WISDOM_SCROLL_FONT_SIZE = 33  # 18

# 疯狂点机会石！！！ 前期别洗珠宝，留着洗73物等的Vaal Axe
CHANCE_ALERT_VAAL_AXE = True
CHANCE_ALERT_KARUI_MAUL = False
CHANCE_ALERT_SORCERER_BOOTS = False

NEED_MAP = True

# RRR BBB
LINKED4_NORMAL_MAX_ITEM_LEVEL = 66  # >60的由0216负责
LINKED4_MAGIC_MAX_ITEM_LEVEL = 55  # change?
LINKED4_RARE_MAX_ITEM_LEVEL = 64  # 0700隐藏了>=65的黄装
LINKED4_SIMPLE_MAX_ITEM_LEVEL = 40  # 覆盖第一难度
LINKED4_CLASS = '"Boots" "Gloves" "Helmets" "Body Armour"'

HIDE_RARES_MIN_ITEM_LEVEL = 15
# >= 15
HIDE_RARES_ALL = '"Sceptres" "Daggers" "Wands"'  # + '"Two Hand"'  # + '"Boots" "Gloves" "Helmets" "Body Armour"'
# >= 15
HIDE_RARES_LOW = '"Shields"' + '"Staves"'
# >= 2
HIDE_NORMAL_MAGIC = '"Shields"' + '"Two Hand Maces" "Staves"'  # + '"Two Hand"'
# >= 2
HIDE_NORMAL = '"Two Hand Maces" "Staves"'

# 三小件
SMALLS_NORMAL_MAX_ITEM_LEVEL = 9  # 出监狱后     隐藏不需要的白色三小件
SMALLS_MAGIC_MAX_ITEM_LEVEL = 23  # 出瓦尔金字塔后隐藏不需要的蓝色三小件
