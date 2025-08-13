import tkinter as tk
from tkinter import ttk
from aspect_abilities import ASPECT_ABILITIES

class AbilitiesTab:
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
        # Ensure auto abilities reflect current unarmed combat status
        self.sync_unarmed_auto_abilities(self.character_data.get('unarmedCombat', False))
        
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
        """Update the ability dropdown to include D12 aspect abilities plus universal abilities."""
        level_one_d12_aspect = self.character_data.get('levelOneD12Aspect')

        # Aspect-specific abilities (if any)
        aspect_abilities = []
        if level_one_d12_aspect and level_one_d12_aspect in ASPECT_ABILITIES:
            aspect_abilities = list(ASPECT_ABILITIES[level_one_d12_aspect].keys())

        # Universal abilities are always available to all characters
        universal_abilities = list(ASPECT_ABILITIES.get('universal', {}).keys())

        # Build combined list; put universal first (alphabetical), then aspect-defined order
        combined = sorted(universal_abilities) + aspect_abilities

        # Exclude already selected
        selected_abilities = self.character_data.get('selectedAbilities', [])
        available_abilities = [a for a in combined if a not in selected_abilities]

        self.ability_dropdown['values'] = available_abilities

        if available_abilities:
            self.ability_dropdown.set(available_abilities[0])
            self.on_ability_selected()
        else:
            self.ability_dropdown.set('')
            helper = "No more abilities available" if combined else "Select a D12 aspect first"
            self.ability_description_label.config(text=helper)
        
        # Update availability display and button state
        self.update_ability_availability()
    
    def on_ability_selected(self, event=None):
        """Show description when an ability is selected"""
        selected_ability = self.ability_var.get()
        level_one_d12_aspect = self.character_data.get('levelOneD12Aspect')

        description = ''
        if selected_ability:
            # Prefer universal, then aspect-specific, then unarmed
            description = ASPECT_ABILITIES.get('universal', {}).get(selected_ability, '')
            if not description and level_one_d12_aspect and level_one_d12_aspect in ASPECT_ABILITIES:
                description = ASPECT_ABILITIES[level_one_d12_aspect].get(selected_ability, '')
            if not description:
                description = ASPECT_ABILITIES.get('unarmed', {}).get(selected_ability, '')
        self.ability_description_label.config(text=description)
    
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

                # Prevent removal of auto-granted Unarmed abilities while enabled
                if removed_ability in self._get_unarmed_auto_abilities() and self.character_data.get('unarmedCombat', False):
                    # Re-insert it and return without changing UI
                    self.character_data['selectedAbilities'].insert(index, removed_ability)
                    return
                
                # Add the ability back to the dropdown options
                current_values = list(self.ability_dropdown['values'])
                if removed_ability not in current_values:
                    current_values.append(removed_ability)
                    # Sort the abilities to maintain order (universal alpha, then aspect order)
                    level_one_d12_aspect = self.character_data.get('levelOneD12Aspect')
                    aspect_abilities = []
                    if level_one_d12_aspect and level_one_d12_aspect in ASPECT_ABILITIES:
                        aspect_abilities = list(ASPECT_ABILITIES[level_one_d12_aspect].keys())
                    universal_abilities = list(ASPECT_ABILITIES.get('universal', {}).keys())
                    sorted_values = sorted([a for a in current_values if a in universal_abilities])
                    sorted_values += [a for a in aspect_abilities if a in current_values and a not in sorted_values]
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
                
                # Prefer universal, then aspect-specific, then unarmed
                description = ASPECT_ABILITIES.get('universal', {}).get(selected_ability, '')
                if not description and level_one_d12_aspect and level_one_d12_aspect in ASPECT_ABILITIES:
                    description = ASPECT_ABILITIES[level_one_d12_aspect].get(selected_ability, '')
                if not description:
                    description = ASPECT_ABILITIES.get('unarmed', {}).get(selected_ability, '')

                # Update the description text widget
                self.selected_ability_description.config(state='normal')
                self.selected_ability_description.delete(1.0, tk.END)
                self.selected_ability_description.insert(1.0, description)
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
        # Exclude auto-granted Unarmed abilities from the count
        selected = self.character_data.get('selectedAbilities', [])
        non_bonus_selected = [a for a in selected if a not in self._get_unarmed_auto_abilities()]
        current_abilities = len(non_bonus_selected)
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
        # Ensure auto abilities are synced based on current unarmed status
        self.sync_unarmed_auto_abilities(self.character_data.get('unarmedCombat', False))
        
        # Update the display
        self.update_ability_dropdown()
        self.update_ability_list()
        
        # Update visibility
        self.update_ability_visibility() 

    # --- Unarmed auto abilities support ---
    def _get_unarmed_auto_abilities(self):
        return ['Flurry of Blows', 'Stunning Strike']

    def sync_unarmed_auto_abilities(self, enabled: bool):
        """Auto-add or remove Unarmed Combat abilities based on checkbox. These do not count toward ability limits."""
        auto = self._get_unarmed_auto_abilities()
        selected = self.character_data.setdefault('selectedAbilities', [])
        changed = False
        if enabled:
            for a in auto:
                if a not in selected:
                    selected.append(a)
                    changed = True
        else:
            # Remove auto abilities if present
            new_selected = [a for a in selected if a not in auto]
            if len(new_selected) != len(selected):
                self.character_data['selectedAbilities'] = new_selected
                changed = True
        if changed:
            self.update_ability_list()
            self.update_ability_availability()