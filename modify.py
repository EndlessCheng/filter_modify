# -*- coding:utf-8 -*-

import time
import os
import platform

import shutil

from utils import FilterBlock, FilterManager
import settings

SHOW = 'Show'
HIDE = 'Hide'
DEBUG = SHOW if settings.DEBUG else HIDE

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
COLOR_SILVER = '200 200 200'
COLOR_GRAY = '150 150 150'
COLOR_BLACK = '0 0 0'
COLOR_RED = '255 0 0'
COLOR_YELLOW = '255 255 0'
COLOR_TANGERINE = '213 159 0'
COLOR_ORANGE = '255 125 0'
COLOR_UNIQUE = '175 96 37'  # Rich Gold
COLOR_OLIVE = '100 75 0'
COLOR_LIME = '0 255 0'
COLOR_LIME_LIGHT = '0 210 0 210'
COLOR_AQUA = '0 255 255'
COLOR_BLUE = '0 0 255'
COLOR_MAGENTA = '255 0 255'
COLOR_MAGENTA_DARK = '129 15 213 200'

SOUND_TOP_VALUE = '8 300'
SOUND_MID_VALUE = '1 300'
SOUND_LOW_VALUE = '2 300'
SOUND_MAP = '4 300'
SOUND_UNIQUE = '6 300'
# SOUND_CHANCE = '4 300'
# SOUND_CHANCE2 = '3 300'
SOUND_LEVELING = '12 300'

STYLE_TOP = {'SetTextColor': COLOR_RED, 'SetBorderColor': COLOR_RED, 'SetBackgroundColor': COLOR_WHITE}
STYLE_TOP_RARE = {'SetBorderColor': COLOR_ORANGE, 'SetBackgroundColor': COLOR_OLIVE}
STYLE_T1_RARE = {'SetBorderColor': COLOR_ORANGE, 'SetBackgroundColor': COLOR_OLIVE + ' 225'}
STYLE_TOP_UNIQUE = {'SetTextColor': COLOR_UNIQUE, 'SetBorderColor': COLOR_UNIQUE, 'SetBackgroundColor': COLOR_WHITE}
_STYLE_MAP_BASE = {'SetFontSize': FONT_SIZE_MAX, 'SetTextColor': COLOR_BLACK, 'SetBackgroundColor': COLOR_SILVER}
STYLE_MAP_HIGH_11_14 = {**_STYLE_MAP_BASE, 'SetBorderColor': COLOR_RED}
STYLE_MAP_MID_9_10 = {**_STYLE_MAP_BASE, 'SetBorderColor': COLOR_ORANGE}
STYLE_MAP_MID_6_8 = {**_STYLE_MAP_BASE, 'SetBorderColor': COLOR_YELLOW}
STYLE_MAP_LOW_3_5 = {**_STYLE_MAP_BASE, 'SetBorderColor': COLOR_BLUE}
STYLE_MAP_LOW_1_2 = {**_STYLE_MAP_BASE, 'SetBorderColor': COLOR_WHITE}
STYLE_LINKS = {'SetBorderColor': COLOR_AQUA}
STYLE_NONE = {'SetFontSize': None, 'SetTextColor': None, 'SetBorderColor': None, 'SetBackgroundColor': None}


# 0200
def modify_endgame_mix(filter_manager):
    filter_manager.add_comment(200, 'Recipes, Magic and Normal items (endgame!)', ignored=True)

    # 8
    blocks = filter_manager.add_comment(201, '6-Linked items')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    # 8
    blocks = filter_manager.add_comment(202, '5-Linked items')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    # 8 1 样式改掉
    blocks = filter_manager.add_comment(203, '6-Socket Items')
    blocks[0].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    blocks[1].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    del blocks[2]  # 移除不需要的提示
    blocks[2].modify(SetTextColor=COLOR_WHITE, SetBorderColor=COLOR_BLACK, SetBackgroundColor=COLOR_TANGERINE,
                     PlayAlertSound=SOUND_MID_VALUE)
    filter_manager.extend_blocks(blocks)

    # 8 1
    blocks = filter_manager.add_comment(204, 'Exclusive bases: Atlas bases, talismans (includes Rare rarity)')
    blocks[0].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    blocks[1].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    blocks[2].modify(PlayAlertSound=SOUND_MID_VALUE, **STYLE_TOP_RARE)
    blocks[3].modify(PlayAlertSound=SOUND_MID_VALUE, **STYLE_TOP_RARE)
    blocks[4].modify(PlayAlertSound=SOUND_MID_VALUE, **STYLE_TOP_RARE)
    filter_manager.extend_blocks(blocks)

    # 改稀有度
    # 项链：+1诅咒，+1球，抗性上限；  腰带：+1球
    # 手：击中附加诅咒；  脚：+1球；  箭袋：+1箭；  爪匕剑：3-6%格挡
    filter_manager.add_comment(205, 'Corrupted items', ignored=True)
    block_small = FilterBlock(Corrupted=True, Class='"Amulets" "Belts"', Rarity=RARITY_N2R,
                              SetFontSize=36, SetBorderColor=COLOR_MAGENTA_DARK)
    block_other = block_small.copy_modify(Class='"Gloves" "Boots" "Quivers" "Claws" "Daggers" "One Hand Swords"',
                                          SetFontSize=None)
    filter_manager.extend_blocks([block_small, block_other])

    # 参考模板 CHANCING_BASE_TYPE
    filter_manager.add_comment(206, 'Chancing items', ignored=True)
    if settings.CHANCING_BASE_TYPE != '':
        block = FilterBlock(Corrupted=False, BaseType=settings.CHANCING_BASE_TYPE, Rarity=RARITY_NORMAL,
                            SetFontSize=38, SetTextColor=COLOR_WHITE, SetBorderColor=COLOR_LIME_LIGHT,
                            # PlayAlertSound=SOUND_CHANCE
                            )
        filter_manager.append_block(block)

    # ALERT_UTILITY_FLASK_BASE_TYPE
    # 无视物等
    blocks = filter_manager.add_comment(207, 'FLASKS (Endgame rules)')
    if settings.ALERT_UTILITY_FLASK_BASE_TYPE != '':
        block_utility = blocks[0].copy_modify(Quality=None, Class='"Utility Flasks"',
                                              BaseType=settings.ALERT_UTILITY_FLASK_BASE_TYPE, ItemLevel=None,
                                              PlayAlertSound=SOUND_LEVELING)
        filter_manager.append_block(block_utility)
    blocks[0].PlayAlertSound = SOUND_LOW_VALUE
    blocks[1].modify(SetFontSize=blocks[0].SetFontSize, PlayAlertSound=SOUND_LOW_VALUE)
    blocks[2] = blocks[1].copy_modify(Quality='>= 5', Class='"Utility Flasks"', BaseType=None, ItemLevel=None)
    filter_manager.extend_blocks(blocks[:3])

    filter_manager.add_comment(208, 'Add your own crafting rules here', ignored=True)

    blocks = filter_manager.add_comment(209, '83/84+ Endgame crafting rules')
    filter_manager.extend_blocks(blocks)

    # 只留第一个 ALERT_JEWEL_BASE_TYPE
    # ALERT_MAGIC_BASE_TYPE
    blocks = filter_manager.add_comment(210, 'Magic jewel and others')
    if settings.ALERT_JEWEL_BASE_TYPE != '':
        block_alert_jewel = blocks[0].copy_modify(BaseType=settings.ALERT_JEWEL_BASE_TYPE,
                                                  PlayAlertSound=SOUND_LEVELING)
        filter_manager.append_block(block_alert_jewel)
    filter_manager.append_block(blocks[0])

    if settings.ALERT_MAGIC_BASE_TYPE != '':
        block_magic = filter_manager.get_blocks(2406)[1]
        block_magic_alert = block_magic.copy_modify(BaseType=settings.ALERT_MAGIC_BASE_TYPE, ItemLevel=None,
                                                    PlayAlertSound=SOUND_LEVELING)
        filter_manager.append_block(block_magic_alert)

    # 去掉 Hide
    blocks = filter_manager.add_comment(211, 'Warband items')
    filter_manager.extend_blocks(blocks[:2])

    # SSF_CRAFT_BASE_TYPE, SSF_CRAFT_AMULETS_BASE_TYPE, SSF_CRAFT_RINGS_BASE_TYPE, SSF_CRAFT_BELTS_BASE_TYPE
    filter_manager.add_comment(212, 'Remaining crafting rules - add your own bases here!', ignored=True)
    if settings.SSF_CRAFT_BASE_TYPE != '':
        block_normal = filter_manager.get_blocks(2406)[0]
        block_normal_alert = block_normal.copy_modify(BaseType=settings.SSF_CRAFT_BASE_TYPE, ItemLevel=None,
                                                      SetFontSize=40, PlayAlertSound=SOUND_LEVELING)
        filter_manager.append_block(block_normal_alert)
    if settings.SSF_CRAFT_AMULETS_BASE_TYPE != '':
        filter_manager.append_block(FilterBlock(
            Class='Amulets', BaseType=settings.SSF_CRAFT_AMULETS_BASE_TYPE, Rarity=RARITY_NORMAL, ItemLevel='>= 13',
            SetTextColor=COLOR_WHITE))
    if settings.SSF_CRAFT_RINGS_BASE_TYPE != '':
        filter_manager.append_block(FilterBlock(
            Class='Rings', BaseType=settings.SSF_CRAFT_RINGS_BASE_TYPE, Rarity=RARITY_NORMAL, ItemLevel='>= 13',
            SetTextColor=COLOR_WHITE))
    if settings.SSF_CRAFT_BELTS_BASE_TYPE != '':
        block_hide_n_leather_belt = filter_manager.get_blocks(2600)[0].copy_modify(
            Class=None, BaseType='"Leather Belt"', Rarity=RARITY_NORMAL, ItemLevel='<= 39')
        filter_manager.append_block(block_hide_n_leather_belt)
        filter_manager.append_block(FilterBlock(
            Class='Belts', BaseType=settings.SSF_CRAFT_BELTS_BASE_TYPE, Rarity=RARITY_NORMAL, ItemLevel='>= 13',
            SetTextColor=COLOR_WHITE))

    # NEED_CHISEL
    blocks = filter_manager.add_comment(213, 'Chisel recipe items')
    for block in blocks:
        block.PlayAlertSound = SOUND_MID_VALUE
    blocks[1].Quality = '>= 10' if settings.NEED_CHISEL else '>= 14'
    blocks[2].Quality = '>= 0' if settings.NEED_CHISEL else '>= 5'
    filter_manager.extend_blocks(blocks[:3])

    # 8
    blocks = filter_manager.add_comment(214, 'Fishing Rod')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(215, 'SRS Crude Bow', ignored=True)

    # NEED_RGB
    blocks = filter_manager.add_comment(216, 'Chromatic recipe items ("RGB Recipe")')
    if settings.NEED_RGB:
        filter_manager.extend_blocks(blocks)

    # SHOW_ENDGAME_4L
    blocks = filter_manager.add_comment(217, 'Endgame-start 4-links')
    if settings.SHOW_ENDGAME_4L:
        filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(218, 'Animate Weapon script - deactivated by default', ignored=True)

    # 8，改稀有度，高亮边框
    blocks = filter_manager.add_comment(219, 'W-soc offhand weapons')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[1].modify(Rarity=RARITY_N2R, SetFontSize=38, SetBorderColor=COLOR_WHITE)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(220, 'Sacrificial Garb')
    filter_manager.extend_blocks(blocks)


# 0600
def modify_endgame_rare(filter_manager):
    filter_manager.add_comment(600, 'RARE ITEMS (ENDGAME)', ignored=True)

    # 1
    blocks = filter_manager.add_comment(601, 'Rare crafting bases')
    blocks[0].PlayAlertSound = SOUND_MID_VALUE
    blocks[1].PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    # T1_RARE_BASE_TYPE
    # HIDE_ENDGAME_BELOW_T1_RARE_CLASS
    blocks = filter_manager.add_comment(602, 'T1 rare items')
    if settings.T1_RARE_BASE_TYPE != '':
        filter_manager.append_block(blocks[0].copy_modify(BaseType=settings.T1_RARE_BASE_TYPE,
                                                          PlayAlertSound=SOUND_MID_VALUE, **STYLE_T1_RARE))
        filter_manager.append_block(blocks[1].copy_modify(BaseType=settings.T1_RARE_BASE_TYPE, ItemLevel=None,
                                                          PlayAlertSound=SOUND_MID_VALUE, **STYLE_T1_RARE))

    if settings.HIDE_ENDGAME_BELOW_T1_RARE_CLASS != '':
        hide_blocks = filter_manager.get_blocks(700)
        for hide_block in hide_blocks[-2:]:
            hide_block.modify(status=DEBUG, Identified=False, Class=settings.HIDE_ENDGAME_BELOW_T1_RARE_CLASS)
            filter_manager.append_block(hide_block)

    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(603, 'T2 rare items')
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(604, 'Breach Rings')
    filter_manager.extend_blocks(blocks)

    # ALERT_SMALLS_RARE
    # 1, 1, 12, 1, 12
    blocks = filter_manager.add_comment(605, 'Amulets, Jewels, Rings, Belts')
    blocks[0].PlayAlertSound = SOUND_MID_VALUE  # rare jewel
    if settings.ALERT_SMALLS_RARE:
        blocks[1].modify(PlayAlertSound=SOUND_MID_VALUE, SetBackgroundColor=COLOR_TANGERINE)  # regal smalls
        blocks[2].PlayAlertSound = SOUND_LEVELING  # 65-74 smalls
        blocks[3].modify(PlayAlertSound=SOUND_MID_VALUE, SetBackgroundColor=COLOR_TANGERINE)  # regal smalls
        blocks[4].PlayAlertSound = SOUND_LEVELING  # 65-74 smalls
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(606, '1H Daggers', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(607, '1H Claws', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(608, '1H Wands', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(609, '1H Foils', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(610, '1H Swords', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(611, '1H Maces', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(612, '1H Axes', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(613, '1H Sceptres', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(614, '2H Staves', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(615, '2H Swords, Axes, Maces', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(616, '2H Bows', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(617, 'AR: Gloves, Boots, Helmets', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(618, 'AR: Body Armors', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(619, 'OH: Shields', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(620, 'OH: Quivers', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)


# 0800-1207
def modify_gem_flask_map(filter_manager):
    filter_manager.add_comment(800, 'OVERRIDE AREA 3 - Override Map, Gem and Flask drops here', ignored=True)

    filter_manager.add_comment(900, 'Gems', ignored=True)

    # 8, 1
    blocks = filter_manager.add_comment(901, 'Value gems')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[1].modify(Quality='>= 15', PlayAlertSound=SOUND_TOP_VALUE)
    blocks[2].modify(SetBackgroundColor=COLOR_WHITE, PlayAlertSound=SOUND_TOP_VALUE)
    blocks[2].BaseType += ' "Added Chaos Damage" "Vaal Summon Skeletons"'
    blocks[3].modify(Quality='>= 10', PlayAlertSound=SOUND_MID_VALUE)
    filter_manager.extend_blocks(blocks)

    # 前两个换位，改成1和2
    # LEVELING_GEMS_BASE_TYPE
    blocks = filter_manager.add_comment(902, 'Other gems')
    blocks[0], blocks[1] = blocks[1], blocks[0]
    blocks[0].PlayAlertSound = SOUND_MID_VALUE
    blocks[1].PlayAlertSound = SOUND_LOW_VALUE
    if settings.LEVELING_GEMS_BASE_TYPE != '':
        block_leveling_gems = blocks[0].copy_modify(BaseType=settings.LEVELING_GEMS_BASE_TYPE,
                                                    PlayAlertSound=SOUND_TOP_VALUE)
        blocks.insert(2, block_leveling_gems)
    else:
        blocks[2].status = DEBUG
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(1000, 'UTILITY FLASKS (Levelling Rules)', ignored=True)

    blocks = filter_manager.add_comment(1100, 'HIDE LAYER 3: Random Endgame Flasks')
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(1200, 'Maps, fragments and labyrinth items', ignored=True)

    # 8
    blocks = filter_manager.add_comment(1201, 'Unique Maps')
    blocks[0].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    blocks[1].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(1202, 'Labyrinth items, Offerings')
    filter_manager.extend_blocks(blocks)

    # T15加红边
    blocks = filter_manager.add_comment(1203, 'Top tier maps (T15-16)')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[1].modify(SetBorderColor=COLOR_RED, PlayAlertSound=SOUND_TOP_VALUE)
    filter_manager.extend_blocks(blocks)

    # 加红边
    blocks = filter_manager.add_comment(1204, 'High tier maps(T11-14)')
    for block in blocks:
        block.modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_MAP_HIGH_11_14)
    filter_manager.extend_blocks(blocks)

    # 加黄边/橙边，不显示稀有度
    blocks = filter_manager.add_comment(1205, 'Mid tier maps (T6-10)')
    for block in blocks[:4]:
        block.modify(PlayAlertSound=SOUND_MAP, **STYLE_MAP_MID_9_10)
    for block in blocks[4:]:
        block.modify(PlayAlertSound=SOUND_MAP, **STYLE_MAP_MID_6_8)
    filter_manager.extend_blocks(blocks)

    # 加蓝边/黑边，不显示稀有度
    blocks = filter_manager.add_comment(1206, 'Low tier maps (T1-T5)')
    for block in blocks[:6]:
        block.modify(PlayAlertSound=SOUND_MAP, **STYLE_MAP_LOW_3_5)
    for block in blocks[6:-1]:
        block.modify(PlayAlertSound=SOUND_MAP, **STYLE_MAP_LOW_1_2)
    filter_manager.extend_blocks(blocks)

    # 8, 4
    blocks = filter_manager.add_comment(1207, 'Map fragments')
    for block in blocks[:-2]:
        block.PlayAlertSound = SOUND_TOP_VALUE
    blocks[-2].PlayAlertSound = SOUND_MAP
    blocks[-1].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)


# 1900-2505
def modify_leveling(filter_manager):
    # HIDE_FLASK_MANA, SHOW_FLASK_LIFE；后期只要42和60级的血瓶
    # HIDE_LEVELING_RARE_CLASS
    # RARE_BOOTS_ALERT  放前面是考虑到[[2200]]的影响
    # MAGIC_BOOTS_IL
    filter_manager.add_comment(1900, 'OVERRIDE AREA 4 - Insert your custom leveling adjustments here', ignored=True)
    block_hide_flasks = FilterBlock(status=DEBUG, Quality='= 0', Class='"Hybrid Flask" ', SetFontSize=FONT_SIZE_MIN)
    if settings.HIDE_FLASK_MANA:
        block_hide_flasks.Class += ' "Mana Flask" '
    if not settings.SHOW_FLASK_LIFE:
        block_hide_flasks.Class += ' "Life Flask" '
    block_hide_some_life_flasks = FilterBlock(status=DEBUG, Quality='= 0', Class='"Life Flask"',
                                              BaseType='Sanctified Eternal', SetFontSize=FONT_SIZE_MIN)
    filter_manager.extend_blocks([block_hide_flasks, block_hide_some_life_flasks])

    if settings.HIDE_LEVELING_RARE_CLASS != '':
        filter_manager.append_block(
            FilterBlock(status=DEBUG, Corrupted=False, Class=settings.HIDE_LEVELING_RARE_CLASS, Rarity=RARITY_RARE,
                        SetFontSize=26))

    # if settings.RARE_BOOTS_ALERT:
    #     block_rare_boots = filter_manager.get_blocks(2301)[2].copy_modify(
    #         ItemLevel=None, SetFontSize=FONT_SIZE_MAX, PlayAlertSound=SOUND_LEVELING, **STYLE_4L)
    #     filter_manager.append_block(block_rare_boots)
    #
    # _magic_boots_il_map = {10: None, 15: '>= 15', 20: '>= 30', 25: '>= 40', 30: '>= 55', -1: '< 1'}
    # block_magic_boots = filter_manager.get_blocks(2404)[0].copy_modify(
    #     ItemLevel=_magic_boots_il_map[settings.MAGIC_BOOTS_IL],
    #     SetFontSize=FONT_SIZE_MAX, PlayAlertSound=SOUND_LEVELING, **STYLE_4L)
    # filter_manager.append_block(block_magic_boots)

    filter_manager.add_comment(2000, 'Leveling - Flasks', ignored=True)

    blocks = filter_manager.add_comment(2001, 'Hide outdated flasks')
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(2002, 'Hybrid flasks', ignored=True)

    # SHOW_FLASK_HALLOWED 42, 60
    blocks = filter_manager.add_comment(2003, 'Life Flasks')
    blocks[-4].ItemLevel = None if settings.SHOW_FLASK_HALLOWED else '<= 1'
    blocks[-2].ItemLevel = None
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(2004, 'Mana Flasks')
    filter_manager.extend_blocks(blocks)

    # 15改成10
    blocks = filter_manager.add_comment(2005, 'Show remaining flasks')
    blocks[1].Quality = '>= 10'
    del blocks[2]  # 移除不需要的提示
    blocks[-1].status = DEBUG
    filter_manager.extend_blocks(blocks)

    # 8
    blocks = filter_manager.add_comment(2100, 'Leveling - Merged Rules')  # 包含 4L RGB
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    # NEED_RGB
    blocks = filter_manager.add_comment(2200, 'Leveling - RGB Recipes')
    if settings.NEED_RGB:
        filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(2300, 'Leveling - RARES', ignored=True)

    # Referred by [[1900]]
    # Rare: 4L/RRG/RRR L3_MAX_IL
    blocks = filter_manager.add_comment(2301, 'Leveling rares - specific items')
    if settings.LINKED_CLASS != '':
        blocks[0].modify(Class=settings.LINKED_CLASS, **STYLE_LINKS)
        blocks.insert(1, blocks[0].copy_modify(LinkedSockets='>= 3', SocketGroup='RRG',
                                               ItemLevel='<= ' + str(settings.L3_MAX_IL)))
        blocks.insert(2, blocks[1].copy_modify(SocketGroup='RRR'))
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(2302, 'Leveling rares - Progression')
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(2303, 'Leveling rares - remaining rules')
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(2400, 'Leveling - Useful items', ignored=True)

    # RR**
    blocks = filter_manager.add_comment(2401, 'Linked gear - 4links')
    if settings.LINKED_CLASS != '':
        for block in blocks:
            block.modify(Class=settings.LINKED_CLASS, SocketGroup='RR', **STYLE_LINKS)
            filter_manager.append_block(block)

    filter_manager.add_comment(2402, 'Linked gear - Caster Weapon Configuration', ignored=True)

    # RG RRG RRR L2_MAX_IL L3_MAX_IL
    blocks = filter_manager.add_comment(2403, 'Linked gear - 3links')
    if settings.LINKED_CLASS != '':
        for block in blocks[:2]:
            block.modify(LinkedSockets=None, Class='"Helmets" "Boots" "Body Armour"', **STYLE_LINKS)
            block_rg = block.copy_modify(SocketGroup='RG', ItemLevel='<= ' + str(settings.L2_MAX_IL),
                                         PlayAlertSound=SOUND_LEVELING)
            block_rrg = block_rg.copy_modify(SocketGroup='RRG', ItemLevel='<= ' + str(settings.L3_MAX_IL))
            block_rrr = block_rg.copy_modify(SocketGroup='RRR', ItemLevel='<= ' + str(settings.L3_MAX_IL))
            filter_manager.extend_blocks([block_rg, block_rrg, block_rrr])

    # Referred by [[1900]]
    filter_manager.add_comment(2404, 'Extra Highlight: Boots', ignored=True)

    filter_manager.add_comment(2405, 'Optional Recipes', ignored=True)

    # Referred by [0210] [0212]
    blocks = filter_manager.add_comment(2406, 'Act 1')
    blocks[0].BaseType = '"Rustic Sash" "Amulet"' if settings.TENCENT else '"Iron Ring" "Rustic Sash" "Amulet"'
    blocks[1].BaseType = '"Iron Ring" "Rustic Sash" "Amulet"'
    filter_manager.extend_blocks(blocks[:2])
    blocks[4].Rarity = RARITY_MAGIC
    filter_manager.append_block(blocks[4])

    filter_manager.add_comment(2407, 'Act 2+3', ignored=True)

    filter_manager.add_comment(2408, 'Act 4+5+6', ignored=True)

    filter_manager.add_comment(2409, 'Jewellery - Regular Highlight', ignored=True)

    filter_manager.add_comment(2410, 'Quivers - Progression', ignored=True)

    filter_manager.add_comment(2411, 'Magic Gear', ignored=True)

    filter_manager.add_comment(2412, '20% quality items for those strange people who want them', ignored=True)

    # MOVE_HAND_MAX_IL
    # BBB_MAX_IL
    filter_manager.add_comment(2500, 'Levelling - normal and magic item progression', ignored=True)
    block_rrg_weapon = FilterBlock(SocketGroup='RRG', Class=' "One Hand" "Claws" "Sceptres" "Daggers" ',
                                   ItemLevel='<= ' + str(settings.MOVE_HAND_MAX_IL),
                                   SetFontSize=42, PlayAlertSound=SOUND_MID_VALUE, **STYLE_LINKS)
    filter_manager.append_block(block_rrg_weapon)

    # for sg in ['RBB', 'BBB']:
    #     block_swap = FilterBlock(SocketGroup=sg, Class='"One Hand" "Claws" "Sceptres" "Daggers"',
    #                              ItemLevel='<= ' + str(settings.BBB_MAX_IL),
    #                              SetFontSize=38, PlayAlertSound=SOUND_MID_VALUE, **STYLE_4L)
    #     filter_manager.append_block(block_swap)

    # 蓝白武器，提取模板
    # HIDE_NORMAL_MAGIC_CLASS
    blocks = filter_manager.add_comment(2501, 'Progression - Part 1 1-30')
    _LEVELING_BASE = [('"Rusted Sword"', 1), ('"Copper Sword"', 5), ('"Sabre"', 10),
                      ('"Rusted Hatchet"', 1), ('"Jade Hatchet"', 6), ('"Boarding Axe"', 11), ('"Broad Axe"', 21),
                      ('"Arming Axe"', 25), ('"Spectral Axe"', 33), ('"Jasper Axe"', 36),
                      ('"War Axe"', 45), ('"Chest Splitter"', 48), ('"Wraith Axe"', 54),
                      ]
    _LEVELING_BASE_IL_GAP = 3
    block_template = blocks[0].copy_modify(DropLevel=None, Class=None, SetFontSize=42)
    block_weapon_list = [block_template.copy_modify(BaseType=leveling_base[0],
                                                    ItemLevel='<= ' + str(leveling_base[1] + _LEVELING_BASE_IL_GAP))
                         for leveling_base in _LEVELING_BASE]
    filter_manager.extend_blocks(block_weapon_list)

    block_hide_n2m = filter_manager.get_blocks(2600)[0].copy_modify(
        Class='"Rings" "Amulets" "Belts" '
              '"Bows" "Quivers" "Two Hand" "Staves" "Shields" "Claws" "Daggers" "Sceptres" "Wands" "One Hand" ' +
              settings.HIDE_NORMAL_MAGIC_CLASS, ItemLevel='>= 2', SetFontSize=FONT_SIZE_MIN)
    block_hide_m5 = block_hide_n2m.copy_modify(Class='"Helmets" "Boots" "Body Armour"', ItemLevel='>= 5')
    filter_manager.extend_blocks([block_hide_n2m, block_hide_m5])

    filter_manager.add_comment(2502, 'Progression - Part 2 30-40', ignored=True)

    filter_manager.add_comment(2503, 'Progression - Part 4 40-65', ignored=True)

    blocks = filter_manager.add_comment(2504, 'Normal items - First 4 levels - exceptions')
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(2505, 'Magic items - general highlight')
    filter_manager.extend_blocks(blocks)


def modify_filter(filter_manager):
    filter_manager.add_comment(100, 'OVERRIDE AREA 1 - Override ALL rules here', ignored=True)

    # 0200
    modify_endgame_mix(filter_manager)

    blocks = filter_manager.add_comment(300, 'HIDE LAYER 1 - MAGIC AND NORMAL ITEMS')
    blocks[0].modify(status=DEBUG)
    filter_manager.extend_blocks(blocks)

    # CURRENCY_ALERT_XXX
    # CURRENCY_XXX_FONT_SIZE
    blocks = filter_manager.add_comment(400, 'Currency - PART 1 - Common currency')
    blocks[0].BaseType = '"Orb of Alteration" "Chromatic Orb" "Jeweller\'s Orb" '
    if settings.CURRENCY_ALERT_TRANSMUTATION:
        blocks[0].BaseType += ' "Orb of Transmutation" '
    if settings.CURRENCY_ALERT_BLACKSMITH:
        blocks[0].BaseType += ' "Blacksmith\'s Whetstone"'
    if settings.CURRENCY_ALERT_AUGMENTATION:
        blocks[0].BaseType += ' "Orb of Augmentation" '
    if not settings.CURRENCY_ALERT_CHANCE:
        blocks[0].BaseType += ' "Orb of Chance" '
    if settings.ALERT_LOW_CURRENCY:
        blocks[0].PlayAlertSound = SOUND_LOW_VALUE
    blocks[1].BaseType += ' "Orb of Augmentation"'
    blocks[2].SetFontSize = settings.CURRENCY_PORTAL_FONT_SIZE
    blocks[3].BaseType = blocks[3].BaseType.replace('"Transmutation Shard"', '')
    blocks[3].SetFontSize = settings.CURRENCY_ARMOURER_SCRAP_FONT_SIZE
    blocks[4].SetFontSize = settings.CURRENCY_WISDOM_FONT_SIZE
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(500, 'OVERRIDE AREA 2 - Override the default rare rulesets here', ignored=True)

    # 0600
    modify_endgame_rare(filter_manager)

    # Referred by [0602]
    blocks = filter_manager.add_comment(700, 'HIDE LAYER 2 - RARE ITEMS (65+ ONLY FOR NON-REGULAR VERSIONS)')
    for block in blocks:
        block.status = DEBUG
    filter_manager.extend_blocks(blocks)

    # 0800-1207
    modify_gem_flask_map(filter_manager)

    filter_manager.add_comment(1300, 'Currency - PART 2 - Rare currency', ignored=True)

    # 8
    blocks = filter_manager.add_comment(1302, 'Top Currency')
    blocks[0].BaseType += ' "Master Cartographer\'s Sextant" "Orb of Annulment" "Stacked Deck" '
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    # CURRENCY_ALERT_XXX
    blocks = filter_manager.add_comment(1301, 'Regular Rare Currency')
    blocks[1].BaseType += ' "Regal Shard"'
    if settings.CURRENCY_ALERT_CHANCE:
        blocks[1].BaseType += ' "Orb of Chance"'
    blocks[0].BaseType += ' ' + blocks[1].BaseType
    blocks[0].PlayAlertSound = SOUND_MID_VALUE
    blocks[1].PlayAlertSound = SOUND_MID_VALUE

    blocks[2].BaseType += ' "Glassblower\'s Bauble"'
    blocks[2].PlayAlertSound = SOUND_MID_VALUE
    blocks.insert(3, blocks[2].copy_modify(BaseType='"Silver Coin"', SetBackgroundColor='190 178 135'))  # Pavlova
    blocks[-2].BaseType += ' "Horizon Shard"'
    blocks[-2].PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    # ALERT_ESSENCE_BASE_TYPE, 8, 1
    blocks = filter_manager.add_comment(1303, 'Essence Tier List')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[0].BaseType += settings.ALERT_ESSENCE_BASE_TYPE
    blocks[1].PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    # alert "Splinter of Chayula"
    blocks = filter_manager.add_comment(1304, 'Special items')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[1].PlayAlertSound = SOUND_MID_VALUE
    blocks[2].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    blocks[3].PlayAlertSound = None
    blocks[-1].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(1400, 'Currency - PART 3 - Divination cards', ignored=True)

    blocks = filter_manager.add_comment(1401, 'Exceptions to prevent ident. mistakes')
    filter_manager.extend_blocks(blocks)

    # 8
    blocks = filter_manager.add_comment(1402, 'T1 - Top tier cards')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    # 8
    blocks = filter_manager.add_comment(1403, 'T2 - Great cards')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[0].BaseType += ' "Humility" "The Encroaching Darkness" "The Throne" '
    filter_manager.extend_blocks(blocks)

    # 1
    blocks = filter_manager.add_comment(1404, 'T3 - Decent cards')
    blocks[0].PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    # 2
    blocks = filter_manager.add_comment(1405, 'T5 - Format trash tier cards... before')
    blocks[0].PlayAlertSound = SOUND_LOW_VALUE
    filter_manager.extend_blocks(blocks)

    # 2
    blocks = filter_manager.add_comment(1406, 'T4 - ...showing the remaining cards')
    blocks[0].PlayAlertSound = SOUND_LOW_VALUE
    filter_manager.extend_blocks(blocks)

    # CATCHALL
    blocks = filter_manager.add_comment(1500, 'Currency - PART 4 - remaining items')
    blocks[0].BaseType += ' "Transmutation Shard" '
    blocks[0].SetFontSize = FONT_SIZE_MIN
    blocks[1].modify(SetFontSize=FONT_SIZE_MAX, PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(1600, 'Leaguestones - Tierlists')
    for block in blocks[:-1]:
        block.PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(1700, 'Uniques!', ignored=True)

    # 改成T1
    blocks = filter_manager.add_comment(1701, 'Exceptions')
    for block in blocks:
        block.PlayAlertSound = SOUND_TOP_VALUE
    blocks[0].modify(**STYLE_TOP_UNIQUE)
    filter_manager.extend_blocks(blocks)

    # 6
    blocks = filter_manager.add_comment(1702, 'Harbinger - Pieces')
    blocks[0].PlayAlertSound = SOUND_UNIQUE
    filter_manager.extend_blocks(blocks)

    # 8
    blocks = filter_manager.add_comment(1703, 'Tier 1 uniques')
    for block in blocks:
        block.PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    # 改成T1
    blocks = filter_manager.add_comment(1704, 'Tier 2 uniques')
    for block in blocks:
        block.modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP_UNIQUE)
    filter_manager.extend_blocks(blocks)

    # 6
    blocks = filter_manager.add_comment(1705, 'Multi-Unique bases')
    blocks[0].PlayAlertSound = SOUND_UNIQUE
    filter_manager.extend_blocks(blocks)

    # 6
    blocks = filter_manager.add_comment(1706, 'Prophecy-Material Uniques')
    blocks[0].PlayAlertSound = SOUND_UNIQUE
    filter_manager.extend_blocks(blocks)

    # 6
    blocks = filter_manager.add_comment(1707, 'Random Uniques')
    blocks[0].PlayAlertSound = SOUND_UNIQUE
    filter_manager.extend_blocks(blocks)

    # 1
    blocks = filter_manager.add_comment(1800, 'Quest Items and Shaper Orbs')
    blocks[0].PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    # 1900-2505
    modify_leveling(filter_manager)

    # Referred by [0212] [2501]
    block = filter_manager.add_comment(2600, 'HIDE LAYER 5 - Remaining Items')[0]
    block.modify(status=DEBUG, SetFontSize=FONT_SIZE_MIN)
    filter_manager.append_block(block)

    # 8
    block = filter_manager.add_comment(2700, 'CATCHALL')[0]
    block.PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.append_block(block)


def main():
    start_time = time.time()

    filter_name = 'res' + os.sep + 'NeverSink\'s filter - 1-REGULAR.filter'
    with open(filter_name) as f:
        fm = FilterManager(f.readlines())

    modify_filter(fm)

    out_file_path = 'out' + os.sep + 'MODIFY.filter'
    with open(out_file_path, 'w') as f:
        f.writelines(fm.new_text)
    if platform.system() == 'Windows':
        shutil.copyfile(out_file_path, os.path.expanduser('~') + "\Documents\My Games\Path of Exile\MODIFY.filter")

    print("Modify success, time cost: {:.0f}ms".format(1000 * (time.time() - start_time)))


if __name__ == '__main__':
    main()
