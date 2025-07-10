import tkinter as tk
from tkinter import ttk

class AbilitiesTab:
    def __init__(self, parent, character_data):
        self.parent = parent
        self.character_data = character_data
        self.tab = ttk.Frame(parent)
        
        # Initialize abilities data
        if 'specialAbilities' not in self.character_data:
            self.character_data['specialAbilities'] = {
                'rank1': '',
                'rank4': '',
                'rank8': ''
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

        # Rank 1 Ability
        self.rank1_frame = ttk.Frame(frame)
        ttk.Label(self.rank1_frame, text="Rank 1 Ability:").pack(side='left', padx=5)
        self.ability_1_text = tk.Text(self.rank1_frame, height=5, width=50)
        self.ability_1_text.pack(side='left', padx=5, fill='x', expand=True)

        # Rank 4 Ability
        self.rank4_frame = ttk.Frame(frame)
        ttk.Label(self.rank4_frame, text="Rank 4 Ability:").pack(side='left', padx=5)
        self.ability_4_text = tk.Text(self.rank4_frame, height=5, width=50)
        self.ability_4_text.pack(side='left', padx=5, fill='x', expand=True)

        # Rank 8 Ability
        self.rank8_frame = ttk.Frame(frame)
        ttk.Label(self.rank8_frame, text="Rank 8 Ability:").pack(side='left', padx=5)
        self.ability_8_text = tk.Text(self.rank8_frame, height=5, width=50)
        self.ability_8_text.pack(side='left', padx=5, fill='x', expand=True)

        # Update visibility based on current rank and race
        self.update_ability_visibility()

    def update_ability_visibility(self):
        """Update visibility of ability text boxes based on current rank and race"""
        current_rank = self.character_data.get('rank', 1)
        current_race = self.character_data.get('race', '')
        
        # Show/hide Dragon's Breath ability
        if current_race == 'Half-Dragon':
            self.dragons_breath_frame.pack(fill='x', padx=5, pady=2, before=self.rank1_frame)
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
            self.dragons_breath_frame.pack_forget()
            
        # Show/hide Rank 1 ability
        if current_rank >= 1:
            self.rank1_frame.pack(fill='x', padx=5, pady=2)
        else:
            self.rank1_frame.pack_forget()
            
        # Show/hide Rank 4 ability
        if current_rank >= 4:
            self.rank4_frame.pack(fill='x', padx=5, pady=2)
        else:
            self.rank4_frame.pack_forget()
            
        # Show/hide Rank 8 ability
        if current_rank >= 8:
            self.rank8_frame.pack(fill='x', padx=5, pady=2)
        else:
            self.rank8_frame.pack_forget()

    def get_data(self):
        """Get abilities data"""
        return {
            'specialAbilities': {
                'rank1': self.ability_1_text.get(1.0, tk.END).strip(),
                'rank4': self.ability_4_text.get(1.0, tk.END).strip(),
                'rank8': self.ability_8_text.get(1.0, tk.END).strip()
            }
        }

    def set_data(self, data):
        """Set abilities data"""
        special_abilities = data.get('specialAbilities', {})
        
        # Clear existing text
        self.ability_1_text.delete(1.0, tk.END)
        self.ability_4_text.delete(1.0, tk.END)
        self.ability_8_text.delete(1.0, tk.END)
        
        # Set new text
        self.ability_1_text.insert(1.0, special_abilities.get('rank1', ''))
        self.ability_4_text.insert(1.0, special_abilities.get('rank4', ''))
        self.ability_8_text.insert(1.0, special_abilities.get('rank8', ''))
        
        # Update character data
        self.character_data['specialAbilities'] = special_abilities
        
        # Update visibility
        self.update_ability_visibility() 