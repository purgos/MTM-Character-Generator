import tkinter as tk
from tkinter import ttk, messagebox

class InventoryTab:
    def __init__(self, parent, character_data):
        self.parent = parent
        self.character_data = character_data
        self.tab = ttk.Frame(parent)
        
        # Initialize inventory data
        if 'inventory' not in self.character_data:
            self.character_data['inventory'] = {
                'stored': [],
                'magic': [],
                'stored_magic': [],
                'elsewhere': []
            }
        
        self.create_tab()
        
    def create_tab(self):
        """Create the inventory tab"""
        # Inventory Frame
        frame = ttk.LabelFrame(self.tab, text="Inventory")
        frame.pack(fill='both', expand=True, padx=5, pady=5)

        # Create notebook for different inventory sections
        inventory_notebook = ttk.Notebook(frame)
        inventory_notebook.pack(fill='both', expand=True, padx=5, pady=5)

        # Stored Equipment
        stored_frame = ttk.Frame(inventory_notebook)
        inventory_notebook.add(stored_frame, text="Stored Equipment")
        
        # Add item frame for stored equipment
        stored_add_frame = ttk.Frame(stored_frame)
        stored_add_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(stored_add_frame, text="Add Item:").pack(side='left', padx=5)
        self.stored_item_var = tk.StringVar()
        stored_entry = ttk.Entry(stored_add_frame, textvariable=self.stored_item_var)
        stored_entry.pack(side='left', padx=5, expand=True, fill='x')
        
        ttk.Label(stored_add_frame, text="Quantity:").pack(side='left', padx=5)
        self.stored_quantity_var = tk.StringVar(value="1")
        stored_quantity = ttk.Entry(stored_add_frame, textvariable=self.stored_quantity_var, width=5)
        stored_quantity.pack(side='left', padx=5)
        
        stored_add_button = ttk.Button(stored_add_frame, text="Add", 
                                     command=lambda: self.add_inventory_item('stored'))
        stored_add_button.pack(side='left', padx=5)
        
        # Listbox for stored items
        self.stored_listbox = tk.Listbox(stored_frame)
        self.stored_listbox.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Controls frame for stored items
        stored_controls = ttk.Frame(stored_frame)
        stored_controls.pack(fill='x', padx=5, pady=5)
        
        stored_remove_button = ttk.Button(stored_controls, text="Remove Selected",
                                        command=lambda: self.remove_inventory_item('stored'))
        stored_remove_button.pack(side='left', padx=5)
        
        stored_decrease_button = ttk.Button(stored_controls, text="Decrease Quantity",
                                          command=lambda: self.adjust_quantity('stored', -1))
        stored_decrease_button.pack(side='left', padx=5)
        
        stored_increase_button = ttk.Button(stored_controls, text="Increase Quantity",
                                          command=lambda: self.adjust_quantity('stored', 1))
        stored_increase_button.pack(side='left', padx=5)

        # Magic Bag
        magic_frame = ttk.Frame(inventory_notebook)
        inventory_notebook.add(magic_frame, text="Magic Bag")
        
        # Add item frame for magic bag
        magic_add_frame = ttk.Frame(magic_frame)
        magic_add_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(magic_add_frame, text="Add Item:").pack(side='left', padx=5)
        self.magic_item_var = tk.StringVar()
        magic_entry = ttk.Entry(magic_add_frame, textvariable=self.magic_item_var)
        magic_entry.pack(side='left', padx=5, expand=True, fill='x')
        
        ttk.Label(magic_add_frame, text="Quantity:").pack(side='left', padx=5)
        self.magic_quantity_var = tk.StringVar(value="1")
        magic_quantity = ttk.Entry(magic_add_frame, textvariable=self.magic_quantity_var, width=5)
        magic_quantity.pack(side='left', padx=5)
        
        magic_add_button = ttk.Button(magic_add_frame, text="Add",
                                    command=lambda: self.add_inventory_item('magic'))
        magic_add_button.pack(side='left', padx=5)
        
        # Listbox for magic items
        self.magic_listbox = tk.Listbox(magic_frame)
        self.magic_listbox.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Controls frame for magic items
        magic_controls = ttk.Frame(magic_frame)
        magic_controls.pack(fill='x', padx=5, pady=5)
        
        magic_remove_button = ttk.Button(magic_controls, text="Remove Selected",
                                       command=lambda: self.remove_inventory_item('magic'))
        magic_remove_button.pack(side='left', padx=5)
        
        magic_decrease_button = ttk.Button(magic_controls, text="Decrease Quantity",
                                         command=lambda: self.adjust_quantity('magic', -1))
        magic_decrease_button.pack(side='left', padx=5)
        
        magic_increase_button = ttk.Button(magic_controls, text="Increase Quantity",
                                         command=lambda: self.adjust_quantity('magic', 1))
        magic_increase_button.pack(side='left', padx=5)

        # Stored Magic Items
        stored_magic_frame = ttk.Frame(inventory_notebook)
        inventory_notebook.add(stored_magic_frame, text="Stored Magic Items")
        
        # Add item frame for stored magic items
        stored_magic_add_frame = ttk.Frame(stored_magic_frame)
        stored_magic_add_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(stored_magic_add_frame, text="Add Item:").pack(side='left', padx=5)
        self.stored_magic_item_var = tk.StringVar()
        stored_magic_entry = ttk.Entry(stored_magic_add_frame, textvariable=self.stored_magic_item_var)
        stored_magic_entry.pack(side='left', padx=5, expand=True, fill='x')
        
        ttk.Label(stored_magic_add_frame, text="Quantity:").pack(side='left', padx=5)
        self.stored_magic_quantity_var = tk.StringVar(value="1")
        stored_magic_quantity = ttk.Entry(stored_magic_add_frame, textvariable=self.stored_magic_quantity_var, width=5)
        stored_magic_quantity.pack(side='left', padx=5)
        
        stored_magic_add_button = ttk.Button(stored_magic_add_frame, text="Add",
                                           command=lambda: self.add_inventory_item('stored_magic'))
        stored_magic_add_button.pack(side='left', padx=5)
        
        # Listbox for stored magic items
        self.stored_magic_listbox = tk.Listbox(stored_magic_frame)
        self.stored_magic_listbox.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Controls frame for stored magic items
        stored_magic_controls = ttk.Frame(stored_magic_frame)
        stored_magic_controls.pack(fill='x', padx=5, pady=5)
        
        stored_magic_remove_button = ttk.Button(stored_magic_controls, text="Remove Selected",
                                              command=lambda: self.remove_inventory_item('stored_magic'))
        stored_magic_remove_button.pack(side='left', padx=5)
        
        stored_magic_decrease_button = ttk.Button(stored_magic_controls, text="Decrease Quantity",
                                                command=lambda: self.adjust_quantity('stored_magic', -1))
        stored_magic_decrease_button.pack(side='left', padx=5)
        
        stored_magic_increase_button = ttk.Button(stored_magic_controls, text="Increase Quantity",
                                                command=lambda: self.adjust_quantity('stored_magic', 1))
        stored_magic_increase_button.pack(side='left', padx=5)

        # Elsewhere
        elsewhere_frame = ttk.Frame(inventory_notebook)
        inventory_notebook.add(elsewhere_frame, text="Elsewhere")
        
        # Add item frame for elsewhere
        elsewhere_add_frame = ttk.Frame(elsewhere_frame)
        elsewhere_add_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(elsewhere_add_frame, text="Add Item:").pack(side='left', padx=5)
        self.elsewhere_item_var = tk.StringVar()
        elsewhere_entry = ttk.Entry(elsewhere_add_frame, textvariable=self.elsewhere_item_var)
        elsewhere_entry.pack(side='left', padx=5, expand=True, fill='x')
        
        ttk.Label(elsewhere_add_frame, text="Quantity:").pack(side='left', padx=5)
        self.elsewhere_quantity_var = tk.StringVar(value="1")
        elsewhere_quantity = ttk.Entry(elsewhere_add_frame, textvariable=self.elsewhere_quantity_var, width=5)
        elsewhere_quantity.pack(side='left', padx=5)
        
        ttk.Label(elsewhere_add_frame, text="Location:").pack(side='left', padx=5)
        self.elsewhere_location_var = tk.StringVar()
        elsewhere_location = ttk.Entry(elsewhere_add_frame, textvariable=self.elsewhere_location_var)
        elsewhere_location.pack(side='left', padx=5, expand=True, fill='x')
        
        elsewhere_add_button = ttk.Button(elsewhere_add_frame, text="Add",
                                        command=lambda: self.add_inventory_item('elsewhere'))
        elsewhere_add_button.pack(side='left', padx=5)
        
        # Listbox for elsewhere items
        self.elsewhere_listbox = tk.Listbox(elsewhere_frame)
        self.elsewhere_listbox.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Controls frame for elsewhere items
        elsewhere_controls = ttk.Frame(elsewhere_frame)
        elsewhere_controls.pack(fill='x', padx=5, pady=5)
        
        elsewhere_remove_button = ttk.Button(elsewhere_controls, text="Remove Selected",
                                           command=lambda: self.remove_inventory_item('elsewhere'))
        elsewhere_remove_button.pack(side='left', padx=5)
        
        elsewhere_decrease_button = ttk.Button(elsewhere_controls, text="Decrease Quantity",
                                             command=lambda: self.adjust_quantity('elsewhere', -1))
        elsewhere_decrease_button.pack(side='left', padx=5)
        
        elsewhere_increase_button = ttk.Button(elsewhere_controls, text="Increase Quantity",
                                             command=lambda: self.adjust_quantity('elsewhere', 1))
        elsewhere_increase_button.pack(side='left', padx=5)
        
        # Edit location button for elsewhere items
        elsewhere_edit_button = ttk.Button(elsewhere_controls, text="Edit Location",
                                         command=self.edit_elsewhere_location)
        elsewhere_edit_button.pack(side='left', padx=5)
        
        # Store listbox references
        self.listboxes = {
            'stored': self.stored_listbox,
            'magic': self.magic_listbox,
            'stored_magic': self.stored_magic_listbox,
            'elsewhere': self.elsewhere_listbox
        }
        
        # Store variable references
        self.item_vars = {
            'stored': self.stored_item_var,
            'magic': self.magic_item_var,
            'stored_magic': self.stored_magic_item_var,
            'elsewhere': self.elsewhere_item_var
        }
        
        self.quantity_vars = {
            'stored': self.stored_quantity_var,
            'magic': self.magic_quantity_var,
            'stored_magic': self.stored_magic_quantity_var,
            'elsewhere': self.elsewhere_quantity_var
        }
        
        # Load existing inventory data
        self.load_inventory_data()

    def add_inventory_item(self, category):
        """Add an item to the specified inventory category"""
        item_name = self.item_vars[category].get().strip()
        quantity_str = self.quantity_vars[category].get().strip()
        
        if not item_name:
            messagebox.showwarning("Warning", "Please enter an item name.")
            return
        
        try:
            quantity = int(quantity_str)
            if quantity <= 0:
                messagebox.showwarning("Warning", "Quantity must be positive.")
                return
        except ValueError:
            messagebox.showwarning("Warning", "Quantity must be a number.")
            return
        
        # Create item entry
        if category == 'elsewhere':
            location = self.elsewhere_location_var.get().strip()
            if not location:
                messagebox.showwarning("Warning", "Please enter a location for elsewhere items.")
                return
            item_entry = f"{item_name} (x{quantity}) - {location}"
        else:
            item_entry = f"{item_name} (x{quantity})"
        
        # Add to listbox and data
        listbox = self.listboxes[category]
        listbox.insert(tk.END, item_entry)
        
        # Store in character data
        if category == 'elsewhere':
            self.character_data['inventory'][category].append({
                'name': item_name,
                'quantity': quantity,
                'location': location
            })
        else:
            self.character_data['inventory'][category].append({
                'name': item_name,
                'quantity': quantity
            })
        
        # Clear input fields
        self.item_vars[category].set("")
        self.quantity_vars[category].set("1")
        if category == 'elsewhere':
            self.elsewhere_location_var.set("")

    def remove_inventory_item(self, category):
        """Remove selected item from inventory"""
        listbox = self.listboxes[category]
        selection = listbox.curselection()
        
        if not selection:
            messagebox.showwarning("Warning", "Please select an item to remove.")
            return
        
        index = selection[0]
        listbox.delete(index)
        
        # Remove from character data
        if index < len(self.character_data['inventory'][category]):
            self.character_data['inventory'][category].pop(index)

    def adjust_quantity(self, category, change):
        """Adjust quantity of selected item"""
        listbox = self.listboxes[category]
        selection = listbox.curselection()
        
        if not selection:
            messagebox.showwarning("Warning", "Please select an item to adjust.")
            return
        
        index = selection[0]
        if index >= len(self.character_data['inventory'][category]):
            return
        
        item_data = self.character_data['inventory'][category][index]
        new_quantity = item_data['quantity'] + change
        
        if new_quantity <= 0:
            # Remove item if quantity becomes 0 or negative
            self.remove_inventory_item(category)
            return
        
        item_data['quantity'] = new_quantity
        
        # Update display
        if category == 'elsewhere':
            new_entry = f"{item_data['name']} (x{new_quantity}) - {item_data['location']}"
        else:
            new_entry = f"{item_data['name']} (x{new_quantity})"
        
        listbox.delete(index)
        listbox.insert(index, new_entry)

    def edit_elsewhere_location(self):
        """Edit location of selected elsewhere item"""
        listbox = self.listboxes['elsewhere']
        selection = listbox.curselection()
        
        if not selection:
            messagebox.showwarning("Warning", "Please select an item to edit.")
            return
        
        index = selection[0]
        if index >= len(self.character_data['inventory']['elsewhere']):
            return
        
        item_data = self.character_data['inventory']['elsewhere'][index]
        
        # Create edit dialog
        dialog = tk.Toplevel(self.parent)
        dialog.title("Edit Location")
        dialog.geometry("300x150")
        dialog.transient(self.parent)
        dialog.grab_set()
        
        ttk.Label(dialog, text="New Location:").pack(pady=10)
        location_var = tk.StringVar(value=item_data['location'])
        location_entry = ttk.Entry(dialog, textvariable=location_var, width=40)
        location_entry.pack(pady=10)
        
        def save_location():
            new_location = location_var.get().strip()
            if new_location:
                item_data['location'] = new_location
                new_entry = f"{item_data['name']} (x{item_data['quantity']}) - {new_location}"
                listbox.delete(index)
                listbox.insert(index, new_entry)
                dialog.destroy()
            else:
                messagebox.showwarning("Warning", "Location cannot be empty.")
        
        ttk.Button(dialog, text="Save", command=save_location).pack(pady=10)

    def load_inventory_data(self):
        """Load existing inventory data into the GUI"""
        for category in ['stored', 'magic', 'stored_magic', 'elsewhere']:
            listbox = self.listboxes[category]
            for item_data in self.character_data['inventory'][category]:
                if category == 'elsewhere':
                    entry = f"{item_data['name']} (x{item_data['quantity']}) - {item_data['location']}"
                else:
                    entry = f"{item_data['name']} (x{item_data['quantity']})"
                listbox.insert(tk.END, entry)

    def get_data(self):
        """Get inventory data"""
        return {
            'inventory': self.character_data['inventory']
        }

    def set_data(self, data):
        """Set inventory data"""
        self.character_data['inventory'] = data.get('inventory', {
            'stored': [],
            'magic': [],
            'stored_magic': [],
            'elsewhere': []
        })
        
        # Clear all listboxes
        for listbox in self.listboxes.values():
            listbox.delete(0, tk.END)
        
        # Load the new data
        self.load_inventory_data() 