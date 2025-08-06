#!/usr/bin/env python3
"""
Magic Items Library for MTM Character Sheet
Contains all magic items with variants for wands, potions, and scrolls
"""

MAGIC_ITEMS = {
    'permanent_items': {
        'All Seeing Goggles': {
            'name': 'All Seeing Goggles',
            'description': 'This permanent use item allows the wearer to see invisible/displaced/blinking creatures and to see normally in total and magical darkness as long as they are worn.',
            'type': 'permanent'
        },
        'Animated Shield': {
            'name': 'Animated Shield',
            'description': 'This permanent use magic item functions as a normal shield except that once it is activated by using its command word, it animates and will protect its’ owner without taking up a gear die slot.',
            'type': 'permanent'
        },
        'Bag of Holding': {
            'name': 'Bag of Holding',
            'description': 'This permanent use seemingly ordinary cloth bag is actually an extra-dimensional space that can be used to store items. It will hold an infinite number of items no larger than 3 feet by 3 feet by 3 feet.',
            'type': 'permanent'
        },
        'Bag of Useful Items': {
            'name': 'Bag of Useful Items',
            'description': 'This permanent use seemingly ordinary cloth bag is actually an extra-dimensional space that produces a useful mundane item per encounter upon command. It will produce any single item no larger than 3 feet by 3 feet by 3 feet.',
            'type': 'permanent'
        },
        'Bag of Useless Items': {
            'name': 'Bag of Useless Items',
            'description': 'This permanent use cursed seemingly ordinary cloth bag is actually an extra- dimensional space that produces a useless item per encounter upon command. It will detect as a Bag of Useful Items but will produce only broken or otherwise useless items upon command unless the curse is detected with an Analyze spell check of 10 or higher. It will produce any single item no larger than 3 feet by 3 feet by 3 feet.',
            'type': 'permanent'
        },
        'Belt of Damaging': {
            'name': 'Belt of Damaging',
            'description': 'This permanent use item allows the wearer to have two damage rolls made for each attack and use the lower of the two as long as it is worn. The item is usable once per encounter.',
            'type': 'permanent'
        },
        'Belt of Futility': {
            'name': 'Belt of Futility',
            'description': 'This permanent use item detects as a Belt of Speed and will function as such; however, this cursed item will require the wearer to roll the absolute maximum on any of their aspect rolls to succeed at a check unless the curse is detected with an Analyze spell check of 10 or higher.',
            'type': 'permanent'
        },
        'Belt of Speed': {
            'name': 'Belt of Speed',
            'description': 'This permanent use item allows the wearer to move at double their normal movement rate as long as it is worn. It does not confer any extra attacks. Does not stack with Boots of Speed.',
            'type': 'permanent'
        },
        'Belt of the Titans': {
            'name': 'Belt of the Titans',
            'description': 'This permanent use magic item will temporarily increase the Warrior Melee aspect die of the wearer and one D12 gear die to a D20 for 10 rounds per day as long as it is worn and once activated by uttering the command word. Can be used multiple times per day but for no more than the 10 total rounds per day. Bolts/Arrows of Armor Penetration: These reusable items come in a quiver of 10. If these items are shot at a target, the bolts/arrows will ignore any armor bonuses.',
            'type': 'permanent'
        },
        'Boots of Free Movement': {
            'name': 'Boots of Free Movement',
            'description': 'This permanent use magic item allows the wearer to move at their normal movement rate over any surface classified as Difficult Terrain.',
            'type': 'permanent'
        },
        'Boots of Speed': {
            'name': 'Boots of Speed',
            'description': 'This permanent use item allows the wearer to move at double their normal movement rate. It does not confer any extra attacks. Does not stack with Belt of Speed. Bracers of Armor (Dx): This permanent use magic item functions just like normal armor except it does not take up a gear die slot. The GM will assign a base gear die value when found from D4-D12. These do not stack with any other type(s) of armor or other Bracers.',
            'type': 'permanent'
        },
        'Brooch of Shielding': {
            'name': 'Brooch of Shielding',
            'description': 'This semi-permanent item allows the wearer to be immune to all missile weapon damage. It does not apply against the Magic Missile spell. It will absorb 12 such attacks after which it crumbles to dust.',
            'type': 'permanent'
        },
        'Caltrop Bomb': {
            'name': 'Caltrop Bomb',
            'description': 'This one-time use item will explode when thrown into any unoccupied square filling up to 12 squares with caltrops in a single round. These caltrops will cause no damage when they are produced but may if stepped on in subsequent rounds as well as creating difficult terrain in the affected squares.',
            'type': 'permanent'
        },
        'Chest of Encampment': {
            'name': 'Chest of Encampment',
            'description': 'This permanent use item is a small metal box 6 inches by 6 inches. Upon opening, the box will turn into a small encampment for up to 8 people complete with tents, bedrolls, firewood, etc.',
            'type': 'permanent'
        },
        'Cloak of Spell Resistance +': {
            'name': 'Cloak of Spell Resistance +',
            'description': 'This permanent use item confers a permanent bonus of +1 to +5 to the wearer's magic saves as long as it is worn.',
            'type': 'permanent',
            'variants': ['+1', '+2', '+3', '+4', '+5']
        },
        'Chime of Opening': {
            'name': 'Chime of Opening',
            'description': 'Striking this object will unlock all locked or magically locked doors within 60 feet. It shatters after one use. Cloak of Displacement (Dx): This permanent use magic item allows the wearer to utilize the Displacement spell once per day when worn for a number of rounds equal to the gear die assigned by the GM when the item is found. For example: A D6 Cloak of Displacement when activated will function as the spell for 6 rounds (no Aspect or Gear Die checks needed). Cloak of Spell Resistance +: This permanent use item confers a permanent bonus of +1 to +5 to the wearer’s magic saves as long as it is worn.',
            'type': 'permanent'
        },
        'Elvin Boots': {
            'name': 'Elvin Boots',
            'description': 'This permanent use item allows the wearer to move silently on a Rogue roll of 2 or more as long as they are worn.',
            'type': 'permanent'
        },
        'Elvin Cloak': {
            'name': 'Elvin Cloak',
            'description': 'This permanent use item allows the wearer to Hide in Shadows on a Rogue roll of 2 as long as it is worn.',
            'type': 'permanent'
        },
        'Elvin Goggles': {
            'name': 'Elvin Goggles',
            'description': 'This permanent use item allows the wearer to find secret or concealed doors on a Rogue roll of 2 as long as they are worn.',
            'type': 'permanent'
        },
        'Ever Burning Lantern': {
            'name': 'Ever Burning Lantern',
            'description': 'This permanent use item when lit casts light in a 60-foot radius and cannot be extinguished except by its owner. It may be reused as often as needed.',
            'type': 'permanent'
        },
        'Flying Carpet': {
            'name': 'Flying Carpet',
            'description': 'This permanent use item is 20 feet by 20 feet and can carry up to 8 people or 2,800 pounds of gear with a flying speed of 60 feet per round for 10 rounds. It is controlled by the owner via telepathy. It can hover at a height no higher than 20 feet and is usable once per day.',
            'type': 'permanent'
        },
        'Gauntlets of Archery': {
            'name': 'Gauntlets of Archery',
            'description': 'This permanent use item will allow the wearer to add +3 to all future Warrior Ranged aspect checks as long as they are worn.',
            'type': 'permanent'
        },
        'Genie Lamp': {
            'name': 'Genie Lamp',
            'description': 'This permanent use magic item grants the wielder one wish per day. The item itself will try to pervert the wish 25% of the time (GM roll each time it is used). The wish can grant anything the GM wishes to allow, but; it can also allow any negative effect the GM will allow as well.',
            'type': 'permanent'
        },
        'Swimming': {
            'name': 'Swimming',
            'description': 'This permanent use magic item allows the wearer to swim or climb without error or penalty indefinitely.',
            'type': 'permanent'
        },
        'Gloves of Rusting': {
            'name': 'Gloves of Rusting',
            'description': 'This permanent use magic item allows the wearer to rust any unattended non-magical metal object (no save) rendering it useless/destroyed. If the item is attended, the item may make a Magic save with a -3 penalty to resist the attack.',
            'type': 'permanent'
        },
        'Halfling Gloves': {
            'name': 'Halfling Gloves',
            'description': 'This permanent use item allows the wearer to find and disarm traps on a Rogue roll of 2 as long as they are worn.',
            'type': 'permanent'
        },
        'Headband of Recall': {
            'name': 'Headband of Recall',
            'description': 'This permanent use item will allow the wearer to return to whatever place the wearer considers home as long as it is worn. The wearer may also opt to return to where they were before returning home. It may be used once per session.',
            'type': 'permanent'
        },
        'Helm of Communication': {
            'name': 'Helm of Communication',
            'description': 'This permanent use item allows the wearer to communicate verbally with any creature(s) that he can see as long as it is worn.',
            'type': 'permanent'
        },
        'Helm of Easy Target': {
            'name': 'Helm of Easy Target',
            'description': 'This cursed item detects as a Helm of Communication and functions as such, however, it will lower the Warrior Melee or Warrior Ranged aspect check needed to hit the wearer to a 2 unless the curse is detected with an Analyze spell check of 10 or higher.',
            'type': 'permanent'
        },
        'Helm of Indifference': {
            'name': 'Helm of Indifference',
            'description': 'This cursed item will detect as a Helm of Read Languages and Magic and will function as such; however, it will cause the wearer to act normally (1- 50%) or not act (51% or higher) randomly each round unless the curse is detected with an Analyze spell check of 10 or higher.',
            'type': 'permanent'
        },
        'Magic': {
            'name': 'Magic',
            'description': 'This permanent use item allows the wearer to be able to decipher any written document magical or non- magical as long as it is worn.',
            'type': 'permanent'
        },
        'Lantern of Summoning': {
            'name': 'Lantern of Summoning',
            'description': 'This Lantern will detect as an Ever-Burning Lantern and function in all ways as an Ever-Burning Lantern except that it summons one random enemy each time it is lit unless the curse is detected with an Analyze spell check of 10 or higher.',
            'type': 'permanent'
        },
        'Magic Holy Symbol': {
            'name': 'Magic Holy Symbol',
            'description': 'This permanent use item allows its wearer to Repel Undead better than normal. The wearer can Repel one creature for every 2 points rolled for a minimum of two and a maximum of six.',
            'type': 'permanent'
        },
        'Magic Ring': {
            'name': 'Magic Ring',
            'description': 'This permanent use item allows the wearer to choose any single spell and cast that spell with a gear die roll of 1D20 as long as it is worn. Ring is usable once per encounter.',
            'type': 'permanent'
        },
        'Spell Name': {
            'name': '',
            'description': 'Spell name field for Magic Ring',
            'type': 'permanent'
        },
        'Mask of Disguise': {
            'name': 'Mask of Disguise',
            'description': 'This permanent use item allows the wearer to assume the appearance of a random creature of their own type as long as it is worn.',
            'type': 'permanent'
        },
        'Necklace of Detect Thoughts': {
            'name': 'Necklace of Detect Thoughts',
            'description': 'This permanent use item allows the wearer to detect the thoughts of any creature it can see as long as it is worn.',
            'type': 'permanent'
        },
        'Necklace of Single Combat': {
            'name': 'Necklace of Single Combat',
            'description': 'This cursed item will detect as a Necklace of Detect Thoughts and will function as such; however, any attacks made against a creature that the wearer is also attacking do no damage unless the curse is detected with an Analyze spell check of 10 or higher.',
            'type': 'permanent'
        },
        'Creature Type': {
            'name': '',
            'description': 'Creature type field for Oil of Opponents Bane',
            'type': 'permanent'
        },
        'Oil of Positive Magic Armor+': {
            'name': 'Oil of Positive Magic Armor+',
            'description': 'This one-time use item permanently increases the damage reduction of any one suit of armor or bracers one to five steps. For example, A suit of D4 armor would absorb 2 points of damage, D6 armor absorbs 3, etc.',
            'type': 'oil',
            'variants': ['+1', '+2', '+3', '+4', '+5']
        },
        'Oil of Resistance + (Bludgeoning)': {
            'name': 'Oil of Resistance + (Bludgeoning)',
            'description': 'This one-time use item when applied to any suit of armor or bracers permanently confers a permanent bonus of +1 to +5 to any armor checks vs. any type of bludgeoning damage.',
            'type': 'oil',
            'variants': ['+1', '+2', '+3', '+4', '+5']
        },
        'Oil of Resistance + (Piercing)': {
            'name': 'Oil of Resistance + (Piercing)',
            'description': 'This one-time use item when applied to any suit of armor or bracers permanently confers a permanent bonus of +1 to +5 to any armor checks vs. any type of piercing damage.',
            'type': 'oil',
            'variants': ['+1', '+2', '+3', '+4', '+5']
        },
        'Oil of Resistance + (Slashing)': {
            'name': 'Oil of Resistance + (Slashing)',
            'description': 'This one-time use item when applied to any suit of armor or bracers permanently confers a permanent bonus of +1 to +5 to any armor checks vs. any type of Slashing damage.',
            'type': 'oil',
            'variants': ['+1', '+2', '+3', '+4', '+5']
        },
        'Type(s)': {
            'name': '',
            'description': 'Type field for Oil of Vulnerability',
            'type': 'permanent'
        },
        'Oil of Vulnerability (Bludgeoning, Piercing or Slashing)': {
            'name': 'Oil of Vulnerability (Bludgeoning, Piercing or Slashing)',
            'description': 'This cursed one time item will function the same as Oil of Resistance vs. Bludgeoning, Piercing, or Slashing damage but it also confers vulnerability to one of the other types of damage. For example: If applied to a suit of Leather Armor it would confer a +1 bonus to armor checks vs. Bludgeoning damage but would confer a -1 penalty vs. Slashing damage.',
            'type': 'oil'
        },
        'Periapt of Health': {
            'name': 'Periapt of Health',
            'description': 'This permanent use item allows the wearer to be immune to all forms of disease and all poisons as long as it is worn.',
            'type': 'permanent'
        },
        'Periapt of Poison Immunity': {
            'name': 'Periapt of Poison Immunity',
            'description': 'This permanent use magic item will confer total immunity to all forms of poison as long as it is worn.',
            'type': 'permanent'
        },
        'Quiver of Infinite Missiles': {
            'name': 'Quiver of Infinite Missiles',
            'description': 'This permanent use item allows the wearer to always have as many normal projectiles as needed for their bow or crossbow.',
            'type': 'permanent'
        },
        'Rod of Necromancy': {
            'name': 'Rod of Necromancy',
            'description': 'This vile item allows the wielder to summon forth a number of zombies equal to the rank of the wielder. These Zombies arrive on the round the Rod if activated.',
            'type': 'permanent'
        },
        'Rod of Resurrection': {
            'name': 'Rod of Resurrection',
            'description': 'This item allows the caster to bring back one creature from the dead per charge. This is very draining on the wand wielder as both the creature resurrected, and the wand wielder permanently lose 3 hit points. Thre charges',
            'type': 'permanent'
        },
        'Saddle of Riding': {
            'name': 'Saddle of Riding',
            'description': 'This permanent use item when fastened to any mount will confer invulnerability to anyone riding that mount to being dislodged from the saddle against their will.',
            'type': 'permanent'
        },
        'Scabbard of Quick Draw': {
            'name': 'Scabbard of Quick Draw',
            'description': 'This permanent use item grants the Fast-Switch weapon ability to the wearer. This item is used at will.',
            'type': 'permanent'
        },
        'Shield of Spell Protection': {
            'name': 'Shield of Spell Protection',
            'description': 'This permanent use magic item functions as a Magic Shield but also confers advantage on all Magic saving throws as well. Spell Component (Non-Consumable): These components are permanent use magic items which are used in conjunction with spells. These are not consumed when the requisite spell is cast.',
            'type': 'permanent'
        },
        'Spell Component Bag': {
            'name': 'Spell Component Bag',
            'description': 'This permanent use magic item will contain any necessary components to cast a spell of the corresponding gear die.',
            'type': 'permanent'
        },
        'Stone of Alarm': {
            'name': 'Stone of Alarm',
            'description': 'This permanent use item allows the owner to be alerted to anyone trying to sneak up on them. The item functions in a 30’ radius from the wearer. The item alerts the wearer that they are in danger but does not provide any specifics.',
            'type': 'permanent'
        },
        'Stone of Faulty Alarm': {
            'name': 'Stone of Faulty Alarm',
            'description': 'This item will detect as a Stone of Alarm and will function as such except that it will randomly go off erringly unless the curse is detected with an Analyze spell check of 10 or better.',
            'type': 'permanent'
        },
    },

    'wands': {
        'Acid Rain': {
            'name': 'Wand of Acid Rain',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Alarm': {
            'name': 'Wand of Alarm',
            'description': 'Functions as per the spell of the same name. Wand of All’s Clear: Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Analyze': {
            'name': 'Wand of Analyze',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Animate Object': {
            'name': 'Wand of Animate Object',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Blindness': {
            'name': 'Wand of Blindness',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Buried Alive': {
            'name': 'Wand of Buried Alive',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Burrow': {
            'name': 'Wand of Burrow',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Chain Lightning': {
            'name': 'Wand of Chain Lightning',
            'description': 'Functions as per the spell of the same name. Wand of Charm Monster/Person: Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Climbing': {
            'name': 'Wand of Climbing',
            'description': 'This item allows the wielder to climb any surface the wand touches without error at ½ movement for a number of rounds equal to the rank of the wielder.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Come to Me': {
            'name': 'Wand of Come to Me',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Comfort': {
            'name': 'Wand of Comfort',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Common Knowledge': {
            'name': 'Wand of Common Knowledge',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Create Portal': {
            'name': 'Wand of Create Portal',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Dazzle': {
            'name': 'Wand of Dazzle',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Deafness': {
            'name': 'Wand of Deafness',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Death': {
            'name': 'Wand of Death',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Disadvantaged': {
            'name': 'Wand of Disadvantaged',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Displacement': {
            'name': 'Wand of Displacement',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Dragon Breath': {
            'name': 'Wand of Dragon Breath',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Drain Protection': {
            'name': 'Wand of Drain Protection',
            'description': 'Functions as per the spell of the same name. Wand of Dude You’re Stoned: Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Enhancement': {
            'name': 'Wand of Enhancement',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Enlarge': {
            'name': 'Wand of Enlarge',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Enrage': {
            'name': 'Wand of Enrage',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Entangle': {
            'name': 'Wand of Entangle',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Exhaustion': {
            'name': 'Wand of Exhaustion',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Eye See You': {
            'name': 'Wand of Eye See You',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Fearful Presence': {
            'name': 'Wand of Fearful Presence',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Fire Resistance': {
            'name': 'Wand of Fire Resistance',
            'description': 'This item allows the wielder to become more resistant to magical and immune to non-magical fire. While under the effect of this wand, the wielder takes only 1 point of damage per round from any magical source of flame and is immune to normal fire for the wand’s duration.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Fireball': {
            'name': 'Wand of Fireball',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Fly': {
            'name': 'Wand of Fly',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Forget': {
            'name': 'Wand of Forget',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Frost Resistance': {
            'name': 'Wand of Frost Resistance',
            'description': 'This item allows the wielder to become more resistant to magical and immune to non-magical cold. While under the effect of this wand, the wielder takes only 1 point of damage per round from any magical source of cold and is immune to normal cold for the wand’s duration.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Gentle Landing': {
            'name': 'Wand of Gentle Landing',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Gotta Have It': {
            'name': 'Wand of Gotta Have It',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Grease': {
            'name': 'Wand of Grease',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Greater Healing': {
            'name': 'Wand of Greater Healing',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Greater Mass Healing': {
            'name': 'Wand of Greater Mass Healing',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Hail Storm': {
            'name': 'Wand of Hail Storm',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Haste': {
            'name': 'Wand of Haste',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'HealAll': {
            'name': 'Wand of HealAll',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Healing': {
            'name': 'Wand of Healing',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Heroism': {
            'name': 'Wand of Heroism',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'I Dare You Too': {
            'name': 'Wand of I Dare You Too',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Icy Blast': {
            'name': 'Wand of Icy Blast',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Illusion': {
            'name': 'Wand of Illusion',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Immobilize': {
            'name': 'Wand of Immobilize',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Incorporeal': {
            'name': 'Wand of Incorporeal',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Inspire': {
            'name': 'Wand of Inspire',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Instant Search': {
            'name': 'Wand of Instant Search',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Invisibility': {
            'name': 'Wand of Invisibility',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Lessen Effect': {
            'name': 'Wand of Lessen Effect',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Levitate': {
            'name': 'Wand of Levitate',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Lightning': {
            'name': 'Wand of Lightning',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Locked': {
            'name': 'Wand of Locked',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Luck': {
            'name': 'Wand of Luck',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Luck of the Irish': {
            'name': 'Wand of Luck of the Irish',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magic Missile': {
            'name': 'Wand of Magic Missile',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magic Shield': {
            'name': 'Wand of Magic Shield',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magical Darkness': {
            'name': 'Wand of Magical Darkness',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magical Light': {
            'name': 'Wand of Magical Light',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magical Sight': {
            'name': 'Wand of Magical Sight',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Mass Healing': {
            'name': 'Wand of Mass Healing',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Metamagic': {
            'name': 'Wand of Metamagic',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Mirror Image': {
            'name': 'Wand of Mirror Image',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'More is Always Better': {
            'name': 'Wand of More is Always Better',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Mutable Form': {
            'name': 'Wand of Mutable Form',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Natures Step': {
            'name': 'Wand of Natures Step',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Night Vision': {
            'name': 'Wand of Night Vision',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Obscure Life Force': {
            'name': 'Wand of Obscure Life Force',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Odorless': {
            'name': 'Wand of Odorless',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Open': {
            'name': 'Wand of Open',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Paralyzing Ray': {
            'name': 'Wand of Paralyzing Ray',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Pardon Me': {
            'name': 'Wand of Pardon Me',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Phantom Weapon': {
            'name': 'Wand of Phantom Weapon',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Polymorph Self': {
            'name': 'Wand of Polymorph Self',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Pray for the Dying': {
            'name': 'Wand of Pray for the Dying',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Purify': {
            'name': 'Wand of Purify',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Purify Area': {
            'name': 'Wand of Purify Area',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Racial Modification': {
            'name': 'Wand of Racial Modification',
            'description': 'This cursed item detects as a Wand of Luck and functions as such, but also modifies the wielder’s race as follows; roll 1d6 to determine: 1. Human 2. Elf 3. Halfling 4. Dwarf 5. Half-Giant 6. PC Choice unless the curse is detected with an Analyze spell check of 10 or higher.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Reach Out': {
            'name': 'Wand of Reach Out',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Repel Undead': {
            'name': 'Wand of Repel Undead',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Repulsion': {
            'name': 'Wand of Repulsion',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Return': {
            'name': 'Wand of Return',
            'description': 'This item allows the reader to return to any one location he has visited for a period of up to 48 hours, and then return to the location where the wand was last used. If the reader does not return within 48 hours, there is a 50% chance they will be teleported to a random safe location instead.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Right Back at You': {
            'name': 'Wand of Right Back at You',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Rooted': {
            'name': 'Wand of Rooted',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Shrink': {
            'name': 'Wand of Shrink',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Silence': {
            'name': 'Wand of Silence',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Sleep': {
            'name': 'Wand of Sleep',
            'description': 'Functions as per the spell of the same name. Wand of So That’s It: Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Sonic Boom': {
            'name': 'Wand of Sonic Boom',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Spectral Servant': {
            'name': 'Wand of Spectral Servant',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Speed': {
            'name': 'Wand of Speed',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Spider Climb': {
            'name': 'Wand of Spider Climb',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Spiritual Helper': {
            'name': 'Wand of Spiritual Helper',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Summon Spiritual Steed': {
            'name': 'Wand of Summon Spiritual Steed',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Summon Swarm': {
            'name': 'Wand of Summon Swarm',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Sustenance': {
            'name': 'Wand of Sustenance',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Telekinesis': {
            'name': 'Wand of Telekinesis',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Teleport': {
            'name': 'Wand of Teleport',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'That Hurts': {
            'name': 'Wand of That Hurts',
            'description': 'Functions as per the spell of the same name. Wand of That’s Nasty: Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Underwater Breathing': {
            'name': 'Wand of Underwater Breathing',
            'description': 'This item allows the wielder to breathe normally underwater for the duration.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Wall of Ice': {
            'name': 'Wand of Wall of Ice',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Water Walking': {
            'name': 'Wand of Water Walking',
            'description': 'This item allows the wielder to walk/run on water at their normal movement rate for the duration.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Web': {
            'name': 'Wand of Web',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'What the Heck Was That': {
            'name': 'Wand of What the Heck Was That',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Whisper in the Wind': {
            'name': 'Wand of Whisper in the Wind',
            'description': 'Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Wondrous Effect': {
            'name': 'Wand of Wondrous Effect',
            'description': 'Functions asper the spell of the same name. Wand of You’re Welcome: Functions asper the spell of the same name. Wand of You’re Not So Tough: Functions as per the spell of the same name. Wand of You’re Special: Functions as per the spell of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
    },

    'potions': {
        'Acid Rain': {
            'name': 'Potion of Acid Rain',
            'description': 'This one- time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Alarm': {
            'name': 'Potion of Alarm',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber. Potion of All’s Clear: This one- time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Analyze': {
            'name': 'Potion of Analyze',
            'description': 'This one- time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Animate Object': {
            'name': 'Potion of Animate Object',
            'description': 'This one- time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Blindness': {
            'name': 'Potion of Blindness',
            'description': 'This one- time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Buried Alive': {
            'name': 'Potion of Buried Alive',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Burrow': {
            'name': 'Potion of Burrow',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Chain Lightning': {
            'name': 'Potion of Chain Lightning',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber. Potion of Charm Monster/Person: This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Climbing': {
            'name': 'Potion of Climbing',
            'description': 'This one-time use item allows the imbiber to climb any surface without error at ½ movement for a number of rounds equal to the rank of the reader.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Come to Me': {
            'name': 'Potion of Come to Me',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Comfort': {
            'name': 'Potion of Comfort',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Common Knowledge': {
            'name': 'Potion of Common Knowledge',
            'description': 'This one- time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Create Portal': {
            'name': 'Potion of Create Portal',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Dazzle': {
            'name': 'Potion of Dazzle',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Deafness': {
            'name': 'Potion of Deafness',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Death': {
            'name': 'Potion of Death',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Disadvantaged': {
            'name': 'Potion of Disadvantaged',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Displacement': {
            'name': 'Potion of Displacement',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Dragon Breath': {
            'name': 'Potion of Dragon Breath',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Drain Protection': {
            'name': 'Potion of Drain Protection',
            'description': 'This one- time use item allows the imbiber to ignore any one drain attack and instead take 1d6 damage. This damage ignores armor and shield bonuses.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Enhancement': {
            'name': 'Potion of Enhancement',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Enlarge': {
            'name': 'Potion of Enlarge',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Enrage': {
            'name': 'Potion of Enrage',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Exhaustion': {
            'name': 'Potion of Exhaustion',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Eye See You': {
            'name': 'Potion of Eye See You',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Fearful Presence': {
            'name': 'Potion of Fearful Presence',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Fire Resistance': {
            'name': 'Potion of Fire Resistance',
            'description': 'This one-time use item allows the imbiber to become more resistant to magical and immune to non-magical fire. While under the effect of this potion, the imbiber takes only 1 point of damage per round from any magical source of flame and is immune to normal fire for the potion’s duration.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Fireball': {
            'name': 'Potion of Fireball',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Fly': {
            'name': 'Potion of Fly',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Forget': {
            'name': 'Potion of Forget',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Frost Resistance': {
            'name': 'Potion of Frost Resistance',
            'description': 'This one-time use item allows the imbiber to become more resistant to magical and immune to non-magical cold. While under the effect of this potion, the imbiber takes only 1 point of damage per round from any magical source of cold and is immune to normal cold for the potion’s duration.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Gentle Landing': {
            'name': 'Potion of Gentle Landing',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Gotta Have It': {
            'name': 'Potion of Gotta Have It',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Grease': {
            'name': 'Potion of Grease',
            'description': 'This one-time use item when applied to a surface functions as per the spell of the same name.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Greater Healing': {
            'name': 'Potion of Greater Healing',
            'description': 'This one- time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Greater Mass Healing': {
            'name': 'Potion of Greater Mass Healing',
            'description': 'This one- time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Hail Storm': {
            'name': 'Potion of Hail Storm',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Haste': {
            'name': 'Potion of Haste',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'HealAll': {
            'name': 'Potion of HealAll',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Healing': {
            'name': 'Potion of Healing',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Heroism': {
            'name': 'Potion of Heroism',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Icy Blast': {
            'name': 'Potion of Icy Blast',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Illusion': {
            'name': 'Potion of Illusion',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Immobilize': {
            'name': 'Potion of Immobilize',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Incorporeal': {
            'name': 'Potion of Incorporeal',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Inspire': {
            'name': 'Potion of Inspire',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Instant Search': {
            'name': 'Potion of Instant Search',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Invisibility': {
            'name': 'Potion of Invisibility',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Lessen Effect': {
            'name': 'Potion of Lessen Effect',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Levitate': {
            'name': 'Potion of Levitate',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Luck': {
            'name': 'Potion of Luck',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Luck of the Irish': {
            'name': 'Potion of Luck of the Irish',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magic Missile': {
            'name': 'Potion of Magic Missile',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magic Shield': {
            'name': 'Potion of Magic Shield',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magical Darkness': {
            'name': 'Potion of Magical Darkness',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magical Sight': {
            'name': 'Potion of Magical Sight',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Mass Healing': {
            'name': 'Potion of Mass Healing',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Metamagic': {
            'name': 'Potion of Metamagic',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Mirror Image': {
            'name': 'Potion of Mirror Image',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'More is Always Better': {
            'name': 'Potion of More is Always Better',
            'description': 'This one- time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Mutable Form': {
            'name': 'Potion of Mutable Form',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Natures Step': {
            'name': 'Potion of Natures Step',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Night Vision': {
            'name': 'Potion of Night Vision',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Obscure Life Force': {
            'name': 'Potion of Obscure Life Force',
            'description': 'This one- time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Odorless': {
            'name': 'Potion of Odorless',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Open': {
            'name': 'Potion of Open',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Paralyzing Ray': {
            'name': 'Potion of Paralyzing Ray',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Pardon Me': {
            'name': 'Potion of Pardon Me',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Phantom Weapon': {
            'name': 'Potion of Phantom Weapon',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Polymorph Self': {
            'name': 'Potion of Polymorph Self',
            'description': 'This one- time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Pray for the Dying': {
            'name': 'Potion of Pray for the Dying',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Purify': {
            'name': 'Potion of Purify',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Purify Area': {
            'name': 'Potion of Purify Area',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Racial Modification': {
            'name': 'Potion of Racial Modification',
            'description': 'This cursed one time use item detects as a Potion of Luck and functions as such, but also changes the imbiber’s race roll 1d6 to determine 1. Human 2. Elf 3. Halfling 4. Dwarf 5. Half-Giant 6. PC Choice unless the curse is detected with an Analyze spell check of 10 or higher.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Reach Out': {
            'name': 'Potion of Reach Out',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Repel Undead': {
            'name': 'Potion of Repel Undead',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Repulsion': {
            'name': 'Potion of Repulsion',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Return': {
            'name': 'Potion of Return',
            'description': 'This one-time use item allows the imbiber to return to any one location he has visited for a period of up to 48 hours, and then return to the location where the potion was consumed. If the imbiber does not return within 48 hours, they are stuck where they initially returned to and will have to find another way back!',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Right Back at You': {
            'name': 'Potion of Right Back at You',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Rooted': {
            'name': 'Potion of Rooted',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Shrink': {
            'name': 'Potion of Shrink',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Silence': {
            'name': 'Potion of Silence',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Sleep': {
            'name': 'Potion of Sleep',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber. Potion of So That’s It: This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Sonic Boom': {
            'name': 'Potion of Sonic Boom',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Spectral Servant': {
            'name': 'Potion of Spectral Servant',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Speed': {
            'name': 'Potion of Speed',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Spider Climb': {
            'name': 'Potion of Spider Climb',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Spiritual Helper': {
            'name': 'Potion of Spiritual Helper',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Summon Spiritual Steed': {
            'name': 'Potion of Summon Spiritual Steed',
            'description': 'This one- time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Summon Swarm': {
            'name': 'Potion of Summon Swarm',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Sustenance': {
            'name': 'Potion of Sustenance',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Take That': {
            'name': 'Potion of Take That',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Telekinesis': {
            'name': 'Potion of Telekinesis',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Teleport': {
            'name': 'Potion of Teleport',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'That Hurts': {
            'name': 'Potion of That Hurts',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber. Potion of That’s Nasty: This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'The Forecast Calls For': {
            'name': 'Potion of The Forecast Calls For',
            'description': 'This one- time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Underwater Breathing': {
            'name': 'Potion of Underwater Breathing',
            'description': 'This one-time use item allows the imbiber to breathe normally underwater for the duration.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Wall of Ice': {
            'name': 'Potion of Wall of Ice',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Water Walking': {
            'name': 'Potion of Water Walking',
            'description': 'This one- time use item allows the imbiber to walk/run on water at their normal movement rate for the duration.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Web': {
            'name': 'Potion of Web',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'What the Heck Was That': {
            'name': 'Potion of What the Heck Was That',
            'description': 'This one- time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Whisper in the Wind': {
            'name': 'Potion of Whisper in the Wind',
            'description': 'This one- time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Wondrous Effect': {
            'name': 'Potion of Wondrous Effect',
            'description': 'This one-time use item functions as per the spell of the same name and only affects the imbiber. Potion of You’re Welcome: This one- time use item functions as per the spell of the same name and only affects the imbiber. Potion of You’re Not So Tough: This one-time use item functions as per the spell of the same name and only affects the imbiber. Potion of You’re Special: This one-time use item functions as per the spell of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
    },

    'scrolls': {
        'Acid Rain': {
            'name': 'Scroll of Acid Rain',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Alarm': {
            'name': 'Scroll of Alarm',
            'description': 'This one-time use item functions as per the spell of the same name. Scroll of All’s Clear: This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Analyze': {
            'name': 'Scroll of Analyze',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Animate Object': {
            'name': 'Scroll of Animate Object',
            'description': 'This one- time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Blindness': {
            'name': 'Scroll of Blindness',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Buried Alive': {
            'name': 'Scroll of Buried Alive',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Burrow': {
            'name': 'Scroll of Burrow',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Chain Lightning': {
            'name': 'Scroll of Chain Lightning',
            'description': 'This one- time use item functions as per the spell of the same name. Scroll of Charm Monster/Person: This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Climbing': {
            'name': 'Scroll of Climbing',
            'description': 'This one-time use item allows the imbiber to climb any surface without error at ½ movement for a number of rounds equal to the rank of the reader.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Come to Me': {
            'name': 'Scroll of Come to Me',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Comfort': {
            'name': 'Scroll of Comfort',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Common Knowledge': {
            'name': 'Scroll of Common Knowledge',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Create Portal': {
            'name': 'Scroll of Create Portal',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Dazzle': {
            'name': 'Scroll of Dazzle',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Deafness': {
            'name': 'Scroll of Deafness',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Death': {
            'name': 'Scroll of Death',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Disadvantaged': {
            'name': 'Scroll of Disadvantaged',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Displacement': {
            'name': 'Scroll of Displacement',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Dragon Breath': {
            'name': 'Scroll of Dragon Breath',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Drain Protection': {
            'name': 'Scroll of Drain Protection',
            'description': 'This one-time use item allows the reader to ignore any one drain attack and instead take 1d6 damage. This damage ignores armor or shield bonuses. Scroll of Dude You’re Stoned: This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Enhancement': {
            'name': 'Scroll of Enhancement',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Enlarge': {
            'name': 'Scroll of Enlarge',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Enrage': {
            'name': 'Scroll of Enrage',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Entangle': {
            'name': 'Scroll of Entangle',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Exhaustion': {
            'name': 'Scroll of Exhaustion',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Eye See You': {
            'name': 'Scroll of Eye See You',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Fearful Presence': {
            'name': 'Scroll of Fearful Presence',
            'description': 'This one- time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Fire Resistance': {
            'name': 'Scroll of Fire Resistance',
            'description': 'This one-time use item allows the reader to become more resistant to magical and immune to non-magical fire. While under the effect of this potion, the reader takes only 1 point of damage per round from any magical source of flame and is immune to normal fire for the scroll’s duration.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Fireball': {
            'name': 'Scroll of Fireball',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Fly': {
            'name': 'Scroll of Fly',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Forget': {
            'name': 'Scroll of Forget',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Frost Resistance': {
            'name': 'Scroll of Frost Resistance',
            'description': 'This one-time use item allows the reader to become more resistant to magical and immune to non-magical cold. While under the effect of this potion, the reader takes only 1 point of damage per round from any magical source of cold and is immune to normal cold for the scroll’s duration.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Gentle Landing': {
            'name': 'Scroll of Gentle Landing',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Gotta Have It': {
            'name': 'Scroll of Gotta Have It',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Grease': {
            'name': 'Scroll of Grease',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Greater Healing': {
            'name': 'Scroll of Greater Healing',
            'description': 'This one- time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Greater Mass Healing': {
            'name': 'Scroll of Greater Mass Healing',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Hail Storm': {
            'name': 'Scroll of Hail Storm',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Haste': {
            'name': 'Scroll of Haste',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'HealAll': {
            'name': 'Scroll of HealAll',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Healing': {
            'name': 'Scroll of Healing',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Heroism': {
            'name': 'Scroll of Heroism',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Icy Blast': {
            'name': 'Scroll of Icy Blast',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Illusion': {
            'name': 'Scroll of Illusion',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Immobilize': {
            'name': 'Scroll of Immobilize',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Incorporeal': {
            'name': 'Scroll of Incorporeal',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Inspire': {
            'name': 'Scroll of Inspire',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Instant Search': {
            'name': 'Scroll of Instant Search',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Invisibility': {
            'name': 'Scroll of Invisibility',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Lessen Effect': {
            'name': 'Scroll of Lessen Effect',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Levitate': {
            'name': 'Scroll of Levitate',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Lightning': {
            'name': 'Scroll of Lightning',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Locked': {
            'name': 'Scroll of Locked',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Luck': {
            'name': 'Scroll of Luck',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Luck of the Irish': {
            'name': 'Scroll of Luck of the Irish',
            'description': 'This one- time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magic Missile': {
            'name': 'Scroll of Magic Missile',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magic Shield': {
            'name': 'Scroll of Magic Shield',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magical Darkness': {
            'name': 'Scroll of Magical Darkness',
            'description': 'This one- time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magical Light': {
            'name': 'Scroll of Magical Light',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magical Sight': {
            'name': 'Scroll of Magical Sight',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Mass Healing': {
            'name': 'Scroll of Mass Healing',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Metamagic': {
            'name': 'Scroll of Metamagic',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Mirror Image': {
            'name': 'Scroll of Mirror Image',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'More is Always Better': {
            'name': 'Scroll of More is Always Better',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Mutable Form': {
            'name': 'Scroll of Mutable Form',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Natures Step': {
            'name': 'Scroll of Natures Step',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Night Vision': {
            'name': 'Scroll of Night Vision',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Obscure Life Force': {
            'name': 'Scroll of Obscure Life Force',
            'description': 'This one- time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Odorless': {
            'name': 'Scroll of Odorless',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Open': {
            'name': 'Scroll of Open',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Paralyzing Ray': {
            'name': 'Scroll of Paralyzing Ray',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Pardon Me': {
            'name': 'Scroll of Pardon Me',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Phantom Weapon': {
            'name': 'Scroll of Phantom Weapon',
            'description': 'This one- time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Polymorph Self': {
            'name': 'Scroll of Polymorph Self',
            'description': 'This one- time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Pray for the Dying': {
            'name': 'Scroll of Pray for the Dying',
            'description': 'This one- time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Purify': {
            'name': 'Scroll of Purify',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Purify Area': {
            'name': 'Scroll of Purify Area',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Racial Modification': {
            'name': 'Scroll of Racial Modification',
            'description': 'This cursed one time use item detects as a Scroll of Luck and functions as such, but also modifies the reader’s race as follows; roll 1d8 to determine: 1. Human 2. Elf 3. Halfling 4. Dwarf 5. Half-Giant 6. Half-Elf 7. Galdur 8. PC Choice unless the curse is detected with an Analyze spell check of 10 or higher.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Reach Out': {
            'name': 'Scroll of Reach Out',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Repel Undead': {
            'name': 'Scroll of Repel Undead',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Repulsion': {
            'name': 'Scroll of Repulsion',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Return': {
            'name': 'Scroll of Return',
            'description': 'This one-time use item allows the reader to return to any one location he has visited for a period of up to 48 hours, and then return to the location where the scroll was read. If the reader does not return within 48 hours, they are stuck where they initially returned to and will have to find another way back!',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Right Back at You': {
            'name': 'Scroll of Right Back at You',
            'description': 'This one- time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Rooted': {
            'name': 'Scroll of Rooted',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Shrink': {
            'name': 'Scroll of Shrink',
            'description': 'This one-time use item allows the reader to shrink himself one size category.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Silence': {
            'name': 'Scroll of Silence',
            'description': 'This one-time use item allows the reader to shrink himself one size category.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Sleep': {
            'name': 'Scroll of Sleep',
            'description': 'This one-time use item functions as per the spell of the same name. Scroll of So That’s It: This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Sonic Boom': {
            'name': 'Scroll of Sonic Boom',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Spectral Servant': {
            'name': 'Scroll of Spectral Servant',
            'description': 'This one- time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Speed': {
            'name': 'Scroll of Speed',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Spider Climb': {
            'name': 'Scroll of Spider Climb',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Spiritual Helper': {
            'name': 'Scroll of Spiritual Helper',
            'description': 'This one- time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Summon Spiritual Steed': {
            'name': 'Scroll of Summon Spiritual Steed',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Summon Swarm': {
            'name': 'Scroll of Summon Swarm',
            'description': 'This one- time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Sustenance': {
            'name': 'Scroll of Sustenance',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Take That': {
            'name': 'Scroll of Take That',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Telekinesis': {
            'name': 'Scroll of Telekinesis',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Teleport': {
            'name': 'Scroll of Teleport',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'That Hurts': {
            'name': 'Scroll of That Hurts',
            'description': 'This one-time use item functions as per the spell of the same name. Scroll of That’s Nasty: This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'The Forecast Calls For': {
            'name': 'Scroll of The Forecast Calls For',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Underwater Breathing': {
            'name': 'Scroll of Underwater Breathing',
            'description': 'This one-time use item allows the reader to breathe normally underwater for the duration.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Wall of Ice': {
            'name': 'Scroll of Wall of Ice',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Water Walking': {
            'name': 'Scroll of Water Walking',
            'description': 'This one-time use item allows the reader to walk/run on water at normal movement rate for the duration.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Web': {
            'name': 'Scroll of Web',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'What the Heck Was That': {
            'name': 'Scroll of What the Heck Was That',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Whisper in the Wind': {
            'name': 'Scroll of Whisper in the Wind',
            'description': 'This one-time use item functions as per the spell of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Wondrous Effect': {
            'name': 'Scroll of Wondrous Effect',
            'description': 'This one- time use item functions as per the spell of the same name. Scroll of You’re Welcome: This one- time use item functions as per the spell of the same name. Scroll of You’re Not So Tough: This one-time use item functions as per the spell of the same name. Scroll of You’re Special: This one-time use item functions as per the spell of the same name. Shape Shifter’s Robe: This permanent use item allows the wearer to assume to look and appearance of any creature type the wearer has seen as long as it is worn. It does not allow the wearer to assume the appearance of specific creatures, nor does it grant any other abilities.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
    },

    'staves': {
        'Cure All': {
            'name': 'Staff of Cure All',
            'description': 'This item will cure any ill effect the target is suffering from to include HP damage, lost limbs, lost digits, curses, diseases, or any other malady afflicting the target other than death.',
            'type': 'staff',
            'charges': 5,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Curing': {
            'name': 'Staff of Curing',
            'description': 'This item can be used to cure damage to the injured. One charge casts a Healing spell, two charges casts a Greater Healing spell, three charges casts a Mass Healing Spell, and four charges casts a HeallAll spell.',
            'type': 'staff',
            'charges': 5,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'the Mimic': {
            'name': 'Staff of the Mimic',
            'description': 'This item allows the wielder to assume the look of any non-living object. It is usable 5 times per day. The item will recharge itself every day at dawn.',
            'type': 'staff',
            'charges': 5,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
    },

    'rings': {
        'Avoidance': {
            'name': 'Ring of Avoidance',
            'description': 'This permanent use item allows the wearer to avoid any one spell or attack cast at them per encounter as though it never happened as long as it is worn.',
            'type': 'ring'
        },
        'Awareness': {
            'name': 'Ring of Awareness',
            'description': 'This permanent use item prevents the wearer from being surprised .',
            'type': 'ring'
        },
        'Diminished Aspect': {
            'name': 'Ring of Diminished Aspect',
            'description': 'This cursed item will permanently lower the wearer’s highest aspect die to a D4 unless the curse is detected with an Analyze spell check of 10 or higher as long as the item is worn.',
            'type': 'ring'
        },
        'Drain Protection': {
            'name': 'Ring of Drain Protection',
            'description': 'This permanent use item will allow the wearer to ignore all drain attacks and instead take 1D6 damage, save or armor bonuses do not apply as long as it is worn.',
            'type': 'ring'
        },
        'Electricity Protection': {
            'name': 'Ring of Electricity Protection',
            'description': 'This permanent use item allows the wearer to be immune to damage from magical and non-magical electricity as long as it is worn.',
            'type': 'ring'
        },
        'Feather Fall': {
            'name': 'Ring of Feather Fall',
            'description': 'This permanent use item allows the wearer to fall safely any distance and suffer no ill effects as long as it is worn.',
            'type': 'ring'
        },
        'Final Insult': {
            'name': 'Ring of Final Insult',
            'description': 'This permanent use item activates when the wearer’s HP total is reduced to zero or lower. It will then explode causing damage to all adjacent enemies equal to the damage dealt that reduced the wearers HP to zero. For example: 4 Orcs attack a character wearing this ring and one attack does 10 HP in damage and reduces the wearer to zero HP. The ring would explode causing 10 HP in damage to all 4 Orcs. There is no save vs. this damage either.',
            'type': 'ring'
        },
        'Fire Protection': {
            'name': 'Ring of Fire Protection',
            'description': 'This permanent use item allows the wearer to be immune to damage from magical and non- magical fire as long as it is worn.',
            'type': 'ring'
        },
        'Frost Protection': {
            'name': 'Ring of Frost Protection',
            'description': 'This permanent use item allows the wearer to be immune to damage from magical and non- magical cold as long as it is worn.',
            'type': 'ring'
        },
        'Jumping': {
            'name': 'Ring of Jumping',
            'description': 'This permanent use magic item will allow the wearer to automatically succeed at any one jump attempt per day out to a maximum distance of 25 feet.',
            'type': 'ring'
        },
        'Metamagic': {
            'name': 'Ring of Metamagic',
            'description': 'This permanent use item allows the wearer the use of the Metamagic spell with automatic success and maximum effect without taking up a gear die slot. It also allows the caster to use all effects once per day.',
            'type': 'ring'
        },
        'Mortal Enemy': {
            'name': 'Ring of Mortal Enemy',
            'description': 'This permanent use item allows to wearer to attack one single creature type using a D20 on all melee and ranged attacks as long as it is worn. This must be chosen the first time you don the ring.',
            'type': 'ring'
        },
        'Preparedness': {
            'name': 'Ring of Preparedness',
            'description': 'This item will allow the wielder to cast any spell in the game (Except Death) as a D12 gear die spell as a standard action. It will always succeed and will always be cast at maximum effectiveness. This item can be used at will though no single spell can be cast forth from the ring more than once per day.',
            'type': 'ring'
        },
        'Regeneration': {
            'name': 'Ring of Regeneration',
            'description': 'This permanent use item allows the wearer to regenerate lost digits, limbs, etc. It will also cure scars. This item will not regenerate a lost head or prevent a creature from dying nor does it restore lost hit points. The item must be worn for 24 hours before it will have any effect.',
            'type': 'ring'
        },
        'Shape Magic': {
            'name': 'Ring of Shape Magic',
            'description': 'This permanent use magic item allows the wearer to use the Shape Magic ability at will and without a chance of Miscast or Spell Fumble.',
            'type': 'ring'
        },
        'Spell Attraction': {
            'name': 'Ring of Spell Attraction',
            'description': 'This cursed item will detect as a Ring of Spell Immunity, however it actually a Ring of Spell Attraction. This item will cause all spells to be redirected toward the wearer unless the curse is detected with an Analyze spell check of 10 or higher.',
            'type': 'ring'
        },
        'Spell Immunity': {
            'name': 'Ring of Spell Immunity',
            'description': 'This permanent use item allows the wearer to be immune to all harmful spells and spell like effects permanently as long as it is worn. Ring of Spell Storing (Dx): This permanent use magic item can store any one spell at the assigned gear die. It will function as the spell would normally but does not take up a gear die slot. This ring can be used once per encounter.',
            'type': 'ring'
        },
        'Supreme Skill': {
            'name': 'Ring of Supreme Skill',
            'description': 'This simple iron band will grant the wearer an increase to ALL aspect die that are currently maximized at D12 an increase to a D20 as long as it is worn.',
            'type': 'ring'
        },
        'Sustenance': {
            'name': 'Ring of Sustenance',
            'description': 'This permanent use item allows the wearer to go without food or water as long as it is worn.',
            'type': 'ring'
        },
        'Swimming': {
            'name': 'Ring of Swimming',
            'description': 'This permanent use item allows the wearer to swim at their normal movement rate while wearing/carrying their gear with no ill effects(s) as long as it is worn.',
            'type': 'ring'
        },
        'Telekinesis and Levitation': {
            'name': 'Ring of Telekinesis and Levitation',
            'description': 'This permanent use item functions as the Potions of Telekinesis and Levitation except that the wearer can use these effects at will as long as they are wearing the item.',
            'type': 'ring'
        },
        'the Caster': {
            'name': 'Ring of the Caster',
            'description': 'This permanent use magic item when found will be empty. Upon discovering its’ nature, a caster can then cast any spell into the ring. This spell will then be cast forth from the ring upon command as a Gear Die D20 spell. The spell cast into the ring will always be successfully cast from the ring and produce the maximum effect. This ring can be used once per day.',
            'type': 'ring'
        },
        'the Conjurer': {
            'name': 'Ring of the Conjurer',
            'description': 'This permanent use item allows the wearer to utilize the Conjurer aspect even if they did not select it at character creation without sacrificing and other current aspect selections. When worn by someone that already has the Conjurer ability, that character can use their Conjurer ability to conjure the requisite item with no GP cost whatsoever and the creation time is only 10 minutes.',
            'type': 'ring'
        },
        'the Dwarf': {
            'name': 'Ring of the Dwarf',
            'description': 'This permanent use item will permanently convey an additional 3 hit points to the wearer’s total as long as it is worn.',
            'type': 'ring'
        },
        'Water Walking': {
            'name': 'Ring of Water Walking',
            'description': 'This permanent use item allows the wearer to walk on water as though they were walking on solid ground as long as it is worn. It does not allow the wearer to walk on any other liquid surface.',
            'type': 'ring'
        },
    },

    'amulets': {
        'Invulnerability': {
            'name': 'Amulet of Invulnerability',
            'description': 'This permanent use cursed item will detect as an Amulet of Invulnerability and will function as such; however, it will also function as an armor of Vulnerability as well. Each time the item is worn, it attunes itself to the wearer and confer Invulnerability to two forms of attack for 1 day while conferring Vulnerability to the remaining two. The Amulet cannot be removed once worn and will move to the nearest available ally after 24 hours at which time the GM will reroll the Invulnerabilities/Vulnerabilities for the new wearer. Roll a 1D4 each time the ring attunes to a new wearer. A 1 confers Invulnerability/Vulnerability to Slashing Attacks, A 2 confers Invulnerability/Vulnerability to Bludgeoning Attacks, A 3 confers Invulnerability/Vulnerability to Piercing Attacks, A 4 confers Invulnerability/Vulnerability to Spells; yes, all spells friendly or otherwise.',
            'type': 'amulet'
        },
        'Recall Spell': {
            'name': 'Amulet of Recall Spell',
            'description': 'This permanent use item allows the wearer to be able to use their Recall Spell ability as a move action instead of a full round action making the recalled spell available in the same round as long as it is worn. This item is only usable by someone with the Recall Spell special ability once per encounter.',
            'type': 'amulet'
        },
        'Spell Absorption': {
            'name': 'Amulet of Spell Absorption',
            'description': 'This one-time use item allows the wearer to absorb the effect of any one spell they choose after which the amulet crumbles to dust. Amulet of Spell Reflection/Deflection: This one-time use item will cause one spell of the wearers choosing to be reflected back at the caster (1-50%) or deflected harmlessly (51% or higher) away after which the amulet crumbles to dust. The spell and the effect must be chosen by the wearer when the amulet is first worn.',
            'type': 'amulet'
        },
        'Taunting': {
            'name': 'Amulet of Taunting',
            'description': 'This permanent use cursed item will detect as an Amulet of the Rogue and will function as such; however, it will also telepathically taunt all enemies within sight of the wearer causing said enemies to attack the wearer unless the curse is detected with an Analyze spell check of 10 or higher.',
            'type': 'amulet'
        },
        'the Rogue': {
            'name': 'Amulet of the Rogue',
            'description': 'This permanent use item allows its wearer to succeed on all Rogue aspect checks with a roll of 2 or more as long as it is worn. It does not stack with Elvin Cloaks or Elvin Boots.',
            'type': 'amulet'
        },
        'the Steed': {
            'name': 'Amulet of the Steed',
            'description': 'This permanent use item allows the wearer to speak the command word and a Phantom Steed will appear forth under the control of the wearer. This steed will transport none other than the wearer and his gear moving at double normal rate for a Riding Horse. The steed is invulnerable to attack and lasts until the wearer speaks the command word again.',
            'type': 'amulet'
        },
    },

    'oils': {
        'Armor Penetration': {
            'name': 'Oil of Armor Penetration',
            'description': 'This one-time use item when applied to a weapon will allow any damage done with that weapon to ignore all armor bonuses. Oil of Cursed Magic Weapon -: This one-time use item reduces the gear die of any one weapon one to five steps to a minimum of D4 unless the curse is detected with an Analyze spell check of 10 or higher.',
            'type': 'oil'
        },
        'Destruction': {
            'name': 'Oil of Destruction',
            'description': 'This one-time use item when applied to any weapon will allow the wearer to do an extra die of damage with each attack up to a D12. This bonus stacks with crits and all other magic items or abilities related to crits. Oil of Improved Critical+: This one- time use item when applied to any weapon conveys a permanent +1 to +3 to the wielder’s aspect die roll to determine a critical hit. +1 +2 +3 Oil of Magic Shield -1: This cursed item will detect as Oil of Magic Shield +1, however, when applied to a shield of any type will cause the shield to crumble to dust when hit unless the curse is detected with an Analyze spell check of 10 or higher. Oil of Magic Shield +1: This one- time use item permanently increases the protection of one shield. When attacked, the attacker rolls three damage rolls and takes the least of the three. Oil of Magic Weapon +: This one-time use item permanently increases the gear die of any one weapon one to five steps and adds a permanent plus one to Warrior Melee or Warrior Ranged aspect checks to hit (once for the life of the weapon). For example, A D8 sword would become a D10 sword, or a D12 sword would become a D12+D4 sword up to a maximum of D12 +D12. +1 +2 +3 +4 +5 Oil of Negative Magic Armor-: This one- time use item decreases the armor or bracers damage reduction value by 1-5 all the way down to zero. -1 -2 -3 -4 -5',
            'type': 'oil'
        },
        'Opponents Bane': {
            'name': 'Oil of Opponents Bane',
            'description': 'This one-time use item when applied to a weapon confers advantage on all Warrior Melee or Warrior Ranged aspect checks to hit an opponent with that weapon of a certain type such as Undead, Plants, etc. The GM will assign a type when the item is found.',
            'type': 'oil'
        },
        'Slipperiness': {
            'name': 'Oil of Slipperiness',
            'description': 'This one-time use magic item when applied to any armor will make the wearer permanently immune to being grabbed or grappled as long as the armor is worn.',
            'type': 'oil'
        },
        'Speed': {
            'name': 'Oil of Speed',
            'description': 'This one-time use item when applied to any weapon allows the wielder to make an extra single attack with that weapon each round.',
            'type': 'oil'
        },
    }
}


def get_item_by_name(item_name):
    """Get an item by its full name"""
    for category in MAGIC_ITEMS.values():
        for item in category.values():
            if item['name'] == item_name:
                return item
    return None

def get_items_by_type(item_type):
    """Get all items of a specific type"""
    if item_type in MAGIC_ITEMS:
        return MAGIC_ITEMS[item_type]
    return {}

def get_wand_variants():
    """Get all wand variants with their die values"""
    variants = {}
    for spell_name, wand_data in MAGIC_ITEMS['wands'].items():
        for variant in wand_data['variants']:
            key = f"{wand_data['name']} ({variant})"
            variants[key] = {
                'name': key,
                'description': wand_data['description'],
                'type': 'wand',
                'charges': wand_data['charges'],
                'die': variant,
                'spell_name': spell_name
            }
    return variants

def get_potion_variants():
    """Get all potion variants with their die values"""
    variants = {}
    for spell_name, potion_data in MAGIC_ITEMS['potions'].items():
        for variant in potion_data['variants']:
            key = f"{potion_data['name']} ({variant})"
            variants[key] = {
                'name': key,
                'description': potion_data['description'],
                'type': 'potion',
                'die': variant,
                'spell_name': spell_name
            }
    return variants

def get_scroll_variants():
    """Get all scroll variants with their die values"""
    variants = {}
    for spell_name, scroll_data in MAGIC_ITEMS['scrolls'].items():
        for variant in scroll_data['variants']:
            key = f"{scroll_data['name']} ({variant})"
            variants[key] = {
                'name': key,
                'description': scroll_data['description'],
                'type': 'scroll',
                'die': variant,
                'spell_name': spell_name
            }
    return variants

def get_staff_variants():
    """Get all staff variants with their die values"""
    variants = {}
    for staff_name, staff_data in MAGIC_ITEMS['staves'].items():
        for variant in staff_data['variants']:
            key = f"{staff_data['name']} ({variant})"
            variants[key] = {
                'name': key,
                'description': staff_data['description'],
                'type': 'staff',
                'charges': staff_data['charges'],
                'die': variant,
                'staff_name': staff_name
            }
    return variants
