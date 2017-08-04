# -*- coding:utf-8 -*-

import time
import os

from filter_modify import FilterBlock, FilterManager
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
COLOR_GRAY_LIGHT = '200 200 200'
COLOR_GRAY = '150 150 150'
COLOR_BLACK = '0 0 0'
COLOR_RED = '255 0 0'
COLOR_RED_LIGHT = '210 0 0'
COLOR_GREEN = '0 255 0'
COLOR_BLUE = '0 0 255'
COLOR_BLUE_LIGHT = '136 136 255'
COLOR_YELLOW = '255 255 0'
COLOR_YELLOW_LIGHT = '255 255 119'
COLOR_AQUA = '0 255 255'
COLOR_CYAN = '100 255 255'
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

STYLE_TOP = {'SetTextColor': COLOR_RED, 'SetBorderColor': COLOR_RED, 'SetBackgroundColor': COLOR_WHITE}
STYLE_TOP_RARE = {'SetBorderColor': COLOR_ORANGE, 'SetBackgroundColor': COLOR_BROWN}
STYLE_T1_RARE = {'SetBorderColor': COLOR_ORANGE, 'SetBackgroundColor': COLOR_BROWN + ' 225'}
STYLE_TOP_UNIQUE = {'SetTextColor': COLOR_UNIQUE, 'SetBorderColor': COLOR_UNIQUE, 'SetBackgroundColor': COLOR_WHITE}
STYLE_4L = {'SetBorderColor': COLOR_AQUA}


def modify0200(filter_manager):
    filter_manager.add_comment(200, 'Recipes, Magic and Normal items (endgame!)')

    # 8
    blocks = filter_manager.add_comment(201, '6-Linked items')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    # 8 无需多言
    blocks = filter_manager.add_comment(202, '5-Linked items')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    # 8 1 样式改掉
    blocks = filter_manager.add_comment(203, '6-Socket Items')
    blocks[0].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    blocks[1].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    del blocks[2]
    blocks[2].modify(SetTextColor=COLOR_WHITE, SetBorderColor=COLOR_BLACK, SetBackgroundColor=COLOR_GOLD,
                     PlayAlertSound=SOUND_MID_VALUE)
    filter_manager.extend_blocks(blocks)

    # 8 1
    blocks = filter_manager.add_comment(204, 'Exclusive bases: Atlas bases, talismans')
    blocks[0].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    blocks[1].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    blocks[2].modify(PlayAlertSound=SOUND_MID_VALUE, **STYLE_TOP_RARE)
    blocks[3].modify(PlayAlertSound=SOUND_MID_VALUE, **STYLE_TOP_RARE)
    blocks[4].modify(PlayAlertSound=SOUND_MID_VALUE, **STYLE_TOP_RARE)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(205, 'FLASKS (Endgame rules)')
    if filter_config.ALERT_UTILITY_FLASK_BASE_TYPE != '':
        block_utility = blocks[0].copy_modify(Quality=None, Class='"Utility Flasks"',
                                              BaseType=filter_config.ALERT_UTILITY_FLASK_BASE_TYPE, ItemLevel=None,
                                              PlayAlertSound=SOUND_CHANCE)
        filter_manager.append_block(block_utility)
    blocks[0].PlayAlertSound = SOUND_LOW_VALUE
    blocks[2] = blocks[1].copy_modify(Quality='>= 5', Class='"Utility Flasks"', BaseType=None, ItemLevel=None,
                                      PlayAlertSound=SOUND_LOW_VALUE)
    filter_manager.extend_blocks(blocks)

    # 加上Gloves Boots Shields Bows Quivers，改稀有度
    # 项链：+1诅咒，+1球，移速，抗性上限
    # 腰带：+1球，技能持续时间/范围
    # 手脚盾：+1技能等级
    # 手：击中附加诅咒
    # 脚：+1球
    # 弓和箭袋：+1箭
    blocks = filter_manager.add_comment(206, 'Corrupted items')
    blocks[0].modify(Class=blocks[0].Class + ' Gloves Boots Shields Bows Quivers', Rarity=RARITY_N2R)
    filter_manager.extend_blocks(blocks)

    # 只留第一个
    block = filter_manager.add_comment(207, 'Chancing items')[0]
    if filter_config.CHANCING_BASE_TYPE != '':
        block.modify(Corrupted=False, BaseType=filter_config.CHANCING_BASE_TYPE, PlayAlertSound=SOUND_CHANCE)
        filter_manager.append_block(block)

    filter_manager.add_comment(208, 'Add your own crafting rules here')

    blocks = filter_manager.add_comment(209, '83/84+ Endgame crafting rules')
    filter_manager.extend_blocks(blocks)

    # 只留第一个
    block = filter_manager.add_comment(210, 'Magic jewel')[0]
    if filter_config.ALERT_JEWEL_BASE_TYPE != '':
        block_alert_jewel = block.copy_modify(BaseType=filter_config.ALERT_JEWEL_BASE_TYPE, PlayAlertSound=SOUND_CHANCE)
        filter_manager.append_block(block_alert_jewel)
    filter_manager.append_block(block)

    filter_manager.add_comment(211, 'Warband items')

    # SSF
    filter_manager.add_comment(212, 'Remaining crafting rules - add your own bases here!')
    if filter_config.SSF_CRAFT_BASE_TYPE != '':
        filter_manager.append_block(FilterBlock(
            BaseType=filter_config.SSF_CRAFT_BASE_TYPE, Rarity=RARITY_NORMAL,
            SetFontSize=38, SetBorderColor=COLOR_WHITE, PlayAlertSound=SOUND_CHANCE))
    if filter_config.SSF_CRAFT_AMULETS_BASE_TYPE != '':
        filter_manager.append_block(FilterBlock(
            Class='Amulets', BaseType=filter_config.SSF_CRAFT_AMULETS_BASE_TYPE, Rarity=RARITY_NORMAL,
            SetTextColor=COLOR_WHITE))
    if filter_config.SSF_CRAFT_RINGS_BASE_TYPE != '':
        filter_manager.append_block(FilterBlock(
            Class='Rings', BaseType=filter_config.SSF_CRAFT_RINGS_BASE_TYPE, Rarity=RARITY_NORMAL,
            SetTextColor=COLOR_WHITE))
    if filter_config.SSF_CRAFT_BELTS_BASE_TYPE != '':
        block_hide_n_rustic_sash = filter_manager.get_blocks(2500)[0].copy_modify(
            Class=None, BaseType='"Rustic Sash"', Rarity=RARITY_NORMAL, ItemLevel='>= 40')
        filter_manager.append_block(block_hide_n_rustic_sash)
        filter_manager.append_block(FilterBlock(
            Class='Belts', BaseType=filter_config.SSF_CRAFT_BELTS_BASE_TYPE, Rarity=RARITY_NORMAL,
            SetTextColor=COLOR_WHITE))

    blocks = filter_manager.add_comment(213, 'Chisel recipe items')
    blocks[1].Quality = '>= 14'
    blocks[2].Quality = '>= 5'
    filter_manager.extend_blocks(blocks[:3])

    # 8
    block = filter_manager.add_comment(214, 'Fishing Rod')[0]
    block.PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.append_block(block)

    # 8
    block = filter_manager.add_comment(215, 'SRS Crude Bow')[0]
    block.PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.append_block(block)

    blocks = filter_manager.add_comment(216, 'Chromatic recipe items ("RGB Recipe")')
    if filter_config.NEED_RGB:
        filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(217, 'Endgame-start 4-links')
    if filter_config.SHOW_ENDGAME_4L:
        filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(218, 'Animate Weapon script - deactivated by default')
    # filter_manager.extend_blocks(?)

    # 改稀有度，高亮边框
    block = filter_manager.add_comment(219, 'W-soc offhand weapons')[0]
    block.modify(Rarity=RARITY_N2R, SetBorderColor=COLOR_WHITE)
    filter_manager.append_block(block)

    blocks = filter_manager.add_comment(220, 'Sacrificial Garb')
    filter_manager.extend_blocks(blocks)


def modify0600(filter_manager):
    filter_manager.add_comment(600, 'RARE ITEMS (ENDGAME)')

    # 1
    blocks = filter_manager.add_comment(601, 'Rare crafting bases')
    blocks[0].PlayAlertSound = SOUND_MID_VALUE
    blocks[1].PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(602, 'T1 rare items')
    for block in blocks:
        block.modify(**STYLE_T1_RARE)
    if filter_config.T1_RARE_BASE_TYPE != '':
        block_t1_rare_75 = blocks[0].copy_modify(BaseType=filter_config.T1_RARE_BASE_TYPE, PlayAlertSound=SOUND_CHANCE)
        block_t1_rare = blocks[1].copy_modify(BaseType=filter_config.T1_RARE_BASE_TYPE, PlayAlertSound=SOUND_CHANCE)
        filter_manager.extend_blocks([block_t1_rare_75, block_t1_rare])
    if filter_config.SHOW_OTHER_T1_RARES:
        filter_manager.extend_blocks(blocks)

    # 提前隐藏部分稀有物品，借鉴0700
    blocks = filter_manager.get_blocks(700)
    if filter_config.HIDE_ENDGAME_BELOW_T1_RARE_CLASS != '':
        for block in blocks:
            block.modify(status=DEBUG, Corrupted=False, Class=filter_config.HIDE_ENDGAME_BELOW_T1_RARE_CLASS)
        filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(603, 'T2 rare items')
    for block in blocks:
        block.SetBorderColor = COLOR_ORANGE_LIGHT
    if filter_config.T2_RARE_BASE_TYPE != '':
        for block in blocks[:2]:
            filter_manager.append_block(block.copy_modify(BaseType=filter_config.T2_RARE_BASE_TYPE))
    if filter_config.SHOW_OTHER_T2_RARES:
        del blocks[2:4]
        del blocks[-2:]
        filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(604, 'Breach Rings')
    filter_manager.extend_blocks(blocks)

    # 4, 1, 4
    blocks = filter_manager.add_comment(605, 'Amulets, Jewels, Rings, Belts')
    blocks[0].PlayAlertSound = SOUND_CHANCE  # rare jewel
    if filter_config.ALERT_SMALLS_RARE:
        blocks[1].modify(PlayAlertSound=SOUND_MID_VALUE, SetBackgroundColor=COLOR_GOLD)  # regal smalls
        blocks[2].PlayAlertSound = SOUND_CHANCE  # 65-74 smalls
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(606, '1H Daggers')
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(607, '1H Claws')

    blocks = filter_manager.add_comment(608, '1H Wands')
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(609, '1H Foils')

    filter_manager.add_comment(610, '1H Swords')

    filter_manager.add_comment(611, '1H Maces')

    filter_manager.add_comment(612, '1H Axes')

    blocks = filter_manager.add_comment(613, '1H Sceptres')
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(614, '2H Staves')

    filter_manager.add_comment(615, '2H Swords, Axes, Maces')

    filter_manager.add_comment(616, '2H Bows')

    blocks = filter_manager.add_comment(617, 'AR: Gloves, Boots, Helmets')
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(618, 'AR: Body Armors')
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(619, 'OH: Shields')
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(620, 'OH: Quivers')


# 0800-1207
def modify_gem_flask_map(filter_manager):
    # Need map, exile?
    filter_manager.add_comment(800, 'OVERRIDE AREA 3 - Override Map, Gem and Flask drops here')
    if filter_config.ALERT_LOW_MAP:  # 样式取自T14
        filter_manager.append_block(filter_manager.get_blocks(1204)[0].copy_modify(DropLevel=None, Rarity=RARITY_N2R))

    # 改成8和1
    blocks = filter_manager.add_comment(901, 'Value gems')
    del blocks[0]
    blocks[0].modify(Quality='>= 15', PlayAlertSound=SOUND_TOP_VALUE)
    blocks[1].modify(SetBackgroundColor=COLOR_WHITE, PlayAlertSound=SOUND_TOP_VALUE)
    blocks[1].BaseType += ' "Added Chaos Damage"'
    blocks[2].modify(Quality='>= 10', PlayAlertSound=SOUND_MID_VALUE)
    filter_manager.extend_blocks(blocks)

    # 前两个换位，改成1和2
    blocks = filter_manager.add_comment(902, 'Other gems')
    blocks[0], blocks[1] = blocks[1], blocks[0]
    blocks[0].PlayAlertSound = SOUND_MID_VALUE
    blocks[1].PlayAlertSound = SOUND_LOW_VALUE
    if filter_config.LEVELING_GEMS_BASE_TYPE != '':
        block_leveling_gems = blocks[0].copy_modify(BaseType=filter_config.LEVELING_GEMS_BASE_TYPE,
                                                    PlayAlertSound=SOUND_TOP_VALUE)
        blocks.insert(2, block_leveling_gems)
    else:
        blocks[2].status = DEBUG
    filter_manager.extend_blocks(blocks)

    # 15改成10
    blocks = filter_manager.add_comment(1000, 'FLASKS (Levelling Rules)')
    blocks[1].Quality = '>= 10'
    del blocks[2:-1]
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(1100, 'HIDE LAYER 3: Random Endgame Flasks')
    filter_manager.extend_blocks(blocks)

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
        block.modify(SetBorderColor=COLOR_RED_LIGHT, PlayAlertSound=SOUND_TOP_VALUE)
    filter_manager.extend_blocks(blocks)

    # 加黄边，不显示稀有度
    blocks = filter_manager.add_comment(1205, 'Mid tier maps (T6-10)')
    for block in blocks:
        block.modify(SetTextColor=COLOR_GRAY_LIGHT, SetBorderColor=COLOR_YELLOW_LIGHT)
    blocks[0].SetFontSize = FONT_SIZE_MAX
    blocks[1].SetFontSize = FONT_SIZE_MAX
    blocks[2].SetFontSize = FONT_SIZE_MAX
    filter_manager.extend_blocks(blocks)

    # 加蓝边/白边，不显示稀有度
    blocks = filter_manager.add_comment(1206, 'Low tier maps (T1-T5)')
    for block in blocks:
        block.SetTextColor = COLOR_GRAY_LIGHT
    for block in blocks[:6]:
        block.SetBorderColor = COLOR_BLUE_LIGHT
    for block in blocks[6:10]:
        block.SetBorderColor = COLOR_GRAY_LIGHT
    filter_manager.extend_blocks(blocks)

    # 8和4
    blocks = filter_manager.add_comment(1207, 'Map fragments')
    for block in blocks[:-1]:
        block.PlayAlertSound = SOUND_TOP_VALUE
    blocks[-1].PlayAlertSound = SOUND_MAP
    filter_manager.extend_blocks(blocks)


# 1900-2303
def modify_leveling(filter_manager):
    # 隐藏混合瓶、魔瓶、血瓶；后期只要42和60级的血瓶；隐藏不需要的黄装
    filter_manager.add_comment(1900, 'OVERRIDE AREA 4 - Insert your custom leveling adjustments here')
    block_hide_flasks = FilterBlock(status=DEBUG, Class=' "Hybrid Flask" ', SetFontSize=FONT_SIZE_MIN)
    if filter_config.HIDE_FLASK_MANA:
        block_hide_flasks.Class += ' "Mana Flask" '
    if not filter_config.SHOW_FLASK_LIFE:
        block_hide_flasks.Class += ' "Life Flask" '
    block_hide_some_life_flasks = FilterBlock(status=DEBUG, Class='"Life Flask"', BaseType='Sanctified Eternal',
                                              SetFontSize=FONT_SIZE_MIN)
    block_hide_some_mana_flasks = FilterBlock(status=DEBUG, Class='"Mana Flask"', BaseType='Colossal Hallowed',
                                              SetFontSize=FONT_SIZE_MIN)
    filter_manager.extend_blocks([block_hide_flasks, block_hide_some_life_flasks, block_hide_some_mana_flasks])
    if filter_config.HIDE_LEVELING_RARE_CLASS != '':
        filter_manager.append_block(
            FilterBlock(status=DEBUG, Corrupted=False, Class=filter_config.HIDE_LEVELING_RARE_CLASS, Rarity=RARITY_RARE,
                        SetFontSize=26))

    blocks = filter_manager.add_comment(2001, 'Hide outdated flasks')
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(2002, 'Hybrid flasks')

    blocks = filter_manager.add_comment(2003, 'Life Flasks')
    blocks[-4].ItemLevel = None if filter_config.SHOW_FLASK_HALLOWED else '<= 1'
    blocks[-2].ItemLevel = None
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(2004, 'Mana Flasks')
    filter_manager.extend_blocks(blocks)

    block = filter_manager.add_comment(2005, 'Show remaining flasks')[0]
    block.status = DEBUG
    filter_manager.append_block(block)

    # 跑鞋，4L RGB
    blocks = filter_manager.add_comment(2100, 'Leveling - Exceptions')
    if filter_config.RARE_BOOTS_ALERT:
        block_rare_boots = filter_manager.get_blocks(2201)[1].copy_modify(
            ItemLevel=None, SetFontSize=FONT_SIZE_MAX, PlayAlertSound=SOUND_CHANCE, **STYLE_4L)
        filter_manager.append_block(block_rare_boots)
    _magic_boots_il_map = {10: None, 20: '>= 30', 30: '>= 55', -1: '< 1'}
    block_magic_boots = filter_manager.get_blocks(2303)[4].copy_modify(
        ItemLevel=_magic_boots_il_map[filter_config.MAGIC_BOOTS_IL],
        SetFontSize=FONT_SIZE_MAX, PlayAlertSound=SOUND_CHANCE, **STYLE_4L)
    filter_manager.append_block(block_magic_boots)
    blocks[0].modify(PlayAlertSound=SOUND_CHANCE, **STYLE_4L)
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(2200, 'Leveling - RARES')

    # 3L/4L Rare
    blocks = filter_manager.add_comment(2201, 'Leveling rares - tier list')
    if filter_config.LINKED_CLASS != '':
        blocks[0].modify(Class=filter_config.LINKED_CLASS, PlayAlertSound=SOUND_CHANCE, **STYLE_4L)
        block_3l_rrr = blocks[0].copy_modify(LinkedSockets='>= 3', SocketGroup='RRR', ItemLevel='<= 25')
        blocks.insert(1, block_3l_rrr)
        blocks[2].PlayAlertSound = SOUND_CHANCE
    else:
        blocks[1].PlayAlertSound = SOUND_CHANCE
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(2202, 'Leveling rares - remaining rules')
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(2300, 'Leveling - Useful items')

    # 提醒部分三小件 9 23
    blocks = filter_manager.add_comment(2301, 'Jewellery & Helpful leveling and racing gear')[-5:-1]
    if filter_config.ALERT_MAGIC_SMALLS_BASE_TYPE != '':
        block_magic_smalls = blocks[1].copy_modify(BaseType=filter_config.ALERT_MAGIC_SMALLS_BASE_TYPE, ItemLevel=None,
                                                   SetFontSize=40, PlayAlertSound=SOUND_CHANCE)
        filter_manager.append_block(block_magic_smalls)
    blocks[0].ItemLevel = '<= ' + str(filter_config.SMALLS_MAX_IL)
    blocks[1].ItemLevel = '<= ' + str(filter_config.SMALLS_MAX_IL)
    del blocks[2:]
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(2302, 'Caster weapons')

    # 4L Hide GGG, 3L RRR RR, 2L RR
    blocks = filter_manager.add_comment(2303, 'Linked gear')
    if filter_config.LINKED_CLASS != '':
        for block in blocks:
            block.modify(Class=filter_config.LINKED_CLASS, **STYLE_4L)
    block_hide_ggg = blocks[0].copy_modify(status=DEBUG, SocketGroup='GGG', Rarity=RARITY_N2M,
                                           SetFontSize=26, SetTextColor=None)
    block_hide_bbb_body = block_hide_ggg.copy_modify(Class='"Body Armour"', SocketGroup='BBB')
    block_hide_ggbb_body = block_hide_ggg.copy_modify(Class='"Body Armour"', SocketGroup='GGBB')
    blocks[0].modify(SetFontSize=42, PlayAlertSound=SOUND_CHANCE)  # still include RRGG, GGBB
    blocks[1].modify(SetFontSize=42, PlayAlertSound=SOUND_CHANCE)
    filter_manager.extend_blocks([block_hide_ggg, block_hide_bbb_body, block_hide_ggbb_body] + blocks[:2])  # 4L
    block_rrr_normal = blocks[2].copy_modify(SocketGroup='RRR', SetFontSize=42, PlayAlertSound=SOUND_CHANCE)
    block_rrr_magic = blocks[3].copy_modify(SocketGroup='RRR', SetFontSize=42, PlayAlertSound=SOUND_CHANCE)
    blocks[2].modify(LinkedSockets=2, SocketGroup='RR', ItemLevel='<= 7', SetFontSize=42)
    blocks[3].modify(LinkedSockets=2, SocketGroup='RR', ItemLevel='<= 7', SetFontSize=42)
    block_rr_normal = blocks[2].copy_modify(ItemLevel='<= 15', SetFontSize=40)
    block_rr_magic = blocks[3].copy_modify(ItemLevel='<= 15', SetFontSize=40)
    filter_manager.extend_blocks(
        [block_rrr_normal, block_rrr_magic] + blocks[2:4] + [block_rr_normal, block_rr_magic])  # 3L 2L

    filter_manager.add_comment(2304, '20% quality items for those strange people who want them')

    filter_manager.add_comment(2400, 'Levelling - normal and magic item progression')
    if filter_config.ALERT_RRG:
        block_rrg_weapon = FilterBlock(SocketGroup='RRG', Class=' "One Hand" "Claws" "Sceptres" "Daggers" ',
                                       SetFontSize=38, PlayAlertSound=SOUND_MID_VALUE,
                                       ItemLevel='<= ' + str(filter_config.SMALLS_MAX_IL), **STYLE_4L)
        filter_manager.append_block(block_rrg_weapon)
    if filter_config.ALERT_RBB:
        for socket_group in ['RRB', 'RBB', 'BBB']:
            block_swap = FilterBlock(SocketGroup=socket_group, Class='"One Hand" "Claws" "Sceptres" "Daggers"',
                                     SetFontSize=38, PlayAlertSound=SOUND_MID_VALUE, **STYLE_4L)
            filter_manager.append_block(block_swap)
    block_hide_n2m = filter_manager.get_blocks(2500)[0].copy_modify(
        Class='"Bows" "Quivers" "Two Hand" "Staves" "Wands" "Shields" "Claws" "Daggers" "Sceptres" "Claws" "Daggers" "One Hand Maces" ' + filter_config.HIDE_NORMAL_MAGIC_CLASS,
        ItemLevel='>= 2', SetFontSize=FONT_SIZE_MIN)
    block_hide_ogs12 = block_hide_n2m.copy_modify(Class='"One Hand Swords"', ItemLevel='>= 12')
    filter_manager.extend_blocks([block_hide_n2m, block_hide_ogs12])

    # 白1-4
    blocks = filter_manager.add_comment(2401, 'Normal items - First 12 levels - exceptions')
    for block in blocks:
        block.ItemLevel = '<= 4'
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(2402, 'Normal weapons - progression')
    _LEVELING_BASE = [('"Rusted Sword"', 1), ('"Copper Sword"', 5), ('"Sabre"', 10),
                      ('"Rusted Hatchet"', 1), ('"Jade Hatchet"', 6), ('"Boarding Axe"', 11), ('"Cleaver"', 16),
                      ('"Arming Axe"', 25), ('"Decorative Axe"', 29), ('"Jasper Axe"', 36), ]
    _LEVELING_BASE_IL_GAP = 3
    block_template = blocks[0].copy_modify(DropLevel=None, Class=None, SetFontSize=None)
    block_weapon_list = [block_template.copy_modify(BaseType=leveling_base[0],
                                                    ItemLevel='<= ' + str(leveling_base[1] + _LEVELING_BASE_IL_GAP))
                         for leveling_base in _LEVELING_BASE]
    filter_manager.extend_blocks(block_weapon_list)

    # 参考2500
    blocks = filter_manager.add_comment(2403, 'Magic items - progression')
    block_hide_m = filter_manager.get_blocks(2500)[0].copy_modify(  # 冗余
        Class='"Boots" "Rings" "Amulets" "Belts" "Two Hand" "Bows" "One Hand" "Wand" "Sceptre" "Staves" "Claws" "Daggers"')
    block_hide_m4 = block_hide_m.copy_modify(Class='"Body Armour" "Helmets"', ItemLevel='>= 4')
    filter_manager.extend_blocks([block_hide_m, block_hide_m4])
    filter_manager.extend_blocks(blocks)


def modify_filter(filter_manager):
    filter_manager.add_comment(100, 'OVERRIDE AREA 1 - Override ALL rules here (includes 6links etc, be careful)')

    modify0200(filter_manager)

    # 61改成66
    block = filter_manager.add_comment(300, 'HIDE LAYER 1 - MAGIC AND NORMAL ITEMS')[0]
    block.modify(status=DEBUG, ItemLevel='>= 66')
    filter_manager.append_block(block)

    blocks = filter_manager.add_comment(400, 'Currency - PART 1 - Common currency')
    blocks[0].BaseType = '"Orb of Alteration" "Chromatic Orb" "Jeweller\'s Orb" '
    if filter_config.CURRENCY_ALERT_BLACKSMITH:
        blocks[0].BaseType += ' "Blacksmith\'s Whetstone"'
    if filter_config.CURRENCY_ALERT_TRANSMUTATION:
        blocks[0].BaseType += ' "Orb of Transmutation" '
    if filter_config.CURRENCY_ALERT_AUGMENTATION:
        blocks[0].BaseType += ' "Orb of Augmentation" '
    if not filter_config.CURRENCY_ALERT_CHANCE:
        blocks[0].BaseType += ' "Orb of Chance" '
    if filter_config.ALERT_LOW_CURRENCY:
        blocks[0].PlayAlertSound = SOUND_LOW_VALUE
    blocks[1].BaseType += ' "Orb of Augmentation" "Alteration Shard" '
    blocks[2].SetFontSize = filter_config.CURRENCY_ARMOURER_SCRAP_FONT_SIZE
    blocks[3].SetFontSize = filter_config.CURRENCY_PORTAL_FONT_SIZE
    blocks[4].SetFontSize = filter_config.CURRENCY_WISDOM_FONT_SIZE
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(500, 'OVERRIDE AREA 2 - Override the default rare rulesets here')

    modify0600(filter_manager)

    blocks = filter_manager.add_comment(700, 'HIDE LAYER 2 - RARE ITEMS (65+ ONLY FOR NON-REGULAR VERSIONS)')
    for block in blocks:
        block.status = DEBUG
    filter_manager.extend_blocks(blocks)

    # 0800-1207
    modify_gem_flask_map(filter_manager)

    blocks = filter_manager.add_comment(1301, 'Regular Rare Currency')
    blocks[0].modify(PlayAlertSound=SOUND_MID_VALUE, **STYLE_TOP)
    blocks[1].modify(PlayAlertSound=SOUND_MID_VALUE, **STYLE_TOP)
    if filter_config.CURRENCY_ALERT_CHANCE:
        blocks[1].BaseType += ' "Orb of Chance"'
    blocks[2].PlayAlertSound = SOUND_MID_VALUE
    blocks[2].BaseType += ' "Glassblower\'s Bauble"'
    blocks.insert(3, blocks[2].copy_modify(BaseType='"Silver Coin"', SetBackgroundColor='190 178 135'))
    filter_manager.extend_blocks(blocks)

    # 8
    blocks = filter_manager.add_comment(1302, 'Top Currency')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    # 高亮"Essence of Zeal"；8和1
    blocks = filter_manager.add_comment(1303, 'Essence Tier List')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[0].BaseType += ' "Essence of Zeal"'
    blocks[1].PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(1304, 'Special items')
    blocks[1].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    blocks[2].PlayAlertSound = None
    blocks[-1].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(1401, 'Exceptions to prevent ident. mistakes')
    filter_manager.extend_blocks(blocks)

    # 8
    blocks = filter_manager.add_comment(1402, 'T1 - Top tier cards')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    # 8
    blocks = filter_manager.add_comment(1403, 'T2 - Great cards')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[0].BaseType += ' "Humility" "The Encroaching Darkness" '
    filter_manager.extend_blocks(blocks)

    # 1
    blocks = filter_manager.add_comment(1404, 'T3 - Decent cards')
    blocks[0].PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(1405, 'T5 - Format trash tier cards... before')
    blocks[0].PlayAlertSound = SOUND_LOW_VALUE
    filter_manager.extend_blocks(blocks)

    # 2
    blocks = filter_manager.add_comment(1406, 'T4 - ...showing the remaining cards')
    blocks[0].PlayAlertSound = SOUND_LOW_VALUE
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(1500, 'Currency - PART 4 - remaining items')
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(1600, 'Leaguestones - Tierlists')
    for block in blocks[:-1]:
        block.PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    # 改成T1
    blocks = filter_manager.add_comment(1701, 'Exceptions')
    for block in blocks:
        block.PlayAlertSound = SOUND_TOP_VALUE
    blocks[0].modify(**STYLE_TOP_UNIQUE)
    filter_manager.extend_blocks(blocks)

    # 8
    blocks = filter_manager.add_comment(1702, 'Tier 1 uniques')
    for block in blocks:
        block.PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    # 改成T1
    blocks = filter_manager.add_comment(1703, 'Tier 2 uniques')
    for block in blocks:
        block.modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP_UNIQUE)
    filter_manager.extend_blocks(blocks)

    # 6
    blocks = filter_manager.add_comment(1704, 'Multi-Unique bases')
    blocks[0].PlayAlertSound = SOUND_UNIQUE
    filter_manager.extend_blocks(blocks)

    # 6
    blocks = filter_manager.add_comment(1705, 'Prophecy-Material Uniques')
    blocks[0].PlayAlertSound = SOUND_UNIQUE
    filter_manager.extend_blocks(blocks)

    # 6
    blocks = filter_manager.add_comment(1706, 'Random Uniques')
    blocks[0].PlayAlertSound = SOUND_UNIQUE
    filter_manager.extend_blocks(blocks)

    # 6
    blocks = filter_manager.add_comment(1707, 'Harbinger - Pieces')
    blocks[0].PlayAlertSound = SOUND_UNIQUE
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(1800, 'Exceptions - Quest Items etc.')
    filter_manager.extend_blocks(blocks)

    # 1900-2403
    modify_leveling(filter_manager)

    block = filter_manager.add_comment(2500, 'HIDE LAYER 5 - Remaining Items')[0]
    block.modify(status=DEBUG, SetFontSize=FONT_SIZE_MIN)
    filter_manager.append_block(block)

    # 8
    block = filter_manager.add_comment(2600, 'CATCHALL')[0]
    block.PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.append_block(block)


def main():
    start_time = time.time()

    filter_name = "NeverSink's filter - 1-REGULAR.filter"
    with open(filter_name) as f:
        fm = FilterManager(f.readlines())

    modify_filter(fm)

    with open(os.path.expanduser('~') + "\Documents\My Games\Path of Exile\MODIFY.filter", 'w') as f:
        f.writelines(fm.new_text)

    print "Modify success, time cost: {:.0f}ms".format(1000 * (time.time() - start_time))


if __name__ == '__main__':
    main()
