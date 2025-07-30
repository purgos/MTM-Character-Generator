import tkinter as tk
from tkinter import ttk

class GearDieTab:
    def __init__(self, parent, character_data):
        self.parent = parent
        self.character_data = character_data
        self.tab = ttk.Frame(parent)
        
        # Initialize gear die variables dictionary
        self.gear_die_slots = {
            'd4': tk.StringVar(value='2'),  # Start with 1 free d4 slot + 1 d4 slot
            'd6': tk.StringVar(value='1'),  # Start with 1 d6 slot
            'd8': tk.StringVar(value='1'),  # Start with 1 d8 slot
            'd10': tk.StringVar(value='1'),  # Start with 1 d10 slot
            'd12': tk.StringVar(value='1')  # Start with 1 d12 slot
        }
        self.gear_die_entries = {}  # Will store text entries for each slot
        
        self.create_tab()
        
    def create_tab(self):
        """Create the gear die tab with text boxes for each spell slot"""
        # Clear existing content
        for widget in self.tab.winfo_children():
            widget.destroy()
            
        # Main frame
        frame = ttk.LabelFrame(self.tab, text="Gear Die Slots")
        frame.pack(fill='both', expand=True, padx=5, pady=5)

        # Instructions and update button frame
        instructions_frame = ttk.Frame(frame)
        instructions_frame.pack(fill='x', padx=5, pady=5)
        
        instructions = ttk.Label(instructions_frame, 
                               text="You start with 1 free d4 slot, 1 d4 slot, 1 d6 slot, 1 d8 slot, 1 d10 slot, and 1 d12 slot.\n"
                                    "At rank 3: Gain 2 additional d4 slots\n"
                                    "At rank 5: Gain 2 additional d6 slots\n"
                                    "At rank 7: Gain 2 additional d8 slots\n"
                                    "At rank 9: Gain 2 additional d10 slots\n"
                                    "At rank 11: Gain 2 additional d12 slots",
                               wraplength=400)
        instructions.pack(side='left', padx=5)

        # Create Free Slot - D4 section first
        free_slot_frame = ttk.Frame(frame)
        free_slot_frame.pack(fill='x', padx=5, pady=2)

        # Free Slot label
        ttk.Label(free_slot_frame, text="Free Slot - D4:").pack(pady=2)

        # Create text entry for free slot
        free_slots_frame = ttk.Frame(free_slot_frame)
        free_slots_frame.pack(fill='x', padx=5)
        
        # Clear existing free slot entries
        if 'free_d4' in self.gear_die_entries:
            for entry in self.gear_die_entries['free_d4']:
                entry.destroy()
        self.gear_die_entries['free_d4'] = []
        
        # Create free slot entry
        entry_frame = ttk.Frame(free_slots_frame)
        entry_frame.pack(fill='x', pady=2)
        entry = ttk.Entry(entry_frame, width=30)
        entry.pack(side='left', padx=2, fill='x', expand=True)
        self.gear_die_entries['free_d4'].append(entry)
        
        # Initialize the free slot entry in character data
        if 'gearDieEntries' not in self.character_data:
            self.character_data['gearDieEntries'] = {'free_d4': [], 'd4': [], 'd6': [], 'd8': [], 'd10': [], 'd12': []}
        if len(self.character_data['gearDieEntries'].get('free_d4', [])) == 0:
            self.character_data['gearDieEntries']['free_d4'] = ['']
        else:
            entry.insert(0, self.character_data['gearDieEntries']['free_d4'][0])

        # Create a frame for each die type (excluding d4 since we handle it separately)
        for die in ['d4', 'd6', 'd8', 'd10', 'd12']:
            die_frame = ttk.Frame(frame)
            die_frame.pack(fill='x', padx=5, pady=2)

            # Die type label
            ttk.Label(die_frame, text=f"{die} Slots:").pack(pady=2)

            # Create text entries for each slot
            slots_frame = ttk.Frame(die_frame)
            slots_frame.pack(fill='x', padx=5)
            
            # Clear existing entries
            if die in self.gear_die_entries:
                for entry in self.gear_die_entries[die]:
                    entry.destroy()
            self.gear_die_entries[die] = []
            
            # For d4, we need to handle it differently since we already have the free slot
            if die == 'd4':
                # Create entries for regular d4 slots (excluding the free slot)
                num_regular_d4_slots = max(0, int(self.gear_die_slots[die].get()) - 1)
                for i in range(num_regular_d4_slots):
                    entry_frame = ttk.Frame(slots_frame)
                    entry_frame.pack(fill='x', pady=2)
                    entry = ttk.Entry(entry_frame, width=30)
                    entry.pack(side='left', padx=2, fill='x', expand=True)
                    self.gear_die_entries[die].append(entry)
                    # Initialize the entry in character data
                    if i >= len(self.character_data['gearDieEntries'].get(die, [])):
                        self.character_data['gearDieEntries'][die].append('')
                    else:
                        entry.insert(0, self.character_data['gearDieEntries'][die][i])
            else:
                # Create initial entries based on available slots for other die types
                for i in range(int(self.gear_die_slots[die].get())):
                    entry_frame = ttk.Frame(slots_frame)
                    entry_frame.pack(fill='x', pady=2)
                    entry = ttk.Entry(entry_frame, width=30)
                    entry.pack(side='left', padx=2, fill='x', expand=True)
                    self.gear_die_entries[die].append(entry)
                    # Initialize the entry in character data
                    if 'gearDieEntries' not in self.character_data:
                        self.character_data['gearDieEntries'] = {die: [] for die in ['free_d4', 'd4', 'd6', 'd8', 'd10', 'd12']}
                    if i >= len(self.character_data['gearDieEntries'].get(die, [])):
                        self.character_data['gearDieEntries'][die].append('')
                    else:
                        entry.insert(0, self.character_data['gearDieEntries'][die][i])

    def update_slots_for_rank(self, rank):
        """Update gear die slots based on character rank"""
        # Reset all slots to base values first
        base_slots = {
            'd4': 2,  # Start with 1 free d4 slot + 1 d4 slot
            'd6': 1,  # Start with 1 d6 slot
            'd8': 1,  # Start with 1 d8 slot
            'd10': 1,  # Start with 1 d10 slot
            'd12': 1  # Start with 1 d12 slot
        }
        
        # Apply rank-based increases
        if rank >= 3:  # Gain 2d4 slots
            base_slots['d4'] += 2
        if rank >= 5:  # Gain 2d6 slots
            base_slots['d6'] += 2
        if rank >= 7:  # Gain 2d8 slots
            base_slots['d8'] += 2
        if rank >= 9:  # Gain 2d10 slots
            base_slots['d10'] += 2
        if rank >= 11:  # Gain 2d12 slots
            base_slots['d12'] += 2
            
        # Update both the GUI variables and character data
        for die, slots in base_slots.items():
            self.gear_die_slots[die].set(str(slots))
            self.character_data['gearDieSlots'][die] = slots
        
        # Recreate the tab to show new slots
        self.create_tab()

    def get_data(self):
        """Get gear die data"""
        gear_die_entries = {}
        
        # Handle free_d4 slot
        if 'free_d4' in self.gear_die_entries:
            gear_die_entries['free_d4'] = [entry.get() for entry in self.gear_die_entries['free_d4']]
        else:
            gear_die_entries['free_d4'] = []
        
        # Handle other die types
        for die in ['d4', 'd6', 'd8', 'd10', 'd12']:
            if die in self.gear_die_entries:
                gear_die_entries[die] = [entry.get() for entry in self.gear_die_entries[die]]
            else:
                gear_die_entries[die] = []
        
        return {
            'gearDieSlots': {die: int(self.gear_die_slots[die].get()) for die in self.gear_die_slots},
            'gearDieEntries': gear_die_entries
        }

    def set_data(self, data):
        """Set gear die data"""
        # Update character data first
        self.character_data.update(data)
        
        # Update gear die slots for current rank
        current_rank = self.character_data.get('rank', 1)
        self.update_slots_for_rank(current_rank)
        
        # Set gear die entries from data
        gear_die_entries = data.get('gearDieEntries', {})
        
        # Ensure free_d4 is included in the gear die entries
        if 'free_d4' not in gear_die_entries:
            gear_die_entries['free_d4'] = ['']
        
        self.character_data['gearDieEntries'] = gear_die_entries
        
        # Recreate the tab to show the data
        self.create_tab() 