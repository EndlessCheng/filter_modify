# -*- coding:utf-8 -*-

import os

from filter_modify import *
import filter_config

SHOW = 'Show'
HIDE = 'Hide'
DEBUG = SHOW if filter_config.DEBUG else HIDE

RARITY_NORMAL = 'Normal'
RARITY_MAGIC = 'Magic'
RARITY_RARE = 'Rare'
RARITY_UNIQUE = 'Unique'
RARITY_N2M = '<= Magic'
RARITY_N2R = '<= Rare'

ITEM_LEVEL_REGAL = '>= 75'
ITEM_LEVEL_CHAOS = '>= 60'

FONT_SIZE_MAX = 45
FONT_SIZE_MIN = 18

COLOR_WHITE = '255 255 255'
COLOR_WHITE_LIGHT = '200 200 200'
COLOR_RED = '255 0 0'
COLOR_RED_LIGHT = '210 0 0'
COLOR_GREEN = '0 255 0'
COLOR_BLUE = '0 0 255'
COLOR_BLUE_LIGHT = '136 136 255'
COLOR_BLACK = '0 0 0'
COLOR_YELLOW = '255 255 0'
COLOR_YELLOW_LIGHT = '255 255 119'
COLOR_AQUA = '0 255 255'
COLOR_GOLD = '213 159 0'
COLOR_ORANGE = '255 125 0'
COLOR_ORANGE_LIGHT = '255 125 0 200'
COLOR_BROWN = '100 75 0'
COLOR_UNIQUE = '175 96 37'

SOUND_TOP_VALUE = '8 300'
SOUND_MID_VALUE = '1 300'
SOUND_LOW_VALUE = '2 300'
SOUND_MAP = '4 300'
SOUND_UNIQUE = '6 300'
SOUND_CHANCE = '4 300'
SOUND_CHANCE2 = '3 300'


def modify0200(filter_manager):
    filter_manager.add_comment(200, 'Recipes, Magic and Normal items (endgame!)')

    # 8
    filter_manager.add_comment(201, '6-Linked items')
    block = filter_manager.get_block(201)[0]
    block.PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.append_block(block)

    # 8
    filter_manager.add_comment(202, '5-Linked items')
    block = filter_manager.get_block(202)[0]
    # tmp = block.copy_modify(Class='"Body Armour"', SetFontSize=45, PlayAlertSound=SOUND_TOP_VALUE)
    # filter_manager.append_block(tmp)
    # tmp = tmp.copy_modify(DropLevel='>= 58', Class='"Two Hand"')  # "Two Hand Axes"
    # filter_manager.append_block(tmp)
    block.PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.append_block(block)

    # 颜色改成和神圣/点金一样的
    filter_manager.add_comment(203, '6-Socket Items')
    blocks = filter_manager.get_block(203)
    blocks[0].modify(SetTextColor=COLOR_RED, SetBorderColor=COLOR_RED, SetBackgroundColor=COLOR_WHITE,
                     PlayAlertSound=SOUND_TOP_VALUE)
    blocks[1].modify(SetTextColor=COLOR_RED, SetBorderColor=COLOR_RED, SetBackgroundColor=COLOR_WHITE,
                     PlayAlertSound=SOUND_TOP_VALUE)
    del blocks[2]
    blocks[2].modify(SetTextColor=COLOR_WHITE, SetBorderColor=COLOR_BLACK, SetBackgroundColor=COLOR_GOLD,
                     PlayAlertSound=SOUND_MID_VALUE)
    filter_manager.extend_blocks(blocks)

    # 8和1
    filter_manager.add_comment(204, 'Exclusive bases: Atlas bases, talismans')
    blocks = filter_manager.get_block(204)
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[1].PlayAlertSound = SOUND_TOP_VALUE
    blocks[2].PlayAlertSound = SOUND_MID_VALUE
    blocks[3].PlayAlertSound = SOUND_MID_VALUE
    blocks[4].PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    # 加上Gloves Boots Shields Bows Quivers，改稀有度
    # 项链：+1诅咒，+1球，移速，抗性上限
    # 腰带：+1球，技能持续时间/范围
    # 手脚盾：+1技能等级
    # 手：击中附加诅咒
    # 脚：+1球
    # 弓和箭袋：+1箭
    filter_manager.add_comment(205, 'Corrupted items')
    block = filter_manager.get_block(205)[0]
    block.modify(Class=block.Class + ' Gloves Boots Shields Bows Quivers', Rarity=RARITY_N2R)
    filter_manager.append_block(block)

    # 只留第一个
    filter_manager.add_comment(206, 'Chancing items')
    if filter_config.CHANCING_ITEM_BASE_TYPE != '':
        block = filter_manager.get_block(206)[0]
        block.modify(Corrupted=False, BaseType=filter_config.CHANCING_ITEM_BASE_TYPE, PlayAlertSound=SOUND_CHANCE)
        filter_manager.append_block(block)

    filter_manager.add_comment(207, 'Add your own crafting rules here')

    # 0208是蓝白，0602是稀有
    filter_manager.add_comment(208, '83/84+ Endgame crafting rules')
    filter_manager.extend_blocks(block_number=208)

    # 只留第一个
    filter_manager.add_comment(209, 'Magic jewel')
    block = filter_manager.get_block(209)[0]
    if filter_config.ALERT_JEWEL_BASE_TYPE != '':
        filter_manager.append_block(
            block.copy_modify(BaseType=filter_config.ALERT_JEWEL_BASE_TYPE, PlayAlertSound=SOUND_CHANCE))
    filter_manager.append_block(block)

    # All Warband mods are prefixes, GG.
    filter_manager.add_comment(210, 'Warband items')

    # 再加上三小件，但不刻意高亮
    filter_manager.add_comment(211, 'Remaining crafting rules - add your own bases here!')
    if filter_config.SSF_CRAFT_BASE_TYPE != '':
        filter_manager.append_block(FilterBlock(
            BaseType=filter_config.SSF_CRAFT_BASE_TYPE, Rarity=RARITY_NORMAL, SetBorderColor=COLOR_WHITE,
            PlayAlertSound=SOUND_CHANCE
        ))
    if filter_config.SSF_CRAFT_AMULET_BASE_TYPE != '':
        filter_manager.append_block(FilterBlock(
            Class='Amulets', BaseType=filter_config.SSF_CRAFT_AMULET_BASE_TYPE, Rarity=RARITY_NORMAL,
            SetTextColor=COLOR_WHITE
        ))
    if filter_config.SSF_CRAFT_RINGS_BASE_TYPE != '':
        filter_manager.append_block(FilterBlock(
            Class='Rings', BaseType=filter_config.SSF_CRAFT_RINGS_BASE_TYPE, Rarity=RARITY_NORMAL,
            SetTextColor=COLOR_WHITE
        ))
    if filter_config.SSF_CRAFT_BELTS_BASE_TYPE != '':
        filter_manager.append_block(FilterBlock(
            Class='Belts', BaseType=filter_config.SSF_CRAFT_BELTS_BASE_TYPE, Rarity=RARITY_NORMAL,
            SetTextColor=COLOR_WHITE
        ))

    filter_manager.add_comment(212, 'Chisel recipe items')
    filter_manager.extend_blocks(block_number=212)

    # 8
    filter_manager.add_comment(213, 'Fishing Rod')
    block = filter_manager.get_block(213)[0]
    block.PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.append_block(block)

    # 8
    filter_manager.add_comment(214, 'SRS Crude Bow')
    block = filter_manager.get_block(214)[0]
    block.PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.append_block(block)

    filter_manager.add_comment(215, 'Chromatic recipe items ("RGB Recipe")')
    if filter_config.NEED_RGB:
        filter_manager.extend_blocks(block_number=215)

    filter_manager.add_comment(216, 'Endgame-start 4-links')
    if filter_config.SHOW_ENDGAME_4L:
        filter_manager.extend_blocks(block_number=216)

    filter_manager.add_comment(217, 'Animate Weapon script - deactivated by default')
    # filter_manager.extend_blocks(block_number=217)

    # 改稀有度，高亮边框
    filter_manager.add_comment(218, 'W-soc offhand weapons')
    block = filter_manager.get_block(218)[0]
    block.modify(Rarity=RARITY_N2R, SetBorderColor=COLOR_WHITE)
    filter_manager.append_block(block)

    filter_manager.add_comment(219, 'Sacrificial Garb')
    filter_manager.extend_blocks(block_number=219)


# ！！！SSF模式下最重要的部分！！！
def modify0600(filter_manager):
    filter_manager.add_comment(600, 'RARE ITEMS (ENDGAME)')

    # 8和1
    filter_manager.add_comment(601, 'Rare Atlas bases (84+)')
    blocks = filter_manager.get_block(601)
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[1].PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(602, 'Rare crafting bases')
    filter_manager.extend_blocks(block_number=602)

    filter_manager.add_comment(603, 'T1 rare items')
    blocks = filter_manager.get_block(603)
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[1].PlayAlertSound = SOUND_TOP_VALUE
    blocks[2].modify(SetBackgroundColor=COLOR_BROWN + ' 225', PlayAlertSound=SOUND_MID_VALUE)
    blocks[3].modify(SetBackgroundColor=COLOR_BROWN + ' 225', PlayAlertSound=SOUND_MID_VALUE)
    for block in blocks[4:]:
        block.modify(SetBorderColor=COLOR_ORANGE_LIGHT, SetBackgroundColor=COLOR_BROWN + ' 225')
    if filter_config.ALERT_RARE_BASE_TYPE != '':
        blocks.insert(4,
                      blocks[2].copy_modify(BaseType=filter_config.ALERT_RARE_BASE_TYPE, PlayAlertSound=SOUND_CHANCE))
        blocks.insert(5,
                      blocks[3].copy_modify(BaseType=filter_config.ALERT_RARE_BASE_TYPE, PlayAlertSound=SOUND_CHANCE))
    # if 'm' in filter_config.SKILL:
    #     blocks.insert(6, blocks[2].copy_modify(DropLevel='>= 58', Class='"Two Hand Axes"', BaseType=None,
    #                                            PlayAlertSound=SOUND_CHANCE))
    #     blocks.insert(7, blocks[3].copy_modify(DropLevel='>= 58', Class='"Two Hand Axes"', BaseType=None,
    #                                            PlayAlertSound=SOUND_CHANCE))
    # elif 's' in filter_config.SKILL:
    #     blocks.insert(6, blocks[2].copy_modify(Class='"Shields"', BaseType='"Spirit Shield"',
    #                                            PlayAlertSound=SOUND_CHANCE))
    #     blocks.insert(7, blocks[3].copy_modify(Class='"Shields"', BaseType='"Spirit Shield"',
    #                                            PlayAlertSound=SOUND_CHANCE))
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(604, 'T1.5 rare items')
    blocks = filter_manager.get_block(604)
    for block in blocks:
        block.SetBorderColor = COLOR_ORANGE_LIGHT
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(605, 'T2 rare items')
    blocks = filter_manager.get_block(605)
    for block in blocks:
        block.SetBorderColor = COLOR_ORANGE_LIGHT
    if filter_config.T2_BIG_WEAPON_BASE_TYPE != '':
        blocks[2].BaseType = filter_config.T2_BIG_WEAPON_BASE_TYPE
        blocks[3].BaseType = filter_config.T2_BIG_WEAPON_BASE_TYPE
    else:
        del blocks[2:4]
    if filter_config.T2_BIG_ARM_BASE_TYPE != '':
        blocks[-2].BaseType = filter_config.T2_BIG_ARM_BASE_TYPE
        blocks[-1].BaseType = filter_config.T2_BIG_ARM_BASE_TYPE
    else:
        del blocks[-2:]
    filter_manager.extend_blocks(blocks)

    # 提前隐藏部分稀有物品，借鉴0700
    blocks = filter_manager.get_block(700)
    for block in blocks:
        block.modify(status=DEBUG, Corrupted=False, Class=filter_config.HIDE_ENDGAME_BELOW_T2_RARE_CLASS)
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(606, 'Breach Rings')
    filter_manager.extend_blocks(block_number=606)

    # 4, 1, 4
    filter_manager.add_comment(607, 'Amulets, Jewels, Rings, Belts')
    blocks = filter_manager.get_block(607)
    blocks[0].PlayAlertSound = SOUND_CHANCE  # rare jewel
    blocks[1].modify(SetBorderColor=COLOR_ORANGE_LIGHT, SetBackgroundColor=COLOR_BROWN + ' 225',
                     PlayAlertSound=SOUND_MID_VALUE)  # regal smalls
    blocks[2].PlayAlertSound = SOUND_CHANCE  # 1-74 smalls
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(608, '1H Daggers')
    filter_manager.extend_blocks(block_number=608)

    filter_manager.add_comment(609, '1H Claws')

    filter_manager.add_comment(610, '1H Wands')
    filter_manager.extend_blocks(block_number=610)

    filter_manager.add_comment(611, '1H Swords and Foils')

    filter_manager.add_comment(612, '1H Axes and Maces')

    filter_manager.add_comment(613, '1H Sceptres')
    blocks = filter_manager.get_block(613)
    blocks[0].DropLevel = None
    blocks[1].DropLevel = None
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(614, '2H Staves')

    filter_manager.add_comment(615, '2H Swords, Axes, Maces')

    filter_manager.add_comment(616, '2H Bows')

    # 隐藏bad
    filter_manager.add_comment(617, 'AR: Gloves, Boots, Helmets')
    blocks = filter_manager.get_block(617)
    # if filter_config.ONLY_HIGHLIGHT_RARE_SMALL_ARMOUR_BASE_TYPE != '':
    #     blocks[0].BaseType = filter_config.ONLY_HIGHLIGHT_RARE_SMALL_ARMOUR_BASE_TYPE
    #     blocks[1].BaseType = filter_config.ONLY_HIGHLIGHT_RARE_SMALL_ARMOUR_BASE_TYPE
    #     blocks[-2].modify(status=DEBUG, Corrupted=False)
    #     blocks[-1].modify(status=DEBUG, Corrupted=False)
    filter_manager.extend_blocks(blocks)

    # 隐藏bad
    filter_manager.add_comment(618, 'AR: Body Armors')
    blocks = filter_manager.get_block(618)
    # if filter_config.ONLY_HIGHLIGHT_RARE_BODY_ARMOUR_BASE_TYPE != '':
    #     blocks[2].BaseType = filter_config.ONLY_HIGHLIGHT_RARE_BODY_ARMOUR_BASE_TYPE
    #     blocks[3].BaseType = filter_config.ONLY_HIGHLIGHT_RARE_BODY_ARMOUR_BASE_TYPE
    # blocks[-2].modify(status=DEBUG, Corrupted=False)
    # blocks[-1].modify(status=DEBUG, Corrupted=False)
    filter_manager.extend_blocks(blocks)

    # 隐藏bad
    filter_manager.add_comment(619, 'OH: Shields')
    blocks = filter_manager.get_block(619)
    blocks[-4].modify(status=DEBUG, Corrupted=False)
    blocks[-3].modify(status=DEBUG, Corrupted=False)
    blocks[-2].modify(status=DEBUG, Corrupted=False)
    blocks[-1].modify(status=DEBUG, Corrupted=False)
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(620, 'OH: Quivers')

    filter_manager.add_comment(621, 'Rare endgame items - remaining rules')
    filter_manager.extend_blocks(block_number=621)


# 0800-1207
def modify_gem_flask_map(filter_manager):
    # Need map, exile?
    filter_manager.add_comment(800, 'OVERRIDE AREA 3 - Override Map, Gem and Flask drops here')
    if filter_config.NEED_MAP:  # 样式取自T14
        filter_manager.append_block(filter_manager.get_block(1204)[0].copy_modify(DropLevel=None, Rarity=RARITY_N2R))

    # 改成8和1
    filter_manager.add_comment(901, 'Value gems')
    blocks = filter_manager.get_block(901)
    del blocks[0]
    blocks[0].modify(Quality='>= 15', PlayAlertSound=SOUND_TOP_VALUE)
    blocks[1].modify(BaseType=blocks[1].BaseType + ' "Added Chaos Damage"', SetBackgroundColor=COLOR_WHITE,
                     PlayAlertSound=SOUND_TOP_VALUE)
    blocks[2].modify(Quality='>= 10', PlayAlertSound=SOUND_MID_VALUE)
    filter_manager.extend_blocks(blocks)

    # 前两个换位，改成1和2
    filter_manager.add_comment(902, 'Other gems')
    blocks = filter_manager.get_block(902)
    blocks[0], blocks[1] = blocks[1], blocks[0]
    blocks[0].PlayAlertSound = SOUND_MID_VALUE
    blocks[1].PlayAlertSound = SOUND_LOW_VALUE
    if filter_config.LEVELING_GEMS_BASE_TYPE != '':
        tmp = blocks[2].copy_modify(BaseType=filter_config.LEVELING_GEMS_BASE_TYPE,
                                    PlayAlertSound=SOUND_TOP_VALUE)
        blocks.insert(2, tmp)
    else:
        blocks[2].status = DEBUG
    filter_manager.extend_blocks(blocks)

    # 低物等15改成10，高亮Q>=5的功能瓶
    filter_manager.add_comment(1000, 'FLASKS (Endgame rules)')
    blocks = filter_manager.get_block(1000)
    if filter_config.ALERT_UTILITY_FLASK_BASE_TYPE != '':
        filter_manager.append_block(
            blocks[4].copy_modify(BaseType=filter_config.ALERT_UTILITY_FLASK_BASE_TYPE, ItemLevel=None,
                                  PlayAlertSound=SOUND_CHANCE))
    blocks[2].Quality = '>= 10'
    filter_manager.extend_blocks(blocks[:3])
    filter_manager.append_block(blocks[5])
    blocks[-3].modify(Quality='>= 5', Class='"Utility Flasks"', BaseType=None, SetFontSize=38)
    filter_manager.append_block(blocks[-3])

    filter_manager.add_comment(1100, 'HIDE LAYER 3: Random Endgame Flasks')
    filter_manager.extend_blocks(block_number=1100)

    # 去掉第一个的BaseType
    filter_manager.add_comment(1201, 'Unique Maps')
    blocks = filter_manager.get_block(1201)
    blocks[0].modify(BaseType=None, PlayAlertSound=SOUND_TOP_VALUE)
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(1202, 'Labyrinth items, Offerings')
    filter_manager.extend_blocks(block_number=1202)

    # 加红边
    filter_manager.add_comment(1203, 'Top tier maps (T15-16)')
    blocks = filter_manager.get_block(1203)
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[1].modify(SetBorderColor=COLOR_RED, PlayAlertSound=SOUND_TOP_VALUE)
    filter_manager.extend_blocks(blocks)

    # 加红边
    filter_manager.add_comment(1204, 'High tier maps(T11-14)')
    blocks = filter_manager.get_block(1204)
    for block in blocks:
        block.modify(SetBorderColor=COLOR_RED_LIGHT, PlayAlertSound=SOUND_TOP_VALUE)
    filter_manager.extend_blocks(blocks)

    # 加黄边，高亮T9T10
    filter_manager.add_comment(1205, 'Mid tier maps (T6-10)')
    blocks = filter_manager.get_block(1205)
    for block in blocks:
        block.modify(SetTextColor=COLOR_WHITE_LIGHT, SetBorderColor=COLOR_YELLOW_LIGHT)
    blocks[0].SetFontSize = FONT_SIZE_MAX
    blocks[1].SetFontSize = FONT_SIZE_MAX
    blocks[2].SetFontSize = FONT_SIZE_MAX
    filter_manager.extend_blocks(blocks)

    # 字体高亮，加蓝边/白边
    filter_manager.add_comment(1206, 'Low tier maps (T1-T5)')
    blocks = filter_manager.get_block(1206)
    for block in blocks:
        block.SetTextColor = COLOR_WHITE_LIGHT
    for block in blocks[:6]:
        block.SetBorderColor = COLOR_BLUE_LIGHT
    for block in blocks[6:10]:
        block.SetBorderColor = COLOR_WHITE_LIGHT
    filter_manager.extend_blocks(blocks)

    # 8和4
    filter_manager.add_comment(1207, 'Map fragments')
    blocks = filter_manager.get_block(1207)
    for block in blocks[:-1]:
        block.PlayAlertSound = SOUND_TOP_VALUE
    blocks[-1].PlayAlertSound = SOUND_MAP
    filter_manager.extend_blocks(blocks)


# 1900-2303
def modify_leveling(filter_manager):
    # 隐藏混合，魔力，血；后期只要42和60级的血瓶
    filter_manager.add_comment(1900, 'OVERRIDE AREA 4 - Insert your custom leveling adjustments here')
    block = FilterBlock(status=DEBUG, Class='"Hybrid Flask"', SetFontSize=FONT_SIZE_MIN)
    if filter_config.HIDE_FLASK_LIFE:
        block.Class += ' "Life Flask"'
    if filter_config.HIDE_FLASK_MANA:
        block.Class += ' "Mana Flask"'
    filter_manager.append_block(block)
    filter_manager.append_block(
        FilterBlock(status=DEBUG, Class='"Life Flask"', BaseType='Sanctified Eternal', SetFontSize=FONT_SIZE_MIN))
    filter_manager.append_block(
        FilterBlock(status=DEBUG, Class='"Mana Flask"', BaseType='Colossal Hallowed', SetFontSize=FONT_SIZE_MIN))
    if filter_config.HIDE_LEVELING_RARE_CLASS != '':
        filter_manager.append_block(
            FilterBlock(status=DEBUG, Corrupted=False, Class=filter_config.HIDE_LEVELING_RARE_CLASS, Rarity=RARITY_RARE,
                        ItemLevel='>= ' + str(filter_config.HIDE_LEVELING_RARE_MIN_ITEM_LEVEL),
                        SetFontSize=FONT_SIZE_MIN))

    filter_manager.add_comment(2001, 'Hide outdated flasks')
    filter_manager.extend_blocks(block_number=2001)

    filter_manager.add_comment(2002, 'Hybrid flasks (normal)')

    filter_manager.add_comment(2003, 'Hybrid flasks (magic)')

    filter_manager.add_comment(2004, 'Life/Mana Flask - Normal (Kudos to Antnee)')
    blocks = filter_manager.get_block(2004)
    blocks[-4].ItemLevel = '<= ' + str(filter_config.HALLOWED_MAX_ITEM_LEVEL)
    blocks[-2].ItemLevel = None
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(2005, 'Life/Mana Flask - Magic (Kudos to Antnee)')
    blocks = filter_manager.get_block(2005)
    blocks[-4].ItemLevel = '<= ' + str(filter_config.HALLOWED_MAX_ITEM_LEVEL)
    blocks[-2].ItemLevel = None
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(2006, 'Show remaining flasks')

    # 4L稀有
    filter_manager.add_comment(2101, 'Leveling rares - tier list')
    blocks = filter_manager.get_block(2101)
    blocks[0].modify(Class=filter_config.LINKED4_CLASS,
                     ItemLevel='<= ' + str(filter_config.LINKED4_RARE_MAX_ITEM_LEVEL), PlayAlertSound=SOUND_CHANCE)
    if filter_config.RARE_BOOTS_ALERT:
        blocks[1].modify(SetFontSize=FONT_SIZE_MAX, PlayAlertSound=SOUND_CHANCE)
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(2102, 'Leveling rares - remaining rules')
    filter_manager.extend_blocks(block_number=2102)

    filter_manager.add_comment(2201, 'Leveling RGB Exceptions 3L')
    filter_manager.extend_blocks(block_number=2201)

    # 显示部分蓝白三小件
    filter_manager.add_comment(2202, 'Jewellery & Helpful leveling and racing gear')
    blocks = filter_manager.get_block(2202)[-5:-1]
    blocks[0].ItemLevel = '<= ' + str(filter_config.SMALLS_NORMAL_MAX_ITEM_LEVEL)
    blocks[1].Class = filter_config.SMALLS_MAGIC_CLASS
    del blocks[2]
    blocks[2].modify(Class=filter_config.SMALLS_MAGIC_CLASS,
                     ItemLevel='<= ' + str(filter_config.SMALLS_MAGIC_MAX_ITEM_LEVEL))
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(2203, 'Caster weapons')
    # if 's' == filter_config.SKILL:
    #     blocks = filter_manager.get_block(2203)
    #     filter_manager.append_block(blocks[1])

    # 4L RRR BBB, 3L RR, 2L RR
    # TODO: 45?
    filter_manager.add_comment(2204, 'Linked gear')
    blocks = filter_manager.get_block(2204)
    blocks[0].modify(SocketGroup='RRR', Class=filter_config.LINKED4_CLASS,
                     ItemLevel='<= 45',
                     SetFontSize=42, PlayAlertSound=SOUND_CHANCE)
    blocks[1].modify(SocketGroup='RRR', Class=filter_config.LINKED4_CLASS,
                     ItemLevel='<= 45',
                     SetFontSize=42, PlayAlertSound=SOUND_CHANCE)
    blocks[2].modify(SocketGroup='RR', Class=filter_config.LINKED4_CLASS, SetFontSize=40)
    blocks[3].modify(SocketGroup='RR', Class=filter_config.LINKED4_CLASS, SetFontSize=42)
    blocks[4].modify(ItemLevel=filter_config.MAGIC_BOOTS_ITEM_LEVEL, SetFontSize=FONT_SIZE_MAX,
                     PlayAlertSound=SOUND_CHANCE)
    blocks[5].modify(LinkedSockets=4, Class=filter_config.LINKED4_CLASS,
                     ItemLevel='<= ' + str(filter_config.LINKED4_SIMPLE_MAX_ITEM_LEVEL))
    blocks[6].modify(LinkedSockets=4, Class=filter_config.LINKED4_CLASS,
                     ItemLevel='<= ' + str(filter_config.LINKED4_SIMPLE_MAX_ITEM_LEVEL))
    blocks[7].modify(LinkedSockets=2, SocketGroup='RR', Class=filter_config.LINKED4_CLASS,
                     ItemLevel='<= 7', SetFontSize=40)
    blocks[8].modify(LinkedSockets=2, SocketGroup='RR', Class=filter_config.LINKED4_CLASS,
                     ItemLevel='<= 15', SetFontSize=40)
    filter_manager.append_block(
        blocks[0].copy_modify(SocketGroup='BBB', ItemLevel='<= ' + str(filter_config.LINKED4_NORMAL_MAX_ITEM_LEVEL)))
    filter_manager.append_block(
        blocks[1].copy_modify(SocketGroup='BBB', ItemLevel='<= ' + str(filter_config.LINKED4_NORMAL_MAX_ITEM_LEVEL)))
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(2205, '20% quality items for those strange people who want them')

    # A1用双持斧/剑，之后用双手斧
    # 法术武器见2203
    filter_manager.add_comment(2300, 'Levelling - normal and magic item progression')
    block = FilterBlock(status=DEBUG,
                        Class='"Bows" "Quivers" "Claws" "One Hand Maces" "Two Hand Swords" "Sceptres" "Daggers" "Wands" ' + filter_config.HIDE_NORMAL_MAGIC_CLASS,
                        Rarity=RARITY_N2M, ItemLevel='>= 2',
                        SetFontSize=FONT_SIZE_MIN, SetBorderColor='0 0 0 150', SetBackgroundColor='0 0 0 165')
    filter_manager.append_block(block)
    filter_manager.append_block(block.copy_modify(Class=filter_config.HIDE_NORMAL_CLASS, Rarity=RARITY_NORMAL))
    tmp = block.copy_modify(DropLevel='<= 12', Class='"Two Hand" "Staves"')
    filter_manager.append_block(tmp)
    tmp = tmp.copy_modify(DropLevel='> 11', Class='"One Hand"')
    filter_manager.append_block(tmp)
    tmp = tmp.copy_modify(DropLevel=None, ItemLevel='>= 13')
    filter_manager.append_block(tmp)
    tmp = tmp.copy_modify(BaseType='"Rusted Spike" "Whalebone Rapier"', ItemLevel=None)
    filter_manager.append_block(tmp)

    # 白装1-4
    filter_manager.add_comment(2301, 'Normal items - First 12 levels - exceptions')
    blocks = filter_manager.get_block(2301)
    for block in blocks:
        block.ItemLevel = '<= 4'
    filter_manager.extend_blocks(blocks)

    # 双持武器阶段隐藏
    filter_manager.add_comment(2302, 'Normal weapons - progression')
    blocks = filter_manager.get_block(2302)
    tmp = blocks[0].copy_modify(DropLevel='>= 1', Class='"One Hand"', ItemLevel='<= 3')
    blocks.insert(0, tmp)  # "Rusted Hatchet" "Rusted Sword"
    blocks.insert(1, tmp.copy_modify(DropLevel='>= 5', ItemLevel='<= 7'))  # "Copper Sword"
    blocks.insert(2, tmp.copy_modify(DropLevel='>= 6', ItemLevel='<= 8'))  # "Jade Hatchet"
    filter_manager.extend_blocks(blocks)

    # 蓝装1-3
    filter_manager.add_comment(2303, 'Magic items - progression')
    blocks = filter_manager.get_block(2303)
    if 'm' in filter_config.SKILL:
        # 这两个部位的蓝装没意义——迟早要被白装/RR替代
        tmp = blocks[3].copy_modify(Width=None, Height=None, Class='"Body Armour" "Helmets"', ItemLevel='<= 3')
        filter_manager.append_block(tmp)
        filter_manager.append_block(tmp.copy_modify(Class='"Gloves"', ItemLevel='<= 12'))
    elif 's' == filter_config.SKILL:
        # for block in blocks:
        #     block.ItemLevel = '<= 4'
        filter_manager.extend_blocks(blocks)


def modify_filter(filter_manager):
    filter_manager.add_comment(100, 'OVERRIDE AREA 1 - Override ALL rules here (includes 6links etc, be careful)')

    modify0200(filter_manager)

    # 隐藏>=65的蓝白
    filter_manager.add_comment(300, 'HIDE LAYER 1 - MAGIC AND NORMAL ITEMS')
    block = filter_manager.get_block(300)[0]
    block.modify(status=DEBUG, ItemLevel='>= 65')
    filter_manager.append_block(block)

    # alt, chance加上2
    filter_manager.add_comment(400, 'Currency - PART 1 - Common currency')
    blocks = filter_manager.get_block(400)
    blocks[0].modify(BaseType='"Orb of Alteration" "Chromatic Orb" "Jeweller\'s Orb" ', PlayAlertSound=SOUND_LOW_VALUE)
    if not filter_config.CURRENCY_ALERT_CHANCE:
        blocks[0].BaseType += ' "Orb of Chance" '
    if filter_config.CURRENCY_ALERT_TRANSMUTATION:
        blocks[0].BaseType += ' "Orb of Transmutation" '
    if filter_config.CURRENCY_ALERT_AUGMENTATION:
        blocks[0].BaseType += ' "Orb of Augmentation" '
    if not filter_config.CURRENCY_ALERT_BLACKSMITH:
        blocks[0].BaseType += ' "Blacksmith\'s Whetstone"'
    blocks[1].BaseType = '"Orb of Transmutation" "Orb of Augmentation" "Alchemy Shard"'
    blocks[2].modify(BaseType='"Armourer\'s Scrap" "Alteration Shard"',
                     SetFontSize=filter_config.CURRENCY_ARMOURER_SCRAP_FONT_SIZE)
    blocks[-1].modify(BaseType='"Portal Scroll"', SetFontSize=filter_config.CURRENCY_PORTAL_SCROLL_FONT_SIZE)
    blocks.append(blocks[-1].copy_modify(BaseType='"Scroll of Wisdom"',
                                         SetFontSize=filter_config.CURRENCY_WISDOM_SCROLL_FONT_SIZE))
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(500, 'OVERRIDE AREA 2 - Override the default rare rulesets here')

    modify0600(filter_manager)

    filter_manager.add_comment(700, 'HIDE LAYER 2 - RARE ITEMS (65+ ONLY FOR NON-REGULAR VERSIONS)')
    blocks = filter_manager.get_block(700)
    for block in blocks:
        block.status = DEBUG
    filter_manager.extend_blocks(blocks)

    # 0800-1207
    modify_gem_flask_map(filter_manager)

    # 第一组加亮，银币单独加个样式
    filter_manager.add_comment(1301, 'Regular Rare Currency')
    blocks = filter_manager.get_block(1301)
    blocks[0].modify(SetTextColor=COLOR_RED, SetBorderColor=COLOR_RED, SetBackgroundColor=COLOR_WHITE,
                     PlayAlertSound=SOUND_MID_VALUE)
    if filter_config.CURRENCY_ALERT_CHANCE:
        blocks[0].BaseType += ' "Orb of Chance"'
    if filter_config.CURRENCY_ALERT_BLACKSMITH:
        blocks[0].BaseType += ' "Blacksmith\'s Whetstone"'
    blocks[1].PlayAlertSound = SOUND_MID_VALUE
    blocks.insert(1, blocks[1].copy_modify(BaseType='"Silver Coin"', SetBackgroundColor='190 178 135'))
    filter_manager.extend_blocks(blocks)

    # 改成8
    filter_manager.add_comment(1302, 'Top Currency')
    blocks = filter_manager.get_block(1302)
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    # 高亮"Essence of Zeal"；8和1
    filter_manager.add_comment(1303, 'Essence Tier List')
    blocks = filter_manager.get_block(1303)
    blocks[0].modify(BaseType=blocks[0].BaseType + ' "Essence of Zeal"', PlayAlertSound=SOUND_TOP_VALUE)
    blocks[1].PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    # 高亮"Splinter of Chayula"，预言改成8
    filter_manager.add_comment(1304, 'Special items')
    blocks = filter_manager.get_block(1304)
    blocks[1].PlayAlertSound = None
    blocks.insert(1, blocks[1].copy_modify(BaseType='"Splinter of Chayula"',
                                           SetTextColor=COLOR_RED, SetBorderColor=COLOR_RED,
                                           SetBackgroundColor=COLOR_WHITE, PlayAlertSound=SOUND_TOP_VALUE))
    blocks[-1].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(1401, 'Exceptions to prevent ident. mistakes')
    filter_manager.extend_blocks(block_number=1401)

    # 8
    filter_manager.add_comment(1402, 'T1 - Top tier cards')
    blocks = filter_manager.get_block(1402)
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    # 8
    filter_manager.add_comment(1403, 'T2 - Great cards')
    blocks = filter_manager.get_block(1403)
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[0].BaseType += ' "Humility" "The Encroaching Darkness" '
    filter_manager.extend_blocks(blocks)

    # 1
    filter_manager.add_comment(1404, 'T3 - Decent cards')
    blocks = filter_manager.get_block(1404)
    blocks[0].PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(1405, 'T5 - Format trash tier cards... before')

    # 2
    filter_manager.add_comment(1406, 'T4 - ...showing the remaining cards')
    blocks = filter_manager.get_block(1406)
    blocks[0].PlayAlertSound = SOUND_LOW_VALUE
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(1500, 'Currency - PART 4 - remaining items')
    filter_manager.extend_blocks(block_number=1500)

    # 改成"Perandus" "Breach" "Essence" 1
    filter_manager.add_comment(1600, 'Leaguestones - Tierlists')
    blocks = filter_manager.get_block(1600)
    for block in blocks:
        block.PlayAlertSound = SOUND_MID_VALUE
    for block in blocks[::2]:
        block.BaseType = '"Perandus" "Breach" "Essence"'
    filter_manager.extend_blocks(blocks)

    # 改成T1
    filter_manager.add_comment(1701, 'Exceptions')
    blocks = filter_manager.get_block(1701)
    blocks[0].modify(SetTextColor=COLOR_UNIQUE, SetBackgroundColor=COLOR_WHITE, PlayAlertSound=SOUND_TOP_VALUE)
    blocks[1].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    # 8
    filter_manager.add_comment(1702, 'Tier 1 uniques')
    blocks = filter_manager.get_block(1702)
    for block in blocks:
        block.PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    # 改成T1
    filter_manager.add_comment(1703, 'Tier 2 uniques')
    blocks = filter_manager.get_block(1703)
    for block in blocks:
        block.modify(SetTextColor=COLOR_UNIQUE, SetBorderColor=COLOR_UNIQUE, SetBackgroundColor=COLOR_WHITE,
                     PlayAlertSound=SOUND_TOP_VALUE)
    filter_manager.extend_blocks(blocks)

    # 6
    filter_manager.add_comment(1704, 'Multi-Unique bases')
    blocks = filter_manager.get_block(1704)
    blocks[0].PlayAlertSound = SOUND_UNIQUE
    filter_manager.extend_blocks(blocks)

    # 6
    filter_manager.add_comment(1705, 'Prophecy-Material Uniques')
    blocks = filter_manager.get_block(1705)
    blocks[0].PlayAlertSound = SOUND_UNIQUE
    filter_manager.extend_blocks(blocks)

    # 6
    filter_manager.add_comment(1706, 'Random Uniques')
    blocks = filter_manager.get_block(1706)
    blocks[0].PlayAlertSound = SOUND_UNIQUE
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(1800, 'Exceptions - Quest Items etc.')
    filter_manager.extend_blocks(block_number=1800)

    # 1900-2303
    modify_leveling(filter_manager)

    # 改成最小
    filter_manager.add_comment(2400, 'HIDE LAYER 5 - Remaining Items')
    block = filter_manager.get_block(2400)[0]
    block.modify(status=DEBUG, SetFontSize=FONT_SIZE_MIN)
    filter_manager.append_block(block)

    # 8
    filter_manager.add_comment(2500, 'CATCHALL - if you see pink items - send me a mail please - should never happen')
    blocks = filter_manager.get_block(2500)
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)


if __name__ == '__main__':
    with open("NeverSink's filter - 1-REGULAR.filter") as f:
        fm = FilterManager(f.readlines())

    modify_filter(fm)

    with open(os.path.expanduser('~') + "\Documents\My Games\Path of Exile\MODIFY.filter", 'w') as f:
        f.writelines(fm.new_text)
