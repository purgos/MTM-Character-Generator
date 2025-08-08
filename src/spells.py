# MTM V7.0 Spell Cards - Python Dictionary Format

SPELLS = {'ACID RAIN': {'area_of_effect': 'One or more connected 5-foot squares.',
               'description': 'Allows the caster to conjure up an acidic rain that fills a single 5-foot square per '
                              'caster rank. All affected squares must be connected. The acid causes its gear die in '
                              'damage to any creatures in the affected squares. Any non-magical armor in the affected '
                              'squares are destroyed unless the item makes an armor save versus a DL11',
               'duration': '1 caster turn',
               'frequency': 'This spell can be cast once per encounter.',
               'prerequisite': 'Magic Aspect D8',
               'spell_components': ['E', 'I', 'O', 'S']},
 'ALARM': {'area_of_effect': '30’ Radius',
           'description': 'You set an alarm against unwanted intrusion. Choose a door, a window, or an area within '
                          'range that is no larger than a 20-foot cube. Until the spell ends, an alarm alerts you '
                          'whenever a Tiny or larger creature touches or enters the warded area. When you cast the '
                          "spell, you can designate creatures that won't set off the alarm. You also choose whether "
                          'the alarm is mental or audible. A mental alarm alerts you with a ping in your mind if you '
                          'are within 1 mile of the warded area. This ping awakens you if you are sleeping. An audible '
                          'alarm produces the sound of a hand bell for 10 seconds within 60 feet. This spell lasts 24 '
                          'hours or until dispelled',
           'duration': 'Persistent',
           'frequency': 'This spell can be cast once per day.',
           'prerequisite': 'Magic Aspect D6',
           'spell_components': ['O', 'S']},
 'ALLS CLEAR': {'area_of_effect': 'The Caster’s Square(s)',
                'description': 'Allows the caster to remove any non-magical impediments in their square(s). This would '
                               'include such items as pitons, ball bearings, spores from a creature, dust, dirt, etc. '
                               'All items this spell can remove are subject to GM approval. This spell lasts a number '
                               'of rounds equal to the gear die rolled',
                'duration': 'Persistent',
                'frequency': 'This spell can be cast once per encounter.',
                'prerequisite': 'Magic Aspect D6',
                'spell_components': ['I', 'S']},
 
 'ANALYZE': {'area_of_effect': 'One Item',
             'description': 'Allows a check to detect if one item is magical. The GM always makes this roll for the '
                            'character. The caster must touch the item and spend one hour studying and using it. '
                            'Scrolls can always be identified with a successful visual check without reading the '
                            'scroll contents out loud; however, potions require the caster to taste a small sample of '
                            'the liquid to identify it and any items require the caster to use/touch the item thus '
                            'meaning that if it produces a baneful effect, the character is subject to the baneful '
                            'effect. A 4 or better is needed to determine if it is magical and a 7 or better is needed '
                            'to determine exactly what it does. If the item is cursed, it will detect as a similar '
                            'beneficial magic item, but cause a baneful effect if applicable. This curse can be '
                            'identified only if the caster check is 10 or greater. This spell can be cast one time on '
                            'each item per week. If the check fails, that caster cannot further identify that item '
                            'until one week has passed. A rank 7 or better caster can attempt to re-analyze an item '
                            'once per day in the event of failure. Note: This spell is always cast “successfully” '
                            'since it is done outside of combat exclusively',
             'duration': '1 Hour',
             'frequency': 'This spell can be cast once per day.',
             'material_component': '50GP Pearl',
             'prerequisite': 'Magic Aspect D12',
             'spell_components': ['O', 'MC']},
 'ANIMATE OBJECT': {'area_of_effect': 'The Casters Line of Vision',
                    'description': 'Allows the caster to animate one unoccupied object up to 10 pounds per rank and '
                                   'not classified as a weapon for a number of rounds equal to the gear die roll and '
                                   'attack with it as if it were an improvised weapon doing a D4 in damage each round '
                                   'to a single target. The animated object may not be used for defense such as '
                                   'Animating a shield and may not exceed a total weight of 50 pounds. A rank 7 caster '
                                   'can animate a number of unoccupied objects equal to the gear die roll each '
                                   'attacking a separate target. The caster must use an attack action each round or a '
                                   'move action to maintain the spell, otherwise it ends at the end of the original '
                                   'casters turn',
                    'duration': 'Persistent',
                    'frequency': 'This spell can be cast once per encounter.',
                    'prerequisite': 'Magic Aspect D8',
                    'spell_components': ['I', 'O', 'S']},
 'BLINDNESS': {'area_of_effect': 'A Single or Multiple Creatures',
               'description': 'Causes one target to lose all sight and take on the blinded condition for a number of '
                              'rounds equal to the gear die roll. A rank 7 caster can affect a number of targets equal '
                              'to the gear die roll.',
               'duration': 'Persistent',
               'frequency': 'This spell can be cast once per encounter.',
               'prerequisite': 'Magic Aspect D8',
               'spell_components': ['I', 'O', 'S']},
 'BURIED ALIVE': {'area_of_effect': 'The Casters Line of Vision',
                  'description': 'This spell causes the affected area to fill with boulders causing its gear die in '
                                 'damage to any targets in the area of effect. The effect lasts a number of rounds '
                                 'equal to the gear die roll. Creatures can make a Magic save vs. DL11 or better to '
                                 'avoid being buried in the rubble. Huge or larger size creatures gain a +2 bonus to '
                                 'the magic save per size category above Large that they are. Buried creatures can '
                                 'take no actions though they may be dug out by others in 1d4 rounds. Buried creatures '
                                 'do not take ongoing damage, however, they are subject to the Drowning rules/effects '
                                 'while buried under the rubble. A rank 7 or better caster can fill a 20x20x20 area.',
                  'duration': 'Persistent',
                  'frequency': 'This spell can be cast once per day.',
                  'prerequisite': 'Magic Aspect D8',
                  'spell_components': ['I']},
 'BURROW': {'area_of_effect': 'The Caster',
            'description': 'Caster grows claws and gains a burrowing speed of 15’ per round for a number of rounds '
                           'equal to the gear die roll. A rank 7 or higher caster can burrow at a speed of 30’ per '
                           'round. The claws cannot be used as a weapon nor can the caster move through or into other '
                           'creatures. A roll of 10 or better is needed to burrow through stone. You cannot burrow '
                           'through metal with this spell. This spell cannot be used in conjunction with Displacement '
                           'or Mirror Image',
            'duration': 'Persistent',
            'frequency': 'This spell can be cast once per encounter.',
            'prerequisite': 'Magic Aspect D10',
            'spell_components': ['I', 'S']},
 'CHAIN LIGHTNING': {'area_of_effect': '2-14 Creatures',
                     'description': 'Unleashes a bolt of electricity that arcs from one target to another affecting 2 '
                                    'targets at minimum plus an additional target per gear die rolled causing its gear '
                                    'die in damage to all affected creatures. A rank 7 or better caster can affect an '
                                    'additional target per rank.',
                     'duration': 'Instantaneous',
                     'frequency': 'This spell can be cast every other round.',
                     'prerequisite': 'Magic Aspect D10',
                     'spell_components': ['E*', 'I', 'O']},
 'CHARM MONSTER/PERSON': {'area_of_effect': 'The Casters Line of Vision',
                          'description': 'This spell allows the caster to compel the target to do their bidding. The target will not '
                                         'bring harm to themselves but will obey any other verbal commands given to them for a number of '
                                         'rounds equal to the gear die rolled. All targets get a Magic save at the beginning of the '
                                         'original casters round to break the Charm effect with a DL of 11. The caster must remain within '
                                         'visual range of any targets and use a full round action to maintain the Charm. A rank 7 or '
                                         'higher caster can affect a number of targets equal to the gear die rolled and may use a Move '
                                         'Action to maintain the spell instead.',
                          'duration': 'Persistent',
                          'frequency': 'This spell can be cast once per day.',
                          'prerequisite': 'Magic Aspect D8',
                          'spell_components': ['I', 'S']},
 'COME TO ME': {'area_of_effect': 'A Single or Multiple Creatures',
                'description': 'Allows the caster to shout taunting insults to a number of creatures equal to the gear '
                               'die roll. The caster may choose to target less creatures than the gear die roll. '
                               'Targets must make a magic save against base DC11. Affected creature(s) will attack the '
                               'caster only, ignoring all other creatures for a number of rounds equal to the gear die '
                               'roll. If an affected creature cannot attack the caster either by melee, ranged, or '
                               'spell attack; they would simply do nothing that round. If an affected character cannot '
                               'attack on 2 nd and subsequent rounds, affected creatures would get another magic save '
                               'as a free action against DC11 for each subsequent round that the original caster '
                               'cannot be targeted',
                'duration': 'Non-Persistent',
                'frequency': 'This spell can be cast once per encounter.',
                'prerequisite': 'Magic Aspect D8',
                'spell_components': ['I', 'S']},
 'COMFORT': {'area_of_effect': 'The Caster',
             'description': 'This spell allows the caster to suffer no ill effects from natural extreme heat or cold '
                            'for a period of 1 hour per gear die rolled. A rank 7 or greater caster can affect a '
                            'number of targets equal to the gear die rolled',
             'duration': '1 Hour',
             'frequency': 'This spell can be cast once per day.',
             'prerequisite': 'Magic Aspect D6',
             'spell_components': ['O', 'S']},
 'COMMON KNOWLEDGE': {'area_of_effect': 'The Caster',
                      'description': 'This spell improves the caster’s’ Gather Information check(s). Upon casting this '
                                     'spell, the caster may add +1 to their Gather Information skill check(s) per gear '
                                     'die rolled. A rank 7 or greater caster can cast this spell twice per day',
                      'duration': '1 Hour',
                      'frequency': 'This spell can be cast once per day.',
                      'prerequisite': 'Magic Aspect D6',
                      'spell_components': ['O', 'S']},
 'CREATE PORTAL': {'area_of_effect': 'See Below',
                   'description': 'Allows the caster to lay their hands on a 5x5x10 section of wall or a door and '
                                  'create a hole large enough to allow 1 medium sized being to pass through per round '
                                  'or allows one projectile or spell to pass through per round. A rank 7 or better '
                                  'caster can create a 10x10x20 opening and allow 2 medium creatures or 1 large '
                                  'creature through per round or two projectiles or two spells through per round. The '
                                  'spell lasts for a number of rounds equal to the gear die roll',
                   'duration': 'Persistent',
                   'frequency': 'This spell can be cast once per day.',
                   'prerequisite': 'Magic Aspect D8',
                   'spell_components': ['I', 'O']},
 'DAZZLE': {'area_of_effect': 'A Single or Multiple Creatures',
            'description': 'Causes one man-sized enemy to hesitate for a number of rounds equal to the gear die roll. '
                           'Victims take on the Dazed condition. Dazzled creatures can’t become undazzled unless '
                           'attacked successfully with a melee or ranged weapon, a spell, (both doing full damage with '
                           'no saves or armor bonuses) or a lessen effect spell. A rank 7 or better caster can affect '
                           'a number of creatures equal to the gear die roll',
            'duration': 'Persistent',
            'frequency': 'This spell can be cast once per encounter per target.',
            'prerequisite': 'Magic Aspect D10',
            'spell_components': ['I', 'S']},
 'DEAFNESS': {'area_of_effect': 'A Single or Multiple Creatures',
              'description': 'Causes one target to lose all hearing and take on the deafened condition for a number of '
                             'rounds equal to the gear die roll. A rank 7 caster can affect a number of targets equal '
                             'to the gear die roll',
              'duration': 'Persistent',
              'frequency': 'This spell can be cast once per encounter.',
              'prerequisite': 'Magic Aspect D8',
              'spell_components': ['I', 'O', 'S']},
 'DEATH': {'area_of_effect': 'One Creature',
           'description': 'Below Allows the caster to select one living target and attempt to steal its life force. '
                          'The target immediately makes a death save with a + or – one per rank difference between the '
                          'caster and the target. Failure results in immediate death. A partial success means the '
                          'target takes the casters gear die multiplied by the casters rank in damage divided by 2 '
                          'while a moderate success results in the target taking one half its current hit point total '
                          'in damage while a total save results in the target instead taking on the sickened condition '
                          'for a number of rounds equal to the casters gear die. This spell also causes the caster to '
                          'take on the exhausted condition for a number of rounds equal to the gear die roll',
           'duration': 'Instantaneous',
           'frequency': 'This spell can be cast once per week.',
           'material_component': '1 Vampires Fang',
           'prerequisite': 'Magic Aspect D12',
           'spell_components': ['I', 'MC']},
 'DISADVANTAGED': {'area_of_effect': 'The Casters Line of Vision',
                   'description': 'This spell allows the caster to plant a mental suggestion into the targets mind '
                                  'causing the target to make two dice rolls on either Aspect Checks, Armor Checks, or '
                                  'Magic Saves for a number of rounds equal to the gear die rolled. The caster must '
                                  'state which roll they want this penalty to apply to upon casting. A rank 7 or '
                                  'better caster can affect a number of targets equal to the gear die rolled',
                   'duration': 'Persistent',
                   'frequency': 'This spell can be cast once per encounter per target.',
                   'prerequisite': 'Magic Aspect D8',
                   'spell_components': ['I', 'S']},
 'DISPLACEMENT': {'area_of_effect': 'The Caster',
                  'description': 'Causes any melee or ranged attack to incur a 25% miss chance for a number of rounds '
                                 'equal to the gear die roll. A rank seven or better caster incurs a 50% miss chance '
                                 'per casting. This spell cannot be used in conjunction with Mirror Image or Burrow.',
                  'duration': 'Persistent',
                  'frequency': 'This spell can be cast once per encounter.',
                  'prerequisite': 'Magic Aspect D10',
                  'spell_components': ['I', 'S']},
 'DOWN THE DRAIN': {'area_of_effect': 'The Caster and One Opponent',
                    'description': 'When making a WM attack, if you successfully hit your opponent and do damage, any '
                                   'damage done to your opponent is immediately added to your HP Total as temporary '
                                   'hit points. You may gain 10HP per rank maximum from each casting. These temporary '
                                   'hit points last for a number of rounds equal to the gear die roll or until '
                                   'depleted.  A rank seven or better caster keeps these HP until they are depleted',
                    'duration': 'Instantaneous',
                    'frequency': 'This spell can be cast once per encounter.',
                    'prerequisite': 'Magic Aspect D10',
                    'spell_components': ['I', 'S']},
 'DRAGON BREATH': {'area_of_effect': 'A 10’x10’ square or a line 4 squares long',
                   'description': 'You gain the ability to breathe gout of energy as a standard/attack action that '
                                  "mimics a dragon's breath. You may choose from fire, cold, lightning, or acid when "
                                  'casting. The spell does its gear die in damage to a 10x10’x10’ square or a line 4 '
                                  'squares long either vertical, horizontal, or diagonally though it cannot be “bent”. '
                                  'The acid breath weapon also causes any non-magical equipment/items in the affected '
                                  'squares to be destroyed unless the items make a magic save versus a DL11. This '
                                  'spell may be cast once per encounter. A rank 7 or better caster can cast this spell '
                                  'twice per encounter.',
                   'duration': 'Instantaneous',
                   'frequency': 'This spell may be cast once per encounter.',
                   'prerequisite': 'Magic Aspect D8',
                   'spell_components': ['E', 'I', 'O']},
 "DUDE YOU'RE STONED": {'area_of_effect': 'Casters Line of Vision',
                        'description': 'This spell grants a gaze attack to the caster that can turn its target to '
                                       'stone temporarily. Any creature affected by this gaze is immediately turned to '
                                       'stone for a number of rounds equal to the gear die rolled. Creatures under the '
                                       'effect of this spell can take no actions except to make a Magic save vs. DL11 '
                                       'each round to break the effect. The target suffers no other effects from this '
                                       'spell. Any creature actively avoiding the casters gaze gets a +10 bonus to the '
                                       'Magic save to avoid its effects.  A rank 7 or better caster can cast this '
                                       'spell once per encounter',
                        'duration': 'Persistent',
                        'frequency': 'This spell can be cast once per day.',
                        'prerequisite': 'Magic Aspect D8',
                        'spell_components': ['I', 'O']},
 'ENHANCEMENT': {'area_of_effect': 'The Casters Line of Vision',
                 'description': 'Allows the caster to temporarily increase a random single targets ability. The caster '
                                'can choose any effect on the chart below at or below his gear die roll. The increase '
                                'lasts a number of rounds equal to the gear die roll though extra HP and gear die once '
                                'used are gone.  1: an extra d4 gear die 8. 5 temp hp 2. 2 temp HP 9. An extra d12 '
                                'gear die 3. An extra d6 gear die 10. 6 temp hp 4. 3 temp hp 11. +1 to all party die '
                                'rolls 5. An extra d8 gear die 12. Gain a temporary d20 6. 4 temp hp gear die on any '
                                'one round of 7. An extra d10 gear die attacks',
                 'duration': 'Persistent',
                 'frequency': 'This spell can be cast once per day.',
                 'prerequisite': 'Magic Aspect D10',
                 'spell_components': ['I']},
 'ENLARGE': {'area_of_effect': 'A Single or Multiple Willing Creatures',
             'description': 'Allows the caster to enlarge a single willing target one size category for a number of '
                            'rounds equal to the gear die roll. A rank 7 caster can enlarge a number of creatures '
                            'equal to the gear die roll and can increase target(s) two size categories. The effect '
                            'lasts a number of rounds equal to the gear die roll',
             'duration': 'Persistent',
             'frequency': 'This spell can be cast once per encounter per target.',
             'prerequisite': 'Magic Aspect D8',
             'spell_components': ['I', 'O', 'S']},
 'ENRAGE': {'area_of_effect': 'The Caster',
            'description': 'Allows the caster to enter a frenzied attack mode for a number of rounds equal to the '
                           'character rank which confers the following bonuses/penalties: 1. Gain 1 temp HP per rank. '
                           'These last until they are taken, or the rage ends whichever comes first 2. Gain +2 on '
                           'Warrior Melee aspect checks to hit 3. Suffers a -2 to defense and a -4 to armor checks '
                           'while raging 4. Character cannot cast spells, use scrolls or take potions while raging 5. '
                           'When the spell ends, you must take a short rest (10 min) or suffer from the exhausted '
                           'condition. If the character is at 0 or less HP at the end of the spell duration or they '
                           'fall unconscious while under the spell effect, they must make an immediate Death Save with '
                           'failure resulting in death. The character must rest before 8 hours expire after the rage '
                           'ends or they fall unconscious for 24 hours automatically',
            'duration': 'Persistent',
            'frequency': 'This spell can be cast one time per day per rank.',
            'prerequisite': 'Magic Aspect D8',
            'spell_components': ['I']},
 'ENTANGLE': {'area_of_effect': 'The Casters Line of Vision',
              'description': 'Conjures a single 10’ long black tentacle that entangles one target and introduces the '
                             'entangled condition. The spell lasts a number of rounds equal to the gear die roll. A '
                             'rank 7 caster can conjure a number of tentacles and affect a number of targets equal to '
                             'the gear die roll and may also move the tentacle(s) 30’ per move action. No creature may '
                             'have more than one tentacle attacking/entangling them at a time. Each tentacle has 10hp '
                             'and is immune to all spell effects',
              'duration': 'Persistent',
              'frequency': 'This spell can be cast once per encounter.',
              'prerequisite': 'Magic Aspect D8',
              'spell_components': ['I', 'S']},
 'EXHAUSTION': {'area_of_effect': 'A Single or Multiple Creatures',
                'description': 'Causes one target to take on the exhausted condition for a number of rounds equal to '
                               'the gear die roll. A rank 7 caster can affect a number of targets equal to the gear '
                               'die roll.',
                'duration': 'Persistent',
                'frequency': 'This spell can be cast once per encounter.',
                'prerequisite': 'Magic Aspect D8',
                'spell_components': ['I', 'O', 'S']},
 'EYE SEE YOU': {'area_of_effect': 'The Casters Line of Vision',
                 'description': 'This spell allows the caster to conjure a magical eye that the caster can use to see '
                                'through. The eye lasts a number of rounds equal to the gear die rolled. This magical '
                                'eye has and confers Darkvision to the caster and allows the caster to cast spells '
                                'through the eye as though they could actually see the target(s) with their own eyes. '
                                'The Magic Eye has 15HP and is subject to attack and spells. The eye uses the casters '
                                'statistics for Magic Saves and Armor Checks. The eye can be moved or maintained by '
                                "the caster using a move action and can move 60' per round indoors or 120' per round "
                                'outdoors. The caster must maintain visual contact with the Magic Eye or the effect '
                                'ends immediately. A rank 7 or better caster can cast this spell once per encounter.',
                 'duration': 'Persistent',
                 'frequency': 'This spell can be cast once per day.',
                 'prerequisite': 'Magic Aspect D8',
                 'spell_components': ['I', 'O', 'S']},
 'FEARFUL PRESENCE': {'area_of_effect': 'A Single or Multiple Creatures',
                      'description': 'Causes one target to take on the panicked condition for a number of rounds equal '
                                     'to the gear die roll. A rank 7 caster can affect a number of targets equal to '
                                     'the gear die roll',
                      'duration': 'Persistent',
                      'frequency': 'This spell can be cast once per encounter.',
                      'prerequisite': 'Magic Aspect D8',
                      'spell_components': ['I', 'O', 'S']},
 'FIREBALL': {'area_of_effect': 'One or More Connected Squares',
              'description': 'Does its gear die plus caster rank in damage to one 5-foot square per rank or a '
                             'line/diagonal up to the characters rank in size. All squares that are targeted must be '
                             'connected. The caster can choose where to center the blast, but it radiates out equally '
                             'from the point of origin. This is magic that dissipates at the end of the casters turn. '
                             'Anyone in an adjacent square to the target takes the character rank damage only unless '
                             'they make a successful magic save',
              'duration': 'Instantaneous',
              'frequency': 'This spell can be used only once per encounter.',
              'prerequisite': 'Magic Aspect D8',
              'spell_components': ['E', 'I', 'S']},
 'FLY': {'area_of_effect': 'The Casters Line of Vision',
         'description': 'Allows the caster to fly like bird for a number of rounds equal to the effect roll at a rate '
                        'of 60 feet per round in any direction. They may cast spells, use missiles, attack as normal '
                        'and may hover, speed up and slow down at will. A rank 7 or above caster can affect an '
                        'additional willing creature',
         'duration': 'Non-Persistent',
         'frequency': 'This spell can be cast once per day.',
         'prerequisite': 'Magic Aspect D10',
         'spell_components': ['I', 'O']},
 'FORGET': {'area_of_effect': 'One or Two Creatures',
            'description': 'Causes the target to forget all spells in any current gear die slots at a cost of one '
                           'spell per 2 points rolled for a minimum of one and a maximum of 6. The spells forgotten go '
                           'from lowest to highest gear die of spells remaining. These slots cannot be repopulated '
                           'with spells unless the target takes a long rest (8+ hours). This spell can only be used '
                           'once per encounter.',
            'duration': 'Persistent',
            'frequency': 'This spell can only be used once per encounter.',
            'material_component': '1,000GP Magic Dust',
            'prerequisite': 'Magic Aspect D12',
            'spell_components': ['I', 'S', 'MC']},
 'GENTLE LANDING': {'area_of_effect': 'The Caster or one other target',
                    'description': 'Choose either the caster or one other target within sight. A falling creature’s '
                                   'rate of descent slows to 60 feet per round for a number of rounds equal to the '
                                   'gear die roll. If the creature lands before the spell ends, it takes no falling '
                                   'damage and can land on its feet, and the spell ends for that creature. A rank 7 or '
                                   'greater caster can affect a number of targets equal to the gear die roll.',
                    'duration': 'Persistent',
                    'frequency': 'This spell can be cast once per day.',
                    'prerequisite': 'Magic Aspect D6',
                    'spell_components': ['I', 'O', 'S']},
 'GOTTA HAVE IT': {'area_of_effect': 'The Caster',
                   'description': 'This spell allows the caster to cast any spell in their spell book when needed '
                                  'without having to have it prepared in either a Spell or Gear Die slot beforehand. '
                                  'The spell gained from this spell is subject to any limitations of the gained spell. '
                                  'The spell can only be at a D4, D6, or D8 level of effect. A Rank 7 or better caster '
                                  'can cast any spell from their spell book when needed at any Spell or Gear Die '
                                  'level. A rank 7 or better caster can cast this spell once per encounter.',
                   'duration': 'Instantaneous',
                   'frequency': 'This spell can be cast once per encounter.',
                   'prerequisite': 'Magic Aspect D8',
                   'spell_components': ['I']},
 'GREASE': {'area_of_effect': 'One or More Connected Squares',
            'description': 'Allows the caster to fill a single 5-foot square with an oily substance per caster rank. '
                           'All affected squares must be connected. Any creatures caught in the affected squares must '
                           'make a magic save to avoid falling prone in the square and affected squares are treated as '
                           'difficult terrain. The grease lasts a number of rounds equal to the gear die roll',
            'duration': 'Persistent',
            'frequency': 'This spell can be cast once per encounter.',
            'prerequisite': 'Magic Aspect D6',
            'spell_components': ['I', 'O', 'S']},
 'GREATER HEALING': {'area_of_effect': 'The Casters Line of Vision',
                     'description': 'Restores twice its gear die in hit points plus caster rank to the person the '
                                    'caster chooses. A rank 7 or higher caster can cast this spell once per encounter '
                                    'per target. This spell can only be used once per encounter.',
                     'duration': 'Instantaneous',
                     'frequency': 'This spell can only be used once per encounter.',
                     'prerequisite': 'Magic Aspect D4',
                     'spell_components': ['E', 'I', 'O', 'S']},
 'GREATER MASS HEALING': {'area_of_effect': 'A Single or Multiple Creatures',
                          'description': 'Restores twice its gear die in hit points plus caster rank to the casters '
                                         'entire party. A rank 7 or higher caster can cast this spell twice per '
                                         'encounter',
                          'duration': 'Instantaneous',
                          'frequency': 'Can be cast once per encounter.',
                          'prerequisite': 'Magic Aspect D4',
                          'spell_components': ['E', 'I', 'O', 'S']},
 'HAIL STORM': {'area_of_effect': 'One or Two Connected Squares',
                'description': 'Conjures several small hail stones to rain down upon a single 5-foot square. The '
                               'number of stones is equal to the gear die rolled. The stones do 1 point of damage per '
                               'stone. At rank 7, the caster can fill 2 five-foot squares, but affected squares must '
                               'be connected',
                'duration': 'Instantaneous',
                'frequency': 'This spell can be cast once per encounter.',
                'prerequisite': 'Magic Aspect D8',
                'spell_components': ['I']},
 'HASTE': {'area_of_effect': 'The Caster or One Ally Duration: Persistent',
           'description': 'Speeds up time for one person, increasing the number of actions they get to take that turn. '
                          'This spell cannot be cast on animals or Spiritual Helpers. Upon successful casting, '
                          'additional actions are granted at the cost of 4 points rolled per action with a minimum of '
                          'one bonus action and a maximum of 3 bonus actions. Actions granted by this spell must be '
                          'used by the end of the casters next turn',
           'duration': 'Persistent',
           'frequency': 'Can be cast once per encounter but only once per day on any character.',
            'material_component': '1 Gold Dragon Eyeball',
           'prerequisite': 'Magic Aspect D12',
           'spell_components': ['I', 'S', 'MC']},
 'HEALALL': {'area_of_effect': 'The Casters Line of Vision',
             'description': 'Restores its die in hit points multiplied by caster rank to one person the caster '
                            'chooses. A rank 7 or higher caster can cast this spell once per encounter',
             'duration': 'Instantaneous',
             'frequency': 'This spell can be cast once per day.',
             'prerequisite': 'Magic Aspect D4',
             'spell_components': ['E', 'I', 'O', 'S']},
 'HEALING': {'area_of_effect': 'The Casters Line of Vision',
             'description': 'Restores its die in hit points plus caster rank to one person the caster chooses. A rank '
                            '7 or higher caster can cast this spell once per encounter per target',
             'duration': 'Instantaneous',
             'frequency': 'This spell can be cast once per encounter.',
             'prerequisite': 'Magic Aspect D4',
             'spell_components': ['E', 'I', 'O', 'S']},
 'HECK WAS THAT': {'area_of_effect': '10x10 per gear die assigned (10x10 for a D4, 20x20 for a D6,',
                   'description': 'This spell allows the recipient to make a single Warrior Melee attack against all '
                                  'creatures that the recipient can see equal to the gear die of the spell regardless '
                                  'of how far away the target(s) are. The recipient will make one Warrior Melee attack '
                                  'roll and apply that to all targets they are attempting to hit, so this spell is all '
                                  'or nothing. The recipient of this spell moves at blinding speed during the round '
                                  'this spell is in effect and ends their turn in the original square they started in '
                                  'after the effect ends. The effect must be used by the end of the recipients next '
                                  'turn after casting or it is simply lost. A rank 7 or better caster can affect two '
                                  'allies per casting',
                   'duration': 'Persistent',
                   'frequency': 'This spell can be cast once per encounter per target.',
                   'prerequisite': 'Magic Aspect D8',
                   'spell_components': ['I', 'S']},
 'HEROISM': {'area_of_effect': 'The caster or one ally',
             'description': 'Grants a temporary +1 to Aspect Checks, Saving Throws, and/or Armor Checks according to '
                            'the table below. A rank 7 or higher caster can cast this once per encounter. 1-4 +1 on '
                            'aspect checks 5-8 +1 on saving throws 9-12 +1 on armor checks',
             'duration': 'Persistent',
             'frequency': 'This spell can be cast once per day.',
             'prerequisite': 'Magic Aspect D8',
             'spell_components': ['I', 'S']},
 'I DARE YOU TO': {'area_of_effect': 'A Single or Multiple Creatures',
                   'description': 'This spell causes iron spikes to erupt from the targets body or armor. These spikes '
                                  'cause damage to any creature of equal or smaller size to the target each time they '
                                  'attack the target with any non-reach or natural weapon(s). The effect lasts a '
                                  'number of rounds equal to the gear die rolled. The spikes cause 1d4 damage per '
                                  'attack that the attacking creature makes against the recipient of this spell. A '
                                  'rank 7 or better caster can cast this spell once per encounter.',
                   'duration': 'Persistent',
                   'frequency': 'This spell can be cast once per encounter.',
                   'prerequisite': 'Magic Aspect D8',
                   'spell_components': ['I', 'S']},
 'ICY BLAST': {'area_of_effect': 'A Single or Multiple Creatures',
               'description': 'Allows the caster to fire a ray of ice that hits a number of targets equal to its gear '
                              'die and doing its gear die in damage to its target(s). A rank 7 or better caster can '
                              'cast this spell every other round',
               'duration': 'Instantaneous',
               'frequency': 'This spell can be cast once per encounter.',
               'prerequisite': 'Magic Aspect D8',
               'spell_components': ['E', 'I', 'S']},
 'ILLUSION': {'area_of_effect': 'The Casters Line of Vision',
              'description': 'Creates an illusion of a single person or creature that the caster has seen that lasts a '
                             'number of rounds equal to the gear die roll. If the gear die roll is a 1-4, the illusion '
                             'has visual capabilities only, 5-8 means it can speak any words the caster communicates '
                             'to the illusion telepathically, 9-12 means that the illusion can actually attack and '
                             'cause force damage of 1D8 per round to the target',
              'duration': 'Persistent',
              'frequency': 'This spell can be cast once per encounter.',
              'prerequisite': 'Magic Aspect D8',
              'spell_components': ['I', 'O', 'S']},
 'IMMOBILIZE': {'area_of_effect': 'A Single or Multiple Creatures',
                'description': 'Same as Dazzle except the held creatures can’t move or free itself automatically if '
                               'attacked. When the affected creature is hit with a weapon or spell (which ignores '
                               'armor and allows no save), the target(s) get a magic save to break the effect after '
                               'each successful attack at DL11 to break the effect. The target is held fast until the '
                               'spell is dispelled, he is attacked and then saves to break the effect, or until 24 '
                               'hours elapse. A rank 7 caster can affect a number of creatures equal to the gear die '
                               'roll',
                'duration': 'Persistent',
                'frequency': 'This spell can be cast once per encounter.',
                        'prerequisite': 'Magic Aspect D10',
                'spell_components': ['I', 'O']},
 'INCORPOREAL': {'area_of_effect': 'The Caster Duration: Non-Persistent',
                 'description': 'Allows the caster to make themselves and any gear they are carrying incorporeal '
                                'immediately and gains the ability to walk through walls and other objects. The caster '
                                'cannot interact with any creatures or objects or attack while in this form. No other '
                                'beneficial spells or effects can exist or be cast on a creature that is Incorporeal. '
                                'This spell lasts a number of rounds equal to the effect roll',
                 'duration': 'Non-Persistent',
                 'frequency': 'This spell can be cast once per day.',
                 'prerequisite': 'Magic Aspect D10',
                 'spell_components': ['I']},
 'INSPIRE': {'area_of_effect': 'Ally',
             'description': 'Grants a temporary bonus to a select character. When inspired, the character adds a D4 to '
                            'their next roll (excluding damage rolls). At Rank 3 it is increased to a D6, at Rank 6 a '
                            'D8 and at rank 10 a D12.',
             'duration': 'Instantaneous',
             'frequency': '',
             'prerequisite': 'Magic Aspect D8',
             'spell_components': ['I', 'S']},
 'INSTANT SEARCH': {'area_of_effect': 'The Caster',
                    'description': 'Allows the caster to concentrate and search a 10’x10’x10’ square and instantly '
                                   'know everything they wish to about the search area. This will provide information '
                                   'on any non-magical details of anything within the search area. A rank 7 or greater '
                                   'caster can search a 20’x20’x20’ area per casting',
                    'duration': 'Instantaneous',
                    'frequency': 'This spell can be cast once per day.',
                    'prerequisite': 'Magic Aspect D6',
                    'spell_components': ['O', 'S']},
 
 'INVISIBILTY': {'area_of_effect': 'A Single or Multiple Willing Creatures',
                 'description': 'Can be cast on one or several willing creatures, making it impossible for them to be '
                                'seen by normal means, at the cost of 4 points rolled per creature with a minimum of '
                                'one and a maximum of 3. Although attacking an enemy while invisible will always grant '
                                'one automatic hit (two if the character dual wields), it will also immediately end '
                                'the invisibility spell for that person. This spell does not grant any extra attacks '
                                'or actions beyond the automatic hit with the first set of attacks. This spell lasts a '
                                'number of rounds equal to the spell roll on each target',
                 'duration': 'Persistent',
                 'frequency': 'Can be cast once per encounter.',
                 'material_component': '1 Vial of Medusa Blood',
                 'prerequisite': 'Magic Aspect D12',
                 'spell_components': ['I', 'O', 'S', 'MC']},
 'IRISH': {'area_of_effect': 'A Single or Multiple Creatures',
           'description': 'This spell allows the caster access to a pool of points that can be applied to any rolls '
                          'the caster makes with the exception of Death saves equal to the gear die rolled. These '
                          'points last a number of rounds equal to the gear die rolled. A rank 7 or better caster can '
                          'choose to affect one ally instead',
           'duration': 'Persistent',
           'frequency': 'This spell can be cast once per day.',
           'prerequisite': 'Magic Aspect D10',
           'spell_components': ['I', 'O', 'S']},
 'LESSEN EFFECT': {'area_of_effect': 'A Single or Multiple Creatures',
                   'description': 'Lessens and possibly removes temporary effects such as blindness, dazzled, '
                                  'sickened, etc. If the effect to be lessened/removed has a duration, it is lessened '
                                  'by a number of rounds equal to the die roll, possibly bringing about an immediate '
                                  'end to the effect. If it has a permanent duration, then one such effect can be '
                                  'removed per casting. This spell will not lessen/remove Aspect or Hit Point '
                                  'drain/damage nor will it remove the conditions brought on by the Dying [Shaken] '
                                  'condition. It will also not lessen/remove any conditions that are self-inflicted '
                                  'such as Sleeping in Armor, etc. A rank 7 or higher caster can lessen/remove one '
                                  'effect from a number of creatures equal to the gear die roll',
                   'duration': 'Instantaneous',
                   'frequency': 'This spell can be cast once per person per encounter or until successful outside of '
                                'combat.',
                   'prerequisite': 'Magic Aspect D4',
                   'spell_components': ['I', 'O', 'S']},
 'LEVITATE': {'area_of_effect': 'The Caster',
              'description': 'Allows the caster to float vertically up and down for a number of rounds equal to the '
                             'effect roll. The caster can float 30 feet per round',
              'duration': 'Persistent',
              'frequency': 'This spell can be cast once per encounter.',
              'prerequisite': 'Magic Aspect D6',
              'spell_components': ['I', 'O', 'S']},
 'LIGHTNING': {'area_of_effect': 'A Single or Multiple Creatures',
               'description': 'Does its gear die in damage to all opponents the caster can see. A rank 7 or better '
                              'caster can cast this every round',
               'duration': 'Instantaneous',
               'frequency': 'Can be cast every other round.',
               'prerequisite': 'Magic Aspect D8',
               'spell_components': ['E', 'I']},
 'LOCKED': {'area_of_effect': 'The Casters Line of Vision',
            'description': 'Allows the caster to lock a number of locks that the caster can see. This spell locks a '
                           'number of locks equal to the effect roll. Locks closest to the caster are affected first',
            'duration': 'Instantaneous',
            'frequency': 'This spell can be cast once per encounter.',
            'prerequisite': 'Magic Aspect D6',
            'spell_components': ['I', 'O', 'S']},
 'LUCK': {'area_of_effect': 'A Single or Multiple Creatures',
          'description': "Allows you to add your gear die to another person's melee/ranged attack or damage roll, "
                         'before they make it. It can also be used to reduce an opponent’s roll by the same amount, '
                         'before they make it. Any luck must be used by the target by the end of the original casters '
                         'next turn. If used against an opponent, the original caster must declare his intention to '
                         'use it BEFORE the opponent acts and the target gets a magic save to resist the effect. A '
                         'rank 7 or better caster can affect a number of creatures equal to the gear die roll. This '
                         'spell cannot be used in combination with Enhancement or Metamagic.',
          'duration': 'Persistent',
          'frequency': 'Can be cast once per encounter.',
          'prerequisite': 'Magic Aspect D10',
          'spell_components': ['I', 'O', 'S']},
 'LUCK OF THE IRISH': {'area_of_effect': 'The Caster',
                       'description': 'This spell allows the caster access to a pool of points that can be applied to '
                                      'any rolls the caster makes with the exception of Death saves equal to the gear '
                                      'die rolled. These points last a number of rounds equal to the gear die rolled. '
                                      'A rank 7 or better caster can choose to affect one ally instead.',
                       'duration': 'Persistent',
                       'frequency': 'This spell can be cast once per encounter.',
                       'prerequisite': 'Magic Aspect D8',
                       'spell_components': ['I', 'O', 'S']},
 'MAGIC MISSILE': {'area_of_effect': 'A Single or Multiple Creatures',
                   'description': 'Fires one bolt of arcane magic through the air doing its gear die plus 1 point per '
                                  'rank in damage. This spell is always cast successfully. A rank 7 or higher caster '
                                  'can fire a number of missiles equal to the gear die roll each hitting a separate '
                                  'target or a maximum of two missiles can be directed at a single target, but not '
                                  'both with the same spell. Each missiles gear die in damage must be rolled '
                                  'separately. In the event of a critically cast Magic Missile spell, ONLY the first '
                                  'missile will crit with the others doing normal damage and at Rank 7 or higher ONLY '
                                  'the first two missiles will crit, the others will do normal damage',
                   'duration': 'Instantaneous',
                   'frequency': 'This spell may be cast every round.',
                   'prerequisite': 'Magic Aspect D4',
                   'spell_components': ['E', 'I']},
 'MAGIC SHIELD': {'area_of_effect': 'A Single or Multiple Creatures',
                  'description': 'Protects a single person the caster chooses (including the caster if she desires) '
                                 'from its die in damage, which is chipped away until it is gone. A rank 7 or higher '
                                 'caster can affect a number of targets equal to the casters rank',
                  'duration': 'Persistent',
                  'frequency': 'Can be cast once per encounter.',
                  'prerequisite': 'Magic Aspect D6',
                  'spell_components': ['I']},
 'MAGICAL DARKNESS': {'area_of_effect': 'A 30x30x30 Cube',
                      'description': 'Allows the caster to cast a darkness spell that darkens an area 30’x30’x10’ with '
                                     'inky black darkness. This spell lasts a number of hours equal to the effect '
                                     'roll. Spells cannot be cast into or out of an area under this effect by either '
                                     'the caster or anyone else. Spells that require concentration such as Phantom '
                                     'Weapon will also not function in the zone. This spell counteracts Magical Light. '
                                     'A rank 7 or better caster can cast this spell once per encounter',
                      'duration': 'Persistent',
                      'frequency': 'This spell can be cast once per day.',
                      'prerequisite': 'Magic Aspect D8',
                      'spell_components': ['I', 'O']},
 'MAGICAL LIGHT': {'area_of_effect': 'A 30x30x10 Cube or One Inanimate',
                   'description': 'Object Allows the caster to cast a light spell that illuminates an area with bright '
                                  'magical light. This spell can be cast on an inanimate object and lasts a number of '
                                  'hours equal to the effect roll. This spell counteracts Magical Darkness. A rank 7 '
                                  'or better caster can cast this spell once per encounter',
                   'duration': 'Persistent',
                   'frequency': 'This spell can be cast once per day.',
                   'prerequisite': 'Magic Aspect D8',
                   'spell_components': ['I', 'O']},
 'MAGICAL SIGHT': {'area_of_effect': 'Casters Line of Vision',
                   'description': 'Allows the caster to see through solid objects up to a distance of 120 feet. A gear '
                                  'die roll of 1-4 allows them to see through flesh and bone, a roll of 5-9 allows '
                                  'them to see through wood, a roll of 9 or10 allows them to see through stone and a '
                                  'roll of 11-12 allows them to see through any material for a number of rounds equal '
                                  'to the gear die roll',
                   'duration': 'Persistent',
                   'frequency': 'This spell can be cast once per day.',
                   'prerequisite': 'Magic Aspect D8',
                   'spell_components': ['I', 'O']},
 'MASS HEALING': {'area_of_effect': 'A Single or Multiple Creatures',
                  'description': 'Restores its gear die in hit points plus caster rank to the casters entire party. A '
                                 'rank 7 or higher caster can cast this spell twice per encounter',
                  'duration': 'Instantaneous',
                  'frequency': 'Can be cast once per encounter.',
                  'prerequisite': 'Magic Aspect D4',
                  'spell_components': ['E', 'I', 'O', 'S']},
 'METAMAGIC': {'area_of_effect': 'A Single Spell',
               'description': 'Allows the caster to manipulate the normal spell limitations of any non-persistent '
                              'spell according to the below table based on the gear die roll. The spell only affects '
                              'spells cast by the original caster. The caster can choose any ability at or below the '
                              'gear die roll to manifest and apply it to any single spell. The metamagic must be used '
                              'by the end of the casters next turn. This spell cannot be used in conjunction with '
                              'Analyze.  A rank 7 or above caster can cast this spell once per encounter on himself or '
                              'an ally. 1-2: Empower: increases the damage/effect of any non-persistent spell by 1.5 '
                              '3-4: Enlarge: increases the spells affected area by 2. Does not affect non-area effect '
                              'spells. 5-6: Extend: increases the duration of any non-persistent spell by 2. 7-8: '
                              'Maximize: causes any variable effects on a non-persistent spell to be at maximum. 9-10: '
                              'Quicken: allows the caster to cast two encounter level spells in a single round. 11-12: '
                              'Repeat: allows the caster to cast a single non-persistent spell and have it auto cast '
                              'again on the casters next round as a free action',
               'duration': 'Persistent',
               'frequency': 'This spell can be cast once per day.',
               'material_component': '1 Illithid Tentacle',
               'prerequisite': 'Magic Aspect D12',
               'spell_components': ['I', 'O', 'MC']},
 'MIRROR IMAGE': {'area_of_effect': 'The Casters Line of Vision',
                  'description': 'Conjures one exact duplicate of the caster per rank. The images occupy the nearest '
                                 'squares to the caster. The caster can control how many images are created, however, '
                                 'the number of images cannot exceed the number of squares that the caster can see. '
                                 'The caster effectively “blinks” around from image to image though they can control '
                                 'this. Anyone attacking the character has a 50% chance to hit the character, (Below '
                                 '51 hits an image), otherwise they hit an image instead and that image dissipates. '
                                 'The spell lasts a number of rounds equal to the gear die roll. This spell may not be '
                                 'used in conjunction with Burrow or Displacement.',
                  'duration': 'Persistent',
                  'frequency': 'This spell may be cast once per encounter.',
                  'material_component': '1 Piece of Mummy Bandage',
                  'prerequisite': 'Magic Aspect D12',
                  'spell_components': ['I', 'S', 'MC']},
 'MORE IS ALWAYS BETTER': {'area_of_effect': 'The Caster or One Ally',
                           'description': 'This spell allows the caster to give the target an additional pair of arms. '
                                          'The effect lasts for a number of rounds equal to the gear die rolled. The '
                                          'target gets an extra attack action as a benefit. If the target does not '
                                          'have weapons available for each new arm, they can instead make an '
                                          'Improvised Weapon attack with those arms as though they had the Improvised '
                                          'Weapon ability. If the target already has the improvised weapon ability, '
                                          'the additional arm attacks would instead be at 1d6 damage. A rank 7 or '
                                          'better caster can cast this spell once per day.',
                           'duration': 'Persistent',
                           'frequency': 'This spell can be cast once per day.',
                           'material_component': '1 Giant Octopus Tentacle',
                           'prerequisite': 'Magic Aspect D12',
                           'spell_components': ['I', 'MC']},
 'MUTABLE FORM': {'area_of_effect': 'A Single or Multiple Creatures',
                  'description': 'This spell allows the recipient to assume a mutable form that makes the target '
                                 'immune from critical hits for a number of rounds equal to the gear die rolled. A '
                                 'rank 7 or better caster can cast this spell on one ally instead.',
                  'duration': 'Persistent',
                  'frequency': 'This spell can be cast once per day per target.',
                  'prerequisite': 'Magic Aspect D8',
                  'spell_components': ['I', 'O', 'S']},
 'NATURES STEP': {'area_of_effect': 'The Caster',
                  'description': 'This spell can only be cast outdoors. This spell allows the caster to merge into any '
                                 'tree or bush and instantly reappear next to any other tree or bush within the '
                                 'casters sight when they first cast the spell. This uses only five’ of movement. This '
                                 'spell lasts a number of rounds equal to the gear die rolled. A rank seven or better '
                                 'caster can affect one ally as well',
                  'duration': 'Instantaneous',
                  'frequency': 'This spell can be cast once per encounter.',
                  'prerequisite': 'Magic Aspect D8',
                  'spell_components': ['I', 'O', 'S']},
 'NIGHT VISION': {'area_of_effect': 'The Caster',
                  'description': 'Allows the caster to see in total and magical darkness as though it were normal '
                                 'daylight. This effect lasts a number of rounds equal to the gear die roll. This '
                                 'spell will not allow you to cast a spell into an area affected by Magical Darkness, '
                                 'however, a rank 7 or better caster can cast out of an area under Magical Darkness '
                                 'while under the effect of this spell',
                  'duration': 'Persistent',
                  'frequency': 'This spell can be cast once per day.',
                  'prerequisite': 'Magic Aspect D8',
                  'spell_components': ['I', 'O']},
 'OBSCURE LIFE FORCE': {'area_of_effect': 'The Caster or Multiple Allies',
                        'description': 'Allows the caster to obscure their life force from creatures with Lifesense '
                                       'such as undead. Undead creatures would not be able to detect the affected '
                                       'creature(s) for the duration of the spell. A rank 7 caster can affect a number '
                                       'of targets equal to the gear die roll. This spell lasts for a number of rounds '
                                       'equal to the gear die roll',
                        'duration': 'Non-Persistent',
                        'frequency': 'This spell can be cast once per day.',
                        'prerequisite': 'Magic Aspect D8',
                        'spell_components': ['I', 'O', 'S']},
 'ODORLESS': {'area_of_effect': 'The Caster or Multiple Allies',
              'description': 'This spell removes all scent from the caster and the gear they are carrying for a number '
                             'of rounds equal to the gear die rolled. A rank 7 or higher caster can affect a number of '
                             'allies equal to the gear die rolled',
              'duration': 'Persistent',
              'frequency': 'This spell can be cast once per day.',
              'prerequisite': 'Magic Aspect D8',
              'spell_components': ['I', 'O', 'S']},
 'OPEN': {'area_of_effect': 'The Casters Line of Vision',
          'description': 'Allows the caster to unlock a number of locks that the caster can see. This spell unlocks a '
                         'number of locks equal to the gear die roll. Locks closest to the caster are affected first',
          'duration': 'Instantaneous',
          'frequency': 'This spell can be cast once per encounter.',
          'prerequisite': 'Magic Aspect D6',
          'spell_components': ['I', 'O', 'S']},
 'PARALYZING RAY': {'area_of_effect': 'A Single or Multiple Creatures',
                    'description': 'Causes one target to take on the paralyzed condition for a number of rounds equal '
                                   'to the gear die roll. A rank 7 caster can affect a number of targets equal to the '
                                   'gear die roll',
                    'duration': 'Persistent',
                    'frequency': 'This spell can be cast once per encounter.',
                    'material_component': '1 Angels Wing Feather',
                    'prerequisite': 'Magic Aspect D12',
                    'spell_components': ['I', 'S', 'MC']},
 'PARDON ME': {'area_of_effect': 'The Casters Line of Vision',
               'description': 'As a full round action, you attempt to interrupt an enemy spell caster from casting a '
                              'spell at you. You choose one target and a particular spell or spell like effect and if '
                              'that creature casts a spell/spell like effect at you, the spell caster must make two '
                              'Magic Checks, if either fails, the spell does not affect you at all, though it would '
                              'affect other potential targets if applicable. This only affects spells that directly '
                              'target you either in a group or individually. Area of effect spells cannot be '
                              'interrupted via this spell. The spell lasts for a number of rounds equal to the gear '
                              'die rolled or until you are targeted and the caster is forced to make the disadvantaged '
                              'Magic check. A rank 7 or better caster can negate two spells/spell like effects instead',
               'duration': 'Instantaneous',
               'frequency': 'This spell can be cast once per encounter.',
               'material_component': '1 Pair of Rust Monster Antennae',
               'prerequisite': 'Magic Aspect D12',
               'spell_components': ['I', 'S', 'MC']},
 
 'PHANTOM WEAPON': {'area_of_effect': 'The Casters Line of Vision',
                    'description': 'Conjures a single one-handed weapon of the casters choice that does its gear die '
                                   'in damage to a single target upon a successful hit. The caster can use the phantom '
                                   'weapon to attack the round after it is summoned. The caster uses their Magic '
                                   'Aspect to attack with this spell. A rank 4 caster can conjure a two-handed weapon. '
                                   'A 7th rank caster can conjure two one hand weapons per casting and can attack with '
                                   'the phantom weapons on the same round it is cast, OR the caster can opt for a '
                                   'single one or two hand weapon that can hit incorporeal/ethereal creatures without '
                                   'penalty. The caster must use an attack action each round or a move action to '
                                   'maintain the spell, otherwise it ends at the end of the original casters turn. If '
                                   'the Magic Aspect check roll to hit is a natural 1, the Phantom Weapon attacking '
                                   'will disappear. The spell lasts a number of rounds equal to the gear die roll. '
                                   'Spell may be cast once per encounter.',
                    'duration': 'Non-Persistent',
                    'frequency': 'This spell may be cast once per encounter.',
                    'prerequisite': 'Magic Aspect D8',
                    'spell_components': ['I', 'S']},
 'POLYMORPH SELF': {'area_of_effect': 'The Caster or One other Ally',
                    'description': 'Allows the caster to assume the shape of any non-unique creature that the caster '
                                   'has personally seen up to a size of medium. On a roll of 7-8 the caster can assume '
                                   'the form of a large creature, 9-10 a Huge creature and 11-12, an Enormous '
                                   'creature. The caster gains all the assumed creature’s abilities. At rank 7 or '
                                   'higher, the caster can affect one other target. Spell lasts for 1 hour or until '
                                   'dispelled',
                    'duration': 'Persistent',
                    'frequency': 'Can be cast once per day per character.',
                    'material_component': '1 Vial of Blood of the Creature Polymorphed Into',
                    'prerequisite': 'Magic Aspect D12',
                    'spell_components': ['I', 'O', 'S', 'MC']},
 'PRAY FOR THE DYING': {'area_of_effect': 'Touch',
                        'description': 'This spell allows the caster to take a full round action and touch an ally who '
                                       'is at zero or less hit points and has yet to make a death save. This touch '
                                       'will automatically heal one point of damage and negate the need for the target '
                                       'to make a death save. The target would then follow the rules regarding HP '
                                       'Recovery. A rank 7 or better caster can affect two targets per casting',
                        'duration': 'Instantaneous',
                        'frequency': 'This spell can be cast once per encounter per target.',
                        'prerequisite': 'Magic Aspect D4',
                        'spell_components': ['I', 'O', 'S']},
 'PURIFY': {'area_of_effect': 'The Caster or One Ally',
            'description': 'Instantly cures any diseases and poisons from either the caster or one ally and restores '
                           'its gear die number in hit points. This spell can only be cast outside of combat but can '
                           'be cast as many times as needed.',
            'duration': 'Instantaneous',
            'frequency': 'This spell can be cast once per encounter.',
            'prerequisite': 'Magic Aspect D4',
            'spell_components': ['O']},
 'PURIFY AREA': {'area_of_effect': 'The Casters Line of Vision',
                 'description': 'This spell removes any negative non-magical effects/objects in the area. All squares '
                                'affected must be connected. A rank 7 or better caster can affect 2 five foot squares '
                                'per rank. Line of sight is not required to cast this spell in your own square. This '
                                'spell lasts a number of rounds equal to the gear die roll.',
                 'duration': 'Persistent',
                 'frequency': 'This spell can be cast once per encounter.',
                 'prerequisite': 'Magic Aspect D8',
                 'spell_components': ['I', 'O', 'S']},
 'REACH OUT': {'area_of_effect': 'The Caster',
               'description': 'This spell extends the reach of the caster an additional five feet as though they were '
                              'one size category larger for a number of rounds equal to the gear die rolled. The spell '
                              'confers no other advantages or penalties related to size. A rank 7 or higher caster can '
                              'affect their self AND one more ally',
               'duration': 'Persistent',
               'frequency': 'This spell can be cast once per encounter per target.',
               'prerequisite': 'Magic Aspect D6',
               'spell_components': ['I', 'S']},
 'REPEL UNDEAD': {'area_of_effect': 'A Single or Multiple Undead Creatures',
                  'description': '*REQUIRES A HOLY SYMBOL TO CAST* Cause’s one undead enemy to turn and flee or cower, '
                                 'upon successful casting, for every 3 points rolled (minimum of one, maximum of 4), '
                                 'the undead creature(s) will take on the panicked condition and flee from the caster '
                                 'at maximum movement, or, if they cannot flee they will instead take on the cowering '
                                 'condition. Creatures can make a magic save to avoid the effect against DL11, if they '
                                 'succeed, they cannot be affected by that caster for 24 hours, if they fail, they are '
                                 'Panicked or Cowered for a number of rounds equal to the gear die roll. Any attack '
                                 'upon a repelled creature will break the enchantment and the repelled creature(s) may '
                                 'act normally and cannot be repelled by that caster for 24 hours. If there are '
                                 'several types of undead creature’s present, the spell affects those with the lowest '
                                 'rank first. A rank 7 or better caster may cast this spell once per round',
                  'duration': 'Non-Persistent',
                  'frequency': 'This spell can be cast once per encounter.',
                  'prerequisite': 'Magic Aspect D10',
                  'spell_components': ['I']},
 'REPULSION': {'area_of_effect': 'A Single or Multiple Creatures',
               'description': 'Allows the caster to erect a wall of force around himself that forces any creature '
                              'attacking him with a melee attack to roll a magic save against DL11. Failure results in '
                              'the enemy not being able to attack the caster for a number of rounds equal to the gear '
                              'die roll',
               'duration': 'Non-Persistent',
               'frequency': 'This spell can be cast once per encounter.',
               'prerequisite': 'Magic Aspect D8',
               'spell_components': ['I']},
 'RIGHT BACK AT YOU': {'area_of_effect': 'The Caster',
                       'description': 'This spell deals damage to would be attackers. If an enemy attacks you with a '
                                      'Warrior Melee attack, you would save as usual, but any damage that you end up '
                                      'taking is immediately returned back upon your attacker as well. The attacker '
                                      'still gets a Magic save at DL11 to avoid this damage. This effect lasts for a '
                                      'number of rounds equal to the gear die rolled. A rank 7 or better caster can '
                                      'affect one other ally per casting',
                       'duration': 'Persistent',
                       'frequency': 'This spell can be cast once per encounter.',
                       'prerequisite': 'Magic Aspect D8',
                       'spell_components': ['I', 'S']},
 'ROOTED': {'area_of_effect': 'A single or multiple creatures',
            'description': 'Allows the caster to anchor himself and/or a number of willing creatures to a particular '
                           'spot. The effect adds a +1 per gear die rolled to any checks against Overrun, Bull Rush or '
                           'any other effect which may attempt to move the protected creature unwillingly for a number '
                           'of rounds equal to the gear die roll. This ability does stack with size modifiers and '
                           'lasts until dismissed by the original caster, the original caster dies/goes unconscious or '
                           'the effect if dispelled/blocked. Dismissing this spell dismisses on all affected creatures '
                           'at the same time however. A rank 7 or better caster can choose to dismiss the effect by '
                           'target instead',
            'duration': 'Persistent',
            'frequency': 'This spell can be cast once per encounter.',
            'prerequisite': 'Magic Aspect D6',
            'spell_components': ['I', 'O', 'S']},
 'SHRINK': {'area_of_effect': 'A Single or Multiple Willing Creatures',
            'description': 'Allows the caster to shrink a single target and all gear/items the target is carrying one '
                           'size category for a number of rounds equal to the gear die roll. A rank 7 caster can '
                           'shrink a number of creatures equal to the gear die roll. The effect lasts a number of '
                           'rounds equal to the gear die roll',
            'duration': 'Persistent',
            'frequency': 'This spell can be cast once per encounter per target.',
            'prerequisite': 'Magic Aspect D6',
            'spell_components': ['I', 'O', 'S']},
 'SILENCE': {'area_of_effect': 'A 30x30x10 Cube',
             'description': 'Allows the caster to target an area they can see creating a 30x30x10 cube that blocks out '
                            'all sound. Since spells require sound to be cast all spells cast within this area will '
                            'fail. The effect lasts for a number of rounds equal to the effect roll. A rank 7 or '
                            'higher caster can affect a 60x60x20 cube',
             'duration': 'Persistent',
             'frequency': 'This spell can be cast once per encounter.',
             'prerequisite': 'Magic Aspect D10',
             'spell_components': ['I', 'O', 'S']},
 'SLEEP': {'area_of_effect': 'A Single or Multiple Creatures',
           'description': 'Causes one enemy to fall asleep and take on the Prone condition, upon successful casting, '
                          'for every 4 points rolled (minimum of one, maximum of 3). Targets may make a magic save to '
                          'minimize the effect. Victims cannot take any action for 4 rounds when they are asleep, nor '
                          'can they be awakened in any non-magical way. Attacking a sleeping creature in any way will '
                          'break the spell instantly and allow them to react normally on their turn. A rank 7 or '
                          'better caster can elect to affect a 30x30x10 cube instead. Can be cast once per encounter.',
           'duration': 'Persistent',
           'frequency': 'This spell can be cast once per day.',
           'material_component': '1 Manticore Tail Spike',
           'prerequisite': 'Magic Aspect D12',
           'spell_components': ['I', 'S']},
 "SO THAT'S IT": {'area_of_effect': 'A Single or Multiple Creatures',
                  'description': 'This spell identifies any protective spell or spell like effects currently active on '
                                 'the target. The caster can choose any one effect and cancel it. If the effect is a '
                                 'natural or permanent in nature, the effect is merely suppressed instead for a number '
                                 'of rounds equal to the gear die roll. A rank seven or better caster can cast this '
                                 'once per encounter',
                  'duration': 'Persistent',
                  'frequency': 'This spell can be cast once per day.',
                  'prerequisite': 'Magic Aspect D12',
                  'spell_components': ['I', 'O', 'S']},
 'SONIC BOOM': {'area_of_effect': 'A Single or Multiple Creatures',
                'description': 'Causes one target to take on the stunned condition for a number of rounds equal to the '
                               'gear die roll. A rank 7 or above caster can affect a number of targets equal to the '
                               'gear die roll',
                'duration': 'Instantaneous',
                'frequency': 'This spell can be cast once per encounter.',
                'prerequisite': 'Magic Aspect D8',
                'spell_components': ['I', 'O', 'S']},
 'SPECTRAL SERVANT': {'area_of_effect': 'Casters Line of Vision',
                      'description': 'This spell summons a spectral servant under the casters control for a number of '
                                     'rounds equal to the gear die rolled. The servant cannot attack or be attacked. '
                                     'The servant can accomplish mundane tasks that the caster would normally have to '
                                     'do such as fetching items, cleaning, mending, lighting fires, etc. It performs '
                                     'these tasks to the best of its ability. A rank 7 or better caster can cast this '
                                     'spell once per rank per day',
                      'duration': 'Persistent',
                      'frequency': 'This spell can be cast once per day.',
                      'prerequisite': 'Magic Aspect D4',
                      'spell_components': ['I', 'O', 'S']},
 'SPEED': {'area_of_effect': 'The Caster or One ally',
           'description': 'Increases the targets movement speed five feet per gear die rolled for a number of rounds '
                          'equal to the gear die roll. This spell does stack and/or apply to any form of movement '
                          'other than land based movement... A rank 7 or higher caster can affect both him/her self '
                          'AND one ally with a single casting',
           'duration': 'Persistent',
           'frequency': 'This spell can be cast once per day per target.',
           'prerequisite': 'Magic Aspect D8',
           'spell_components': ['I', 'O', 'S']},
 'SPIDER CLIMB': {'area_of_effect': 'A Single or Multiple Creatures',
                  'description': 'The caster gains the ability to crawl up walls and hang from ceilings without '
                                 'falling for a number of rounds equal to the gear die roll. The caster can take no '
                                 'actions except climbing at a walking pace until the spell wears off or is dispelled. '
                                 'This spell lasts a number of rounds equal to the gear die roll. A rank 7 or better '
                                 'caster can affect a number of targets equal to the gear die roll',
                  'duration': 'Persistent',
                  'frequency': 'This spell can be cast once per encounter.',
                  'prerequisite': 'Magic Aspect D6',
                  'spell_components': ['I', 'O', 'S']},
 'SPIRITUAL HELPER': {'area_of_effect': 'The Casters Line of Vision',
                      'description': 'Summons a spiritual creature with the ability to provide certain curative '
                                     'effects. The creature summoned is under the telepathic control of the caster for '
                                     'a number of rounds equal to the gear die rolled or until the helper has exhausted '
                                     'all of its abilities whichever is shorter. The helper’s movement is equal to the '
                                     'original caster’s movement. The helper is also the same rank as the original '
                                     'caster. The helper is immune to attack and can only use the effects listed '
                                     'below. The helper may also take a full round action to identify what effect, if '
                                     'any, a creature is under. This check is always successful. The caster can choose '
                                     'any effect at or below the gear die roll. These effects remain available until '
                                     'the spell ends or all effects are used. The helper can cast the following spells '
                                     'at the gear die of the Spiritual Helper spell: 1-2 Healing 3-4 Purify OR Pray '
                                     'for the Dying 5-6 Greater Healing 7-8 Lessen Effect 9-10 Mass Healing 11-12 '
                                     'Healall Each effect may be accomplished once per casting. The spell  A rank 7 or '
                                     'higher caster can use each effect twice up to the gear die roll per casting. No '
                                     'more than one Spiritual Helper may be in existence at a time',
                      'duration': 'Persistent',
                      'frequency': 'can be cast once per day and requires the caster to utilize a full round action '
                                   'each round to maintain the spell.',
                      'prerequisite': 'Magic Aspect D4',
                      'spell_components': ['I', 'S']},
 'SUMMON SPIRITUAL STEED': {'area_of_effect': '(Galdur Only) One Mile',
                            'description': 'This spell summons a spirit that takes the form of a large horse. This '
                                           'steed is intelligent and loyal to the caster. The caster has a telepathic '
                                           'link with the steed as long as the steed is within one mile of the caster. '
                                           'The steed is a non-combatant, but may serve other roles such as a scout or '
                                           'on a watch/guard duty. The steed can only exist outdoors and will remain '
                                           'until dismissed by the original caster, 24 hours have passed, is '
                                           'dispelled, or the caster goes out of range. The steed may be dismissed as '
                                           'a free action. Once dismissed, the spell cannot be cast by that caster '
                                           'again for one day. Only one steed per caster may be summoned at any time',
                            'duration': 'Persistent',
                            'frequency': 'This spell can be cast once per day.',
                            'prerequisite': 'Magic Aspect D6',
                            'spell_components': ['I', 'O', 'S']},
 'SUMMON SWARM': {'area_of_effect': 'One or Two Creatures',
                  'description': 'The caster summons a swarm of vermin which will fight a single, chosen foe that the '
                                 'caster can see for a number of rounds equal to the effect roll causing 1 point of '
                                 'damage per round (no save) and causing any creature who is swarmed to incur the '
                                 'Shaken condition for a number of rounds equal to the gear die roll. The creatures '
                                 'that make up the swarm can not cause any other effects than the damage and shaken '
                                 'condition. As a move action, the caster can elect to do ongoing damage each round or '
                                 'if the caster elects not to use the spell to cause ongoing damage in a given round, '
                                 'they can instead make a Magic aspect check as a free action to maintain the spell '
                                 'with a difficulty level of 7. If the affected creature dies, the original caster can '
                                 'redirect the swarm at any single target they can see using their standard attack '
                                 'action for whatever rounds remain from the original casting though the new target(s) '
                                 'get a save vs. the effect. Moving the swarm is always successful. A rank 7 or higher '
                                 'caster can affect two creatures per casting. The creatures’ summoned is equal to the '
                                 'gear die roll per the chart below.  1-2. Ants, Bats, Crabs 5-6. Centipedes, Locusts, '
                                 'Octopi9-10. Snakes, Wasps, Kuo-ToA 11-12. Spiders, Flies, Lizardfolk 3-4. Beetles, '
                                 'Bees, Crocodiles 7-8. Rats, Ravens, Sharks',
                  'duration': 'Non-Persistent',
                  'frequency': 'This spell can be cast once per encounter.',
                  'prerequisite': 'Magic Aspect D10',
                  'spell_components': ['E*', 'I', 'O', 'S']},
 'SUSTENANCE': {'area_of_effect': 'Within 30 feet',
                'description': 'This spell allows the caster to create one day’s worth of rations and water for one '
                               'person per gear die rolled. A rank 7 or higher caster can create one day’s worth of '
                               'rations and water for a number of persons equal to the gear die rolled.',
                'duration': 'Persistent',
                'frequency': 'This spell can be cast once per day.',
                'prerequisite': 'Magic Aspect D4',
                'spell_components': ['O', 'S']},
 'TAKE THAT': {'area_of_effect': 'Within 30 feet',
               'description': 'This spell allows the caster to possibly redirect the spell energy of any spell cast at '
                              'them. The effect lasts until the end of the casters next turn. The caster can choose '
                              'any ability at or below the gear die roll to manifest. The resulting effect must be '
                              'used by the end of the casters next turn.  A rank 7 or above caster can cast this spell '
                              'once per encounter on himself and the effect lasts for a number of rounds equal to one '
                              'half the gear die rolled (rounded up). The following effects are possible: 1-4 Spell '
                              'Deflection – Any spell cast at the caster deflects in a random direction (possibly '
                              'hitting an ally). If this effect is used, the energy is redirected as follows: 1: '
                              'Forward 2. Left 3. Right 4. Backward. The energy will continue on that path until it '
                              'hits a target(s) or a wall or other object. 4-8 Spell Reflection – Any spell cast at '
                              'the caster is immediately reflected back at the original caster who may then make a '
                              'Magic save accordingly to avoid its effects with a -2 penalty to the Magic save. 9-12 '
                              'Spell Absorption – Any spell cast at the caster is absorbed by the target and its '
                              'energy can be used to allow the recipient of this extra spell energy to cast an extra '
                              'spell on their next turn at the same gear die as the spell that was originally '
                              'absorbed. This spell energy must be used by the end of the recipients next turn or it '
                              'is forever lost',
               'duration': 'Persistent',
               'frequency': 'This spell can be cast once per day.',
                'material_component': '1 Carrion Crawler Tentacle',
               'prerequisite': 'Magic Aspect D4',
                'spell_components': ['I', 'S', 'MC']},
 'TELEKINESIS': {'area_of_effect': 'The Casters Line of Vision',
                 'description': 'Allows the caster to move one small object up to about 10lbs in weight about at a '
                                'rate of 5 feet per round. These objects cannot be used as weapons. This spell lasts a '
                                'number of rounds equal to the effect roll. A rank 7 or better caster can move a '
                                'number of objects equal to the gear die roll',
                 'duration': 'Non-Persistent',
                 'frequency': 'This spell can be cast once per encounter.',
                 'prerequisite': 'Magic Aspect D6',
                 'spell_components': ['I', 'O', 'S']},
 'TELEPORT': {'area_of_effect': 'A Single or Multiple Willing Creatures',
              'description': 'Allows the caster to transport themselves or others from one spot to another over a '
                             'short distance equal to 100 yards per rank of the caster. The caster must be able to see '
                             'or visualize (have been there before) the place being teleported to. The caster may also '
                             'teleport one additional willing person with him at the cost of 4 points rolled per '
                             'person (minimum the caster only, maximum caster + 3). A rank 7 or better caster can '
                             'teleport a number of willing creatures equal to the gear die roll. Unconscious creatures '
                             'may also be teleported via this spell. Can be cast once per encounter. This spell '
                             'introduces the sickened condition upon its target(s). You pick one creature and if '
                             'affected, the target takes on the Sickened condition for a number of rounds equal to the '
                             'gear die rolled. A rank 7 or better caster can affect a number of targets equal to the '
                             'gear die rolled.',
              'duration': 'Instantaneous',
              'frequency': 'This spell can be cast once per encounter.',
              'prerequisite': 'Magic Aspect D8',
              'spell_components': ['I', 'O', 'S']},
 'THAT HURTS': {'area_of_effect': 'A Single or Multiple Willing Creatures',
                'description': 'This spell allows the recipient to increase the threat range on their or one allies '
                               'Aspect Checks to achieve critical hits. This spell grants a +1 bonus to any Aspect '
                               'Check to hit with a weapon and on a natural 11 or better, the hit will result in a '
                               'critical hit. The effect lasts a number of rounds equal to the gear die rolled. A rank '
                               '7 or better caster can also allow the target to achieve critical castings on spells '
                               'that the target casts instead of just melee damage. This spell can be cast once per '
                               'day per target',
                'duration': 'Instantaneous',
                'frequency': 'This spell can be cast once per encounter.',
                'prerequisite': 'Magic Aspect D8',
                'spell_components': ['I']},
 'THE FORECAST CALLS FOR': {'area_of_effect': 'The Casters Field of Vision',
                            'description': 'This spell can only be cast outdoors. The caster can alter the weather in '
                                           'the local area for a number of hours equal to the gear die rolled. The '
                                           'caster can choose from the following effects: 1. Temperature increase '
                                           'D4X10 degrees 2. Temperature decrease D4X10 degrees 3. Gentle Rain .1” per '
                                           'hour 4. Downpour, .25’ per hour 5. Light Wind up to 10 MPH 6. Windy, '
                                           'Steady 25MPH1 7. Light Snow .1’ per hour 8. Heavy Snow .25’ per hour 9. '
                                           'Sunny Skies 10. Sleet .1” per hour 11. Hail, Pea Size 12. Caster’s Choice',
                            'duration': 'Persistent',
                            'frequency': 'This spell can be cast once per week.',
                            'material_component': '1 Pair of Giant Spider Fangs',
                            'prerequisite': 'Magic Aspect D12',
                            'spell_components': ['I', 'O', 'S', 'MC']},
 'WALL OF ICE': {'area_of_effect': 'See Below',
                 'description': 'Creates a large wall of ice equal to one 20x10x5 cube plus an additional 5 foot in '
                                'length per caster rank, the wall lasts a number of rounds equal to the gear die roll '
                                'and has a number of hit points equal to the caster. The wall can only be conjured in '
                                'unoccupied squares. A rank 7 or better caster adds an additional 10 feet to the '
                                'wall’s height. To break down the wall, it must take damage equal to its HP or more. '
                                'The wall has HP equal to the original caster, has no armor value and takes ½ damage '
                                'from all spells',
                 'duration': 'Persistent',
                 'frequency': 'Can be cast once per encounter.',
                 'prerequisite': 'Magic Aspect D10',
                 'spell_components': ['I', 'O', 'S']},
 'WEB': {'area_of_effect': '10x10 per gear die assigned (10x10 for a D4, 20x20 for a D6,',
     'description': 'etc.) Creates a layered mass of strong, sticky strands. These masses must be anchored to two '
            'or more solid and diametrically opposed points or else the web collapses upon itself and '
            'disappears. Creatures caught within a web become stuck (including allies). Attacking a '
            'creature in a web won’t cause you to become entangled. Anyone in the effect’s area when the '
            'spell is cast must make a Magic save. If this save fails, the target(s) take on the Entangled '
            'condition. An Entangled creature may take a full round action to break free from the Web on '
            'their turn by making a Magic save of 17 or better, failure results in remaining stuck until '
            'their next turn. The caster must take a standard/attack action to maintain the spell on '
            'his/her turn; otherwise the webs dissipate at the end of the casters turn. This spell may be '
            'cast once per day.',
     'duration': 'Persistent',
     'frequency': 'This spell may be cast once per day.',
     'prerequisite': 'Magic Aspect D8',
     'spell_components': ['I', 'O']},
 'WHAT THE HECK WAS THAT': {'area_of_effect': 'The Caster or One Ally',
                            'description': 'This spell allows the recipient to make a single Warrior Melee attack '
                                           'against all creatures that the recipient can see equal to the gear die of '
                                           'the spell regardless of how far away the target(s) are. The recipient will '
                                           'make one Warrior Melee attack roll and apply that to all targets they are '
                                           'attempting to hit, so this spell is all or nothing. The recipient of this '
                                           'spell moves at blinding speed during the round this spell is in effect and '
                                           'ends their turn in the original square they started in after the effect '
                                           'ends. The effect must be used by the end of the recipients next turn after '
                                           'casting or it is simply lost. A rank 7 or better caster can affect two '
                                           'allies per casting.',
                            'duration': '1 Round',
                            'frequency': 'This spell can be cast once per encounter per target.',
                            'material_component': '1 Gorgon Horn',
                            'prerequisite': 'Magic Aspect D12',
                            'spell_components': ['I', 'S', 'MC']},
 'WHISPER IN THE WIND': {'area_of_effect': 'The Casters Line of Vision',
                         'description': 'This spell allows the caster to choose any one ally within line of sight and '
                                        'communicate a message in a whispery voice that only the target can hear. The '
                                        'target can reply as well and the response will also be in a whispery voice '
                                        'that only the caster can hear. This effect lasts for a number of rounds equal '
                                        'to the gear die rolled. A rank 7 or better caster can speak to a number of '
                                        'targets equal to the gear die rolled',
                         'duration': 'Persistent',
                         'frequency': 'This spell can be cast once per day.',
                         'prerequisite': 'Magic Aspect D6',
                         'spell_components': ['I', 'O', 'S']},
 'WONDROUS EFFECT': {'area_of_effect': 'The Casters Line of Vision',
                     'description': 'Allows the caster to produce minor magical effects that last a number of rounds '
                                    'equal to the gear die roll. You may choose from the effects below: 1. Create a '
                                    'harmless sensory effect, sparks, small puff of wind, faint music or voices, odors '
                                    'for a number of rounds equal to the gear die. 2. Instantaneously light or snuff '
                                    'out a candle, or small fire for a number of rounds equal to the gear die. 3. '
                                    'Instantaneously clean or soil a single object for a number of rounds equal to the '
                                    'gear die. 4. Instantaneously chill or warm up any liquid to 40 degrees-80 degrees '
                                    'for a number of rounds equal to the gear die. 5. Make a small mark or symbol '
                                    'appear on a surface or an object for a number of rounds equal to the gear die. 6. '
                                    'Create a small non-magical item that can fit in your hand for a number of rounds '
                                    'equal to the gear die.',
                     'duration': 'Instantaneous',
                     'frequency': 'This spell can be cast once per encounter.',
                     'material_component': '1 Piece of a Lich’s Phylactery',
                     'prerequisite': 'Magic Aspect D8',
                     'spell_components': ['I', 'O', 'S', 'MC']},
 "YOU'RE NOT SO TOUGH": {'area_of_effect': 'The Caster or One Ally',
                         'description': 'This spell allows the caster to grant themselves or one ally the ability to '
                                        'do extra damage to targets larger than them. For each size category above the '
                                        'size of the spells target that the creature is, the spell recipient adds +2 '
                                        'to the damage for each successful Warrior Melee attack against that target '
                                        'that they make. The effect lasts a number of rounds equal to the gear die '
                                        'rolled. A rank 7 or better caster adds +4 to the damage roll instead.',
                         'duration': 'Persistent',
                         'frequency': 'This spell can be cast once per encounter.',
                         'prerequisite': 'Magic Aspect D8',
                         'spell_components': ['I']},
 "YOU'RE SPECIAL": {'area_of_effect': 'The Caster',
                    'description': 'This spell allows the caster to select any special ability from their Aspect that '
                                   'they initially put their D12 aspect die into and use that ability for a number of '
                                   'rounds equal to the gear die rolled. A rank 7 or better caster can instead choose '
                                   'any special ability from any list and use it for a number of rounds equal to the '
                                   'gear die rolled.',
                    'duration': 'Persistent',
                    'frequency': 'This spell can be cast once per day.',
                    'material_component': "1 Piece of a Lich's Phylactery",
                    'prerequisite': 'Magic Aspect D12',
                    'spell_components': ['I', 'S', 'MC']},
 "YOU'RE WELCOME": {'area_of_effect': 'One ally',
                    'description': "Allows the caster to take ½ of the allies' damage for a number of rounds equal to "
                                   'the gear die roll. A rank 7 or higher caster can elect to take all damage instead. '
                                   'The caster can also elect to not take the damage in any given round though not '
                                   'taking the damage does not extend the length of the spell.',
                    'duration': 'Persistent',
                    'frequency': 'This spell can be cast once per encounter.',
                    'prerequisite': 'Magic Aspect D8',
                    'spell_components': ['I', 'S']},
 'THAT’S NASTY': {'prerequisite': 'Magic Aspect D8',
                  'spell_components': ['I', 'S'],
                  'area_of_effect': 'The Casters Line of Vision',
                  'duration': 'Persistent',
                  'frequency': 'This spell can be cast once per encounter.',
                  'description': ('This spell introduces the sickened condition upon its target(s). '
                                  'You pick one creature and if affected, the target takes on the Sickened condition '
                                  'for a number of rounds equal to the gear die rolled. A rank 7 or better caster can '
                                  'affect a number of targets equal to the gear die rolled.')}
}

# Material Components overrides sourced from 'SPELL COMPONENTS LIST.vb'.
# This mapping is applied at import time to keep spells.py in sync.
MATERIAL_COMPONENTS_OVERRIDES = {
    'ACID RAIN': '1oz. Gelatinous Cube',
    'ALLS CLEAR': 'A Blank Parchment',
    'ANALYZE': '1 50GP Pearl',
    'ANIMATE OBJECT': '1oz. Spider Venom',
    'BURIED ALIVE': '1oz. Quartz Stone',
    'BLINDNESS': '1 Pair Broken Eyeglasses',
    'BURROW': '1 Claw from an Umber Hulk',
    'CHAIN LIGHTNING': '1 Piece of Bark from a Tree Struck by Lightning',
    'CHARM MONSTER/PERSON': '1 oz. Perfume',
    'COME TO ME': '1 Small Silver Mirror',
    'COMFORT': '1 Bead of Glass',
    'COMMON KNOWLEDGE': '1 oz. Straw',
    'CREATE PORTAL': '1 Golden Needle',
    'DAZZLE': '1 Amber Rod',
    'DEAFNESS': '1 Black Onyx Stone',
    'DEATH': '1 Vampires Fang',
    'DISADVANTAGED': '1 Ruby',
    'DISPLACEMENT': '1 Small Ivory Statue',
    'DOWN THE DRAIN': '1 Glass Eye',
    'DRAGON BREATH': '1 Dragon Scale',
    "DUDE YOU'RE STONED": '1 Polished Marble Stone',
    'ENHANCEMENT': '1 Owl Bear Feather',
    'ENLARGE': '1oz. Giant Rat Bile',
    'ENRAGE': '1oz. Mercury',
    'ENTANGLE': '1 Roper Tentacle',
    'EYE SEE YOU': '1 Undead Eyeball',
    'FEARFUL PRESENCE': '1 Owlbear Claw',
    'FIREBALL': '1oz. Guano and 1oz. Sulfur',
    'FLY': '1 Griffon Feather',
    'FORGET': '1,000GP Magic Dust',
    'GENTLE LANDING': '1 Owl Feather',
    'GOTTA HAVE IT': '1 Hydra Claw',
    'GREASE': '1oz. Animal Fat',
    'GREATER HEALING': None,
    'GREATER MASS HEALING': None,
    'HAIL STORM': '1 Shark Dorsal Fin',
    'HASTE': '1 Gold Dragon Eye',
    'HEALALL': None,
    'HEALING': None,
    'HEROISM': '1 Piece Troll Skin',
    'I DARE YOU TO': '1oz. Basilisk Bile',
    'ICY BLAST': '1oz. Centipede Venom',
    'ILLUSION': '1 Vial Snake Venom',
    'IMMOBILIZE': '1 Crocodile Tooth',
    'INCORPOREAL': '1oz. Crushed Ettin Bone',
    'INSPIRE': '1 Harpy Claw',
    'INSTANT SEARCH': '1oz. Fine Wine',
    'INVISIBILITY': '1 Vial of Medusa Blood',
    'LESSEN EFFECT': None,
    'LEVITATE': '1 Orc Bone',
    'LOCKED': '1 Small Padlock',
    'LUCK': '1oz. Treant Bark',
    'LUCK OF THE IRISH': '1 Treant Leaf',
    'MAGICAL DARKNESS': '1 8oz. Obsidian Stone',
    'MAGICAL LIGHT': '1 8oz. Pumice Stone',
    'MAGIC MISSILE': None,
    'MAGIC SHIELD': '1 Piece of a Shield Broken in Battle',
    'MAGICAL SIGHT': '1 Small Magnifying Lens',
    'MASS HEALING': None,
    'METAMAGIC': '1 Illithid Tentacle',
    'MIRROR IMAGE': '1 Piece of Mummy Bandage',
    'MORE IS ALWAYS BETTER': '1 Giant Octopus Tentacle',
    'MUTABLE FORM': '1 Piece of Mimic Pseudopod',
    'NATURES STEP': '1 Sprig Mistletoe',
    'NIGHT VISION': '1 Black Silk Square',
    'OBSCURE LIFE FORCE': '1 Black Pearl',
    'ODORLESS': '1oz. Beaver Castor',
    'OPEN': '1 Small Broken Padlock',
    'PARALYZING RAY': '1 Angels Wing Feather',
    'PURIFY': None,
    'PURIFY AREA': None,
    'REACH OUT': '1 Bow String',
    'REPEL UNDEAD': '1 Piece Ghoul Flesh',
    'REPULSION': '1 Piece Manticore Tongue',
    'RIGHT BACK AT YOU': '1 Vial Unholy Water',
    'ROOTED': '1 Piece Oak Tree Root',
    'SHRINK': '1 Piece Lizard Skin',
    'SILENCE': '1 Piece Ochre Jelly Pseudopod',
    'SLEEP': '1 Manticore Tail Spike',
    "SO THAT'S IT": "1 Beholders Eye Stalk",
    'SONIC BOOM': '1 Piece Granite',
    'SPECTRAL SERVANT': None,
    'SPEED': '1 Small Turquoise Gem',
    'SPIDER CLIMB': '1 Vial Spider Silk',
    'SPIRITUAL HELPER': None,
    'SUMMON SPIRITUAL STEED': '1 Handful Horse Hair',
    'SUMMON SWARM': '1 Square Finest Velvet',
    'SUSTENANCE': None,
    'TAKE THAT': '1 Carrion Crawler Tentacle',
    'TELEKINESIS': '1 Small Magnet',
    'TELEPORT': '1 Amber Pendant',
    "THAT'S NASTY": '1 Flask Mercury',
    'THAT HURTS': '1 Small Piece Mithral',
    'THE FORECAST CALLS FOR': '1 Pair of Giant Spider Fangs',
    'WALL OF ICE': '1 Oz. Platinum Dust',
    'WEB': '1 Silk Cloak',
    'WHAT THE HECK WAS THAT': '1 Gorgon Horn',
    'WHISPER IN THE WIND': '1 Hand Fan',
    'WONDROUS EFFECT': '1oz. Ground Jade Dust',
    "YOU'RE NOT SO TOUGH": '1oz. Crushed Dragon Shells',
    "YOU'RE SPECIAL": '1 Piece of a Lich’s Phylactery',
    "YOU'RE WELCOME": '1 Molted Snake Skin',
}

def _normalize_name(name: str) -> str:
    if not isinstance(name, str):
        return name
    k = name.upper().strip()
    # normalize curly quotes to straight for matching
    k = k.replace('’', "'").replace('“', '"').replace('”', '"')
    return k

def _find_spell_key(spell_name: str):
    n = _normalize_name(spell_name)
    # direct match
    if n in SPELLS:
        return n
    # known alias/misspelling corrections
    aliases = {
        'INVISIBILITY': 'INVISIBILTY',
        "THAT'S NASTY": 'THAT’S NASTY',
        "YOU'RE NOT SO TOUGH": "YOU'RE NOT SO TOUGH",
        "SO THAT'S IT": 'SO THAT’S IT',
    }
    if n in aliases and aliases[n] in SPELLS:
        return aliases[n]
    # fuzzy: compare normalized forms of existing keys
    for key in SPELLS.keys():
        if _normalize_name(key) == n:
            return key
    return None

# Apply overrides: add/remove material_component and MC flag consistently
for _name, _mat in MATERIAL_COMPONENTS_OVERRIDES.items():
    key = _find_spell_key(_name)
    if not key:
        continue
    spell = SPELLS[key]
    comps = spell.get('spell_components', [])
    if _mat is None or (_is_none := isinstance(_mat, str) and _mat.strip().lower() == 'none'):
        # remove material and MC
        spell.pop('material_component', None)
        if 'MC' in comps:
            comps = [c for c in comps if c != 'MC']
            spell['spell_components'] = comps
    else:
        # set/replace material and ensure MC present
        spell['material_component'] = _mat
        if 'MC' not in comps:
            comps.append('MC')
            spell['spell_components'] = comps

# Component type definitions
COMPONENT_TYPES = {
    "E": "Elemental",
    "I": "Incantation", 
    "O": "Occult",
    "S": "Somatic",
    "MC": "Material Component"
}

# Helper functions
def get_spell_by_name(spell_name):
    """Get spell information by name (case-insensitive)"""
    return SPELLS.get(spell_name.upper())

def get_spells_by_component(component):
    """Get all spells that use a specific component"""
    return {name: spell for name, spell in SPELLS.items() 
            if component in spell["spell_components"]}

def get_spells_by_prerequisite(prerequisite):
    """Get all spells with a specific prerequisite"""
    return {name: spell for name, spell in SPELLS.items() 
            if spell["prerequisite"] == prerequisite}

def list_all_spells():
    """Get a list of all spell names"""
    return list(SPELLS.keys())

def get_spell_components(spell_name):
    """Get the components for a specific spell"""
    spell = get_spell_by_name(spell_name)
    return spell["spell_components"] if spell else None