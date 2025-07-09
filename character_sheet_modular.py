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
            'type': 'non-specialized',
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
        self.aspects_tab = AspectsTab(self.notebook, self.character_data)
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

    def on_rank_update(self, *args):
        """Handle rank updates from basic info tab"""
        try:
            total_points = int(self.basic_info_tab.total_rank_points_var.get())
            new_rank = min(12, 1 + (total_points // 25))
            
            # Update character data
            self.character_data['rank'] = new_rank
            self.character_data['rankPoints'] = total_points
            
            # Update gear die slots
            self.gear_die_tab.update_slots_for_rank(new_rank)
            
            # Update abilities visibility
            self.abilities_tab.update_ability_visibility()
            
        except ValueError:
            pass

    def on_race_update(self, *args):
        """Handle race updates from basic info tab"""
        race = self.basic_info_tab.race_var.get()
        self.character_data['race'] = race
        
        # Update abilities visibility
        self.abilities_tab.update_ability_visibility()

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
            # Reset character data
            self.character_data = {
                'name': '',
                'playerName': '',
                'rank': 1,
                'rankPoints': 0,
                'race': '',
                'profession': '',
                'type': 'non-specialized',
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
        combat_info = [
            ['Current HP:', str(combat_stats.get('hp', 0))],
            ['Max HP:', str(combat_stats.get('maxHp', 0))],
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
            aspects_info.append([aspect.capitalize(), die_type, f"{modifier:+d}"])
        
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
        modifiers = {'d4': -1, 'd6': 0, 'd8': 1, 'd10': 2, 'd12': 3}
        return modifiers.get(die_type, 0)

def main():
    root = tk.Tk()
    app = CharacterSheetGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 