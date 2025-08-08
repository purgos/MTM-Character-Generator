import tkinter as tk
from tkinter import ttk, messagebox
import re
try:
    from magic_items import MAGIC_ITEMS  # when src/ is on sys.path
except ModuleNotFoundError:
    try:
        from ..magic_items import MAGIC_ITEMS  # when using package relative import
    except Exception:
        import os, sys as _sys
        _base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if _base_dir not in _sys.path:
            _sys.path.insert(0, _base_dir)
        from magic_items import MAGIC_ITEMS

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

        # Stored Magic Items (Refactored to mirror Basic Info tab magic items)
        stored_magic_frame = ttk.Frame(inventory_notebook)
        inventory_notebook.add(stored_magic_frame, text="Stored Magic Items")
        
        # Build magic items lookup and values for stored magic
        self.SM_CUSTOM_ITEM_LABEL = 'Custom Item...'
        self.sm_magic_item_lookup = {}
        sm_all_items = []
        for group, group_dict in MAGIC_ITEMS.items():
            for key, item_def in group_dict.items():
                raw_name = item_def.get('name', key)
                display_name = self.sanitize_item_name(raw_name)
                if display_name not in self.sm_magic_item_lookup:
                    stored = dict(item_def)
                    stored['name'] = display_name
                    if 'description' in stored:
                        stored['description'] = self.sanitize_text(stored['description'])
                    self.sm_magic_item_lookup[display_name] = stored
                    sm_all_items.append(display_name)
        sm_values = [self.SM_CUSTOM_ITEM_LABEL] + sorted(sm_all_items)
        
        # Add item frame for stored magic items
        stored_magic_add_frame = ttk.Frame(stored_magic_frame)
        stored_magic_add_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(stored_magic_add_frame, text="Magic Item:").pack(side='left', padx=5)
        self.sm_item_var = tk.StringVar()
        self.sm_item_combo = ttk.Combobox(stored_magic_add_frame, textvariable=self.sm_item_var,
                                          values=sm_values, state='readonly', width=40)
        self.sm_item_combo.pack(side='left', padx=5)
        self.sm_item_combo.bind('<<ComboboxSelected>>', self.on_sm_item_selected)
        
        self.sm_variant_var = tk.StringVar()
        self.sm_variant_combo = ttk.Combobox(stored_magic_add_frame, textvariable=self.sm_variant_var,
                                             state='readonly', width=12)
        self.sm_variant_combo.pack(side='left', padx=5)
        
        self.sm_charges_var = tk.StringVar(value="")
        self.sm_charges_entry = ttk.Entry(stored_magic_add_frame, textvariable=self.sm_charges_var, width=6)
        self.sm_charges_entry.pack(side='left', padx=5)
        
        stored_magic_add_button = ttk.Button(stored_magic_add_frame, text="Add Item",
                                           command=self.add_stored_magic_item)
        stored_magic_add_button.pack(side='left', padx=5)
        
        # Listbox for stored magic items
        self.stored_magic_listbox = tk.Listbox(stored_magic_frame)
        self.stored_magic_listbox.pack(fill='both', expand=True, padx=5, pady=5)
        self.stored_magic_listbox.bind('<<ListboxSelect>>', self.sm_update_use_charge_state)
        
        # Controls frame for stored magic items
        stored_magic_controls = ttk.Frame(stored_magic_frame)
        stored_magic_controls.pack(fill='x', padx=5, pady=5)
        
        self.sm_remove_button = ttk.Button(stored_magic_controls, text="Remove Selected",
                                              command=self.sm_remove_item)
        self.sm_remove_button.pack(side='left', padx=5)
        
        # Removed Use Charge button per request
        # self.sm_use_charge_button = ttk.Button(stored_magic_controls, text="Use Charge",
        #                                         command=self.sm_use_charge)
        # self.sm_use_charge_button.pack(side='left', padx=5)
        
        self.sm_recharge_button = ttk.Button(stored_magic_controls, text="Recharge Item",
                                                command=self.sm_recharge_item)
        self.sm_recharge_button.pack(side='left', padx=5)

        # Description panel for stored magic items
        sm_desc_frame = ttk.LabelFrame(stored_magic_frame, text="Magic Item Description")
        sm_desc_frame.pack(fill='both', expand=False, padx=5, pady=5)
        self.sm_desc_text = tk.Text(sm_desc_frame, wrap='word', height=6, state='disabled')
        self.sm_desc_text.pack(fill='both', expand=True, padx=5, pady=5)

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
        
        # Store variable references (exclude stored_magic, handled separately)
        self.item_vars = {
            'stored': self.stored_item_var,
            'magic': self.magic_item_var,
            'elsewhere': self.elsewhere_item_var
        }
        
        self.quantity_vars = {
            'stored': self.stored_quantity_var,
            'magic': self.magic_quantity_var,
            'elsewhere': self.elsewhere_quantity_var
        }
        
        # Load existing inventory data
        self.load_inventory_data()

    # --- Helpers to sanitize names/description (match BasicInfoTab) ---
    def sanitize_item_name(self, name: str) -> str:
        if not name:
            return name
        name = re.sub(r"[\u2018\u2019\u02BC\u2032`']", "", name)
        name = re.sub(r"\s+", " ", name).strip()
        return name

    def sanitize_text(self, text: str) -> str:
        if not text:
            return text
        text = re.sub(r"[\u2018\u2019\u02BC\u2032`']", "", text)
        text = re.sub(r"\s+", " ", text)
        return text.strip()

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

    # --- Stored Magic specific methods ---
    def on_sm_item_selected(self, event=None):
        """Update variant/charges/description based on selected item in combobox."""
        name = self.sm_item_var.get().strip() if hasattr(self, 'sm_item_var') else ''
        if not name:
            self.sm_update_description(None)
            self.sm_update_use_charge_state()
            return
        if name == self.SM_CUSTOM_ITEM_LABEL:
            self.open_sm_custom_item_dialog()
            return
        item_def = self.sm_magic_item_lookup.get(name, {})
        # Variants
        if 'variants' in item_def:
            self.sm_variant_combo['values'] = item_def['variants']
            cur = self.sm_variant_var.get()
            if cur not in item_def['variants']:
                self.sm_variant_combo.set(item_def['variants'][0])
        else:
            self.sm_variant_combo['values'] = []
            self.sm_variant_combo.set('')
        # Charges default
        if 'charges' in item_def:
            self.sm_charges_var.set(str(item_def['charges']))
        else:
            self.sm_charges_var.set('')
        # Description
        self.sm_update_description(item_def)

    def sm_update_description(self, item_def):
        if not hasattr(self, 'sm_desc_text'):
            return
        self.sm_desc_text.config(state='normal')
        self.sm_desc_text.delete('1.0', tk.END)
        if item_def:
            desc = self.sanitize_text(item_def.get('description', '(No description available)'))
            if 'variants' in item_def:
                desc += "\n\nVariants: " + ", ".join(item_def['variants'])
            if 'charges' in item_def:
                desc += f"\nDefault Charges: {item_def['charges']}"
        else:
            desc = "Select a magic item to view its description."
        self.sm_desc_text.insert('1.0', desc)
        self.sm_desc_text.config(state='disabled')

    def add_stored_magic_item(self):
        """Add selected magic item to stored_magic with unlimited count (no cap)."""
        name = self.sm_item_var.get().strip() if hasattr(self, 'sm_item_var') else ''
        if not name:
            messagebox.showwarning("Warning", "Please select a magic item.")
            return
        if name == self.SM_CUSTOM_ITEM_LABEL:
            self.open_sm_custom_item_dialog()
            return
        item_def = self.sm_magic_item_lookup.get(name)
        if not item_def:
            messagebox.showwarning("Warning", "Unknown magic item.")
            return
        entry = {'name': item_def.get('name', name)}
        var = self.sm_variant_var.get().strip() if hasattr(self, 'sm_variant_var') else ''
        if var:
            entry['variant'] = var
        if 'description' in item_def:
            entry['description'] = self.sanitize_text(item_def['description'])
        # Charges
        max_charges = None
        raw_ch = self.sm_charges_var.get().strip() if hasattr(self, 'sm_charges_var') else ''
        if raw_ch:
            try:
                max_charges = int(raw_ch)
            except ValueError:
                max_charges = None
        if max_charges is None and 'charges' in item_def:
            try:
                max_charges = int(item_def['charges'])
            except Exception:
                max_charges = None
        if max_charges is not None:
            entry['max_charges'] = max_charges
            entry['current_charges'] = max_charges
        # Append to data
        self.character_data['inventory']['stored_magic'].append(entry)
        # Update UI
        self.sm_refresh_listbox()
        # Select last
        self.stored_magic_listbox.select_clear(0, tk.END)
        self.stored_magic_listbox.select_set(tk.END)
        self.stored_magic_listbox.event_generate('<<ListboxSelect>>')
        self.sm_update_use_charge_state()

    def sm_refresh_listbox(self):
        if not hasattr(self, 'stored_magic_listbox'):
            return
        self.stored_magic_listbox.delete(0, tk.END)
        for item in self.character_data['inventory']['stored_magic']:
            # Legacy fallback: if it had quantity (should be normalized), show with (xN)
            if 'quantity' in item and isinstance(item.get('quantity'), int):
                display = f"{item.get('name','')} (x{item.get('quantity',1)})"
            else:
                parts = [item.get('name','')]
                if item.get('variant'):
                    parts.append(f"({item['variant']})")
                if 'current_charges' in item and 'max_charges' in item:
                    parts.append(f"Charges {item['current_charges']}/{item['max_charges']}")
                display = ' - '.join([p for p in parts if p])
            self.stored_magic_listbox.insert(tk.END, display)

    def sm_update_use_charge_state(self, event=None):
        # Enable/disable buttons based on selection
        def disable(btn):
            try:
                btn.state(['disabled'])
            except Exception:
                btn.configure(state='disabled')
        def enable(btn):
            try:
                btn.state(['!disabled'])
            except Exception:
                btn.configure(state='normal')
        if not hasattr(self, 'stored_magic_listbox'):
            return
        sel = self.stored_magic_listbox.curselection()
        if not sel:
            # Only recharge button remains
            if hasattr(self, 'sm_recharge_button'):
                disable(self.sm_recharge_button)
            return
        idx = sel[0]
        items = self.character_data['inventory']['stored_magic']
        if idx >= len(items):
            if hasattr(self, 'sm_recharge_button'):
                disable(self.sm_recharge_button)
            return
        item = items[idx]
        # Update description view to selected item's saved description if present
        self.sm_update_description({'description': item.get('description','')})
        # Enable recharge only if not at max
        if 'current_charges' in item and 'max_charges' in item and item['current_charges'] < item['max_charges']:
            if hasattr(self, 'sm_recharge_button'):
                enable(self.sm_recharge_button)
        else:
            if hasattr(self, 'sm_recharge_button'):
                disable(self.sm_recharge_button)

    def sm_use_charge(self):
        sel = self.stored_magic_listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        items = self.character_data['inventory']['stored_magic']
        if idx >= len(items):
            return
        item = items[idx]
        if 'current_charges' in item and item['current_charges'] > 0:
            item['current_charges'] -= 1
            if item['current_charges'] < 0:
                item['current_charges'] = 0
            self.sm_refresh_listbox()
            self.stored_magic_listbox.select_set(idx)
            self.stored_magic_listbox.event_generate('<<ListboxSelect>>')

    def sm_recharge_item(self):
        sel = self.stored_magic_listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        items = self.character_data['inventory']['stored_magic']
        if idx >= len(items):
            return
        item = items[idx]
        if 'current_charges' in item and 'max_charges' in item:
            item['current_charges'] = item['max_charges']
            self.sm_refresh_listbox()
            self.stored_magic_listbox.select_set(idx)
            self.stored_magic_listbox.event_generate('<<ListboxSelect>>')

    def sm_remove_item(self):
        sel = self.stored_magic_listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        if idx < len(self.character_data['inventory']['stored_magic']):
            del self.character_data['inventory']['stored_magic'][idx]
        self.sm_refresh_listbox()
        # Select nearest remaining item
        items = self.character_data['inventory']['stored_magic']
        if items:
            new_index = min(idx, len(items) - 1)
            self.stored_magic_listbox.select_set(new_index)
            self.stored_magic_listbox.event_generate('<<ListboxSelect>>')
        else:
            self.sm_update_use_charge_state()

    def open_sm_custom_item_dialog(self):
        dialog = tk.Toplevel(self.tab)
        dialog.title('Create Custom Magic Item')
        dialog.transient(self.tab)
        dialog.grab_set()

        tk.Label(dialog, text='Name:').grid(row=0, column=0, sticky='e', padx=5, pady=5)
        name_var = tk.StringVar()
        name_entry = ttk.Entry(dialog, textvariable=name_var, width=40)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(dialog, text='Max Charges (optional):').grid(row=1, column=0, sticky='e', padx=5, pady=5)
        charges_var = tk.StringVar()
        charges_entry = ttk.Entry(dialog, textvariable=charges_var, width=10)
        charges_entry.grid(row=1, column=1, sticky='w', padx=5, pady=5)

        tk.Label(dialog, text='Description:').grid(row=2, column=0, sticky='ne', padx=5, pady=5)
        desc_text = tk.Text(dialog, width=50, height=10, wrap='word')
        desc_text.grid(row=2, column=1, padx=5, pady=5)

        button_frame = ttk.Frame(dialog)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)

        def confirm():
            name = self.sanitize_item_name(name_var.get().strip())
            if not name:
                dialog.destroy()
                return
            if name in self.sm_magic_item_lookup:
                dialog.destroy()
                return
            description = self.sanitize_text(desc_text.get('1.0', tk.END).strip())
            charges_input = charges_var.get().strip()
            item_def = {'name': name, 'description': description}
            if charges_input:
                try:
                    ch = int(charges_input)
                    item_def['charges'] = ch
                except ValueError:
                    pass
            self.sm_magic_item_lookup[name] = item_def
            # Update combobox values
            current_vals = list(self.sm_item_combo['values'])
            if name not in current_vals:
                base = [v for v in current_vals if v not in (self.SM_CUSTOM_ITEM_LABEL, name) and v]
                self.sm_item_combo['values'] = [self.SM_CUSTOM_ITEM_LABEL] + sorted(base + [name])
            self.sm_item_var.set(name)
            if 'charges' in item_def:
                self.sm_charges_var.set(str(item_def['charges']))
            else:
                self.sm_charges_var.set('')
            self.sm_variant_combo['values'] = []
            self.sm_variant_var.set('')
            self.sm_update_description(item_def)
            dialog.destroy()

        ttk.Button(button_frame, text='Add Item', command=confirm).pack(side='left', padx=5)
        ttk.Button(button_frame, text='Cancel', command=dialog.destroy).pack(side='left', padx=5)
        name_entry.focus_set()

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

    def normalize_stored_magic(self):
        """Normalize legacy stored_magic entries with quantities into individual items."""
        items = self.character_data['inventory'].get('stored_magic', [])
        normalized = []
        for item in items:
            if isinstance(item, dict) and 'quantity' in item and isinstance(item.get('quantity'), int):
                count = max(1, item.get('quantity', 1))
                for _ in range(count):
                    normalized.append({'name': item.get('name', '')})
            else:
                normalized.append(item)
        self.character_data['inventory']['stored_magic'] = normalized

    def load_inventory_data(self):
        """Load existing inventory data into the GUI"""
        # Normalize legacy stored_magic first
        self.normalize_stored_magic()
        
        for category in ['stored', 'magic', 'stored_magic', 'elsewhere']:
            listbox = self.listboxes[category]
            # Clear any existing items first to avoid duplicates on reload
            listbox.delete(0, tk.END)
            for item_data in self.character_data['inventory'][category]:
                if category == 'elsewhere':
                    entry = f"{item_data['name']} (x{item_data['quantity']}) - {item_data['location']}"
                elif category == 'stored_magic':
                    # Use rich display like in BasicInfoTab
                    if 'quantity' in item_data and isinstance(item_data.get('quantity'), int):
                        entry = f"{item_data.get('name','')} (x{item_data.get('quantity',1)})"
                    else:
                        parts = [item_data.get('name','')]
                        if item_data.get('variant'):
                            parts.append(f"({item_data['variant']})")
                        if 'current_charges' in item_data and 'max_charges' in item_data:
                            parts.append(f"Charges {item_data['current_charges']}/{item_data['max_charges']}")
                        entry = ' - '.join([p for p in parts if p])
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