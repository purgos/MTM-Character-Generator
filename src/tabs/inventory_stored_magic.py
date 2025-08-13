import tkinter as tk
from tkinter import ttk

class InventoryStoredMagic:
    def __init__(self, parent, item_var, variant_var, charges_var, add_callback, listbox):
        # Outer frame for the tab; left side will host the list (created by parent),
        # right side shows item details/controls.
        self.frame = ttk.Frame(parent)

        # Bindings
        self.item_var = item_var
        self.variant_var = variant_var
        self.charges_var = charges_var
        self.add_callback = add_callback
        self.listbox = listbox

        # Load MAGIC_ITEMS
        try:
            from src.magic_items import MAGIC_ITEMS
        except ImportError:
            from magic_items import MAGIC_ITEMS
        self.MAGIC_ITEMS = MAGIC_ITEMS
        self.items_index = self._flatten_items(MAGIC_ITEMS)

        # Right panel container
        self.right_frame = ttk.Frame(self.frame)
        # Caller is responsible for gridding right_frame; we just populate it.

        # Item selection
        ttk.Label(self.right_frame, text="Select Magic Item:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.item_combo = ttk.Combobox(self.right_frame, textvariable=self.item_var, state='readonly', width=40)
        self.item_combo['values'] = sorted(self.items_index.keys())
        self.item_combo.grid(row=0, column=1, padx=5, pady=5, sticky='ew')
        self.item_combo.bind('<<ComboboxSelected>>', self.on_item_selected)

        # Variant (hidden unless item has variants)
        self.variant_label = ttk.Label(self.right_frame, text="Variant:")
        self.variant_combo = ttk.Combobox(self.right_frame, textvariable=self.variant_var, state='readonly', width=20)

        # Charges (hidden unless item has charges)
        self.charges_label = ttk.Label(self.right_frame, text="Charges:")
        self.charges_entry = ttk.Entry(self.right_frame, textvariable=self.charges_var, width=8)

        # Description
        ttk.Label(self.right_frame, text="Description:").grid(row=4, column=0, padx=5, pady=(10, 5), sticky='nw')
        self.desc_text = tk.Text(self.right_frame, wrap='word', height=10, state='disabled')
        self.desc_text.grid(row=4, column=1, padx=5, pady=(10, 5), sticky='nsew')
        self.right_frame.grid_rowconfigure(4, weight=1)
        self.right_frame.grid_columnconfigure(1, weight=1)

        # Add button
        handler = self.add_callback if self.add_callback else self.add_item
        ttk.Button(self.right_frame, text='Add', command=handler).grid(row=5, column=0, columnspan=2, padx=5, pady=(5, 10), sticky='w')

        # Initialize defaults if available
        if self.item_combo['values']:
            self.item_combo.current(0)
            self.on_item_selected()

    def _flatten_items(self, items_dict):
        index = {}
        for category, items in (items_dict or {}).items():
            if not isinstance(items, dict):
                continue
            for key, obj in items.items():
                name = obj.get('name') or key
                # Skip placeholders with empty names
                if not name:
                    continue
                # Keep first occurrence if duplicates
                if name not in index:
                    index[name] = {
                        'category': category,
                        'key': key,
                        'description': obj.get('description', ''),
                        'variants': obj.get('variants', []),
                        'charges': obj.get('charges'),
                        'type': obj.get('type', ''),
                    }
        return index

    def get_selected_meta(self):
        return self.items_index.get(self.item_var.get(), {})

    def on_item_selected(self, event=None):
        meta = self.get_selected_meta()
        # Variants
        variants = meta.get('variants') or []
        if variants:
            self.variant_combo['values'] = variants
            self.variant_combo.current(0)
            self.variant_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
            self.variant_combo.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        else:
            self.variant_label.grid_remove()
            self.variant_combo.grid_remove()
            self.variant_var.set('')

        # Charges
        charges = meta.get('charges')
        if isinstance(charges, int):
            self.charges_var.set(str(charges))
            self.charges_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')
            self.charges_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        else:
            self.charges_label.grid_remove()
            self.charges_entry.grid_remove()
            self.charges_var.set('')

        # Description
        self.desc_text.configure(state='normal')
        self.desc_text.delete('1.0', tk.END)
        self.desc_text.insert(tk.END, meta.get('description', ''))
        self.desc_text.configure(state='disabled')

    def set_selection_from_entry(self, entry: dict):
        """Sync right panel controls from a stored_magic entry."""
        try:
            name = (entry or {}).get('name', '')
            if name and name in self.items_index:
                # Set item and trigger dependent UI
                self.item_var.set(name)
                # Manually call selection handler to refresh variants/charges/description
                self.on_item_selected()
                # Variant
                var = (entry or {}).get('variant', '')
                if var and self.variant_combo['values']:
                    if var in self.variant_combo['values']:
                        self.variant_var.set(var)
                    else:
                        # Fallback to first available
                        self.variant_combo.current(0)
                        self.variant_var.set(self.variant_combo.get())
                else:
                    self.variant_var.set('')
                # Charges
                cur = (entry or {}).get('current_charges')
                maxc = (entry or {}).get('max_charges')
                if cur is not None and maxc is not None:
                    try:
                        self.charges_var.set(str(int(cur)))
                    except Exception:
                        self.charges_var.set(str(cur))
            else:
                # Clear selection
                self.item_var.set('')
                self.variant_var.set('')
                self.charges_var.set('')
        except Exception:
            pass

    def add_item(self):
        # Fallback if parent didn't provide a callback
        meta = self.get_selected_meta()
        name = self.item_var.get()
        parts = [name]
        if self.variant_var.get():
            parts.append(f"({self.variant_var.get()})")
        entry = ' '.join(parts)
        ch = self.charges_var.get().strip()
        if ch:
            try:
                c = int(ch)
                entry += f" - Charges {c}/{meta.get('charges', c)}"
            except Exception:
                pass
        self.listbox.insert(tk.END, entry)
