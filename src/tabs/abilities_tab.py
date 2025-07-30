import tkinter as tk
from tkinter import ttk

class AbilitiesTab:
    # Aspect-specific ability definitions
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
    def __init__(self, parent, character_data):
        self.parent = parent
        self.character_data = character_data
        self.tab = ttk.Frame(parent)
        
        # Define when characters gain special abilities based on specialization
        self.ABILITY_RANKS = {
            'Non-Specialized': [1, 4, 8],
            'Warrior': [1, 2, 3, 6, 8, 10],
            'Mage': [1, 2, 3, 6, 8, 10],
            'Rogue': [1, 2, 3, 6, 8, 10],
            'Specialized Caster': [1, 2, 3, 6, 8, 10],
            'Specialized Warrior Melee': [1, 2, 3, 6, 8, 10],
            'Specialized Warrior Ranged': [1, 2, 3, 6, 8, 10],
            'Specialized Rogue': [1, 2, 3, 6, 8, 10],
            'Shield Master': [1, 2, 3, 6, 8, 10]
        }
        
        # Initialize abilities data with all possible ranks
        if 'specialAbilities' not in self.character_data:
            self.character_data['specialAbilities'] = {
                'rank1': '',
                'rank2': '',
                'rank3': '',
                'rank4': '',
                'rank6': '',
                'rank8': '',
                'rank10': ''
            }
        
        self.create_tab()
        
    def create_tab(self):
        """Create the abilities tab"""
        # Abilities Frame
        frame = ttk.LabelFrame(self.tab, text="Special Abilities")
        frame.pack(fill='both', expand=True, padx=5, pady=5)

        # Dragon's Breath Ability (only for Half-Dragon)
        self.dragons_breath_frame = ttk.Frame(frame)
        ttk.Label(self.dragons_breath_frame, text="Dragon's Breath:").pack(side='left', padx=5)
        
        # Create a frame for the fixed text
        dragons_breath_text_frame = ttk.Frame(self.dragons_breath_frame)
        dragons_breath_text_frame.pack(side='left', padx=5, fill='x', expand=True)
        
        # Calculate range and damage based on rank
        current_rank = self.character_data.get('rank', 1)
        range_value = 10 + (5 * (current_rank - 1))
        
        # Calculate damage based on rank
        if current_rank >= 11:
            damage = "1d12+1d4"
        elif current_rank >= 9:
            damage = "1d12"
        elif current_rank >= 7:
            damage = "1d10"
        elif current_rank >= 5:
            damage = "1d8"
        elif current_rank >= 3:
            damage = "1d6"
        else:
            damage = "1d4"
            
        # Calculate uses per encounter based on rank
        uses = 1
        if current_rank >= 11:
            uses = 4
        elif current_rank >= 9:
            uses = 3
        elif current_rank >= 5:
            uses = 2
        
        # Add the fixed text with dynamic range and damage
        self.dragons_breath_label = ttk.Label(dragons_breath_text_frame, 
                                            text=f"Range: 10x{range_value} feet\nDamage: {damage} fire damage\nUses per Encounter: {uses}")
        self.dragons_breath_label.pack(anchor='w')
        
        # Pack Dragon's Breath frame at the top initially (will be hidden if not Half-Dragon)
        self.dragons_breath_frame.pack(fill='x', padx=5, pady=2)

        # Create ability selection frame
        self.ability_selection_frame = ttk.Frame(frame)
        self.ability_selection_frame.pack(fill='x', padx=5, pady=5)
        
        # Ability dropdown and add button
        ttk.Label(self.ability_selection_frame, text="Select Ability:").pack(side='left', padx=5)
        
        # Create dropdown with aspect-specific abilities
        self.ability_var = tk.StringVar()
        self.ability_dropdown = ttk.Combobox(self.ability_selection_frame, textvariable=self.ability_var, 
                                           state='readonly', width=30)
        self.ability_dropdown.pack(side='left', padx=5)
        
        # Add button
        self.add_ability_button = ttk.Button(self.ability_selection_frame, text="Add Ability", 
                                           command=self.add_ability)
        self.add_ability_button.pack(side='left', padx=5)
        
        # Description label
        self.ability_description_label = ttk.Label(self.ability_selection_frame, text="", wraplength=300)
        self.ability_description_label.pack(side='left', padx=5)
        
        # Bind dropdown selection to show description
        self.ability_dropdown.bind('<<ComboboxSelected>>', self.on_ability_selected)
        
        # Create ability list frame
        self.ability_list_frame = ttk.Frame(frame)
        self.ability_list_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Ability list label
        ttk.Label(self.ability_list_frame, text="Selected Abilities:").pack(anchor='w', padx=5)
        
        # Create frame for listbox and description side by side
        listbox_desc_frame = ttk.Frame(self.ability_list_frame)
        listbox_desc_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Create listbox frame (left side)
        listbox_frame = ttk.Frame(listbox_desc_frame)
        listbox_frame.pack(side='left', fill='both', expand=True)
        
        # Create listbox for selected abilities
        self.ability_listbox = tk.Listbox(listbox_frame, height=10, width=30)
        self.ability_listbox.pack(side='left', fill='both', expand=True)
        
        # Create scrollbar for listbox
        listbox_scrollbar = tk.Scrollbar(listbox_frame, orient='vertical', command=self.ability_listbox.yview)
        listbox_scrollbar.pack(side='right', fill='y')
        self.ability_listbox.config(yscrollcommand=listbox_scrollbar.set)
        
        # Create description frame (right side)
        desc_frame = ttk.Frame(listbox_desc_frame)
        desc_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        # Description label
        ttk.Label(desc_frame, text="Selected Ability Description:", font=('Arial', 10, 'bold')).pack(anchor='w')
        
        # Create text widget for description with scrollbar
        desc_text_frame = ttk.Frame(desc_frame)
        desc_text_frame.pack(fill='both', expand=True, pady=(5, 0))
        
        self.selected_ability_description = tk.Text(desc_text_frame, height=10, width=40, wrap='word', state='disabled')
        self.selected_ability_description.pack(side='left', fill='both', expand=True)
        
        desc_scrollbar = tk.Scrollbar(desc_text_frame, orient='vertical', command=self.selected_ability_description.yview)
        desc_scrollbar.pack(side='right', fill='y')
        self.selected_ability_description.config(yscrollcommand=desc_scrollbar.set)
        
        # Remove button
        self.remove_ability_button = ttk.Button(self.ability_list_frame, text="Remove Selected", 
                                              command=self.remove_ability)
        self.remove_ability_button.pack(anchor='w', padx=5)
        
        # Bind listbox selection to show description
        self.ability_listbox.bind('<<ListboxSelect>>', self.on_listbox_selection)
        
        # Initialize ability list
        if 'selectedAbilities' not in self.character_data:
            self.character_data['selectedAbilities'] = []
        
        # Create ability availability label
        self.ability_availability_label = ttk.Label(frame, text="", font=('Arial', 9, 'italic'))
        self.ability_availability_label.pack(anchor='w', padx=5, pady=2)
        
        # Update the dropdown and display
        self.update_ability_dropdown()
        self.update_ability_list()
        self.update_ability_availability()
        
        # Update visibility (for Dragon's Breath)
        self.update_ability_visibility()
    
    def update_ability_dropdown(self):
        """Update the ability dropdown based on the level 1 D12 aspect"""
        level_one_d12_aspect = self.character_data.get('levelOneD12Aspect')
        
        if level_one_d12_aspect and level_one_d12_aspect in self.ASPECT_ABILITIES:
            # Get all abilities for the specific aspect
            all_abilities = list(self.ASPECT_ABILITIES[level_one_d12_aspect].keys())
            
            # Get currently selected abilities
            selected_abilities = self.character_data.get('selectedAbilities', [])
            
            # Filter out already selected abilities
            available_abilities = [ability for ability in all_abilities if ability not in selected_abilities]
            
            self.ability_dropdown['values'] = available_abilities
            
            if available_abilities:
                self.ability_dropdown.set(available_abilities[0])
                self.on_ability_selected()
            else:
                self.ability_dropdown.set('')
                self.ability_description_label.config(text="No more abilities available")
        else:
            # No D12 aspect set, show empty dropdown
            self.ability_dropdown['values'] = []
            self.ability_dropdown.set('')
            self.ability_description_label.config(text="Select a D12 aspect first")
        
        # Update availability display and button state
        self.update_ability_availability()
    
    def on_ability_selected(self, event=None):
        """Show description when an ability is selected"""
        selected_ability = self.ability_var.get()
        level_one_d12_aspect = self.character_data.get('levelOneD12Aspect')
        
        if selected_ability and level_one_d12_aspect and level_one_d12_aspect in self.ASPECT_ABILITIES:
            description = self.ASPECT_ABILITIES[level_one_d12_aspect].get(selected_ability, '')
            self.ability_description_label.config(text=description)
        else:
            self.ability_description_label.config(text="")
    
    def add_ability(self):
        """Add the selected ability to the list"""
        selected_ability = self.ability_var.get()
        if selected_ability:
            # Add to character data
            if 'selectedAbilities' not in self.character_data:
                self.character_data['selectedAbilities'] = []
            self.character_data['selectedAbilities'].append(selected_ability)
            
            # Remove the ability from the dropdown options
            current_values = list(self.ability_dropdown['values'])
            if selected_ability in current_values:
                current_values.remove(selected_ability)
                self.ability_dropdown['values'] = current_values
                
                # If the dropdown is now empty, disable the add button
                if not current_values:
                    self.add_ability_button.config(state='disabled')
                    self.ability_var.set('')
                    self.ability_description_label.config(text="No more abilities available")
                else:
                    # Set the dropdown to the first available ability
                    self.ability_dropdown.set(current_values[0])
                    self.on_ability_selected()
            
            # Update the display
            self.update_ability_list()
            self.update_ability_availability()
            print(f"[DEBUG] Added ability: {selected_ability}")
            print(f"[DEBUG] Remaining abilities: {current_values}")
    
    def remove_ability(self):
        """Remove the selected ability from the list"""
        selection = self.ability_listbox.curselection()
        if selection:
            index = selection[0]
            if 'selectedAbilities' in self.character_data and index < len(self.character_data['selectedAbilities']):
                removed_ability = self.character_data['selectedAbilities'].pop(index)
                
                # Add the ability back to the dropdown options
                current_values = list(self.ability_dropdown['values'])
                if removed_ability not in current_values:
                    current_values.append(removed_ability)
                    # Sort the abilities to maintain order
                    level_one_d12_aspect = self.character_data.get('levelOneD12Aspect')
                    if level_one_d12_aspect and level_one_d12_aspect in self.ASPECT_ABILITIES:
                        aspect_abilities = list(self.ASPECT_ABILITIES[level_one_d12_aspect].keys())
                        # Sort current_values based on the original order
                        sorted_values = [ability for ability in aspect_abilities if ability in current_values]
                        self.ability_dropdown['values'] = sorted_values
                    
                    # Re-enable the add button if it was disabled
                    self.add_ability_button.config(state='normal')
                    
                    # Set the dropdown to the removed ability
                    self.ability_dropdown.set(removed_ability)
                    self.on_ability_selected()
                
                self.update_ability_list()
                self.update_ability_availability()
                print(f"[DEBUG] Removed ability: {removed_ability}")
                print(f"[DEBUG] Available abilities: {self.ability_dropdown['values']}")
    
    def update_ability_list(self):
        """Update the ability listbox display"""
        self.ability_listbox.delete(0, tk.END)
        selected_abilities = self.character_data.get('selectedAbilities', [])
        for ability in selected_abilities:
            self.ability_listbox.insert(tk.END, ability)
        
        # Clear description if no abilities selected
        if not selected_abilities:
            self.selected_ability_description.config(state='normal')
            self.selected_ability_description.delete(1.0, tk.END)
            self.selected_ability_description.config(state='disabled')
    
    def on_listbox_selection(self, event=None):
        """Show description when an ability is selected in the listbox"""
        selection = self.ability_listbox.curselection()
        if selection:
            index = selection[0]
            selected_abilities = self.character_data.get('selectedAbilities', [])
            if index < len(selected_abilities):
                selected_ability = selected_abilities[index]
                level_one_d12_aspect = self.character_data.get('levelOneD12Aspect')
                
                if level_one_d12_aspect and level_one_d12_aspect in self.ASPECT_ABILITIES:
                    description = self.ASPECT_ABILITIES[level_one_d12_aspect].get(selected_ability, '')
                    
                    # Update the description text widget
                    self.selected_ability_description.config(state='normal')
                    self.selected_ability_description.delete(1.0, tk.END)
                    self.selected_ability_description.insert(1.0, description)
                    self.selected_ability_description.config(state='disabled')
                else:
                    self.selected_ability_description.config(state='normal')
                    self.selected_ability_description.delete(1.0, tk.END)
                    self.selected_ability_description.config(state='disabled')
        else:
            # No selection, clear description
            self.selected_ability_description.config(state='normal')
            self.selected_ability_description.delete(1.0, tk.END)
            self.selected_ability_description.config(state='disabled')
    
    def get_ability_ranks_for_specialization(self, specialization):
        """Get the ranks when abilities are gained for a given specialization"""
        return self.ABILITY_RANKS.get(specialization, [1, 4, 8])  # Default to Non-Specialized
    
    def get_available_abilities_count(self):
        """Get the number of abilities the character should have at their current rank"""
        current_rank = self.character_data.get('rank', 1)
        specialization = self.character_data.get('type', 'Non-Specialized')
        ability_ranks = self.get_ability_ranks_for_specialization(specialization)
        
        # Count how many ability ranks are at or below current rank
        available_count = sum(1 for rank in ability_ranks if rank <= current_rank)
        return available_count
    
    def update_ability_availability(self):
        """Update the ability availability display"""
        current_rank = self.character_data.get('rank', 1)
        specialization = self.character_data.get('type', 'Non-Specialized')
        ability_ranks = self.get_ability_ranks_for_specialization(specialization)
        current_abilities = len(self.character_data.get('selectedAbilities', []))
        available_count = self.get_available_abilities_count()
        
        # Find next ability rank
        next_ability_rank = None
        for rank in ability_ranks:
            if rank > current_rank:
                next_ability_rank = rank
                break
        
        # Create availability message
        if current_abilities < available_count:
            message = f"Available abilities: {current_abilities}/{available_count} (Rank {current_rank})"
            if next_ability_rank:
                message += f" - Next ability at rank {next_ability_rank}"
        elif current_abilities == available_count:
            message = f"All abilities gained: {current_abilities}/{available_count} (Rank {current_rank})"
            if next_ability_rank:
                message += f" - Next ability at rank {next_ability_rank}"
        else:
            message = f"Warning: {current_abilities} abilities selected, but only {available_count} should be available at rank {current_rank}"
        
        self.ability_availability_label.config(text=message)
        
        # Update button state based on availability
        if current_abilities >= available_count:
            self.add_ability_button.config(state='disabled')
        else:
            # Check if dropdown has values and button should be enabled
            if self.ability_dropdown['values']:
                self.add_ability_button.config(state='normal')
            else:
                self.add_ability_button.config(state='disabled')
    
    def update_ability_visibility(self):
        """Update visibility of Dragon's Breath ability based on race"""
        current_rank = self.character_data.get('rank', 1)
        current_race = self.character_data.get('race', '')
        
        print(f"[DEBUG] update_ability_visibility: race={current_race}, rank={current_rank}")
        
        # Show/hide Dragon's Breath ability
        if current_race == 'Half-Dragon':
            print(f"[DEBUG] Showing Dragon's Breath for Half-Dragon")
            self.dragons_breath_frame.pack(fill='x', padx=5, pady=2)
            # Update range and damage values
            range_value = 10 + (5 * (current_rank - 1))
            
            # Calculate damage based on rank
            if current_rank >= 11:
                damage = "1d12+1d4"
            elif current_rank >= 9:
                damage = "1d12"
            elif current_rank >= 7:
                damage = "1d10"
            elif current_rank >= 5:
                damage = "1d8"
            elif current_rank >= 3:
                damage = "1d6"
            else:
                damage = "1d4"
                
            # Calculate uses per encounter based on rank
            uses = 1
            if current_rank >= 11:
                uses = 4
            elif current_rank >= 9:
                uses = 3
            elif current_rank >= 5:
                uses = 2
                
            self.dragons_breath_label.config(text=f"Range: 10x{range_value} feet\nDamage: {damage} fire damage\nUses per Encounter: {uses}")
        else:
            print(f"[DEBUG] Hiding Dragon's Breath for {current_race}")
            self.dragons_breath_frame.pack_forget()

    def get_data(self):
        """Get abilities data"""
        return {
            'selectedAbilities': self.character_data.get('selectedAbilities', [])
        }

    def set_data(self, data):
        """Set abilities data"""
        selected_abilities = data.get('selectedAbilities', [])
        
        # Update character data
        self.character_data['selectedAbilities'] = selected_abilities
        
        # Update the display
        self.update_ability_dropdown()
        self.update_ability_list()
        
        # Update visibility
        self.update_ability_visibility() 