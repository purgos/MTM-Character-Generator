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
            'description': 'This permanent use magic item will temporarily increase the Warrior Melee aspect die of the wearer and one D12 gear die to a D20 for 10 rounds per day as long as it is worn and once activated by uttering the command word. Can be used multiple times per day but for no more than the 10 total rounds per day.',
            'type': 'permanent'
        },
        'Bolts/Arrows of Armor Penetration': {
            'name': 'Bolts/Arrows of Armor Penetration',
            'description': 'These reusable items come in a quiver of 10. If these items are shot at a target, the bolts/arrows will ignore any armor bonuses.',
            'type': 'permanent'
        },
        'Boots of Free Movement': {
            'name': 'Boots of Free Movement',
            'description': 'This permanent use magic item allows the wearer to move at their normal movement rate over any surface classified as Difficult Terrain.',
            'type': 'permanent'
        },
        'Boots of Speed': {
            'name': 'Boots of Speed',
            'description': 'This permanent use item allows the wearer to move at double their normal movement rate. It does not confer any extra attacks. Does not stack with Belt of Speed.',
            'type': 'permanent'
        },
        'Bracers of Armor': {
            'name': 'Bracers of Armor',
            'description': 'This permanent use magic item functions just like normal armor except it does not take up a gear die slot. The GM will assign a base gear die value when found from D4-D12. These do not stack with any other type(s) of armor or other Bracers.',
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
        'Cloak of Spell Resistance': {
            'name': 'Cloak of Spell Resistance',
            'description': "This permanent use item confers a permanent bonus of +1 to +5 to the wearer's magic saves as long as it is worn.",
            'type': 'permanent',
            'variants': ['+1', '+2', '+3', '+4', '+5']
        },
        'Chime of Opening': {
            'name': 'Chime of Opening',
            'description': 'Striking this object will unlock all locked or magically locked doors within 60 feet. It shatters after one use.',
            'type': 'permanent'
        },
        'Cloak of Displacement': {
            'name': 'Cloak of Displacement',
            'description': 'This permanent use magic item allows the wearer to utilize the Displacement spell once per day when worn for a number of rounds equal to the gear die assigned by the GM when the item is found. For example: A D6 Cloak of Displacement when activated will function as the spell for 6 rounds (no Aspect or Gear Die checks needed).',
            'type': 'permanent',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
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
        'Oil of Positive Magic Armor': {
            'name': 'Oil of Positive Magic Armor',
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
            'description': 'Allows the caster to conjure up an acidic rain that fills a single 5-foot square per caster rank. All affected squares must be connected. The acid causes its gear die in damage to any creatures in the affected squares. Any non-magical armor in the affected squares are destroyed unless the item makes an armor save versus a DL11',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Alarm': {
            'name': 'Wand of Alarm',
            'description': 'You set an alarm against unwanted intrusion. Choose a door, a window, or an area within range that is no larger than a 20-foot cube. Until the spell ends, an alarm alerts you whenever a Tiny or larger creature touches or enters the warded area. When you cast the spell, you can designate creatures that won\'t set off the alarm. You also choose whether the alarm is mental or audible. A mental alarm alerts you with a ping in your mind if you are within 1 mile of the warded area. This ping awakens you if you are sleeping. An audible alarm produces the sound of a hand bell for 10 seconds within 60 feet. This spell lasts 24 hours or until dispelled',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Analyze': {
            'name': 'Wand of Analyze',
            'description': 'Allows a check to detect if one item is magical. The GM always makes this roll for the character. The caster must touch the item and spend one hour studying and using it. Scrolls can always be identified with a successful visual check without reading the scroll contents out loud; however, potions require the caster to taste a small sample of the liquid to identify it and any items require the caster to use/touch the item thus meaning that if it produces a baneful effect, the character is subject to the baneful effect. A 4 or better is needed to determine if it is magical and a 7 or better is needed to determine exactly what it does. If the item is cursed, it will detect as a similar beneficial magic item, but cause a baneful effect if applicable. This curse can be identified only if the caster check is 10 or greater. This wand can be cast one time on each item per week. If the check fails, that caster cannot further identify that item until one week has passed. A rank 7 or better caster can attempt to re-analyze an item once per day in the event of failure. Note: This wand is always cast “successfully” since it is done outside of combat exclusively',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Animate Object': {
            'name': 'Wand of Animate Object',
            'description': 'Allows the caster to animate one unoccupied object up to 10 pounds per rank and not classified as a weapon for a number of rounds equal to the gear die roll and attack with it as if it were an improvised weapon doing a D4 in damage each round to a single target. The animated object may not be used for defense such as Animating a shield and may not exceed a total weight of 50 pounds. A rank 7 caster can animate a number of unoccupied objects equal to the gear die roll each attacking a separate target. The caster must use an attack action each round or a move action to maintain the wand, otherwise it ends at the end of the original casters turn',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Blindness': {
            'name': 'Wand of Blindness',
            'description': 'Causes one target to lose all sight and take on the blinded condition for a number of rounds equal to the gear die roll. A rank 7 caster can affect a number of targets equal to the gear die roll.  Buried Alive (I) This wand causes the affected area to fill with boulders causing its gear die in damage to any targets in the area of effect. The effect lasts a number of rounds equal to the gear die roll. Creatures can make a Magic save vs. DL11 or better to avoid being buried in the rubble. Huge or larger size creatures gain a +2 bonus to the magic save per size category above Large that they are. Buried creatures can take no actions though they may be dug out by others in 1d4 rounds. Buried creatures do not take ongoing damage, however, they are subject to the Drowning rules/effects while buried under the rubble. A rank 7 or better caster can fill a 20x20x20 area. This wand can be cast once per day',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'All’s Clear': {
            'name': 'Wand of All’s Clear',
            'description': 'Allows the caster to remove any non-magical impediments in their square(s). This would include such items as pitons, ball bearings, spores from a creature, dust, dirt, etc. All items this wand can remove are subject to GM approval. This wand lasts a number of rounds equal to the gear die rolled',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Buried Alive': {
            'name': 'Wand of Buried Alive',
            'description': 'This wand causes the affected area to fill with boulders causing its gear die in damage to any targets in the area of effect. The effect lasts a number of rounds equal to the gear die roll. Creatures can make a Magic save vs. DL11 or better to avoid being buried in the rubble. Huge or larger size creatures gain a +2 bonus to the magic save per size category above Large that they are. Buried creatures can take no actions though they may be dug out by others in 1d4 rounds. Buried creatures do not take ongoing damage, however, they are subject to the Drowning rules/effects while buried under the rubble. A rank 7 or better caster can fill a 20x20x20 area.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Burrow': {
            'name': 'Wand of Burrow',
            'description': 'Caster grows claws and gains a burrowing speed of 15’ per round for a number of rounds equal to the gear die roll. A rank 7 or higher caster can burrow at a speed of 30’ per round. The claws cannot be used as a weapon nor can the caster move through or into other creatures. A roll of 10 or better is needed to burrow through stone. You cannot burrow through metal with this wand. This wand cannot be used in conjunction with Displacement or Mirror Image',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Chain Lightning': {
            'name': 'Wand of Chain Lightning',
            'description': 'Unleashes a bolt of electricity that arcs from one target to another affecting 2 targets at minimum plus an additional target per gear die rolled causing its gear die in damage to all affected creatures. A rank 7 or better caster can affect an additional target per rank. This wand can be cast every other round. CHARM MONSTER/PERSON (I, S) This wand allows the caster to compel the target to do their bidding. The target will not bring harm to themselves, but will obey any other verbal commands given to them for a number of rounds equal to the gear die rolled. All targets get a Magic save at the beginning of the original casters round to break the Charm effect with a DL of 11. The caster must remain within visual range of any targets and use a full round action to maintain the Charm. A rank 7 or higher caster can affect a number of targets equal to the gear die rolled and may use a Move Action to maintain the wand instead',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Charm Monster/Person': {
            'name': 'Wand of Charm Monster/Person',
            'description': 'This wand allows the caster to compel the target to do their bidding. The target will not bring harm to themselves, but will obey any other verbal commands given to them for a number of rounds equal to the gear die rolled. All targets get a Magic save at the beginning of the original casters round to break the Charm effect with a DL of 11. The caster must remain within visual range of any targets and use a full round action to maintain the Charm. A rank 7 or higher caster can affect a number of targets equal to the gear die rolled and may use a Move Action to maintain the wand instead',
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
            'description': 'Allows the caster to shout taunting insults to a number of creatures equal to the gear die roll. The caster may choose to target less creatures than the gear die roll. Targets must make a magic save against base DC11. Affected creature(s) will attack the caster only, ignoring all other creatures for a number of rounds equal to the gear die roll. If an affected creature cannot attack the caster either by melee, ranged, or wand attack; they would simply do nothing that round. If an affected character cannot attack on 2 nd and subsequent rounds, affected creatures would get another magic save as a free action against DC11 for each subsequent round that the original caster cannot be targeted',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Comfort': {
            'name': 'Wand of Comfort',
            'description': 'This wand allows the caster to suffer no ill effects from natural extreme heat or cold for a period of 1 hour per gear die rolled. A rank 7 or greater caster can affect a number of targets equal to the gear die rolled',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Common Knowledge': {
            'name': 'Wand of Common Knowledge',
            'description': 'This wand improves the caster’s’ Gather Information check(s). Upon casting this wand, the caster may add +1 to their Gather Information skill check(s) per gear die rolled. A rank 7 or greater caster can cast this wand twice per day',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Create Portal': {
            'name': 'Wand of Create Portal',
            'description': 'Allows the caster to lay their hands on a 5x5x10 section of wall or a door and create a hole large enough to allow 1 medium sized being to pass through per round or allows one projectile or wand to pass through per round. A rank 7 or better caster can create a 10x10x20 opening and allow 2 medium creatures or 1 large creature through per round or two projectiles or two wands through per round. The wand lasts for a number of rounds equal to the gear die roll',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Dazzle': {
            'name': 'Wand of Dazzle',
            'description': 'Causes one man-sized enemy to hesitate for a number of rounds equal to the gear die roll. Victims take on the Dazed condition. Dazzled creatures can’t become undazzled unless attacked successfully with a melee or ranged weapon, a wand, (both doing full damage with no saves or armor bonuses) or a lessen effect wand. A rank 7 or better caster can affect a number of creatures equal to the gear die roll',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Deafness': {
            'name': 'Wand of Deafness',
            'description': 'Causes one target to lose all hearing and take on the deafened condition for a number of rounds equal to the gear die roll. A rank 7 caster can affect a number of targets equal to the gear die roll',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Death': {
            'name': 'Wand of Death',
            'description': 'Below Allows the caster to select one living target and attempt to steal its life force. The target immediately makes a death save with a + or – one per rank difference between the caster and the target. Failure results in immediate death. A partial success means the target takes the casters gear die multiplied by the casters rank in damage divided by 2 while a moderate success results in the target taking one half its current hit point total in damage while a total save results in the target instead taking on the sickened condition for a number of rounds equal to the casters gear die. This wand also causes the caster to take on the exhausted condition for a number of rounds equal to the gear die roll',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Disadvantaged': {
            'name': 'Wand of Disadvantaged',
            'description': 'This wand allows the caster to plant a mental suggestion into the targets mind causing the target to make two dice rolls on either Aspect Checks, Armor Checks, or Magic Saves for a number of rounds equal to the gear die rolled. The caster must state which roll they want this penalty to apply to upon casting. A rank 7 or better caster can affect a number of targets equal to the gear die rolled',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Displacement': {
            'name': 'Wand of Displacement',
            'description': 'Causes one man-sized enemy to hesitate for a number of rounds equal to the gear die roll. Victims take on the Dazed condition. Dazzled creatures can’t become undazzled unless attacked successfully with a melee or ranged weapon, a wand, (both doing full damage with no saves or armor bonuses) or a lessen effect wand. A rank 7 or better caster can affect a number of creatures equal to the gear die roll',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Dragon Breath': {
            'name': 'Wand of Dragon Breath',
            'description': 'You gain the ability to breathe gout of energy as a standard/attack action that mimics a dragon\'s breath. You may choose from fire, cold, lightning, or acid when casting. The spell does its gear die in damage to a 10x10’x10’ square or a line 4 squares long either vertical, horizontal, or diagonally though it cannot be “bent”. The acid breath weapon also causes any non-magical equipment/items in the affected squares to be destroyed unless the items make a magic save versus a DL11. This spell may be cast once per encounter. A rank 7 or better caster can cast this spell twice per encounter. Dude You’re Stoned (I, O) This spells grants a gaze attack to the caster that can turn its target to stone temporarily. Any creature affected by this gaze is immediately turned to stone for a number of rounds equal to the gear die rolled. Creatures under the effect of this spell can take no actions except to make a Magic save vs. DL11 each round to break the effect. The target suffers no other effects from this spell. Any creature actively avoiding the casters gaze gets a +10 bonus to the Magic save to avoid its effects.  A rank 7 or better caster can cast this spell once per encounter',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Dude You’re Stoned': {
            'name': 'Wand of Dude You’re Stoned',
            'description': 'This wands grants a gaze attack to the caster that can turn its target to stone temporarily. Any creature affected by this gaze is immediately turned to stone for a number of rounds equal to the gear die rolled. Creatures under the effect of this wand can take no actions except to make a Magic save vs. DL11 each round to break the effect. The target suffers no other effects from this wand. Any creature actively avoiding the casters gaze gets a +10 bonus to the Magic save to avoid its effects.  A rank 7 or better caster can cast this wand once per encounter',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Enhancement': {
            'name': 'Wand of Enhancement',
            'description': 'Allows the caster to temporarily increase a random single targets ability. The caster can choose any effect on the chart below at or below his gear die roll. The increase lasts a number of rounds equal to the gear die roll though extra HP and gear die once used are gone.  1: an extra d4 gear die 8. 5 temp hp 2. 2 temp HP 9. An extra d12 gear die 3. An extra d6 gear die 10. 6 temp hp 4. 3 temp hp 11. +1 to all party die rolls 5. An extra d8 gear die 12. Gain a temporary d20 6. 4 temp hp gear die on any one round of 7. An extra d10 gear die attacks',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Enlarge': {
            'name': 'Wand of Enlarge',
            'description': 'Allows the caster to enlarge a single willing target one size category for a number of rounds equal to the gear die roll. A rank 7 caster can enlarge a number of creatures equal to the gear die roll and can increase target(s) two size categories. The effect lasts a number of rounds equal to the gear die roll',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Enrage': {
            'name': 'Wand of Enrage',
            'description': 'Allows the caster to enter a frenzied attack mode for a number of rounds equal to the character rank which confers the following bonuses/penalties: 1. Gain 1 temp HP per rank. These last until they are taken, or the rage ends whichever comes first 2. Gain +2 on Warrior Melee aspect checks to hit 3. Suffers a -2 to defense and a -4 to armor checks while raging 4. Character cannot cast wands, use scrolls or take potions while raging 5. When the wand ends, you must take a short rest (10 min) or suffer from the exhausted condition. If the character is at 0 or less HP at the end of the wand duration or they fall unconscious while under the wand effect, they must make an immediate Death Save with failure resulting in death. The character must rest before 8 hours expire after the rage ends or they fall unconscious for 24 hours automatically',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Entangle': {
            'name': 'Wand of Entangle',
            'description': 'Conjures a single 10’ long black tentacle that entangles one target and introduces the entangled condition. The wand lasts a number of rounds equal to the gear die roll. A rank 7 caster can conjure a number of tentacles and affect a number of targets equal to the gear die roll and may also move the tentacle(s) 30’ per move action. No creature may have more than one tentacle attacking/entangling them at a time. Each tentacle has 10hp and is immune to all wand effects',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Exhaustion': {
            'name': 'Wand of Exhaustion',
            'description': 'Causes one target to take on the exhausted condition for a number of rounds equal to the gear die roll. A rank 7 caster can affect a number of targets equal to the gear die roll.  Eye See You (I, O, S) This wand allows the caster to conjure a magical eye that the caster can use to see through. The eye lasts a number of rounds equal to the gear die rolled. This magical eye has and confers Darkvision to the caster and allows the caster to cast wands through the eye as though they could actually see the target(s) with their own eyes. The Magic Eye has 15HP and is subject to attack and wands. The eye uses the casters statistics for Magic Saves and Armor Checks. The eye can be moved or maintained by the caster using a move action and can move 60’ per round indoors or 120’ per round outdoors. The caster must maintain visual contact with the Magic Eye or the effect ends immediately. This wand can be cast once per day. A rank 7 or better caster can cast this wand once per encounter',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Eye See You': {
            'name': 'Wand of Eye See You',
            'description': 'This spell allows the caster to conjure a magical eye that the caster can use to see through. The eye lasts a number of rounds equal to the gear die rolled. This magical eye has and confers Darkvision to the caster and allows the caster to cast spells through the eye as though they could actually see the target(s) with their own eyes. The Magic Eye has 15HP and is subject to attack and spells. The eye uses the casters statistics for Magic Saves and Armor Checks. The eye can be moved or maintained by the caster using a move action and can move 60\' per round indoors or 120\' per round outdoors. The caster must maintain visual contact with the Magic Eye or the effect ends immediately. A rank 7 or better caster can cast this spell once per encounter.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Fearful Presence': {
            'name': 'Wand of Fearful Presence',
            'description': 'Causes one target to take on the panicked condition for a number of rounds equal to the gear die roll. A rank 7 caster can affect a number of targets equal to the gear die roll',
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
            'description': 'Does its gear die plus caster rank in damage to one 5-foot square per rank or a line/diagonal up to the characters rank in size. All squares that are targeted must be connected. The caster can choose where to center the blast, but it radiates out equally from the point of origin. This is magic that dissipates at the end of the casters turn. Anyone in an adjacent square to the target takes the character rank damage only unless they make a successful magic save',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Fly': {
            'name': 'Wand of Fly',
            'description': 'Allows the caster to fly like bird for a number of rounds equal to the effect roll at a rate of 60 feet per round in any direction. They may cast wands, use missiles, attack as normal and may hover, speed up and slow down at will. A rank 7 or above caster can affect an additional willing creature',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Forget': {
            'name': 'Wand of Forget',
            'description': 'Causes the target to forget all wands in any current gear die slots at a cost of one wand per 2 points rolled for a minimum of one and a maximum of 6. The wands forgotten go from lowest to highest gear die of wands remaining. These slots cannot be repopulated with wands unless the target takes a long rest (8+ hours). This wand can only be used once per encounter.',
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
            'description': 'Choose either the caster or one other target within sight. A falling creature’s rate of descent slows to 60 feet per round for a number of rounds equal to the gear die roll. If the creature lands before the wand ends, it takes no falling damage and can land on its feet, and the wand ends for that creature. A rank 7 or greater caster can affect a number of targets equal to the gear die roll.  Gotta Have It (I) This wand allows the caster to cast any wand in their wand book when needed without having to have it prepared in either a Wand or Gear Die slot beforehand. The wand gained from this wand is subject to any limitations of the gained wand. The wand can only be at a D4, D6, or D8 level of effect. A Rank 7 or better caster can cast any wand from their wand book when needed at any Wand or Gear Die level.  A rank 7 or better caster can cast this wand once per encounter',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Gotta Have It': {
            'name': 'Wand of Gotta Have It',
            'description': 'This wand allows the caster to cast any wand in their wand book when needed without having to have it prepared in either a Wand or Gear Die slot beforehand. The wand gained from this wand is subject to any limitations of the gained wand. The wand can only be at a D4, D6, or D8 level of effect. A Rank 7 or better caster can cast any wand from their wand book when needed at any Wand or Gear Die level. A rank 7 or better caster can cast this wand once per encounter.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Grease': {
            'name': 'Wand of Grease',
            'description': 'Allows the caster to fill a single 5-foot square with an oily substance per caster rank. All affected squares must be connected. Any creatures caught in the affected squares must make a magic save to avoid falling prone in the square and affected squares are treated as difficult terrain. The grease lasts a number of rounds equal to the gear die roll',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Greater Healing': {
            'name': 'Wand of Greater Healing',
            'description': 'Restores twice its gear die in hit points plus caster rank to the person the caster chooses. A rank 7 or higher caster can cast this wand once per encounter per target. This wand can only be used once per encounter.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Greater Mass Healing': {
            'name': 'Wand of Greater Mass Healing',
            'description': 'Restores twice its gear die in hit points plus caster rank to the casters entire party. A rank 7 or higher caster can cast this wand twice per encounter',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Hail Storm': {
            'name': 'Wand of Hail Storm',
            'description': 'Conjures several small hail stones to rain down upon a single 5-foot square. The number of stones is equal to the gear die rolled. The stones do 1 point of damage per stone. At rank 7, the caster can fill 2 five-foot squares, but affected squares must be connected',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Haste': {
            'name': 'Wand of Haste',
            'description': 'Speeds up time for one person, increasing the number of actions they get to take that turn. This wand cannot be cast on animals or Spiritual Helpers. Upon successful casting, additional actions are granted at the cost of 4 points rolled per action with a minimum of one bonus action and a maximum of 3 bonus actions. Actions granted by this wand must be used by the end of the casters next turn',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'HealAll': {
            'name': 'Wand of HealAll',
            'description': 'Restores its die in hit points multiplied by caster rank to one person the caster chooses. A rank 7 or higher caster can cast this wand once per encounter',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Healing': {
            'name': 'Wand of Healing',
            'description': 'Restores its die in hit points plus caster rank to one person the caster chooses. A rank 7 or higher caster can cast this wand once per encounter per target',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Heroism': {
            'name': 'Wand of Heroism',
            'description': 'Grants a temporary +1 to Aspect Checks, Saving Throws, and/or Armor Checks according to the table below. A rank 7 or higher caster can cast this once per encounter.  1-4 +1 on aspect checks 5-8 +1 on saving throws 9-12 +1 on armor checks I Dare You To (I) This wand causes iron spikes to erupt from the targets body or armor. These spikes cause damage to any creature of equal or smaller size to the target each time they attack the target with any non- reach or natural weapon(s). The effect lasts a number of rounds equal to the gear die rolled. The spikes cause 1d4 damage per attack that the attacking creature makes against the recipient of this wand. A rank 7 or better caster can cast this wand once per encounter',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'I Dare You Too': {
            'name': 'Wand of I Dare You Too',
            'description': 'This wand causes iron spikes to erupt from the targets body or armor. These spikes cause damage to any creature of equal or smaller size to the target each time they attack the target with any non-reach or natural weapon(s). The effect lasts a number of rounds equal to the gear die rolled. The spikes cause 1d4 damage per attack that the attacking creature makes against the recipient of this wand. A rank 7 or better caster can cast this wand once per encounter.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Icy Blast': {
            'name': 'Wand of Icy Blast',
            'description': 'Allows the caster to fire a ray of ice that hits a number of targets equal to its gear die and doing its gear die in damage to its target(s). A rank 7 or better caster can cast this wand every other round',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Illusion': {
            'name': 'Wand of Illusion',
            'description': 'Creates an illusion of a single person or creature that the caster has seen that lasts a number of rounds equal to the gear die roll. If the gear die roll is a 1-4, the illusion has visual capabilities only, 5-8 means it can speak any words the caster communicates to the illusion telepathically, 9-12 means that the illusion can actually attack and cause force damage of 1D8 per round to the target',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Immobilize': {
            'name': 'Wand of Immobilize',
            'description': 'Same as Dazzle except the held creatures can’t move or free itself automatically if attacked. When the affected creature is hit with a weapon or wand (which ignores armor and allows no save), the target(s) get a magic save to break the effect after each successful attack at DL11 to break the effect. The target is held fast until the wand is dispelled, he is attacked and then saves to break the effect, or until 24 hours elapse. A rank 7 caster can affect a number of creatures equal to the gear die roll',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Incorporeal': {
            'name': 'Wand of Incorporeal',
            'description': 'Allows the caster to make themselves and any gear they are carrying incorporeal immediately and gains the ability to walk through walls and other objects. The caster cannot interact with any creatures or objects or attack while in this form. No other beneficial wands or effects can exist or be cast on a creature that is Incorporeal. This wand lasts a number of rounds equal to the effect roll',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Inspire': {
            'name': 'Wand of Inspire',
            'description': 'Grants a temporary bonus to a select character. When inspired, the character adds a D4 to their next roll (excluding damage rolls). At Rank 3 it is increased to a D6, at Rank 6 a D8 and at rank 10 a D12.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Instant Search': {
            'name': 'Wand of Instant Search',
            'description': 'Allows the caster to concentrate and search a 10’x10’x10’ square and instantly know everything they wish to about the search area. This will provide information on any non-magical details of anything within the search area. A rank 7 or greater caster can search a 20’x20’x20’ area per casting',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Invisibility': {
            'name': 'Wand of Invisibility',
            'description': 'Can be cast on one or several willing creatures, making it impossible for them to be seen by normal means, at the cost of 4 points rolled per creature with a minimum of one and a maximum of 3. Although attacking an enemy while invisible will always grant one automatic hit (two if the character dual wields), it will also immediately end the invisibility wand for that person. This wand does not grant any extra attacks or actions beyond the automatic hit with the first set of attacks. This wand lasts a number of rounds equal to the wand roll on each target.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Lessen Effect': {
            'name': 'Wand of Lessen Effect',
            'description': 'Lessens and possibly removes temporary effects such as blindness, dazzled, sickened, etc. If the effect to be lessened/removed has a duration, it is lessened by a number of rounds equal to the die roll, possibly bringing about an immediate end to the effect. If it has a permanent duration, then one such effect can be removed per casting. This wand will not lessen/remove Aspect or Hit Point drain/damage nor will it remove the conditions brought on by the Dying [Shaken] condition. It will also not lessen/remove any conditions that are self-inflicted such as Sleeping in Armor, etc. A rank 7 or higher caster can lessen/remove one effect from a number of creatures equal to the gear die roll',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Levitate': {
            'name': 'Wand of Levitate',
            'description': 'Allows the caster to float vertically up and down for a number of rounds equal to the effect roll. The caster can float 30 feet per round',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Lightning': {
            'name': 'Wand of Lightning',
            'description': 'Creatures Does its gear die in damage to all opponents the caster can see. A rank 7 or better caster can cast this every round',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Locked': {
            'name': 'Wand of Locked',
            'description': 'Allows the caster to lock a number of locks that the caster can see. This wand locks a number of locks equal to the effect roll. Locks closest to the caster are affected first',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Luck': {
            'name': 'Wand of Luck',
            'description': 'Allows you to add your gear die to another person\'s melee/ranged attack or damage roll, before they make it! It can also be used to reduce an opponent’s roll by the same amount, before they make it. Any luck must be used by the target by the end of the original casters next turn. If used against an opponent, the original caster must declare his intention to use it BEFORE the opponent acts and the target gets a magic save to resist the effect. A rank 7 or better caster can affect a number of creatures equal to the gear die roll. This spell cannot be used in combination with Enhancement or Metamagic. Can be cast once per encounter. Luck of the Irish (I, O, S) This spell allows the caster access to a pool of points that can be applied to any rolls the caster makes with the exception of Death saves equal to the gear die rolled. These points last a number of rounds equal to the gear die rolled. A rank 7 or better caster can choose to affect one ally instead',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Luck of the Irish': {
            'name': 'Wand of Luck of the Irish',
            'description': 'This wand allows the caster access to a pool of points that can be applied to any rolls the caster makes with the exception of Death saves equal to the gear die rolled. These points last a number of rounds equal to the gear die rolled. A rank 7 or better caster can choose to affect one ally instead.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magic Missile': {
            'name': 'Wand of Magic Missile',
            'description': 'Fires one bolt of arcane magic through the air doing its gear die plus 1 point per rank in damage. This wand is always cast successfully. A rank 7 or higher caster can fire a number of missiles equal to the gear die roll each hitting a separate target or a maximum of two missiles can be directed at a single target, but not both with the same wand. Each missiles gear die in damage must be rolled separately. In the event of a critically cast Magic Missile wand, ONLY the first missile will crit with the others doing normal damage and at Rank 7 or higher ONLY the first two missiles will crit, the others will do normal damage',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magic Shield': {
            'name': 'Wand of Magic Shield',
            'description': 'Protects a single person the caster chooses (including the caster if she desires) from its die in damage, which is chipped away until it is gone. A rank 7 or higher caster can affect a number of targets equal to the casters rank',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magical Darkness': {
            'name': 'Wand of Magical Darkness',
            'description': 'Allows the caster to cast a darkness wand that darkens an area 30’x30’x10’ with inky black darkness. This wand lasts a number of hours equal to the effect roll. Wands cannot be cast into or out of an area under this effect by either the caster or anyone else. Wands that require concentration such as Phantom Weapon will also not function in the zone. This wand counteracts Magical Light. A rank 7 or better caster can cast this wand once per encounter',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magical Light': {
            'name': 'Wand of Magical Light',
            'description': 'Object Allows the caster to cast a light wand that illuminates an area with bright magical light. This wand can be cast on an inanimate object and lasts a number of hours equal to the effect roll. This wand counteracts Magical Darkness. A rank 7 or better caster can cast this wand once per encounter',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magical Sight': {
            'name': 'Wand of Magical Sight',
            'description': 'Allows the caster to see through solid objects up to a distance of 120 feet. A gear die roll of 1-4 allows them to see through flesh and bone, a roll of 5-9 allows them to see through wood, a roll of 9 or10 allows them to see through stone and a roll of 11-12 allows them to see through any material for a number of rounds equal to the gear die roll',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Mass Healing': {
            'name': 'Wand of Mass Healing',
            'description': 'Restores its gear die in hit points plus caster rank to the casters entire party. A rank 7 or higher caster can cast this wand twice per encounter',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Metamagic': {
            'name': 'Wand of Metamagic',
            'description': 'Allows the caster to manipulate the normal wand limitations of any non-persistent wand according to the below table based on the gear die roll. The wand only affects wands cast by the original caster. The caster can choose any ability at or below the gear die roll to manifest and apply it to any single wand. The metamagic must be used by the end of the casters next turn. This wand cannot be used in conjunction with Analyze.  A rank 7 or above caster can cast this wand once per encounter on himself or an ally. 1-2: Empower: increases the damage/effect of any non-persistent wand by 1.5 3-4: Enlarge: increases the wands affected area by 2. Does not affect non-area effect wands. 5-6: Extend: increases the duration of any non-persistent wand by 2. 7-8: Maximize: causes any variable effects on a non-persistent wand to be at maximum. 9-10: Quicken: allows the caster to cast two encounter level wands in a single round. 11-12: Repeat: allows the caster to cast a single non-persistent wand and have it auto cast again on the casters next round as a free action',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Mirror Image': {
            'name': 'Wand of Mirror Image',
            'description': 'Conjures one exact duplicate of the caster per rank. The images occupy the nearest squares to the caster. The caster can control how many images are created, however, the number of images cannot exceed the number of squares that the caster can see. The caster effectively “blinks” around from image to image though they can control this. Anyone attacking the character has a 50% chance to hit the character, (Below 51 hits an image), otherwise they hit an image instead and that image dissipates. The wand lasts a number of rounds equal to the gear die roll. This wand may not be used in conjunction with Burrow or Displacement. This wand may be cast once per encounter. More is Always Better (I) This wand allows the caster to give the target an additional pair of arms. The effect lasts for a number of rounds equal to the gear die rolled. The target gets an extra attack action as a benefit. If the target does not have weapons available for each new arm, they can instead make an Improvised Weapon attack with those arms as though they had the Improvised Weapon ability. If the target already has the improvised weapon ability, the additional arm attacks would instead be at 1d6 damage. A rank 7 or better caster can cast this wand once per encounter.  Mutable Form (I, 0, S) This wand allows the recipient to assume a mutable form that makes the target immune from critical hits for a number of rounds equal to the gear die rolled. A rank 7 or better caster can cast this wand on one ally instead. This wand can be cast once per day per target',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'More is Always Better': {
            'name': 'Wand of More is Always Better',
            'description': 'This wand allows the caster to give the target an additional pair of arms. The effect lasts for a number of rounds equal to the gear die rolled. The target gets an extra attack action as a benefit. If the target does not have weapons available for each new arm, they can instead make an Improvised Weapon attack with those arms as though they had the Improvised Weapon ability. If the target already has the improvised weapon ability, the additional arm attacks would instead be at 1d6 damage. A rank 7 or better caster can cast this wand once per encounter.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Mutable Form': {
            'name': 'Wand of Mutable Form',
            'description': 'This wand allows the recipient to assume a mutable form that makes the target immune from critical hits for a number of rounds equal to the gear die rolled. A rank 7 or better caster can cast this wand on one ally instead.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Natures Step': {
            'name': 'Wand of Natures Step',
            'description': 'This wand can only be cast outdoors. This wand allows the caster to merge into any tree or bush and instantly reappear next to any other tree or bush within the casters sight when they first cast the wand. This uses only five’ of movement. This wand lasts a number of rounds equal to the gear die rolled. A rank seven or better caster can affect one ally as well',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Night Vision': {
            'name': 'Wand of Night Vision',
            'description': 'Allows the caster to see in total and magical darkness as though it were normal daylight. This effect lasts a number of rounds equal to the gear die roll. This wand will not allow you to cast a wand into an area affected by Magical Darkness, however, a rank 7 or better caster can cast out of an area under Magical Darkness while under the effect of this wand',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Obscure Life Force': {
            'name': 'Wand of Obscure Life Force',
            'description': 'Allows the caster to obscure their life force from creatures with Lifesense such as undead. Undead creatures would not be able to detect the affected creature(s) for the duration of the wand. A rank 7 caster can affect a number of targets equal to the gear die roll. This wand lasts for a number of rounds equal to the gear die roll',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Odorless': {
            'name': 'Wand of Odorless',
            'description': 'This wand removes all scent from the caster and the gear they are carrying for a number of rounds equal to the gear die rolled. A rank 7 or higher caster can affect a number of allies equal to the gear die rolled',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Open': {
            'name': 'Wand of Open',
            'description': 'Allows the caster to unlock a number of locks that the caster can see. This wand unlocks a number of locks equal to the gear die roll. Locks closest to the caster are affected first',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Paralyzing Ray': {
            'name': 'Wand of Paralyzing Ray',
            'description': 'Causes one target to take on the paralyzed condition for a number of rounds equal to the gear die roll. A rank 7 caster can affect a number of targets equal to the gear die roll',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Pardon Me': {
            'name': 'Wand of Pardon Me',
            'description': 'As a full round action, you attempt to interrupt an enemy wand caster from casting a wand at you. You choose one target and a particular wand or wand like effect and if that creature casts a wand/wand like effect at you, the wand caster must make two Magic Checks, if either fails, the wand does not affect you at all, though it would affect other potential targets if applicable. This only affects wands that directly target you either in a group or individually. Area of effect wands cannot be interrupted via this wand. The wand lasts for a number of rounds equal to the gear die rolled or until you are targeted and the caster is forced to make the disadvantaged Magic check. A rank 7 or better caster can negate two wands/wand like effects instead',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Phantom Weapon': {
            'name': 'Wand of Phantom Weapon',
            'description': 'Conjures a single one-handed weapon of the casters choice that does its gear die in damage to a single target upon a successful hit. The caster can use the phantom weapon to attack the round after it is summoned. The caster uses their Magic Aspect to attack with this wand. A rank 4 caster can conjure a two-handed weapon. A 7th rank caster can conjure two one hand weapons per casting and can attack with the phantom weapons on the same round it is cast, OR the caster can opt for a single one or two hand weapon that can hit incorporeal/ethereal creatures without penalty. The caster must use an attack action each round or a move action to maintain the wand, otherwise it ends at the end of the original casters turn. If the Magic Aspect check roll to hit is a natural 1, the Phantom Weapon attacking will disappear. The wand lasts a number of rounds equal to the gear die roll. Wand may be cast once per encounter.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Polymorph Self': {
            'name': 'Wand of Polymorph Self',
            'description': 'Allows the caster to assume the shape of any non-unique creature that the caster has personally seen up to a size of medium. On a roll of 7-8 the caster can assume the form of a large creature, 9-10 a Huge creature and 11-12, an Enormous creature. The caster gains none of the assumed creature’s abilities, simply the look of the creature and extended reach. At rank 7 or higher, the caster can affect one other target. Wand lasts for 1 hour or until dispelled',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Pray for the Dying': {
            'name': 'Wand of Pray for the Dying',
            'description': 'This wand allows the caster to take a full round action and touch an ally who is at zero or less hit points and has yet to make a death save. This touch will automatically heal one point of damage and negate the need for the target to make a death save. The target would then follow the rules regarding HP Recovery. A rank 7 or better caster can affect two targets per casting',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Purify': {
            'name': 'Wand of Purify',
            'description': 'Instantly cures any diseases and poisons from either the caster or one ally and restores its gear die number in hit points. This wand can only be cast outside of combat but can be cast as many times as needed. Purify Area (I, O, S) This wand removes any negative non-magical effects/objects in the area. All squares affected must be connected. A rank 7 or better caster can affect 2 five foot squares per rank. Line of sight is not required to cast this wand in your own square. This wand lasts a number of rounds equal to the gear die roll',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Purify Area': {
            'name': 'Wand of Purify Area',
            'description': 'This wand removes any negative non-magical effects/objects in the area. All squares affected must be connected. A rank 7 or better caster can affect 2 five foot squares per rank. Line of sight is not required to cast this wand in your own square. This wand lasts a number of rounds equal to the gear die roll.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Racial Modification': {
            'name': 'Wand of Racial Modification',
            'description': 'This cursed item detects as a Wand of Luck and functions as such, but also modifies the wielder’s race as follows; roll 1d6 to determine: 1. Human 2. Elf 3. Halfling 4. Dwarf 5. Half-Giant 6. PC Choice unless the curse is detected with an Analyze wand check of 10 or higher.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Reach Out': {
            'name': 'Wand of Reach Out',
            'description': 'This wand extends the reach of the caster an additional five feet as though they were one size category larger for a number of rounds equal to the gear die rolled. The wand confers no other advantages or penalties related to size. A rank 7 or higher caster can affect their self AND one more ally',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Repel Undead': {
            'name': 'Wand of Repel Undead',
            'description': '*REQUIRES A HOLY SYMBOL TO CAST* Cause’s one undead enemy to turn and flee or cower, upon successful casting, for every 3 points rolled (minimum of one, maximum of 4), the undead creature(s) will take on the panicked condition and flee from the caster at maximum movement, or, if they cannot flee they will instead take on the cowering condition. Creatures can make a magic save to avoid the effect against DL11, if they succeed, they cannot be affected by that caster for 24 hours, if they fail, they are Panicked or Cowered for a number of rounds equal to the gear die roll. Any attack upon a repelled creature will break the enchantment and the repelled creature(s) may act normally and cannot be repelled by that caster for 24 hours. If there are several types of undead creature’s present, the wand affects those with the lowest rank first. A rank 7 or better caster may cast this wand once per round',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Repulsion': {
            'name': 'Wand of Repulsion',
            'description': 'Allows the caster to erect a wall of force around himself that forces any creature attacking him with a melee attack to roll a magic save against DL11. Failure results in the enemy not being able to attack the caster for a number of rounds equal to the gear die roll',
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
            'description': 'This wand deals damage to would be attackers. If an enemy attacks you with a Warrior Melee attack, you would save as usual, but any damage that you end up taking is immediately returned back upon your attacker as well. The attacker still gets a Magic save at DL11 to avoid this damage. This effect lasts for a number of rounds equal to the gear die rolled. A rank 7 or better caster can affect one other ally per casting',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Rooted': {
            'name': 'Wand of Rooted',
            'description': 'Allows the caster to anchor himself and/or a number of willing creatures to a particular spot. The effect adds a +1 per gear die rolled to any checks against Overrun, Bull Rush or any other effect which may attempt to move the protected creature unwillingly for a number of rounds equal to the gear die roll. This ability does stack with size modifiers and lasts until dismissed by the original caster, the original caster dies/goes unconscious or the effect if dispelled/blocked. Dismissing this wand dismisses on all affected creatures at the same time however. A rank 7 or better caster can choose to dismiss the effect by target instead',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Shrink': {
            'name': 'Wand of Shrink',
            'description': 'Allows the caster to shrink a single target and all gear/items the target is carrying one size category for a number of rounds equal to the gear die roll. A rank 7 caster can shrink a number of creatures equal to the gear die roll. The effect lasts a number of rounds equal to the gear die roll',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Silence': {
            'name': 'Wand of Silence',
            'description': 'Allows the caster to target an area they can see creating a 30x30x10 cube that blocks out all sound. Since wands require sound to be cast all wands cast within this area will fail. The effect lasts for a number of rounds equal to the effect roll. A rank 7 or higher caster can affect a 60x60x20 cube',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Sleep': {
            'name': 'Wand of Sleep',
            'description': 'Causes one enemy to fall asleep and take on the Prone condition, upon successful casting, for every 4 points rolled (minimum of one, maximum of 3). Targets may make a magic save to minimize the effect. Victims cannot take any action for 4 rounds when they are asleep, nor can they be awakened in any non-magical way. Attacking a sleeping creature in any way will break the wand instantly and allow them to react normally on their turn. A rank 7 or better caster can elect to affect a 30x30x10 cube instead. Can be cast once per encounter. SO THAT’S IT (I, O, S) This wand identifies any protective wand or wand like effects currently active on the target. The caster can choose any one effect and cancel it. If the effect is a natural or permanent in nature, the effect is merely suppressed instead for a number of rounds equal to the gear die roll. A rank seven or better caster can cast this once per encounter',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'So That’s It': {
            'name': 'Wand of So That’s It',
            'description': 'This wand identifies any protective wand or wand like effects currently active on the target. The caster can choose any one effect and cancel it. If the effect is a natural or permanent in nature, the effect is merely suppressed instead for a number of rounds equal to the gear die roll. A rank seven or better caster can cast this once per encounter',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Sonic Boom': {
            'name': 'Wand of Sonic Boom',
            'description': 'Causes one target to take on the stunned condition for a number of rounds equal to the gear die roll. A rank 7 or above caster can affect a number of targets equal to the gear die roll',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Spectral Servant': {
            'name': 'Wand of Spectral Servant',
            'description': 'This wand summons a spectral servant under the casters control for a number of rounds equal to the gear die rolled. The servant cannot attack or be attacked. The servant can accomplish mundane tasks that the caster would normally have to do such as fetching items, cleaning, mending, lighting fires, etc. It performs these tasks to the best of its ability. A rank 7 or better caster can cast this wand once per rank per day',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Speed': {
            'name': 'Wand of Speed',
            'description': 'Increases the targets movement speed five feet per gear die rolled for a number of rounds equal to the gear die roll. This wand does stack and/or apply to any form of movement other than land based movement... A rank 7 or higher caster can affect both him/her self AND one ally with a single casting',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Spider Climb': {
            'name': 'Wand of Spider Climb',
            'description': 'The caster gains the ability to crawl up walls and hang from ceilings without falling for a number of rounds equal to the gear die roll. The caster can take no actions except climbing at a walking pace until the wand wears off or is dispelled. This wand lasts a number of rounds equal to the gear die roll. A rank 7 or better caster can affect a number of targets equal to the gear die roll',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Spiritual Helper': {
            'name': 'Wand of Spiritual Helper',
            'description': 'Summons a spiritual creature with the ability to provide certain curative effects. The creature summoned is under the telepathic control of the caster for a number of rounds equal to the gear die roll or until the helper has exhausted all of its abilities whichever is shorter. The helper’s movement is equal to the original caster’s movement. The helper is also the same rank as the original caster. The helper is immune to attack and can only use the effects listed below. The helper may also take a full round action to identify what effect, if any, a creature is under. This check is always successful. The caster can choose any effect at or below the gear die roll. These effects remain available until the wand ends or all effects are used. The helper can cast the following wands at the gear die of the Spiritual Helper wand: 1-2 Healing 3-4 Purify OR Pray for the Dying 5-6 Greater Healing 7-8 Lessen Effect 9-10 Mass Healing 11-12 Healall Each effect may be accomplished once per casting. The wand  A rank 7 or higher caster can use each effect twice up to the gear die roll per casting. No more than one Spiritual Helper may be in existence at a time',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Summon Spiritual Steed': {
            'name': 'Wand of Summon Spiritual Steed',
            'description': 'This wand summons a spirit that takes the form of a large horse. This steed is intelligent and loyal to the caster. The caster has a telepathic link with the steed as long as the steed is within one mile of the caster. The steed is a non-combatant, but may serve other roles such as a scout or on a watch/guard duty. The steed can only exist outdoors and will remain until dismissed by the original caster, 24 hours have passed, is dispelled, or the caster goes out of range. The steed may be dismissed as a free action. Once dismissed, the wand cannot be cast by that caster again for one day. Only one steed per caster may be summoned at any time',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Summon Swarm': {
            'name': 'Wand of Summon Swarm',
            'description': 'The caster summons a swarm of vermin which will fight a single, chosen foe that the caster can see for a number of rounds equal to the effect roll causing 1 point of damage per round (no save) and causing any creature who is swarmed to incur the Shaken condition for a number of rounds equal to the gear die roll. The creatures that make up the swarm can not cause any other effects than the damage and shaken condition. As a move action, the caster can elect to do ongoing damage each round or if the caster elects not to use the wand to cause ongoing damage in a given round, they can instead make a Magic aspect check as a free action to maintain the wand with a difficulty level of 7. If the affected creature dies, the original caster can redirect the swarm at any single target they can see using their standard attack action for whatever rounds remain from the original casting though the new target(s) get a save vs. the effect. Moving the swarm is always successful. A rank 7 or higher caster can affect two creatures per casting. The creatures’ summoned is equal to the gear die roll per the chart below.  1-2. Ants, Bats, Crabs 5-6. Centipedes, Locusts, Octopi9-10. Snakes, Wasps, Kuo-ToA 11-12. Spiders, Flies, Lizardfolk 3-4. Beetles, Bees, Crocodiles 7-8. Rats, Ravens, Sharks',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Sustenance': {
            'name': 'Wand of Sustenance',
            'description': 'This wand allows the caster to create one day’s worth of rations and water for one person per gear die rolled. A rank 7 or higher caster can create one day’s worth of rations and water for a number of persons equal to the gear die rolled.  Take That (I, S) This wand allows the caster to possibly redirect the wand energy of any wand cast at them. The effect lasts until the end of the casters next turn. The caster can choose any ability at or below the gear die roll to manifest. The resulting effect must be used by the end of the casters next turn.  A rank 7 or above caster can cast this wand once per encounter on himself and the effect lasts for a number of rounds equal to one half the gear die rolled (rounded up). The following effects are possible: 1-4 Wand Deflection – Any wand cast at the caster deflects in a random direction (possibly hitting an ally). If this effect is used, the energy is redirected as follows: 1: Forward 2. Left 3. Right 4. Backward. The energy will continue on that path until it hits a target(s) or a wall or other object. 4-8 Wand Reflection – Any wand cast at the caster is immediately reflected back at the original caster who may then make a Magic save accordingly to avoid its effects with a -2 penalty to the Magic save. 9-12 Wand Absorption – Any wand cast at the caster is absorbed by the target and its energy can be used to allow the recipient of this extra wand energy to cast an extra wand on their next turn at the same gear die as the wand that was originally absorbed. This wand energy must be used by the end of the recipients next turn or it is forever lost',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Telekinesis': {
            'name': 'Wand of Telekinesis',
            'description': 'Allows the caster to move one small object up to about 10lbs in weight about at a rate of 5 feet per round. These objects cannot be used as weapons. This wand lasts a number of rounds equal to the effect roll. A rank 7 or better caster can move a number of objects equal to the gear die roll',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Teleport': {
            'name': 'Wand of Teleport',
            'description': 'Allows the caster to transport themselves or others from one spot to another over a short distance equal to 100 yards per rank of the caster. The caster must be able to see or visualize (have been there before) the place being teleported to. The caster may also teleport one additional willing person with him at the cost of 4 points rolled per person (minimum the caster only, maximum caster + 3). A rank 7 or better caster can teleport a number of willing creatures equal to the gear die roll. Unconscious creatures may also be teleported via this wand. Can be cast once per encounter . This wand introduces the sickened condition upon its target(s). You pick one creature and if affected, the target takes on the Sickened condition for a number of rounds equal to the gear die rolled. A rank 7 or better caster can affect a number of targets equal to the gear die rolled.  That Hurts (I) This wand allows the recipient to increase the threat range on their or one allies Aspect Checks to achieve critical hits. This wand grants a +1 bonus to any Aspect Check to hit with a weapon and on a natural 11 or better, the hit will result in a critical hit. The effect lasts a number of rounds equal to the gear die rolled. A rank 7 or better caster can also allow the target to achieve critical castings on wands that the target casts instead of just melee damage. This wand can be cast once per day per target',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'That Hurts': {
            'name': 'Wand of That Hurts',
            'description': 'This wand allows the recipient to increase the threat range on their or one allies Aspect Checks to achieve critical hits. This wand grants a +1 bonus to any Aspect Check to hit with a weapon and on a natural 11 or better, the hit will result in a critical hit. The effect lasts a number of rounds equal to the gear die rolled. A rank 7 or better caster can also allow the target to achieve critical castings on wands that the target casts instead of just melee damage. This wand can be cast once per day per target',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'That’s Nasty': {
            'name': 'Wand of That’s Nasty',
            'description': 'This wand introduces the sickened condition upon its target(s). You pick one creature and if affected, the target takes on the Sickened condition for a number of rounds equal to the gear die rolled. A rank 7 or better caster can affect a number of targets equal to the gear die rolled.',
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
            'description': 'Creates a large wall of ice equal to one 20x10x5 cube plus an additional 5 foot in length per caster rank, the wall lasts a number of rounds equal to the gear die roll and has a number of hit points equal to the caster. The wall can only be conjured in unoccupied squares. A rank 7 or better caster adds an additional 10 feet to the wall’s height. To break down the wall, it must take damage equal to its HP or more. The wall has HP equal to the original caster, has no armor value and takes ½ damage from all wands',
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
            'description': 'etc.) Creates a layered mass of strong, sticky strands. These masses must be anchored to two or more solid and diametrically opposed points or else the web collapses upon itself and disappears. Creatures caught within a web become stuck (including allies). Attacking a creature in a web won’t cause you to become entangled. Anyone in the effect’s area when the wand is cast must make a Magic save. If this save fails, the target(s) take on the Entangled condition. An Entangled creature may take a full round action to break free from the Web on their turn by making a Magic save of 17 or better, failure results in remaining stuck until their next turn. The caster must take a standard/attack action to maintain the wand on his/her turn; otherwise the webs dissipate at the end of the casters turn. This wand may be cast once per day. What the Heck Was That (I, S) This wand allows the recipient to make a single Warrior Melee attack against all creatures that the recipient can see equal to the gear die of the wand regardless of how far away the target(s) are. The recipient will make one Warrior Melee attack roll and apply that to all targets they are attempting to hit, so this wand is all or nothing. The recipient of this wand moves at blinding speed during the round this wand is in effect and ends their turn in the original square they started in after the effect ends. The effect must be used by the end of the recipients next turn after casting or it is simply lost. A rank 7 or better caster can affect two allies per casting',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'What the Heck Was That': {
            'name': 'Wand of What the Heck Was That',
            'description': 'This wand allows the recipient to make a single Warrior Melee attack against all creatures that the recipient can see equal to the gear die of the wand regardless of how far away the target(s) are. The recipient will make one Warrior Melee attack roll and apply that to all targets they are attempting to hit, so this wand is all or nothing. The recipient of this wand moves at blinding speed during the round this wand is in effect and ends their turn in the original square they started in after the effect ends. The effect must be used by the end of the recipients next turn after casting or it is simply lost. A rank 7 or better caster can affect two allies per casting.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Whisper in the Wind': {
            'name': 'Wand of Whisper in the Wind',
            'description': 'This wand allows the caster to choose any one ally within line of sight and communicate a message in a whispery voice that only the target can hear. The target can reply as well and the response will also be in a whispery voice that only the caster can hear. This effect lasts for a number of rounds equal to the gear die rolled. A rank 7 or better caster can speak to a number of targets equal to the gear die rolled',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Wondrous Effect': {
            'name': 'Wand of Wondrous Effect',
            'description': 'Functions asper the wand of the same name.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'You’re Welcome': {
            'name': 'Wand of You’re Welcome',
            'description': 'Allows the caster to take ½ of the allies\' damage for a number of rounds equal to the gear die roll. A rank 7 or higher caster can elect to take all damage instead. The caster can also elect to not take the damage in any given round though not taking the damage does not extend the length of the spell.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'You’re Not So Tough': {
            'name': 'Wand of You’re Not So Tough',
            'description': 'This wand allows the caster to grant themselves or one ally the ability to do extra damage to targets larger than them. For each size category above the size of the wands target that the creature is, the wand recipient adds +2 to the damage for each successful Warrior Melee attack against that target that they make. The effect lasts a number of rounds equal to the gear die rolled. A rank 7 or better caster adds +4 to the damage roll instead.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'You’re Special': {
            'name': 'Wand of You’re Special',
            'description': 'This wand allows the caster to select any special ability from their Aspect that they initially put their D12 aspect die into and use that ability for a number of rounds equal to the gear die rolled. A rank 7 or better caster can instead choose any special ability from any list and use it for a number of rounds equal to the gear die rolled.',
            'type': 'wand',
            'charges': 7,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
    },

    'potions': {
        'Acid Rain': {
            'name': 'Potion of Acid Rain',
            'description': 'This one- time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Alarm': {
            'name': 'Potion of Alarm',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'All’s Clear': {
            'name': 'Potion of All’s Clear',
            'description': 'This one- time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Analyze': {
            'name': 'Potion of Analyze',
            'description': 'This one- time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Animate Object': {
            'name': 'Potion of Animate Object',
            'description': 'This one- time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Blindness': {
            'name': 'Potion of Blindness',
            'description': 'This one- time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Buried Alive': {
            'name': 'Potion of Buried Alive',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Burrow': {
            'name': 'Potion of Burrow',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Chain Lightning': {
            'name': 'Potion of Chain Lightning',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Charm Monster/Person': {
            'name': 'Potion of Charm Monster/Person',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
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
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Comfort': {
            'name': 'Potion of Comfort',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Common Knowledge': {
            'name': 'Potion of Common Knowledge',
            'description': 'This one- time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Create Portal': {
            'name': 'Potion of Create Portal',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Dazzle': {
            'name': 'Potion of Dazzle',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Deafness': {
            'name': 'Potion of Deafness',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Death': {
            'name': 'Potion of Death',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Disadvantaged': {
            'name': 'Potion of Disadvantaged',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Displacement': {
            'name': 'Potion of Displacement',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Dragon Breath': {
            'name': 'Potion of Dragon Breath',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
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
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Enlarge': {
            'name': 'Potion of Enlarge',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Enrage': {
            'name': 'Potion of Enrage',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Exhaustion': {
            'name': 'Potion of Exhaustion',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Eye See You': {
            'name': 'Potion of Eye See You',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Fearful Presence': {
            'name': 'Potion of Fearful Presence',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
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
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Fly': {
            'name': 'Potion of Fly',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Forget': {
            'name': 'Potion of Forget',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
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
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Gotta Have It': {
            'name': 'Potion of Gotta Have It',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Grease': {
            'name': 'Potion of Grease',
            'description': 'This one-time use item when applied to a surface functions as per the potion of the same name.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Greater Healing': {
            'name': 'Potion of Greater Healing',
            'description': 'This one- time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Greater Mass Healing': {
            'name': 'Potion of Greater Mass Healing',
            'description': 'This one- time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Hail Storm': {
            'name': 'Potion of Hail Storm',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Haste': {
            'name': 'Potion of Haste',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'HealAll': {
            'name': 'Potion of HealAll',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Healing': {
            'name': 'Potion of Healing',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Heroism': {
            'name': 'Potion of Heroism',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Icy Blast': {
            'name': 'Potion of Icy Blast',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Illusion': {
            'name': 'Potion of Illusion',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Immobilize': {
            'name': 'Potion of Immobilize',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Incorporeal': {
            'name': 'Potion of Incorporeal',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Inspire': {
            'name': 'Potion of Inspire',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Instant Search': {
            'name': 'Potion of Instant Search',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Invisibility': {
            'name': 'Potion of Invisibility',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Lessen Effect': {
            'name': 'Potion of Lessen Effect',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Levitate': {
            'name': 'Potion of Levitate',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Luck': {
            'name': 'Potion of Luck',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Luck of the Irish': {
            'name': 'Potion of Luck of the Irish',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magic Missile': {
            'name': 'Potion of Magic Missile',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magic Shield': {
            'name': 'Potion of Magic Shield',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magical Darkness': {
            'name': 'Potion of Magical Darkness',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magical Sight': {
            'name': 'Potion of Magical Sight',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Mass Healing': {
            'name': 'Potion of Mass Healing',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Metamagic': {
            'name': 'Potion of Metamagic',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Mirror Image': {
            'name': 'Potion of Mirror Image',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'More is Always Better': {
            'name': 'Potion of More is Always Better',
            'description': 'This one- time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Mutable Form': {
            'name': 'Potion of Mutable Form',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Natures Step': {
            'name': 'Potion of Natures Step',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Night Vision': {
            'name': 'Potion of Night Vision',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Obscure Life Force': {
            'name': 'Potion of Obscure Life Force',
            'description': 'This one- time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Odorless': {
            'name': 'Potion of Odorless',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Open': {
            'name': 'Potion of Open',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Paralyzing Ray': {
            'name': 'Potion of Paralyzing Ray',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Pardon Me': {
            'name': 'Potion of Pardon Me',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Phantom Weapon': {
            'name': 'Potion of Phantom Weapon',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Polymorph Self': {
            'name': 'Potion of Polymorph Self',
            'description': 'This one- time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Pray for the Dying': {
            'name': 'Potion of Pray for the Dying',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Purify': {
            'name': 'Potion of Purify',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Purify Area': {
            'name': 'Potion of Purify Area',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Racial Modification': {
            'name': 'Potion of Racial Modification',
            'description': 'This cursed one time use item detects as a Potion of Luck and functions as such, but also changes the imbiber’s race roll 1d6 to determine 1. Human 2. Elf 3. Halfling 4. Dwarf 5. Half-Giant 6. PC Choice unless the curse is detected with an Analyze potion check of 10 or higher.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Reach Out': {
            'name': 'Potion of Reach Out',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Repel Undead': {
            'name': 'Potion of Repel Undead',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Repulsion': {
            'name': 'Potion of Repulsion',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
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
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Rooted': {
            'name': 'Potion of Rooted',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Shrink': {
            'name': 'Potion of Shrink',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Silence': {
            'name': 'Potion of Silence',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Sleep': {
            'name': 'Potion of Sleep',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber. Potion of So That’s It: This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Sonic Boom': {
            'name': 'Potion of Sonic Boom',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Spectral Servant': {
            'name': 'Potion of Spectral Servant',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Speed': {
            'name': 'Potion of Speed',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Spider Climb': {
            'name': 'Potion of Spider Climb',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Spiritual Helper': {
            'name': 'Potion of Spiritual Helper',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Summon Spiritual Steed': {
            'name': 'Potion of Summon Spiritual Steed',
            'description': 'This one- time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Summon Swarm': {
            'name': 'Potion of Summon Swarm',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Sustenance': {
            'name': 'Potion of Sustenance',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Take That': {
            'name': 'Potion of Take That',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Telekinesis': {
            'name': 'Potion of Telekinesis',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Teleport': {
            'name': 'Potion of Teleport',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'That Hurts': {
            'name': 'Potion of That Hurts',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber. Potion of That’s Nasty: This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'The Forecast Calls For': {
            'name': 'Potion of The Forecast Calls For',
            'description': 'This one- time use item functions as per the potion of the same name and only affects the imbiber.',
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
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
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
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'What the Heck Was That': {
            'name': 'Potion of What the Heck Was That',
            'description': 'This one- time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Whisper in the Wind': {
            'name': 'Potion of Whisper in the Wind',
            'description': 'This one- time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Wondrous Effect': {
            'name': 'Potion of Wondrous Effect',
            'description': 'This one-time use item functions as per the potion of the same name and only affects the imbiber. Potion of You’re Welcome: This one- time use item functions as per the potion of the same name and only affects the imbiber. Potion of You’re Not So Tough: This one-time use item functions as per the potion of the same name and only affects the imbiber. Potion of You’re Special: This one-time use item functions as per the potion of the same name and only affects the imbiber.',
            'type': 'potion',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
    },

    'scrolls': {
        'Acid Rain': {
            'name': 'Scroll of Acid Rain',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Alarm': {
            'name': 'Scroll of Alarm',
            'description': 'This one-time use item functions as per the scroll of the same name.',
        },
        'All’s Clear': {
            'name': 'Scroll of All’s Clear',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Analyze': {
            'name': 'Scroll of Analyze',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Animate Object': {
            'name': 'Scroll of Animate Object',
            'description': 'This one- time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Blindness': {
            'name': 'Scroll of Blindness',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Buried Alive': {
            'name': 'Scroll of Buried Alive',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Burrow': {
            'name': 'Scroll of Burrow',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Chain Lightning': {
            'name': 'Scroll of Chain Lightning',
            'description': 'This one- time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Charm Monster/Person': {
            'name': 'Scroll of Charm Monster/Person',
            'description': 'This one-time use item functions as per the scroll of the same name.',
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
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Comfort': {
            'name': 'Scroll of Comfort',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Common Knowledge': {
            'name': 'Scroll of Common Knowledge',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Create Portal': {
            'name': 'Scroll of Create Portal',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Dazzle': {
            'name': 'Scroll of Dazzle',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Deafness': {
            'name': 'Scroll of Deafness',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Death': {
            'name': 'Scroll of Death',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Disadvantaged': {
            'name': 'Scroll of Disadvantaged',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Displacement': {
            'name': 'Scroll of Displacement',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Dragon Breath': {
            'name': 'Scroll of Dragon Breath',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Drain Protection': {
            'name': 'Scroll of Drain Protection',
            'description': 'This one-time use item allows the reader to ignore any one drain attack and instead take 1d6 damage. This damage ignores armor or shield bonuses.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Dude You’re Stoned': {
            'name': 'Scroll of Dude You’re Stoned',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Enhancement': {
            'name': 'Scroll of Enhancement',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Enlarge': {
            'name': 'Scroll of Enlarge',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Enrage': {
            'name': 'Scroll of Enrage',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Entangle': {
            'name': 'Scroll of Entangle',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Exhaustion': {
            'name': 'Scroll of Exhaustion',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Eye See You': {
            'name': 'Scroll of Eye See You',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Fearful Presence': {
            'name': 'Scroll of Fearful Presence',
            'description': 'This one- time use item functions as per the scroll of the same name.',
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
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Fly': {
            'name': 'Scroll of Fly',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Forget': {
            'name': 'Scroll of Forget',
            'description': 'This one-time use item functions as per the scroll of the same name.',
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
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Gotta Have It': {
            'name': 'Scroll of Gotta Have It',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Grease': {
            'name': 'Scroll of Grease',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Greater Healing': {
            'name': 'Scroll of Greater Healing',
            'description': 'This one- time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Greater Mass Healing': {
            'name': 'Scroll of Greater Mass Healing',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Hail Storm': {
            'name': 'Scroll of Hail Storm',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Haste': {
            'name': 'Scroll of Haste',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'HealAll': {
            'name': 'Scroll of HealAll',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Healing': {
            'name': 'Scroll of Healing',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Heroism': {
            'name': 'Scroll of Heroism',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Icy Blast': {
            'name': 'Scroll of Icy Blast',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Illusion': {
            'name': 'Scroll of Illusion',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Immobilize': {
            'name': 'Scroll of Immobilize',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Incorporeal': {
            'name': 'Scroll of Incorporeal',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Inspire': {
            'name': 'Scroll of Inspire',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Instant Search': {
            'name': 'Scroll of Instant Search',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Invisibility': {
            'name': 'Scroll of Invisibility',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Lessen Effect': {
            'name': 'Scroll of Lessen Effect',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Levitate': {
            'name': 'Scroll of Levitate',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Lightning': {
            'name': 'Scroll of Lightning',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Locked': {
            'name': 'Scroll of Locked',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Luck': {
            'name': 'Scroll of Luck',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Luck of the Irish': {
            'name': 'Scroll of Luck of the Irish',
            'description': 'This one- time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magic Missile': {
            'name': 'Scroll of Magic Missile',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magic Shield': {
            'name': 'Scroll of Magic Shield',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magical Darkness': {
            'name': 'Scroll of Magical Darkness',
            'description': 'This one- time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magical Light': {
            'name': 'Scroll of Magical Light',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Magical Sight': {
            'name': 'Scroll of Magical Sight',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Mass Healing': {
            'name': 'Scroll of Mass Healing',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Metamagic': {
            'name': 'Scroll of Metamagic',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Mirror Image': {
            'name': 'Scroll of Mirror Image',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'More is Always Better': {
            'name': 'Scroll of More is Always Better',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Mutable Form': {
            'name': 'Scroll of Mutable Form',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Natures Step': {
            'name': 'Scroll of Natures Step',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Night Vision': {
            'name': 'Scroll of Night Vision',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Obscure Life Force': {
            'name': 'Scroll of Obscure Life Force',
            'description': 'This one- time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Odorless': {
            'name': 'Scroll of Odorless',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Open': {
            'name': 'Scroll of Open',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Paralyzing Ray': {
            'name': 'Scroll of Paralyzing Ray',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Pardon Me': {
            'name': 'Scroll of Pardon Me',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Phantom Weapon': {
            'name': 'Scroll of Phantom Weapon',
            'description': 'This one- time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Polymorph Self': {
            'name': 'Scroll of Polymorph Self',
            'description': 'This one- time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Pray for the Dying': {
            'name': 'Scroll of Pray for the Dying',
            'description': 'This one- time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Purify': {
            'name': 'Scroll of Purify',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Purify Area': {
            'name': 'Scroll of Purify Area',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Racial Modification': {
            'name': 'Scroll of Racial Modification',
            'description': 'This cursed one time use item detects as a Scroll of Luck and functions as such, but also modifies the reader’s race as follows; roll 1d8 to determine: 1. Human 2. Elf 3. Halfling 4. Dwarf 5. Half-Giant 6. Half-Elf 7. Galdur 8. PC Choice unless the curse is detected with an Analyze scroll check of 10 or higher.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Reach Out': {
            'name': 'Scroll of Reach Out',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Repel Undead': {
            'name': 'Scroll of Repel Undead',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Repulsion': {
            'name': 'Scroll of Repulsion',
            'description': 'This one-time use item functions as per the scroll of the same name.',
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
            'description': 'This one- time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Rooted': {
            'name': 'Scroll of Rooted',
            'description': 'This one-time use item functions as per the scroll of the same name.',
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
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'So That’s It': {
            'name': 'Scroll of So That’s It',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Sonic Boom': {
            'name': 'Scroll of Sonic Boom',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Spectral Servant': {
            'name': 'Scroll of Spectral Servant',
            'description': 'This one- time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Speed': {
            'name': 'Scroll of Speed',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Spider Climb': {
            'name': 'Scroll of Spider Climb',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Spiritual Helper': {
            'name': 'Scroll of Spiritual Helper',
            'description': 'This one- time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Summon Spiritual Steed': {
            'name': 'Scroll of Summon Spiritual Steed',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Summon Swarm': {
            'name': 'Scroll of Summon Swarm',
            'description': 'This one- time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Sustenance': {
            'name': 'Scroll of Sustenance',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Take That': {
            'name': 'Scroll of Take That',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Telekinesis': {
            'name': 'Scroll of Telekinesis',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Teleport': {
            'name': 'Scroll of Teleport',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'That Hurts': {
            'name': 'Scroll of That Hurts',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'That’s Nasty': {
            'name': 'Scroll of That’s Nasty',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'The Forecast Calls For': {
            'name': 'Scroll of The Forecast Calls For',
            'description': 'This one-time use item functions as per the scroll of the same name.',
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
            'description': 'This one-time use item functions as per the scroll of the same name.',
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
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'What the Heck Was That': {
            'name': 'Scroll of What the Heck Was That',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Whisper in the Wind': {
            'name': 'Scroll of Whisper in the Wind',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Wondrous Effect': {
            'name': 'Scroll of Wondrous Effect',
            'description': 'This one- time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'You’re Welcome': {
            'name': 'Scroll of You’re Welcome',
            'description': 'This one- time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'You’re Not So Tough': {
            'name': 'Scroll of You’re Not So Tough',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'You’re Special': {
            'name': 'Scroll of You’re Special',
            'description': 'This one-time use item functions as per the scroll of the same name.',
            'type': 'scroll',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
    },

    'staves': {
        'Cure All': {
            'name': 'Staff of Cure All',
            'description': 'This item will cure any ill effect the target is suffering from to include HP damage, lost limbs, lost digits, curses, diseases, or any other malady afflicting the target other than death.',
            'type': 'staff',
            'charges': 3,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'Curing': {
            'name': 'Staff of Curing',
            'description': 'This item can be used to cure damage to the injured. One charge casts a Healing staff, two charges casts a Greater Healing staff, and three charges casts a Mass Healing staff.',
            'type': 'staff',
            'charges': 3,
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
        },
        'the Mimic': {
            'name': 'Staff of the Mimic',
            'description': 'This item allows the wielder to assume the look of any non-living object. It is usable 3 times per day. The item will recharge itself every day at dawn.',
            'type': 'staff',
            'charges': 3,
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
            'description': 'This permanent use item allows the wearer to be immune to all harmful spells and spell like effects permanently as long as it is worn.',
            'type': 'ring'
        },
        'Spell Storing': {
            'name': 'Ring of Spell Storing',
            'description': 'This permanent use magic item can store any one spell at the assigned gear die. It will function as the spell would normally but does not take up a gear die slot. This ring can be used once per encounter.',
            'type': 'ring',
            'variants': ['d4', 'd6', 'd8', 'd10', 'd12']
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
            'description': 'This one-time use item when applied to any weapon will allow the wearer to do an extra die of damage with each attack up to a D12. This bonus stacks with crits and all other magic items or abilities related to crits.',
            'type': 'oil'
        },
        'Magic Shield -1': {
            'name': 'Oil of Magic Shield -1',
            'description': 'This cursed item will detect as Oil of Magic Shield +1, however, when applied to a shield of any type will cause the shield to crumble to dust when hit unless the curse is detected with an Analyze spell check of 10 or higher.',
            'type': 'oil'
        },
        'Magic Shield +1': {
            'name': 'Oil of Magic Shield +1',
            'description': 'This one-time use item permanently increases the protection of one shield. When attacked, the attacker rolls three damage rolls and takes the least of the three.',
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
