import tkinter as tk
from tkinter import messagebox

item_icons = {
    "Water": "💧",
    "Soda": "🥤",
    "Chips": "🍟",
    "Chocolate": "🍫",
    "Coffee": "☕",
    "Juice": "🧃",
    "Sandwich": "🥪",
    "Energy Drink": "⚡"
}

vending_items = {
    1: {"name": "Water", "price": 2.00},
    2: {"name": "Soda", "price": 3.50},
    3: {"name": "Chips", "price": 4.50},
    4: {"name": "Chocolate", "price": 6.00},
    5: {"name": "Coffee", "price": 7.50},
    6: {"name": "Juice", "price": 8.50},
    7: {"name": "Sandwich", "price": 9.00},
    8: {"name": "Energy Drink", "price": 10.00}
}

# Malaysia Ringgit note/button colors (approximate, can be customized)
note_colors = {
    0.5: "#9ad3de",     # Blue/grayish (coin)
    1:   "#6cc5ac",     # Greenish (coin/note)
    5:   "#25aae1",     # Blue
    10:  "#ff914d",     # Orange
    20:  "#f9d342",     # Yellow
    50:  "#36a3eb",     # Turquoise/blue
    100: "#ad1f52"      # Purple/pink
}

BG_COLOR = "#F6F7EB"
BTN_COLOR = "#7A9E9F"
ACCENT_COLOR = "#DB5461"
BAG_BG = "#FFFBE7"

class VendingMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🛒 Happy Vending Machine")
        self.root.config(bg=BG_COLOR)
        self.bag = []
        self.mode = tk.StringVar(value="NFA")
        self.setup_ui()

    def setup_ui(self):
        main_frame = tk.Frame(self.root, bg=BG_COLOR, padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        title = tk.Label(main_frame, text="🛒 Happy Vending Machine 🛒", font=("Arial Rounded MT Bold", 24, "bold"), fg=ACCENT_COLOR, bg=BG_COLOR)
        title.pack(pady=(0, 12))
        mode_frame = tk.Frame(main_frame, bg=BG_COLOR)
        mode_frame.pack(pady=(0, 15))
        tk.Label(mode_frame, text="Select Mode:", font=("Arial", 13), bg=BG_COLOR).pack(side="left")
        style = {"font": ("Arial", 11), "bg": BG_COLOR, "activebackground": BTN_COLOR}
        tk.Radiobutton(mode_frame, text="NFA (Flexible)", variable=self.mode, value="NFA", **style).pack(side="left", padx=8)
        tk.Radiobutton(mode_frame, text="DFA (Strict)", variable=self.mode, value="DFA", **style).pack(side="left")
        bag_btn = tk.Button(main_frame, text="👜 View Bag (Inventory)", bg=BTN_COLOR, fg="white",
                            font=("Arial Rounded MT Bold", 12), bd=0, padx=12, pady=6, command=self.show_bag,
                            activebackground=ACCENT_COLOR, activeforeground="white", cursor="hand2")
        bag_btn.pack(pady=(0, 10))
        items_label = tk.Label(main_frame, text="Items:", font=("Arial", 14, "bold"), bg=BG_COLOR)
        items_label.pack(anchor='w')
        self.items_frame = tk.Frame(main_frame, bg=BG_COLOR)
        self.items_frame.pack(pady=(3, 0))
        self.display_items()

    def display_items(self):
        for widget in self.items_frame.winfo_children():
            widget.destroy()
        for idx, item in vending_items.items():
            frame = tk.Frame(self.items_frame, bg="white", highlightbackground=BTN_COLOR, highlightthickness=2, bd=0)
            frame.grid(row=(idx-1)//2, column=(idx-1)%2, padx=14, pady=12, sticky='ew')
            icon = item_icons[item['name']]
            name = item['name']
            price = item['price']
            tk.Label(frame, text=f"{icon} {name}", font=("Arial Rounded MT Bold", 15), bg="white").grid(row=0, column=0, padx=5, pady=7, sticky='w')
            tk.Label(frame, text=f"RM{price:.2f}", font=("Arial", 13, "italic"), bg="white", fg=ACCENT_COLOR).grid(row=1, column=0, padx=5, sticky='w')
            buy_btn = tk.Button(frame, text="Buy", font=("Arial Rounded MT Bold", 11), bg=BTN_COLOR, fg="white",
                                bd=0, padx=18, pady=6,
                                activebackground=ACCENT_COLOR, activeforeground="white", cursor="hand2",
                                command=lambda idx=idx: self.start_purchase(idx))
            buy_btn.grid(row=0, column=1, rowspan=2, padx=(20,10))

    def start_purchase(self, item_id):
        item = vending_items[item_id]
        InsertMoneyWindow(self.root, item, self.mode.get(), self.add_to_bag)

    def add_to_bag(self, item_name):
        self.bag.append(item_name)
        messagebox.showinfo("Bag Updated", f"{item_icons[item_name]} {item_name} added to your bag!")

    def show_bag(self):
        bag_window = tk.Toplevel(self.root)
        bag_window.title("👜 Your Bag / Inventory")
        bag_window.config(bg=BAG_BG)
        bag_window.geometry("320x260")
        tk.Label(bag_window, text="Your Bag", font=("Arial Rounded MT Bold", 17, "bold"),
                 bg=BAG_BG, fg=ACCENT_COLOR).pack(pady=10)
        bag_frame = tk.Frame(bag_window, bg=BAG_BG)
        bag_frame.pack(expand=True, fill="both")
        if not self.bag:
            tk.Label(bag_frame, text="Your bag is empty.", font=("Arial", 13), bg=BAG_BG).pack(pady=20)
        else:
            bag_dict = {}
            for name in self.bag:
                bag_dict[name] = bag_dict.get(name, 0) + 1
            for i, (name, count) in enumerate(bag_dict.items()):
                icon = item_icons[name]
                txt = f"{icon} {name} x{count}"
                tk.Label(bag_frame, text=txt, font=("Arial Rounded MT Bold", 13), bg=BAG_BG).pack(anchor='w', padx=25, pady=5)
        tk.Button(bag_window, text="Close", command=bag_window.destroy,
                  font=("Arial Rounded MT Bold", 11), bg=BTN_COLOR, fg="white", bd=0,
                  padx=16, pady=4, activebackground=ACCENT_COLOR, activeforeground="white", cursor="hand2").pack(pady=12)

class InsertMoneyWindow:
    def __init__(self, master, item, mode, on_purchase_callback):
        self.top = tk.Toplevel(master)
        self.top.title("Insert Money")
        self.top.config(bg=BG_COLOR)
        self.item = item
        self.mode = mode
        self.on_purchase_callback = on_purchase_callback

        self.total = 0.0
        self.finished = False  # To prevent more money after dispense

        tk.Label(self.top, text=f"Buying: {item_icons[item['name']]} {item['name']}", font=("Arial Rounded MT Bold", 16),
                 bg=BG_COLOR, fg=BTN_COLOR).pack(pady=(14, 7))
        tk.Label(self.top, text=f"Price: RM{item['price']:.2f}", font=("Arial", 13, "italic"), bg=BG_COLOR, fg=ACCENT_COLOR).pack()

        self.total_label = tk.Label(self.top, text=f"Inserted: RM{self.total:.2f}", font=("Arial", 14, "bold"), bg=BG_COLOR)
        self.total_label.pack(pady=12)

        self.msg_label = tk.Label(self.top, text="", font=("Arial", 11), bg=BG_COLOR, fg="#d66")
        self.msg_label.pack(pady=(0, 6))

        # Money button panel
        btn_frame = tk.Frame(self.top, bg=BG_COLOR)
        btn_frame.pack(pady=7)

        self.money_btns = {}
        notes = [0.5, 1, 5, 10, 20, 50, 100]
        for i, val in enumerate(notes):
            col = note_colors[val]
            label = f"RM{val if val != 0.5 else '0.50'}"
            btn = tk.Button(btn_frame, text=label, width=10, font=("Arial Rounded MT Bold", 11), fg="white", bg=col,
                            activebackground="#888", activeforeground="white", bd=0, pady=8, padx=8, cursor="hand2",
                            command=lambda v=val: self.insert_money(v))
            btn.grid(row=0, column=i, padx=2, pady=2)
            self.money_btns[val] = btn

        self.cancel_btn = tk.Button(self.top, text="Cancel", bg="#bbb", fg="white",
                  activebackground="#d18", activeforeground="white", cursor="hand2",
                  font=("Arial Rounded MT Bold", 11), width=24, pady=6, command=self.top.destroy)
        self.cancel_btn.pack(pady=(16, 0))

        tip = "Only RM0.5 and RM1 are accepted. Others will be returned."
        self.tip_label = tk.Label(self.top, text=tip + f" Mode: {mode}", font=("Arial", 10), bg=BG_COLOR, fg="#888")
        self.tip_label.pack(pady=(3, 12))

    def insert_money(self, amount):
        if self.finished:
            return  # Don't allow after transaction completed

        if amount not in [0.5, 1]:
            # User inserted RM5, RM10, etc.
            col_map = {5: "Blue", 10: "Orange", 20: "Yellow", 50: "Turquoise", 100: "Purple"}
            note_color = col_map.get(amount, "Unknown")
            if self.mode == "NFA":
                self.msg_label.config(
                    text=f"❌ RM{int(amount)} note ({note_color}) rejected! (NFA: continue inserting)"
                )
                # Don't reset, just ignore, but visually notify
            else:
                self.msg_label.config(
                    text=f"❌ RM{int(amount)} note ({note_color}) rejected! (DFA: All money returned!)"
                )
                self.total = 0.0
                self.total_label.config(text=f"Inserted: RM{self.total:.2f}")
        else:
            self.msg_label.config(text="")
            self.total += amount
            self.total_label.config(text=f"Inserted: RM{self.total:.2f}")

            if self.total == self.item['price']:
                self.finish_transaction(dispensed=True)
            elif self.total > self.item['price']:
                self.finish_transaction(change=self.total - self.item['price'])

    def finish_transaction(self, dispensed=False, change=0.0):
        # Disable all money buttons
        for btn in self.money_btns.values():
            btn.config(state="disabled")
        self.cancel_btn.config(text="Close")
        self.finished = True

        if dispensed:
            messagebox.showinfo("Dispensed",
                                f"🎉 Dispensing {item_icons[self.item['name']]} {self.item['name']}!\nThank you for your purchase!")
            self.on_purchase_callback(self.item['name'])
            self.top.after(150, self.top.destroy)
        elif change > 0:
            messagebox.showinfo("Dispensed",
                                f"🎉 Dispensing {item_icons[self.item['name']]} {self.item['name']}!\nChange returned: RM{change:.2f}")
            self.on_purchase_callback(self.item['name'])
            self.top.after(150, self.top.destroy)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("880x560")
    app = VendingMachineApp(root)
    root.mainloop()
