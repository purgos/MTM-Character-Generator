# MTM V7.0 Aspect Abilities - Python Dictionary Format

ASPECT_ABILITIES = {
    'melee': {
        'Cleave': 'When you kill an opponent or reduce them to 0 HP, you can make a single free attack at your best Gear die against all adjacent foes. You may not move at all. If you do, your turn ends immediately. If you kill another foe, you may cleave again and continue doing so as long as you kill at least one foe each round and that you do not move.',
        'Disarm': 'As a Move Action, the attacker can attempt to disarm an opponent. The attacker and the opponent both roll an opposed WM check, if the attackers roll is higher, the opponent is disarmed of one weapon. Modifiers for size, attached weapons, and two-handed weapons etc. apply (+2/-2 to check for each applicable disadvantage) with +2/-2 per size category difference.',
        'Divine Purpose': 'When fighting Hellspawn or Undead the warrior gains an additional +1 to WM aspect checks to hit and an extra D4 of damage on a successful hit. This damage ignores armor and receives no save.',
        'Fast Switch Weapon': 'Once per encounter, you may stow and draw a single weapon as a free action instead of a move action.',
        'Flare for the Dramatic': 'Allows the character to vividly describe the Warrior Melee attack they are making. At GM discretion, that single attack may gain advantage to hit OR do 1.5 times damage (character choice). You may use this ability a number of times equal to your rank per encounter.',
        'Get Back Here': 'This ability allows the Warrior to choose to make an opposed Rogue Roll against the opponent. If the Warrior wins, the target is tripped and falls prone. Situational modifiers still apply.',
        'Improved Critical': 'means that if you roll a natural twelve on your Warrior Melee Aspect check to hit, you will then do three times damage on the hit instead of two times damage. The first two die would be automatically max, and you would roll the third one. For example, you roll a natural twelve to hit, you hit with your d12 sword so that would mean the damage would be twenty-four plus 1d12 plus rank.',
        'Not Quite': 'This ability makes the Warrior immune to effects that introduce disadvantage rolls and allows them to roll with advantage on any one roll per encounter. This roll must be announced prior to the roll being made.',
        'Opportunistic Strike': 'Once per encounter, if an opponent leaves a square or moves through a square that you threaten with a hand-to-hand melee attack, you may make an instant attack at your highest gear die. This attack is at +2 on the Warrior Melee check to hit and all damage done ignores armor/shield bonuses.',
        'Thick Skin': 'When unarmored, the warrior gains a D4 armor equivalent and can choose to ignore damage from any one WM attack per encounter.',
        'Warriors Fury': 'This ability allows the warrior to continue rolling D12\'s when they critically hit an opponent. The Warrior can roll an extra number of D12 up to their rank.',
        'Weak Spot': 'As a full round action, the Warrior can take the time to focus on their opponent and make their next attack roll with advantage. If the attack hits, it deals an extra D6 of damage. This damage increase to D8 at rank seven.',
        'Weapon Master': 'These warriors are so in tune with their weapons that they gain advantage on any WM aspect checks to hit in melee combat.',
        'Whirlwind': 'When the warrior is engaged with multiple enemies in melee combat, the warrior can make an attack against each enemy. This ability cannot be combined with another abilities.'
    },
    'ranged': {
        'Bomb Mastery': 'When using Exploding Projectiles, the ranged Warrior gains one extra die of damage, i.e., D6 becomes D8, D8 becomes D10, etc.',
        'Bow Mastery': 'When using a bow of any type, the ranged warrior gains the ability to attach a small exploding pebble that causes an additional D4 in damage to projectiles from the weapon.',
        'Bow String Music': 'As a full round action, the ranged warrior can elect to play a song with their bow string that causes disadvantage on any one enemies next Aspect check.',
        'Deflect Missiles': 'Anytime you are hit by a fired or thrown projectile, you can make a Warrior Ranged aspect check. On a roll of seven or higher, you deflect the projectile and suffer no damage from it. This does not apply to spells or spell-like effects. This ability counteracts Snipe.',
        'Divine Purpose': 'When fighting Hellspawn or Undead the warrior gains an additional +1 to WM aspect checks to hit and an extra D4 of damage on a successful hit. This damage ignores armor and receives no save.',
        'Doubleshot': 'As a standard action, you may knock and shoot two projectiles at a time. You roll two attack rolls; the first one is a normal attack roll while the second one incurs a -3 penalty to the shot.',
        'Mow Them Down': 'As a full round action, you may knock and shoot a number of arrows equal to your rank and attack any target(s) you can see up to your rank per round with no more than one arrow striking any single target. You must make a Warrior Ranged aspect check to hit for EACH projectile.',
        'Ranged Crit': 'Anytime a natural twelve is rolled on any Warrior Ranged aspect check to hit a target, add an extra die of damage the same as you would for a standard critical hit.',
        'Ranged Prowess': 'As a full round action, the ranged warrior can make a Warrior Ranged attack and if it hits, any allies within thirty\' of the target gain a +1 to their next aspect check. This can be used once per day.',
        'Snipe': 'As a full round action, you can spend the time targeting your enemy and launch a single projectile that automatically hits doing normal damage.',
        'Weapon Master': 'These warriors are so in tune with their weapons that they gain advantage on any WR aspect checks to hit in melee combat.',
        'Whistling Arrow': 'As a move action, you can choose one ally and attune the harmonics of your projectile to inspire your ally. The recipient can then add a D4 to one Aspect Check, Gear Die Roll, or Magic Save. This can be used once per day per rank.',
        'Who Are You Talking To': 'This ability allows the Warrior to communicate with trees, bushes, animals, etc. The target will answer questions to the best of their ability but may not know the answer(s) or may simply choose to ignore the question(s) entirely.'
    },
    'rogue': {
        'Fleet of Foot': 'You may move forty-five feet per round instead of thirty, or ninety instead of thirty on a double move or (90/180 outdoors).',
        'How Old Are You': 'This ability causes the Rogue to age much slower. Each 10 years ages the caster only one year instead.',
        'Improved Trap Detection': 'Add +2 to any active search and disarm rolls for both Mechanical and Magical traps.',
        'Jack of All Trades': 'You are adept at all skills. Add +3 to all future skill checks.',
        'Precise Strike': 'As a standard action, when attempting a Called Shot, the attacker adds a +1 to the Aspect Check to hit. A nine or better results in a success.',
        'Silver Tongue': 'You are very adept in social settings and interactions with others. You gain a +2 to any Intimidate, Bluff, NPC interactions, etc. checks.',
        'Sleep Powder': 'Allows the Rogue the knowledge to mix common components into a concoction that when inserted into a vial and broken in a square occupied by an opponent, that opponent must make an immediate Magic save at DC11 or fall asleep instantly. The affected opponent gets a Magic Save each time they are attacked to shake off the effects and wake up. This ability can be used once per encounter.',
        'Stealth Master': 'You gain the ability to be completely undetectable for one round per day per rank. Tremorsense, Lifesense, See Invisible, etc. will not function against you during this time. The rounds must be consecutive. A rank 7 or higher can take the rounds of movement in a staggered fashion.',
        'Summon Animal Friend': 'Allows the character to summon an Animal friend. The friend can be either a Bear, Eagle, or Shark. The summoned creature will last for a number of rounds equal to the gear die rolled or until it loses all its\' HP. This spell can be cast once per day. The animal friend will have the following stats/abilities based on character rank: 1-2: Small, 20HP, D4 Natural Armor, D4 Bite Attack, D4 Claw Attack; 3-4: Medium, 30HP, D6 Natural Armor, D6 Bite Attack, D6 Claw Attack; 5-6 Large, 40HP, D8 Natural Armor, D8 Bite Attack, D8 Claw Attack, D8 Claw Attack; 7-8 Huge, 50HP, D10 Natural Armor, D10 Bite Attack, D10 Claw Attack, D10 Claw Attack, D6 Rend (if both claws hit); 9-10 Enormous, 60HP, D12 Natural Armor, D12 Bite Attack, D12 Claw Attack, D12 Claw Attack, D8 Rend (if both claws hit); 11-12 Enormous, 70HP, D12+1 Natural Armor, D12 Bite Attack, D12 Claw Attack, D12 Claw Attack, D10 Rend (if both claws hit).',
        'Superior Dexterity': 'You are very Dexterous. When making Climb, Hide, Jump, Move Silently, Perform, Sleight of Hand, Swim, or opposed Rogue rolls, you may add an additional +2 to you check(s).',
        'Surprising Strike': 'If the Rogue has surprise initially or by virtue of a spell such as Invisibility, the Rogue does 1.5 times damage on their first attack action.',
        'Trapmaking': 'You are proficient at designing, building, and setting traps. Traps are either mechanical or spell based. You can set a number of traps per day equal to 3+ character rank if they are mechanical or 1 per day if they are spell based. You are only limited by your creativity on what the trap(s) may be. When a mechanical trap is set, it will do damage equal to d6 plus rank of the builder and take 10 minutes to set and build time will vary from trap to trap based on scale and complexity, the GM will determine this for you. A Magic trap will do damage equal to the gear die plus rank of the spell the builder cast to set the trap and will take 1 hour to prepare and set. Trap spells must have a designated trigger that will set them off that is defined by the trap\'s creator at trap creation. The spell effect will persist until dispelled, or the trap is set off/disabled. Any trap can still be detected by a standard rogue roll.',
        'You Thought You Had Me': 'This ability allows the Rogue to choose any one WM or WR attack that successfully hits and instead choose to have the attack miss instead. This ability may be used once per encounter.'
    },
    'magic': {
        'Arcane Dodge': 'Pick any one spell that does not cause HP damage. You are forever immune to its effects, even while sleeping or otherwise incapacitated.',
        'Arcane Wit': 'The caster can no longer fumble when casting spells, any fumble would instead be a miscast.',
        'Detect Dweomer': 'As a full round action, the caster can detect if a single item is magical. Also, as a full round action, the caster can analyze a 10x10x10 area per rank that the caster can see with unaided sight to determine if any magical auras are present. This does not identify specific magic on either items or areas; it just simply alerts the caster to their presence. Optionally, the GM can denote the strength of the dweomer based on the result of the check.',
        'Elementalism': 'When casting element-based damage spells, the caster gains +1d4 to damage. This ability may be used at-will.',
        'Healing Song': 'As a full round action, you can sing a song that cures wounds done to your allies. You can cure 1D4 in HP damage to all allies that can hear your song. This ability may be used once per encounter.',
        'Mage Armor': 'The first time the caster is successfully hit with a single WM attack in an encounter, the hit will become a miss instead.',
        'Master Caster': 'This ability allows the caster to cast spells without the need to vocalize their words. A rank seven caster not only can cast silently but also without semantics.',
        'Join Me': 'As a full round action, this ability allows the caster to combine their Magic abilities with other casters. If the casters involved are casting the same spell, any target(s) of their spell suffer disadvantage on their Magic Saves. The duration of the spell is the highest gear die rolled among the casters.',
        'Practiced Caster': 'You may pick any one damage causing spell. You may cast this spell automatically without the need to make Magic Aspect checks to cast that spell. You always have this spell available, even when sleeping. Alternatively, you can choose any one spell and not be required to have a spell component to cast that spell.',
        'Recall/Swap Spell': 'As a full round action, this allows the caster to spend this time refocusing his/her mind to recall/swap a swappable encounter level spell that has been previously cast in the current encounter and have it available for use again this encounter on the following round on the original gear die. This check is always successful. This ability can be used only once per encounter.',
        'Song of Freedom': 'As a full round action, you can sing a song that will allow one ally to make an immediate Magic save vs. one ongoing mind affecting spell currently affecting them. If they are successful, the effect ends at the end of their next turn. This ability can be used once per encounter.',
        'Summoning': 'When casting summoning spells, the spells can be maintained as a free action instead of a Move action.',
        'Try, Try Again': 'As a Move action, the caster can attempt to recast a spell that was attempted in the previous round but was miscast. This ability adds a plus one to each subsequent attempt up to plus five. The caster may only attempt to recast the exact spell that was miscast the previous round and may continue doing so for five additional rounds using this ability. If the original miscast spell was an every other round spell such as Chain Lightning, the caster can still use this ability every other round if the intention to do so is announced on the subsequent round after the initial failed casting.',
        'Where Did You Go': 'Allows the caster to teleport up to thirty feet as a Move action.'
    }
}

# Helper functions
def get_abilities_by_aspect(aspect):
    """Get all abilities for a specific aspect"""
    return ASPECT_ABILITIES.get(aspect, {})

def get_ability_description(aspect, ability_name):
    """Get the description of a specific ability"""
    aspect_abilities = get_abilities_by_aspect(aspect)
    return aspect_abilities.get(ability_name, '')

def list_all_aspects():
    """Get a list of all available aspects"""
    return list(ASPECT_ABILITIES.keys())

def list_abilities_for_aspect(aspect):
    """Get a list of all ability names for a specific aspect"""
    aspect_abilities = get_abilities_by_aspect(aspect)
    return list(aspect_abilities.keys())

def get_all_abilities():
    """Get all abilities across all aspects"""
    all_abilities = {}
    for aspect, abilities in ASPECT_ABILITIES.items():
        all_abilities[aspect] = list(abilities.keys())
    return all_abilities 