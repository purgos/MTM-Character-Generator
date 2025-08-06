import tkinter as tk
from tkinter import ttk, messagebox
from spells import SPELLS

class GearDieTab:
    def __init__(self, parent, character_data):
        self.parent = parent
        self.character_data = character_data
        self.tab = ttk.Frame(parent)
        
        # Initialize gear die allocation data
        if 'gearDieAllocations' not in self.character_data:
            self.character_data['gearDieAllocations'] = {}
        
        # Gear die slot counts based on rank
        self.gear_die_slots = {
            'd4': 2,  # Start with 1 free d4 slot + 1 d4 slot
            'd6': 1,  # Start with 1 d6 slot
            'd8': 1,  # Start with 1 d8 slot
            'd10': 1,  # Start with 1 d10 slot
            'd12': 1  # Start with 1 d12 slot
        }
        
        # Store allocation widgets
        self.allocation_widgets = {}
        
        # Lock state
        self.choices_locked = False
        
        self.create_tab()
        
    def create_tab(self):
        """Create the gear die allocation tab"""
        # Clear existing content
        for widget in self.tab.winfo_children():
            widget.destroy()
            
        # Create a scrollable frame
        canvas = tk.Canvas(self.tab)
        scrollbar = ttk.Scrollbar(self.tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack the canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Main frame
        frame = ttk.LabelFrame(scrollable_frame, text="Gear Die Allocations")
        frame.pack(fill='both', expand=True, padx=5, pady=5)

        # Create allocation sections
        self.create_free_slot_section(frame)
        self.create_allocation_sections(frame)
        
    def create_free_slot_section(self, parent):
        """Create the free slot section"""
        free_frame = ttk.LabelFrame(parent, text="Free Slot - D4")
        free_frame.pack(fill='x', padx=5, pady=5)
        
        # Free slot options frame
        options_frame = ttk.Frame(free_frame)
        options_frame.pack(fill='x', padx=5, pady=5)
        
        # Label
        ttk.Label(options_frame, text="Free slot options:", 
                 font=('Arial', 9, 'bold')).pack(anchor='w', pady=(0, 5))
        
        # Free slot selection variable
        self.free_slot_var = tk.StringVar(value='none')
        
        # Create radio buttons for the three options
        self.none_radio = ttk.Radiobutton(options_frame, text="Single dagger, club, or similar small weapon", 
                                         variable=self.free_slot_var, value='none')
        self.none_radio.pack(anchor='w', padx=10, pady=2)
        
        self.improvised_radio = ttk.Radiobutton(options_frame, text="Improvised combat", 
                                               variable=self.free_slot_var, value='improvised')
        self.improvised_radio.pack(anchor='w', padx=10, pady=2)
        
        self.unarmed_radio = ttk.Radiobutton(options_frame, text="Unarmed", 
                                            variable=self.free_slot_var, value='unarmed')
        self.unarmed_radio.pack(anchor='w', padx=10, pady=2)
        
        # Description label
        self.free_slot_desc = ttk.Label(options_frame, text="", 
                                       wraplength=600, font=('Arial', 9), justify='left')
        self.free_slot_desc.pack(fill='x', padx=10, pady=(10, 0))
        
        # Bind the variable to update description
        self.free_slot_var.trace_add('write', self.on_free_slot_change)
        
        # Load existing free slot data
        self.load_free_slot_data()
    
    def create_allocation_sections(self, parent):
        """Create allocation sections for each die type"""
        # Create sections for each die type
        for die in ['d4', 'd6', 'd8', 'd10', 'd12']:
            self.create_die_allocation_section(parent, die)
    
    def create_die_allocation_section(self, parent, die):
        """Create allocation section for a specific die type"""
        # Skip d4 if it's the free slot (we handle regular d4 slots separately)
        if die == 'd4':
            num_slots = max(0, self.gear_die_slots[die] - 1)  # Subtract free slot
        else:
            num_slots = self.gear_die_slots[die]
        
        if num_slots <= 0:
            return
        
        # Create frame for this die type
        die_frame = ttk.LabelFrame(parent, text=f"{die.upper()} Slots ({num_slots} available)")
        die_frame.pack(fill='x', padx=5, pady=2)
        
        # Store widgets for this die type
        self.allocation_widgets[die] = []
        
        # Create allocation widgets for each slot
        for slot_num in range(num_slots):
            slot_widgets = self.create_slot_allocation_widgets(die_frame, die, slot_num)
            self.allocation_widgets[die].append(slot_widgets)
    
    def create_slot_allocation_widgets(self, parent, die, slot_num):
        """Create widgets for a single slot allocation"""
        slot_frame = ttk.Frame(parent)
        slot_frame.pack(fill='x', padx=5, pady=2)
        
        # Top row for controls
        controls_frame = ttk.Frame(slot_frame)
        controls_frame.pack(fill='x', pady=2)
        
        # Slot label
        ttk.Label(controls_frame, text=f"Slot {slot_num + 1}:", width=8).pack(side='left', padx=2)
        
        # Allocation type dropdown
        allocation_var = tk.StringVar(value='hitpoints')
        allocation_combo = ttk.Combobox(controls_frame, textvariable=allocation_var, 
                                      values=['hitpoints', 'spell', 'melee', 'ranged', 'shield', 'tower shield', 'armor', 'dodge', 'parry'],
                                      state='readonly', width=10)
        allocation_combo.pack(side='left', padx=2)
        
        # Value entry (for melee/ranged/shield/armor/dodge/parry) - larger
        value_var = tk.StringVar()
        value_entry = ttk.Entry(controls_frame, textvariable=value_var, width=40)
        value_entry.pack(side='left', padx=2)
        
        # Spell dropdown (initially hidden) - larger
        spell_var = tk.StringVar()
        spell_combo = ttk.Combobox(controls_frame, textvariable=spell_var, width=50)
        spell_combo.pack(side='left', padx=2)
        spell_combo.pack_forget()  # Initially hidden
        
        # Bottom row for description
        desc_frame = ttk.Frame(slot_frame)
        desc_frame.pack(fill='x', pady=2)
        
        # Description label - larger and with more space
        desc_label = ttk.Label(desc_frame, text="", wraplength=800, font=('Arial', 9), justify='left')
        desc_label.pack(fill='x', padx=10, pady=2)
        
        # Store widget references
        widgets = {
            'allocation_var': allocation_var,
            'allocation_combo': allocation_combo,
            'value_var': value_var,
            'value_entry': value_entry,
            'spell_var': spell_var,
            'spell_combo': spell_combo,
            'desc_label': desc_label,
            'die': die,  # Store the die type for option filtering
            'slot_num': slot_num  # Store the slot number for unique allocation checking
        }
        
        # Bind events
        allocation_combo.bind('<<ComboboxSelected>>', 
                            lambda e, w=widgets, d=die, s=slot_num: self.on_allocation_type_change(w, d, s))
        spell_combo.bind('<<ComboboxSelected>>', 
                        lambda e, w=widgets, d=die, s=slot_num: self.on_spell_selected(w, d, s))
        
        # Load existing data
        self.load_slot_data(widgets, die, slot_num)
        
        # Update dropdown options based on unarmed combat status
        self.update_allocation_options(widgets)
        
        # Trigger change handler for default value if no existing data
        if not self.character_data.get('gearDieAllocations', {}).get(f"{die}_{slot_num}"):
            self.on_allocation_type_change(widgets, die, slot_num)
        
        return widgets
    
    def on_free_slot_change(self, *args):
        """Handle free slot option change"""
        option = self.free_slot_var.get()
        
        # Update description based on selection
        descriptions = {
            'none': "Character can use a single dagger, club, or similar small weapon.",
            'improvised': "Character can use improvised weapons and objects in combat.",
            'unarmed': "Character is trained in unarmed combat techniques."
        }
        
        self.free_slot_desc.config(text=descriptions.get(option, ""))
        
        # Save the free slot data
        self.save_free_slot_data()
    
    def update_free_slot_radio_states(self):
        """Update radio button states based on unarmed combat status"""
        if not hasattr(self, 'none_radio') or not hasattr(self, 'improvised_radio') or not hasattr(self, 'unarmed_radio'):
            return
        
        unarmed_combat = self.character_data.get('unarmedCombat', False)
        
        if unarmed_combat:
            # When unarmed combat is enabled, force unarmed choice and disable other options
            self.free_slot_var.set('unarmed')
            self.none_radio.config(state='disabled')
            self.improvised_radio.config(state='disabled')
            self.unarmed_radio.config(state='normal')
        else:
            # When unarmed combat is disabled, enable none and improvised, disable unarmed
            if self.free_slot_var.get() == 'unarmed':
                self.free_slot_var.set('none')
            self.none_radio.config(state='normal')
            self.improvised_radio.config(state='normal')
            self.unarmed_radio.config(state='disabled')
    
    def load_free_slot_data(self):
        """Load existing free slot data"""
        free_slot_data = self.character_data.get('freeSlotOption', 'none')
        self.free_slot_var.set(free_slot_data)
        self.on_free_slot_change()  # Update description
        self.update_free_slot_radio_states()  # Update radio button states
    
    def save_free_slot_data(self):
        """Save free slot data to character data"""
        self.character_data['freeSlotOption'] = self.free_slot_var.get()
    
    def on_allocation_type_change(self, widgets, die, slot_num):
        """Handle allocation type change"""
        allocation_type = widgets['allocation_var'].get()
        
        # Check if parry is selected but unarmed combat is not enabled
        if allocation_type == 'parry' and not self.character_data.get('unarmedCombat', False):
            messagebox.showwarning("Unarmed Combat Required", 
                                 "Parry is only available when Unarmed Combat is selected.")
            # Reset to hitpoints
            widgets['allocation_var'].set('hitpoints')
            allocation_type = 'hitpoints'
        
        # Check if unarmed is selected but unarmed combat is not enabled
        if allocation_type == 'unarmed' and not self.character_data.get('unarmedCombat', False):
            messagebox.showwarning("Unarmed Combat Required", 
                                 "Unarmed is only available when Unarmed Combat is selected.")
            # Reset to hitpoints
            widgets['allocation_var'].set('hitpoints')
            allocation_type = 'hitpoints'
        
        # Hide/show appropriate widgets
        if allocation_type == 'spell':
            widgets['value_entry'].pack_forget()
            widgets['spell_combo'].pack(side='left', padx=2)
            self.update_spell_dropdown(widgets, die)
        else:
            widgets['spell_combo'].pack_forget()
            widgets['value_entry'].pack(side='left', padx=2)
            
            if allocation_type == 'hitpoints':
                # Set hitpoints value based on die
                hp_values = {'d4': 2, 'd6': 3, 'd8': 4, 'd10': 5, 'd12': 6}
                widgets['value_var'].set(str(hp_values[die]))
                widgets['value_entry'].config(state='readonly')
                widgets['desc_label'].config(text=f"Adds {hp_values[die]} hitpoints")
            else:  # melee, ranged, shield, tower shield, armor, dodge, parry, or unarmed
                widgets['value_entry'].config(state='normal')
                widgets['value_var'].set('')
                widgets['desc_label'].config(text=f"Enter {allocation_type} bonus value")
        
        # Save the allocation
        self.save_slot_data(widgets, die, slot_num)
        
        # Update all allocation options to reflect the new unique allocation usage
        self.update_allocation_options_for_all_slots()
    
    def update_allocation_options(self, widgets):
        """Update allocation dropdown options based on unarmed combat status, die type, and aspect status"""
        unarmed_combat = self.character_data.get('unarmedCombat', False)
        current_selection = widgets['allocation_var'].get()
        die = widgets.get('die', 'd12')  # Default to d12 if not found
        slot_num = widgets.get('slot_num', 0)  # Get slot number
        
        # Get aspect status
        aspects = self.character_data.get('aspects', {})
        melee_aspect = aspects.get('melee', 'd4')
        ranged_aspect = aspects.get('ranged', 'd4')
        magic_aspect = aspects.get('magic', 'd4')
        
        # Get currently used unique allocation types, excluding the current slot
        used_unique_allocations = self.get_used_unique_allocations(exclude_slot=f"{die}_{slot_num}")
        
        # Get currently used defensive options (dodge/parry are mutually exclusive)
        used_defensive_options = self.get_mutually_exclusive_defensive_options(exclude_slot=f"{die}_{slot_num}")
        
        # Base options (excluding spell - will add conditionally)
        options = ['hitpoints']
        
        # Add shield only if unarmed combat is not selected
        if not unarmed_combat:
            options.append('shield')
        
        # Add tower shield only if unarmed combat is not selected and die is d4
        if not unarmed_combat and die == 'd4':
            options.append('tower shield')
        
        # Add dodge only if unarmed combat is selected and no defensive option is used
        if unarmed_combat and not used_defensive_options:
            options.append('dodge')
        
        # Add armor only if unarmed combat is not selected and not already used
        if not unarmed_combat and 'armor' not in used_unique_allocations:
            options.append('armor')
        
        # Add spell only if magic aspect is not disabled
        if magic_aspect != 'NULL':
            options.append('spell')
        
        # Add melee only if melee aspect is not disabled and unarmed combat is not selected
        if melee_aspect != 'NULL' and not unarmed_combat:
            options.append('melee')
        
        # Add ranged only if ranged aspect is not disabled
        if ranged_aspect != 'NULL':
            options.append('ranged')
        
        # Add unarmed options for d4, d6, d8 slots if unarmed combat is enabled
        if unarmed_combat and die in ['d4', 'd6', 'd8']:
            options.append('unarmed')
        
        # Add parry only if unarmed combat is enabled and no defensive option is used
        if unarmed_combat and not used_defensive_options:
            options.append('parry')
        
        # Update dropdown values
        widgets['allocation_combo']['values'] = options
        
        # If current selection is no longer valid, reset to hitpoints
        if current_selection not in options:
            widgets['allocation_var'].set('hitpoints')
            # Trigger the change handler
            self.on_allocation_type_change(widgets, die, slot_num)

    def get_used_unique_allocations(self, exclude_slot=None):
        """Get list of unique allocation types that are currently in use"""
        unique_allocations = ['dodge', 'parry', 'armor']
        used_allocations = []
        
        allocations = self.character_data.get('gearDieAllocations', {})
        
        for slot_key, data in allocations.items():
            # Skip the excluded slot
            if exclude_slot and slot_key == exclude_slot:
                continue
                
            allocation_type = data.get('type', '')
            if allocation_type in unique_allocations:
                used_allocations.append(allocation_type)
        
        return used_allocations

    def get_mutually_exclusive_defensive_options(self, exclude_slot=None):
        """Get list of defensive options that are mutually exclusive (dodge/parry)"""
        defensive_options = ['dodge', 'parry']
        used_defensive = []
        
        allocations = self.character_data.get('gearDieAllocations', {})
        
        for slot_key, data in allocations.items():
            # Skip the excluded slot
            if exclude_slot and slot_key == exclude_slot:
                continue
                
            allocation_type = data.get('type', '')
            if allocation_type in defensive_options:
                used_defensive.append(allocation_type)
        
        return used_defensive
    
    def update_allocation_options_for_all_slots(self):
        """Update allocation options for all slots when unarmed combat status changes"""
        for die in self.allocation_widgets:
            for slot_widgets in self.allocation_widgets[die]:
                self.update_allocation_options(slot_widgets)
    
    def update_spell_dropdown(self, widgets, die):
        """Update spell dropdown with available spells"""
        # Get character's magic aspect
        magic_aspect = self.character_data.get('aspects', {}).get('magic', 'NULL')
        
        # Filter spells by prerequisites
        available_spells = []
        for spell_name, spell_data in SPELLS.items():
            prerequisite = spell_data.get('prerequisite', '')
            if self.check_prerequisite(prerequisite, magic_aspect):
                available_spells.append(spell_name)
        
        # Update dropdown
        widgets['spell_combo']['values'] = available_spells
        if available_spells:
            widgets['spell_combo'].set(available_spells[0])
            self.on_spell_selected(widgets, die, 0)  # slot_num not used in this context
        else:
            widgets['spell_combo'].set('')
            widgets['desc_label'].config(text="No spells available with current prerequisites")
    
    def check_prerequisite(self, prerequisite, magic_aspect):
        """Check if character meets spell prerequisite"""
        if not prerequisite or magic_aspect == 'NULL':
            return False
        
        # Parse prerequisite (e.g., "Magic Aspect D8")
        if 'Magic Aspect' in prerequisite:
            required_die = prerequisite.split()[-1]  # Get the die value (D8, D12, etc.)
            die_values = {'d4': 1, 'd6': 2, 'd8': 3, 'd10': 4, 'd12': 5}
            magic_die_values = {'d4': 1, 'd6': 2, 'd8': 3, 'd10': 4, 'd12': 5}
            
            required_level = die_values.get(required_die.lower(), 0)
            magic_level = magic_die_values.get(magic_aspect.lower(), 0)
            
            return magic_level >= required_level
        
        return False
    
    def on_spell_selected(self, widgets, die, slot_num):
        """Handle spell selection"""
        spell_name = widgets['spell_var'].get()
        if spell_name in SPELLS:
            spell_data = SPELLS[spell_name]
            # Show full spell description with all details
            description = f"{spell_name}\n"
            description += f"Prerequisite: {spell_data.get('prerequisite', 'None')}\n"
            description += f"Components: {', '.join(spell_data.get('spell_components', []))}\n"
            if spell_data.get('material_component'):
                description += f"Material: {spell_data['material_component']}\n"
            description += f"Area: {spell_data.get('area_of_effect', 'None')}\n"
            description += f"Duration: {spell_data.get('duration', 'None')}\n"
            description += f"Frequency: {spell_data.get('frequency', 'None')}\n"
            description += f"Description: {spell_data['description']}"
            widgets['desc_label'].config(text=description)
            self.save_slot_data(widgets, die, slot_num)
    
    def load_slot_data(self, widgets, die, slot_num):
        """Load existing slot data"""
        allocations = self.character_data.get('gearDieAllocations', {})
        slot_key = f"{die}_{slot_num}"
        
        if slot_key in allocations:
            data = allocations[slot_key]
            widgets['allocation_var'].set(data.get('type', 'hitpoints'))
            self.on_allocation_type_change(widgets, die, slot_num)
            
            if data.get('type') == 'spell':
                widgets['spell_var'].set(data.get('value', ''))
            else:
                widgets['value_var'].set(data.get('value', ''))
    
    def save_slot_data(self, widgets, die, slot_num):
        """Save slot data to character data"""
        slot_key = f"{die}_{slot_num}"
        allocation_type = widgets['allocation_var'].get()
        
        if allocation_type == 'spell':
            value = widgets['spell_var'].get()
        else:
            value = widgets['value_var'].get()
        
        if 'gearDieAllocations' not in self.character_data:
            self.character_data['gearDieAllocations'] = {}
        
        self.character_data['gearDieAllocations'][slot_key] = {
            'type': allocation_type,
            'value': value,
            'die': die
        }
        
        # Notify basic info tab to update max HP if this was a hitpoints allocation
        if allocation_type == 'hitpoints':
            self.notify_max_hp_update()
    
    def update_slots_for_rank(self, rank):
        """Update gear die slots based on character rank"""
        # Reset to base values
        self.gear_die_slots = {
            'd4': 2,  # 1 free + 1 regular
            'd6': 1,
            'd8': 1,
            'd10': 1,
            'd12': 1
        }
        
        # Apply rank-based increases
        if rank >= 3:
            self.gear_die_slots['d4'] += 2
        if rank >= 5:
            self.gear_die_slots['d6'] += 2
        if rank >= 7:
            self.gear_die_slots['d8'] += 2
        if rank >= 9:
            self.gear_die_slots['d10'] += 2
        if rank >= 11:
            self.gear_die_slots['d12'] += 2
        
        # Update character data
        self.character_data['gearDieSlots'] = self.gear_die_slots.copy()
        
        # Recreate the tab
        self.create_tab()
    
    def on_unarmed_combat_change(self, unarmed_combat):
        """Handle unarmed combat status change"""
        # Update allocation options for all slots
        self.update_allocation_options_for_all_slots()
        
        # Update radio button states (handles auto-selection and enabling/disabling)
        self.update_free_slot_radio_states()
    
    def on_aspects_change(self):
        """Handle aspect changes - update allocation options"""
        # Update allocation options for all slots
        self.update_allocation_options_for_all_slots()
    
    def get_data(self):
        """Get gear die allocation data"""
        return {
            'gearDieSlots': self.gear_die_slots.copy(),
            'gearDieAllocations': self.character_data.get('gearDieAllocations', {}),
            'freeSlotOption': self.character_data.get('freeSlotOption', 'none'),
            'choices_locked': self.choices_locked
        }
    
    def calculate_gear_die_hitpoints(self):
        """Calculate total hitpoints from gear die allocations"""
        total_hp = 0
        allocations = self.character_data.get('gearDieAllocations', {})
        
        for slot_key, data in allocations.items():
            if data.get('type') == 'hitpoints':
                # The value is already calculated as 1/2 the die value
                try:
                    hp_value = int(data.get('value', 0))
                    total_hp += hp_value
                except (ValueError, TypeError):
                    pass
        
        return total_hp
    
    def notify_max_hp_update(self):
        """Notify the basic info tab to update max HP display"""
        # This will be set by the main character sheet
        if hasattr(self, 'max_hp_callback'):
            self.max_hp_callback()
    
    def set_data(self, data):
        """Set gear die allocation data"""
        # Update character data
        self.character_data.update(data)
        
        # Update slots for current rank
        current_rank = self.character_data.get('rank', 1)
        self.update_slots_for_rank(current_rank)
        
        # Load free slot data if available
        if hasattr(self, 'free_slot_var'):
            self.load_free_slot_data()
        
        # Notify basic info tab to update max HP if there are hitpoints allocations
        if 'gearDieAllocations' in data:
            allocations = data['gearDieAllocations']
            has_hitpoints = any(allocation.get('type') == 'hitpoints' for allocation in allocations.values())
            if has_hitpoints:
                self.notify_max_hp_update()
        
        # Handle lock state
        self.choices_locked = data.get('choices_locked', False)
        if self.choices_locked:
            self.lock_gear_die_choices()

    def lock_gear_die_choices(self):
        """Lock gear die choices - only hitpoints, dodge, and parry are locked"""
        self.choices_locked = True
        
        # Lock allocation types that should be locked
        locked_allocation_types = ['hitpoints', 'dodge', 'parry']
        
        for die in self.allocation_widgets:
            for slot_widgets in self.allocation_widgets[die]:
                allocation_type = slot_widgets['allocation_var'].get()
                
                if allocation_type in locked_allocation_types:
                    # Lock the allocation combo and value entry
                    slot_widgets['allocation_combo'].config(state='disabled')
                    slot_widgets['value_entry'].config(state='disabled')
                    
                    # Lock spell combo if it's a spell allocation
                    if allocation_type == 'spell':
                        slot_widgets['spell_combo'].config(state='disabled')
                else:
                    # Keep other allocation types unlocked
                    slot_widgets['allocation_combo'].config(state='readonly')
                    slot_widgets['value_entry'].config(state='normal')
                    
                    # Keep spell combo unlocked if it's a spell allocation
                    if allocation_type == 'spell':
                        slot_widgets['spell_combo'].config(state='readonly')
        
        # Lock free slot radio buttons
        if hasattr(self, 'none_radio'):
            self.none_radio.config(state='disabled')
        if hasattr(self, 'improvised_radio'):
            self.improvised_radio.config(state='disabled')
        if hasattr(self, 'unarmed_radio'):
            self.unarmed_radio.config(state='disabled')

    def unlock_gear_die_choices(self):
        """Unlock all gear die choices"""
        self.choices_locked = False
        
        for die in self.allocation_widgets:
            for slot_widgets in self.allocation_widgets[die]:
                # Unlock all allocation combos
                slot_widgets['allocation_combo'].config(state='readonly')
                slot_widgets['value_entry'].config(state='normal')
                
                # Unlock spell combos
                if 'spell_combo' in slot_widgets:
                    slot_widgets['spell_combo'].config(state='readonly')
        
        # Unlock free slot radio buttons
        if hasattr(self, 'none_radio'):
            self.none_radio.config(state='normal')
        if hasattr(self, 'improvised_radio'):
            self.improvised_radio.config(state='normal')
        if hasattr(self, 'unarmed_radio'):
            self.unarmed_radio.config(state='normal') 