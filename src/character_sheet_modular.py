import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

# Import the tab modules
from tabs.basic_info_tab import BasicInfoTab
from tabs.aspects_tab import AspectsTab
from tabs.gear_die_tab import GearDieTab
from tabs.inventory_tab import InventoryTab
from tabs.abilities_tab import AbilitiesTab

class CharacterSheetGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MTM Character Sheet")
        self.root.geometry("1200x800")
        
        # Initialize character data
        self.character_data = {
            'name': '',
            'playerName': '',
            'rank': 1,
            'rankPoints': 0,
            'race': '',
            'profession': '',
            'type': 'Non-Specialized',
            'unarmedCombat': False,
            'aspects': {
                'melee': 'd4',
                'ranged': 'd4',
                'rogue': 'd4',
                'magic': 'd4'
            },
            'aspectIncreases': {
                'allowed': 0,
                'history': {}
            },
            'gearDieSlots': {
                'd4': 2,
                'd6': 1,
                'd8': 1,
                'd10': 1,
                'd12': 1
            },
            'gearDieEntries': {
                'd4': [],
                'd6': [],
                'd8': [],
                'd10': [],
                'd12': []
            },
            'combatStats': {
                'hp': 0,
                'maxHp': 0,
                'initiative': 0,
                'indoorSpeed': 30,
                'heroPoints': 0
            },
            'resources': {
                'money': 0,
                'magicDust': 0
            },
            'magicItems': [],
            'inventory': {
                'stored': [],
                'magic': [],
                'stored_magic': [],
                'elsewhere': []
            },
            'specialAbilities': {
                'rank1': '',
                'rank4': '',
                'rank8': ''
            }
        }
        
        self.create_menu_bar()
        self.create_notebook()
        
    def create_menu_bar(self):
        """Create the menu bar"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save Character", command=self.save_character)
        file_menu.add_command(label="Load Character", command=self.load_character)
        file_menu.add_command(label="Reset Character", command=self.reset_character)
        file_menu.add_separator()
        file_menu.add_command(label="Print Character", command=self.print_character)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
    def create_notebook(self):
        """Create the notebook with all tabs"""
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Create tab instances
        self.basic_info_tab = BasicInfoTab(self.notebook, self.character_data)
        self.aspects_tab = AspectsTab(
            self.notebook,
            self.character_data,
            lambda: None,  # on_data_change (no-op)
            lambda: int(self.basic_info_tab.rank_var.get())  # get_rank_callback
        )
        self.gear_die_tab = GearDieTab(self.notebook, self.character_data)
        self.inventory_tab = InventoryTab(self.notebook, self.character_data)
        self.abilities_tab = AbilitiesTab(self.notebook, self.character_data)
        
        # Add tabs to notebook
        self.notebook.add(self.basic_info_tab.tab, text="Basic Info")
        self.notebook.add(self.aspects_tab.tab, text="Aspects")
        self.notebook.add(self.gear_die_tab.tab, text="Gear Die")
        self.notebook.add(self.inventory_tab.tab, text="Inventory")
        self.notebook.add(self.abilities_tab.tab, text="Abilities")
        
        # Set up callbacks for rank updates
        self.basic_info_tab.total_rank_points_var.trace_add('write', self.on_rank_update)
        self.basic_info_tab.race_var.trace_add('write', self.on_race_update)
        self.basic_info_tab.unarmed_combat_var.trace_add('write', self.on_unarmed_combat_update)
        self.basic_info_tab.type_var.trace_add('write', self.on_type_update)
        
        # Initialize aspect die increases
        self.update_aspect_die_increases()

    def on_rank_update(self, *args):
        """Handle rank updates from basic info tab"""
        try:
            total_points = int(self.basic_info_tab.total_rank_points_var.get())
            new_rank = min(12, 1 + (total_points // 25))
            
            print(f"Rank update: total_points={total_points}, new_rank={new_rank}")
            
            # Update character data
            self.character_data['rank'] = new_rank
            self.character_data['rankPoints'] = total_points
            
            # Update the rank variable in the info tab so aspects_tab sees the new value
            self.basic_info_tab.rank_var.set(str(new_rank))
            
            # Ensure aspects tab locking logic is triggered
            self.aspects_tab.on_rank_change()
            
            # Lock fields if any points have been added (total_points > 0)
            if total_points > 0:
                print(f"Locking fields - first rank point added")
                self.basic_info_tab.lock_fields()
                self.aspects_tab.locked = True
                self.aspects_tab.update_lock_state()
            else:
                print(f"Not locking - no points added yet")
            
            # Update gear die slots
            self.gear_die_tab.update_slots_for_rank(new_rank)
            
            # Update abilities visibility
            self.abilities_tab.update_ability_visibility()
            
            # Update aspect die increases for the new rank
            self.update_aspect_die_increases()
            
        except ValueError as e:
            print(f"Error in on_rank_update: {e}")
            pass

    def on_race_update(self, *args):
        """Handle race updates from basic info tab"""
        race = self.basic_info_tab.race_var.get()
        self.character_data['race'] = race
        
        # Update abilities visibility
        self.abilities_tab.update_ability_visibility()

    def on_unarmed_combat_update(self, *args):
        """Handle unarmed combat checkbox changes"""
        unarmed_combat = self.basic_info_tab.unarmed_combat_var.get()
        self.character_data['unarmedCombat'] = unarmed_combat
        
        # Update aspects tab
        self.aspects_tab.update_unarmed_combat_effects(unarmed_combat)

    def on_type_update(self, *args):
        """Handle type/specialization changes"""
        new_type = self.basic_info_tab.type_var.get()
        print(f"[DEBUG] on_type_update called with new_type: {new_type}")
        self.character_data['type'] = new_type
        
        # First revert any existing locks and NULL values from previous specializations
        self.revert_specialization_effects()
        
        # Handle Specialized Caster selection
        if new_type == 'Specialized Caster':
            print(f"[DEBUG] Calling handle_specialized_caster_selection")
            self.handle_specialized_caster_selection()
        
        # Handle Specialized Warrior Melee selection
        elif new_type == 'Specialized Warrior Melee':
            print(f"[DEBUG] Calling handle_specialized_warrior_melee_selection")
            self.handle_specialized_warrior_melee_selection()
        
        # Handle Specialized Warrior Ranged selection
        elif new_type == 'Specialized Warrior Ranged':
            print(f"[DEBUG] Calling handle_specialized_warrior_ranged_selection")
            self.handle_specialized_warrior_ranged_selection()
        
        # Handle Specialized Rogue selection
        elif new_type == 'Specialized Rogue':
            print(f"[DEBUG] Calling handle_specialized_rogue_selection")
            self.handle_specialized_rogue_selection()
        
        # Handle Shield Master selection
        elif new_type == 'Shield Master':
            print(f"[DEBUG] Calling handle_shield_master_selection")
            self.handle_shield_master_selection()

    def revert_specialization_effects(self):
        """Revert any NULL values and locks that were applied by specializations"""
        # Reset all aspects to their original state (not NULL unless they were originally NULL)
        # and unlock all aspects
        for aspect in ['melee', 'ranged', 'rogue', 'magic']:
            # Only reset to NULL if it was set to NULL by a specialization
            # For now, we'll reset to NULL and let the user set them again
            # This is a simple approach - in a more complex system you might track the original values
            if self.character_data['aspects'].get(aspect) == 'NULL':
                # Reset to NULL (default state)
                self.character_data['aspects'][aspect] = 'NULL'
                self.aspects_tab.set_aspect_value(aspect, 'NULL')
            
            # Unlock the aspect (re-enable combobox and buttons)
            self.aspects_tab.unlock_aspect(aspect)

    def handle_specialized_caster_selection(self):
        """Show popup for Specialized Caster to choose which warrior aspect to lose"""
        from tkinter import messagebox
        
        # Create a custom dialog
        dialog = tk.Toplevel(self.root)
        dialog.title("Specialized Caster Choice")
        dialog.geometry("400x200")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center the dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (400 // 2)
        y = (dialog.winfo_screenheight() // 2) - (200 // 2)
        dialog.geometry(f"400x200+{x}+{y}")
        
        # Dialog content
        ttk.Label(dialog, text="As a Specialized Caster, you must choose to lose either\nWarrior Melee or Warrior Ranged aspects.", 
                 wraplength=350, justify='center').pack(pady=20)
        
        choice_var = tk.StringVar(value="melee")
        
        choice_frame = ttk.Frame(dialog)
        choice_frame.pack(pady=10)
        
        ttk.Radiobutton(choice_frame, text="Lose Warrior Melee", variable=choice_var, 
                       value="melee").pack(side='left', padx=10)
        ttk.Radiobutton(choice_frame, text="Lose Warrior Ranged", variable=choice_var, 
                       value="ranged").pack(side='left', padx=10)
        
        def confirm_choice():
            chosen_aspect = choice_var.get()
            
            # Set the chosen aspect to NULL and lock it
            self.character_data['aspects'][chosen_aspect] = 'NULL'
            
            # Update the aspects tab
            self.aspects_tab.set_aspect_value(chosen_aspect, 'NULL')
            self.aspects_tab.lock_aspect(chosen_aspect)
            
            dialog.destroy()
            messagebox.showinfo("Choice Confirmed", 
                              f"Warrior {chosen_aspect.capitalize()} aspect has been set to NULL and locked.")
        
        button_frame = ttk.Frame(dialog)
        button_frame.pack(pady=20)
        
        ttk.Button(button_frame, text="Confirm Choice", command=confirm_choice).pack(side='left', padx=10)
        ttk.Button(button_frame, text="Cancel", command=dialog.destroy).pack(side='left', padx=10)

    def handle_specialized_warrior_melee_selection(self):
        """Handle Specialized Warrior Melee selection - set magic aspect to NULL and lock it"""
        from tkinter import messagebox
        
        print(f"[DEBUG] Specialized Warrior Melee selected - setting magic to NULL")
        
        # Set magic aspect to NULL and lock it
        self.character_data['aspects']['magic'] = 'NULL'
        print(f"[DEBUG] Character data magic aspect set to: {self.character_data['aspects']['magic']}")
        
        self.aspects_tab.set_aspect_value('magic', 'NULL')
        print(f"[DEBUG] Called set_aspect_value for magic")
        
        self.aspects_tab.lock_aspect('magic')
        print(f"[DEBUG] Called lock_aspect for magic")
        
        messagebox.showinfo("Specialized Warrior Melee", 
                          "Magic aspect has been set to NULL and locked for Specialized Warrior Melee.")

    def handle_specialized_warrior_ranged_selection(self):
        """Handle Specialized Warrior Ranged selection - set magic aspect to NULL and lock it"""
        from tkinter import messagebox
        
        print(f"[DEBUG] Specialized Warrior Ranged selected - setting magic to NULL")
        
        # Set magic aspect to NULL and lock it
        self.character_data['aspects']['magic'] = 'NULL'
        print(f"[DEBUG] Character data magic aspect set to: {self.character_data['aspects']['magic']}")
        
        self.aspects_tab.set_aspect_value('magic', 'NULL')
        print(f"[DEBUG] Called set_aspect_value for magic")
        
        self.aspects_tab.lock_aspect('magic')
        print(f"[DEBUG] Called lock_aspect for magic")
        
        messagebox.showinfo("Specialized Warrior Ranged", 
                          "Magic aspect has been set to NULL and locked for Specialized Warrior Ranged.")

    def handle_specialized_rogue_selection(self):
        """Handle Specialized Rogue selection - set magic aspect to NULL and lock it"""
        from tkinter import messagebox
        
        print(f"[DEBUG] Specialized Rogue selected - setting magic to NULL")
        
        # Set magic aspect to NULL and lock it
        self.character_data['aspects']['magic'] = 'NULL'
        print(f"[DEBUG] Character data magic aspect set to: {self.character_data['aspects']['magic']}")
        
        self.aspects_tab.set_aspect_value('magic', 'NULL')
        print(f"[DEBUG] Called set_aspect_value for magic")
        
        self.aspects_tab.lock_aspect('magic')
        print(f"[DEBUG] Called lock_aspect for magic")
        
        messagebox.showinfo("Specialized Rogue", 
                          "Magic aspect has been set to NULL and locked for Specialized Rogue.")

    def handle_shield_master_selection(self):
        """Handle Shield Master selection - set ranged aspect to NULL and lock it"""
        from tkinter import messagebox
        
        print(f"[DEBUG] Shield Master selected - setting ranged to NULL")
        
        # Set ranged aspect to NULL and lock it
        self.character_data['aspects']['ranged'] = 'NULL'
        print(f"[DEBUG] Character data ranged aspect set to: {self.character_data['aspects']['ranged']}")
        
        self.aspects_tab.set_aspect_value('ranged', 'NULL')
        print(f"[DEBUG] Called set_aspect_value for ranged")
        
        self.aspects_tab.lock_aspect('ranged')
        print(f"[DEBUG] Called lock_aspect for ranged")
        
        messagebox.showinfo("Shield Master", 
                          "Ranged aspect has been set to NULL and locked for Shield Master.")

    def update_aspect_die_increases(self):
        """Update the aspect die increases available based on current rank"""
        current_rank = self.character_data.get('rank', 1)
        
        # Calculate aspect die increases based on rank
        # Aspect die increases happen every even rank (2, 4, 6, 8, 10, 12)
        total_increases = 0
        if current_rank >= 2:
            total_increases += 1  # Rank 2
        if current_rank >= 4:
            total_increases += 1  # Rank 4
        if current_rank >= 6:
            total_increases += 1  # Rank 6
        if current_rank >= 8:
            total_increases += 1  # Rank 8
        if current_rank >= 10:
            total_increases += 1  # Rank 10
        if current_rank >= 12:
            total_increases += 1  # Rank 12
        
        # Update the aspects tab
        self.aspects_tab.update_aspect_die_increases(total_increases)

    def save_character(self):
        """Save character data to JSON file"""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if file_path:
            try:
                # Collect data from all tabs
                basic_data = self.basic_info_tab.get_data()
                aspects_data = self.aspects_tab.get_data()
                gear_die_data = self.gear_die_tab.get_data()
                inventory_data = self.inventory_tab.get_data()
                abilities_data = self.abilities_tab.get_data()
                
                # Combine all data
                save_data = {
                    **basic_data,
                    **aspects_data,
                    **gear_die_data,
                    **inventory_data,
                    **abilities_data
                }
                
                # Save to file
                with open(file_path, 'w') as f:
                    json.dump(save_data, f, indent=4)
                messagebox.showinfo("Success", "Character saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save character: {str(e)}")

    def load_character(self):
        """Load character data from JSON file"""
        file_path = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'r') as f:
                    load_data = json.load(f)
                
                # Update character data
                self.character_data.update(load_data)
                
                # Update all tabs
                self.basic_info_tab.set_data(load_data)
                self.aspects_tab.set_data(load_data)
                self.gear_die_tab.set_data(load_data)
                self.inventory_tab.set_data(load_data)
                self.abilities_tab.set_data(load_data)
                
                messagebox.showinfo("Success", "Character loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load character: {str(e)}")

    def reset_character(self):
        """Reset character to default state"""
        if messagebox.askyesno("Reset Character", "Are you sure you want to reset the character sheet?"):
            # Unlock all fields first so they can be reset
            self.basic_info_tab.unlock_fields()
            self.aspects_tab.locked = False
            self.aspects_tab.update_lock_state()
            
            # Reset character data
            self.character_data = {
                'name': '',
                'playerName': '',
                'rank': 1,
                'rankPoints': 0,
                'race': '',
                'profession': '',
                'type': 'Non-Specialized',
                'unarmedCombat': False,
                'aspects': {
                    'melee': 'NULL',
                    'ranged': 'NULL',
                    'rogue': 'NULL',
                    'magic': 'NULL'
                },
                'aspectIncreases': {
                    'allowed': 0,
                    'history': {}
                },
                'lockedAspects': {},
                'aspectDieIncreases': 0,
                'gearDieSlots': {
                    'd4': 2,
                    'd6': 1,
                    'd8': 1,
                    'd10': 1,
                    'd12': 1
                },
                'gearDieEntries': {
                    'd4': [],
                    'd6': [],
                    'd8': [],
                    'd10': [],
                    'd12': []
                },
                'combatStats': {
                    'hp': 0,
                    'maxHp': 0,
                    'initiative': 0,
                    'indoorSpeed': 30,
                    'heroPoints': 0
                },
                'resources': {
                    'money': 0,
                    'magicDust': 0
                },
                'magicItems': [],
                'inventory': {
                    'stored': [],
                    'magic': [],
                    'stored_magic': [],
                    'elsewhere': []
                },
                'specialAbilities': {
                    'rank1': '',
                    'rank4': '',
                    'rank8': ''
                }
            }
            
            # Reset all tabs
            self.basic_info_tab.set_data(self.character_data)
            self.aspects_tab.set_data(self.character_data)
            self.gear_die_tab.set_data(self.character_data)
            self.inventory_tab.set_data(self.character_data)
            self.abilities_tab.set_data(self.character_data)
            
            # Fields remain unlocked since rank points are 0

    def print_character(self):
        """Print character sheet to PDF"""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if file_path:
            try:
                # Collect data from all tabs
                basic_data = self.basic_info_tab.get_data()
                aspects_data = self.aspects_tab.get_data()
                gear_die_data = self.gear_die_tab.get_data()
                inventory_data = self.inventory_tab.get_data()
                abilities_data = self.abilities_tab.get_data()
                
                # Combine all data
                print_data = {
                    **basic_data,
                    **aspects_data,
                    **gear_die_data,
                    **inventory_data,
                    **abilities_data
                }
                
                # Create PDF
                self.create_pdf(file_path, print_data)
                messagebox.showinfo("Success", "Character sheet printed successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to print character: {str(e)}")

    def create_pdf(self, file_path, data):
        """Create PDF character sheet"""
        doc = SimpleDocTemplate(file_path, pagesize=letter)
        story = []
        styles = getSampleStyleSheet()
        
        # Title
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=16,
            spaceAfter=30
        )
        story.append(Paragraph(f"MTM Character Sheet - {data.get('name', 'Unnamed')}", title_style))
        story.append(Spacer(1, 12))
        
        # Basic Information
        basic_info = [
            ['Character Name:', data.get('name', '')],
            ['Player Name:', data.get('playerName', '')],
            ['Race:', data.get('race', '')],
            ['Profession:', data.get('profession', '')],
            ['Specialization:', data.get('type', 'Non-Specialized')],
            ['Unarmed Combat:', 'Yes' if data.get('unarmedCombat', False) else 'No'],
            ['Rank:', str(data.get('rank', 1))],
            ['Rank Points:', str(data.get('rankPoints', 0))]
        ]
        
        basic_table = Table(basic_info, colWidths=[2*inch, 4*inch])
        basic_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        story.append(basic_table)
        story.append(Spacer(1, 12))
        
        # Combat Stats
        combat_stats = data.get('combatStats', {})
        indoor_speed = combat_stats.get('indoorSpeed', 30)
        outside_speed = indoor_speed * 2
        combat_info = [
            ['Current HP:', str(combat_stats.get('hp', 0))],
            ['Max HP:', str(combat_stats.get('maxHp', 0))],
            ['Indoor Speed:', f"{indoor_speed} feet"],
            ['Outside Speed:', f"{outside_speed} feet"],
            ['Initiative:', str(combat_stats.get('initiative', 0))],
            ['Hero Points:', str(combat_stats.get('heroPoints', 0))]
        ]
        
        combat_table = Table(combat_info, colWidths=[2*inch, 4*inch])
        combat_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        story.append(combat_table)
        story.append(Spacer(1, 12))
        
        # Aspects
        aspects = data.get('aspects', {})
        aspects_info = [
            ['Aspect', 'Die Type', 'Modifier']
        ]
        for aspect, die_type in aspects.items():
            modifier = self.get_die_modifier(die_type)
            if modifier is None:
                modifier_str = "--"
            else:
                modifier_str = f"{modifier:+d}"
            aspects_info.append([aspect.capitalize(), die_type, modifier_str])
        
        aspects_table = Table(aspects_info, colWidths=[2*inch, 2*inch, 2*inch])
        aspects_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        story.append(aspects_table)
        story.append(Spacer(1, 12))
        
        # Build the PDF
        doc.build(story)

    def get_die_modifier(self, die_type):
        """Get the modifier for a die type"""
        modifiers = {'NULL': None, 'd4': -1, 'd6': 0, 'd8': 1, 'd10': 2, 'd12': 3}
        return modifiers.get(die_type, 0)

def main():
    root = tk.Tk()
    app = CharacterSheetGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 