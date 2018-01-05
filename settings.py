# -*- coding:utf-8 -*-

DEBUG = False

TEMP = False
TENCENT = True or TEMP

# A1(1-13), A2(13-23), A3(23-33), A4(33-40), A5(41-45)
# A6(45-50), A7(50-55), A8(55-60), A9(61-64), A10(64-67)
# Socket = 2 25 35 50(A7+)

#
# Part 1 - A1-10
#

ALERT_MAGIC_BASE_TYPE = ' '.join([
    '"Leather Belt"',  # 血抗 / 深渊珠宝有血抗
    '"Siege Axe"',  # ~100%
    '"Lapis Amulet" "Turquoise Amulet" "Onyx Amulet"',  # 血抗，后期Lv6大师上点伤，下同
    '"Ruby Ring" "Topaz Ring" "Sapphire Ring" "Two-Stone Ring"',  # 血抗
    '"Amulet"',  # Hide >=20 敏+智
    '"Iron Ring"',  # Hide >=20 血抗 / 抗性戒指有点伤
    '"Gloves"',  # Hide >=25 攻速/点伤(IL 12+)
    '"Rustic Sash"',  # Hide >= 30
])

SHOW_FLASK_HALLOWED = True
SHOW_FLASK_LIFE = True

# Life: 70+(Rings), 80+(Amulets, Gloves, Boots), 90+(Helmets, Belts, Body Armour), 100+(Body Armour, IL 73+)
ALERT_NORMAL_BASE_TYPE = ' '.join([
    '"Astral Plate"',  # 62
    '"Siege Axe"',  # 59 73
    '"Titan Greaves" "Vaal Greaves"',  # 62 68
    '"Royal Burgonet" "Eternal Burgonet"',  # 65 69
])
HIDE_BELOW_T1_RARE_CLASS = ' '.join([
    # '"Sceptres" "Claws" "One Hand"',  # 双高抗/智力
    # '"Helmets"',  # 高血
    # '"Boots"',  # 高血
    # '"Gloves"',  # 高血+点伤/攻速

    # '"Daggers" "Wands"',
    # '"Body Armour"',  # 血量精华
    # '"Bows" "Quivers" "Two Hand" "Staves" "Shields"',
])
LINKED_CLASS = ' '.join([
    '"Helmets"',
    '"Boots"',
    '"Body Armour"',
    '"Gloves"',
])

CURRENCY_ALERT_TRANSMUTATION = True

ALERT_UTILITY_FLASK_BASE_TYPE = ' '.join([
    '"Ruby" "Sapphire" "Topaz" "Amethyst"',
    '"Stibnite" "Granite" "Basalt"',
    '"Bismuth" "Silver" "Jade" "Quartz" "Sulphur" "Quicksilver"' if SHOW_FLASK_HALLOWED else '',
]).strip()

#
# Part 2 - Maps
#

ALERT_JEWEL_BASE_TYPE = ' '.join([
    '"Crimson" "Viridian" "Cobalt" "Searching Eye"',
    '"Murderous Eye"',  # 找血，抗性，点伤
    '"Eye"' if SHOW_FLASK_LIFE else '',
]).strip()

# 参考T1T2
T1_RARE_BASE_TYPE = ' '.join([
    '"Nightmare Mace" "Pernarch" "Legion Hammer" "Tenderizer" "Dragon Mace"',  # 等一个算上攻速过3.0分的武器
    '"Infernal Axe" "Butcher Axe" "Karui Axe" "Engraved Hatchet" "Wraith Axe"',
    '"Behemoth Mace" "Vaal Hatchet" "Runic Hatchet"',

    '"Royal Burgonet" "Eternal Burgonet" "Ezomyte Burgonet"',
    '"Titan Greaves" "Vaal Greaves"',
    '"Titan Gauntlets" "Vaal Gauntlets"',
    '"Siege Axe"',
    '"Astral Plate" "Glorious Plate" "Gladiator Plate"',
])
ALERT_RARE_ACCESSORY = True  # 血+抗性+攻速

ALERT_ATLAS_BASE_TYPE = ' '.join([
    '"Gripped Gloves" "Fingerless Silk Gloves"',
    '"Bone Helmet"',
    '"Spiked Gloves"',
    '"Blue Pearl Amulet" "Marble Amulet" "Vanguard Belt" "Crystal Belt"',
    '"Two-Toned Boots"',
])

CURRENCY_ALERT_CHANCE = True

NEED_REGAL = False
NEED_CHISEL = False

#
# Part 3 - Others
#

L3_MAX_IL = 19  # RRG 头/脚
LEVELING_GEMS_BASE_TYPE = ' '.join([
    '"Immortal Call" "Cast when Damage Taken"',
    '"Fortify" "Blood Magic" "Increased Duration" "Concentrated Effect" "Enfeeble"',  # A6支线
]) if SHOW_FLASK_HALLOWED else ''
NEED_RGB = True and SHOW_FLASK_LIFE
SHOW_N2M_ONE_HAND = True and SHOW_FLASK_LIFE
CURRENCY_ALERT_BLACKSMITH = True and ALERT_UTILITY_FLASK_BASE_TYPE != ''  # Trade 8 for 1 glass
CURRENCY_ALERT_AUGMENTATION = True and ALERT_JEWEL_BASE_TYPE != ''
CURRENCY_WISDOM_FONT_SIZE = [40, 33, 18][max(0, 0 if SHOW_FLASK_LIFE else 1, 0 if CURRENCY_ALERT_TRANSMUTATION else 2)]
CURRENCY_PORTAL_FONT_SIZE = [40, 33, 18][max(0, 0 if CURRENCY_ALERT_TRANSMUTATION else 1)]
CURRENCY_ARMOURER_SCRAP_FONT_SIZE = [40, 33, 18][max(0, 0 if CURRENCY_ALERT_TRANSMUTATION else 1)]
ALERT_LOW_CURRENCY = '"Siege Axe"' in ALERT_MAGIC_BASE_TYPE
SSF_CRAFT_AMULETS_BASE_TYPE = ' '.join(
    ['"Turquoise"', '"Lapis"']
    [max(0, 0 if SHOW_FLASK_LIFE else 1, 0 if '"Lapis Amulet"' in ALERT_MAGIC_BASE_TYPE else 2):])
SSF_CRAFT_BELTS_BASE_TYPE = ' '.join(  # 深渊赛季结束后去掉 0 if SHOW_FLASK_LIFE else 2
    ['"Rustic Sash"', '"Leather Belt"'][max(0, 0 if SHOW_FLASK_HALLOWED else 1, 0 if SHOW_FLASK_LIFE else 2):])
SSF_CRAFT_RINGS_BASE_TYPE = '"Two-Stone"' if '"Two-Stone Ring"' in ALERT_MAGIC_BASE_TYPE else ''

ALERT_ESSENCE_BASE_TYPE = ' ' + '"Essence of Greed" "Essence of Zeal" "Essence of Contempt"'
IGNORE_RARE_UNDER_T2 = False

# Ring-Amulet-Belt's T1-Life >= 44(A6), 54(A8), 64(A10)
# Resistance = 12x : Fire12-48, Lighting13-49, Cold14-50
# Essence = (1-46 12-66 30 48 68) = 12 30 47 48 67 68
# Ex >= 35(A4)

L2_MAX_IL = min(4, L3_MAX_IL)
SHOW_FLASK_MANA = True and SHOW_FLASK_HALLOWED and SHOW_FLASK_LIFE
CHANCING_BASE_TYPE = ''
if not CURRENCY_ALERT_CHANCE:
    CHANCING_BASE_TYPE += ' '.join(['"Glorious Plate"', '"Full Wyrmscale"'][1:])

if TENCENT and '"Astral Plate"' not in ALERT_NORMAL_BASE_TYPE:
    HIDE_BELOW_T1_RARE_CLASS += ' "Body Armour" '
    LINKED_CLASS = LINKED_CLASS.replace('"Body Armour"', '')  # .replace('"Gloves"', '')
    T1_RARE_BASE_TYPE = T1_RARE_BASE_TYPE.replace('"Astral Plate" "Glorious Plate" "Gladiator Plate"', '')
