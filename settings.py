# -*- coding:utf-8 -*-

DEBUG = False

TEMP = False
TENCENT = False or TEMP

# A1(1-13), A2(13-23), A3(23-33), A4(33-40), A5(41-45)
# A6(45-50), A7(50-55), A8(55-61), A9(61-63), A10(64-65)
# Socket = 2 25 35 50(A7)

#
# Part 1 - A1-10
#

ALERT_MAGIC_BASE_TYPE = ' '.join([
    '"Gloves"',  # 攻速/点伤(12+)
    '"Amulet"',  # 智敏有用的
    '"Rustic Sash" "Leather Belt"',  # 血抗 / 深渊腰带有抗
    '"Iron Ring"',  # 血抗 / 抗性戒指有点伤

    '"Siege Axe"',
    '"Lapis Amulet" "Turquoise Amulet" "Onyx Amulet"',  # 血抗
    '"Ruby Ring" "Topaz Ring" "Sapphire Ring"',  # 血抗，后期Lv6大师上点伤，下同
    '"Two-Stone Ring"',  # 血抗
])

SHOW_FLASK_HALLOWED = True
SHOW_FLASK_LIFE = True

ALERT_NORMAL_BASE_TYPE = ' '.join([
    '"Astral Plate"',  # 62
    '"Siege Axe"',  # 59 73
    '"Royal Burgonet" "Eternal Burgonet"',  # 65 69
])
# Life: 70+(Rings), 80+(Gloves, Boots, Amulets), 90+(Helmets, Belts), 90-100+(Body Armour, Shields)
HIDE_BELOW_T1_RARE_CLASS = ' '.join([
    # '"Body Armour"',  # 血量精华

    # '"Sceptres" "Claws" "One Hand"',  # 双高抗/智力
    # '"Helmets"',  # 高血
    # '"Boots"',  # 高血
    # '"Gloves"',  # 高血+点伤/攻速

    # '"Daggers" "Wands"',
    # '"Bows" "Quivers" "Two Hand" "Staves" "Shields"',
])

LINKED_CLASS = ' '.join([
    '"Body Armour"',
    '"Gloves"',
    '"Boots"',
    '"Helmets"',
])

SSF_CRAFT_BELTS_BASE_TYPE = ' '.join(['"Rustic Sash"', '"Leather Belt"'][max(0, 0 if SHOW_FLASK_HALLOWED else 1):])
SSF_CRAFT_AMULETS_BASE_TYPE = ' '.join(['"Turquoise"', '"Lapis"'][max(0, 0 if SHOW_FLASK_LIFE else 1):])
SSF_CRAFT_RINGS_BASE_TYPE = ' '.join(['"Two-Stone"'][0:])

#
# Part 2 - Maps
#

# Life: 70+(Rings), 80+(Amulets, Gloves, Boots), 90+(Helmets), 90-100+(Body Armour, Shields), 125+(Belts)
# 参考T1T2
T1_RARE_BASE_TYPE = ' '.join([
    '"Astral Plate" "Glorious Plate" "Gladiator Plate"',
    '"Tiger Hook"',

    '"Royal Burgonet" "Eternal Burgonet" "Ezomyte Burgonet"',
    '"Titan Greaves" "Vaal Greaves"',
    '"Titan Gauntlets" "Vaal Gauntlets"',

    '"Nightmare Mace" "Pernarch" "Legion Hammer" "Tenderizer" "Dragon Mace"',
    '"Infernal Axe" "Butcher Axe" "Karui Axe" "Engraved Hatchet" "Wraith Axe"',
    '"Behemoth Mace" "Vaal Hatchet" "Runic Hatchet"',
    '"Siege Axe"',
])
ALERT_RARE_ACCESSORY = True

CURRENCY_WISDOM_FONT_SIZE = [40, 33, 18][max(0, 0 if SHOW_FLASK_LIFE else 1)]
CURRENCY_ARMOURER_SCRAP_FONT_SIZE = [40, 33, 18][0]
CURRENCY_ALERT_TRANSMUTATION = True

ALERT_UTILITY_FLASK_BASE_TYPE = ' '.join([
    '"Ruby" "Sapphire" "Topaz" "Amethyst"',
    '"Stibnite" "Granite" "Basalt"',
])
if SHOW_FLASK_LIFE:
    ALERT_UTILITY_FLASK_BASE_TYPE += ' "Bismuth" "Silver" "Jade" "Quartz" "Sulphur" "Quicksilver" '

ALERT_JEWEL_BASE_TYPE = ' '.join([
    '"Crimson" "Viridian" "Cobalt"',
    '"Eye"',  # 找血，抗性，点伤
])

ALERT_LOW_CURRENCY = True  # 斧头成型后False

ALERT_ATLAS_BASE_TYPE = ' '.join([
    '"Bone Helmet"',
    '"Gripped Gloves" "Fingerless Silk Gloves"',
    '"Spiked Gloves"',
    '"Blue Pearl Amulet" "Marble Amulet" "Vanguard Belt" "Crystal Belt"',
    '"Two-Toned Boots"',
])

CURRENCY_ALERT_CHANCE = True

NEED_CHISEL = False

#
# Part 3 - Others
#

L3_MAX_IL = 19  # RRG+RR
L2_MAX_IL = min(4, L3_MAX_IL)

LEVELING_GEMS_BASE_TYPE = ' '.join([
    '"Immortal Call" "Cast when Damage Taken"',
    '"Fortify" "Blood Magic" "Increased Duration" "Concentrated Effect" "Enfeeble"',  # A6支线
]) if SHOW_FLASK_HALLOWED else ''

NEED_RGB = True and SHOW_FLASK_LIFE
SHOW_FLASK_MANA = True and SHOW_FLASK_HALLOWED and SHOW_FLASK_LIFE
SHOW_N2M_ONE_HAND = True and SHOW_FLASK_LIFE

CURRENCY_ALERT_BLACKSMITH = True and ALERT_UTILITY_FLASK_BASE_TYPE != ''  # Trade 8 for 1 glass
CURRENCY_ALERT_AUGMENTATION = True and ALERT_JEWEL_BASE_TYPE != ''

SHOW_ENDGAME_4L = False

CURRENCY_PORTAL_FONT_SIZE = [40, 33, 18][0]

CHANCING_BASE_TYPE = ''
if not ALERT_LOW_CURRENCY:
    CHANCING_BASE_TYPE += ' '.join(['"Glorious Plate"', '"Full Wyrmscale"'][1:])

ALERT_ESSENCE_BASE_TYPE = ' ' + '"Essence of Greed" "Essence of Zeal" "Essence of Contempt"'

IGNORE_RARE_UNDER_T2 = False

MAGIC_BOOTS_IL = -1  # ★★★ 10/-1 (15:Lv15, 20:Lv30, 25:Lv40, 30:Lv55)  ★★★
RARE_BOOTS_ALERT = (MAGIC_BOOTS_IL != -1)

# Ring-Amulet-Belt's T1-Life >= 44(A6), 54(A8), 64(A10)
# Resistance = 12x : Fire12-48, Lighting13-49, Cold14-50

# Essence = (1-46 12-66 30 48 68) = 12 30 47 48 67 68

# Ex >= 35(A4)
