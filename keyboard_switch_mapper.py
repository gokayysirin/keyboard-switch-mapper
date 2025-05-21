import tkinter as tk
from tkinter import ttk, colorchooser, messagebox
import json
import os

class KeyboardSwitchMapper:
    def __init__(self, root):
        self.root = root
        self.root.title("Klavye Switch Haritası")
        self.root.geometry("1480x650")
        self.root.resizable(False, False)
        
        style = ttk.Style()
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TButton", font=("Arial", 10), background="#4a6ea9")
        style.configure("TLabel", font=("Arial", 10), background="#f0f0f0")
        style.configure("Title.TLabel", font=("Arial", 14, "bold"), background="#f0f0f0")
        
        self.root.configure(bg="#f0f0f0")
        
        self.default_switch_types = {
            "Gateron Red": "#FF0000",
            "Gateron Blue": "#0000FF",
            "Gateron Brown": "#8B4513",
            "Cherry MX Red": "#FF6666",
            "Cherry MX Blue": "#6666FF",
            "Cherry MX Brown": "#A0522D",
            "Tanımsız": "#CCCCCC"
        }
        
        self.load_data()
        self.create_frames()
        self.create_widgets()
        self.draw_keyboard()
        
    def load_data(self):
        self.data_file = "keyboard_switch_data.json"
        
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.switch_types = data.get("switch_types", self.default_switch_types)
                    self.keyboard_layout = data.get("keyboard_layout", {})
            except Exception as e:
                messagebox.showerror("Hata", f"Veri yüklenirken bir hata oluştu: {e}")
                self.switch_types = self.default_switch_types.copy()
                self.keyboard_layout = {}
        else:
            self.switch_types = self.default_switch_types.copy()
            self.keyboard_layout = {}
        
        self.active_switch_type = list(self.switch_types.keys())[0]
            
    def save_data(self):
        data = {
            "switch_types": self.switch_types,
            "keyboard_layout": self.keyboard_layout
        }
        
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            messagebox.showinfo("Başarılı", "Klavye haritası başarıyla kaydedildi.")
        except Exception as e:
            messagebox.showerror("Hata", f"Veriler kaydedilirken bir hata oluştu: {e}")
            
    def create_frames(self):
        self.left_frame = ttk.Frame(self.root, padding=10, style="TFrame")
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        
        self.right_frame = ttk.Frame(self.root, padding=10, style="TFrame")
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.keyboard_frame = ttk.Frame(self.right_frame, padding=5, style="TFrame")
        self.keyboard_frame.pack(fill=tk.BOTH, expand=True)
        
        self.footer_frame = ttk.Frame(self.root, style="TFrame")
        self.footer_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)
        
    def create_widgets(self):
        ttk.Label(self.left_frame, text="Switch Türleri", style="Title.TLabel").pack(pady=(0, 10))
        
        switch_frame = ttk.Frame(self.left_frame)
        switch_frame.pack(pady=5, fill=tk.X)
        
        self.switch_listbox = tk.Listbox(switch_frame, width=25, height=10, font=("Arial", 10),
                                        borderwidth=2, relief=tk.SUNKEN)
        self.switch_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(switch_frame, orient=tk.VERTICAL, command=self.switch_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.switch_listbox.config(yscrollcommand=scrollbar.set)
        
        self.refresh_switch_list()
        self.switch_listbox.bind('<<ListboxSelect>>', self.on_switch_select)
        
        ttk.Separator(self.left_frame, orient='horizontal').pack(fill=tk.X, pady=10)
        ttk.Label(self.left_frame, text="Yeni Switch Ekle", style="Title.TLabel").pack(pady=(10, 5))
        
        new_switch_frame = ttk.Frame(self.left_frame)
        new_switch_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(new_switch_frame, text="İsim:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.new_switch_name = ttk.Entry(new_switch_frame, width=20)
        self.new_switch_name.grid(row=0, column=1, pady=2)
        
        ttk.Label(new_switch_frame, text="Renk:").grid(row=1, column=0, sticky=tk.W, pady=2)
        
        color_frame = ttk.Frame(new_switch_frame)
        color_frame.grid(row=1, column=1, pady=2)
        
        self.color_preview = tk.Canvas(color_frame, width=20, height=20, bg="#CCCCCC", 
                                     borderwidth=1, relief=tk.SUNKEN)
        self.color_preview.pack(side=tk.LEFT)
        
        self.select_color_btn = ttk.Button(color_frame, text="Seç", command=self.select_color)
        self.select_color_btn.pack(side=tk.LEFT, padx=5)
        
        self.selected_color = "#CCCCCC"
        
        self.add_switch_btn = ttk.Button(new_switch_frame, text="Ekle", command=self.add_switch_type)
        self.add_switch_btn.grid(row=2, column=0, columnspan=2, pady=5)
        
        self.delete_switch_btn = ttk.Button(self.left_frame, text="Seçili Switch'i Sil", command=self.delete_switch_type)
        self.delete_switch_btn.pack(pady=5)
        
        ttk.Separator(self.left_frame, orient='horizontal').pack(fill=tk.X, pady=10)
        self.save_btn = ttk.Button(self.left_frame, text="Haritayı Kaydet", command=self.save_data)
        self.save_btn.pack(pady=10)
        
        info_text = "Tuşlara switch atamak için önce\nsol listeden switch türünü seçin,\nardından klavyede bir tuşa tıklayın."
        info_label = ttk.Label(self.left_frame, text=info_text, justify=tk.LEFT, 
                            background="#e0e8f0", padding=10)
        info_label.pack(pady=10, fill=tk.X)
        
        footer_text = "Developed by Gökay Şirin via Claude 3.7 Sonnet"
        self.footer_label = ttk.Label(self.root, text=footer_text, font=("Arial", 9, "italic"), 
                                   background="#e0e0e0", foreground="#555555")
        self.footer_label.pack(side=tk.BOTTOM, fill=tk.X, pady=5)
        
    def refresh_switch_list(self):
        self.switch_listbox.delete(0, tk.END)
        for idx, (name, color) in enumerate(self.switch_types.items()):
            self.switch_listbox.insert(idx, name)
            self.switch_listbox.itemconfig(idx, {'bg': color})
            
            r, g, b = self.hex_to_rgb(color)
            brightness = (r * 299 + g * 587 + b * 114) / 1000
            text_color = "#000000" if brightness > 128 else "#FFFFFF"
            self.switch_listbox.itemconfig(idx, {'fg': text_color})
            
    def hex_to_rgb(self, hex_color):
        h = hex_color.lstrip('#')
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        
    def on_switch_select(self, event):
        try:
            index = self.switch_listbox.curselection()[0]
            selected_switch = self.switch_listbox.get(index)
            self.active_switch_type = selected_switch
        except IndexError:
            pass
            
    def select_color(self):
        color = colorchooser.askcolor(self.selected_color)[1]
        if color:
            self.selected_color = color
            self.color_preview.config(bg=color)
            
    def add_switch_type(self):
        name = self.new_switch_name.get().strip()
        
        if not name:
            messagebox.showerror("Hata", "Switch ismi boş olamaz!")
            return
            
        if name in self.switch_types:
            messagebox.showerror("Hata", f"'{name}' isimli switch zaten mevcut!")
            return
            
        self.switch_types[name] = self.selected_color
        self.refresh_switch_list()
        
        self.new_switch_name.delete(0, tk.END)
        self.selected_color = "#CCCCCC"
        self.color_preview.config(bg=self.selected_color)
            
    def delete_switch_type(self):
        try:
            index = self.switch_listbox.curselection()[0]
            selected_switch = self.switch_listbox.get(index)
            
            if selected_switch == "Tanımsız":
                messagebox.showerror("Hata", "'Tanımsız' switch'i silinemez!")
                return
                
            if messagebox.askyesno("Onay", f"'{selected_switch}' switch türünü silmek istediğinize emin misiniz?"):
                del self.switch_types[selected_switch]
                
                for key_id, switch_type in self.keyboard_layout.items():
                    if switch_type == selected_switch:
                        self.keyboard_layout[key_id] = "Tanımsız"
                
                if self.active_switch_type == selected_switch:
                    self.active_switch_type = list(self.switch_types.keys())[0]
                
                self.refresh_switch_list()
                self.draw_keyboard()
                
        except IndexError:
            messagebox.showerror("Hata", "Lütfen silinecek bir switch seçin!")
            
    def draw_keyboard(self):
        for widget in self.keyboard_frame.winfo_children():
            widget.destroy()
            
        keyboard_layout = [
            ["ESC", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "BACKSPACE"],
            ["TAB", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "Ğ", "Ü", "ENTER"],
            ["CAPS", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ş", "İ", ","],
            ["SHIFT", "Z", "X", "C", "V", "B", "N", "M", "Ö", "Ç", "."],
            ["CTRL", "WIN", "ALT", "SPACE", "ALT GR", "FN", "MENU", "CTRLR"]
        ]
        
        special_keys = {
            "BACKSPACE": 2,
            "TAB": 1.5,
            "ENTER": 1.5,
            "CAPS": 1.75,
            "SHIFT": 2.25,
            "CTRL": 1.25,
            "CTRLR": 1.25,
            "WIN": 1.25,
            "ALT": 1.25,
            "SPACE": 6,
            "ALT GR": 1.25,
            "FN": 1,
            "MENU": 1,
        }
        
        key_size = 50
        padding = 5
        row_offset = 0
        
        keyboard_bg = tk.Canvas(self.keyboard_frame, bg="#333333", highlightthickness=0)
        keyboard_bg.place(relwidth=1, relheight=1)
        
        title_label = tk.Label(keyboard_bg, text="Klavye Switch Haritası", 
                            font=("Arial", 14, "bold"), bg="#333333", fg="white")
        title_label.place(x=10, y=10)
        
        start_y = 60
        
        for row_idx, row in enumerate(keyboard_layout):
            if row_idx == 1:
                row_offset = key_size * 0.5
            elif row_idx == 2:
                row_offset = key_size * 0.75
            elif row_idx == 3:
                row_offset = key_size * 1.15
            elif row_idx == 4:
                row_offset = key_size * 0.75
            
            current_x = row_offset + 20
            for key_text in row:
                key_width = special_keys.get(key_text, 1) * key_size
                
                key_id = f"{row_idx}_{key_text}"
                
                switch_type = self.keyboard_layout.get(key_id, "Tanımsız")
                switch_color = self.switch_types.get(switch_type, "#CCCCCC")
                
                key_frame = ttk.Frame(keyboard_bg)
                key_frame.place(x=current_x, y=start_y + row_idx * (key_size + padding), 
                               width=key_width, height=key_size)
                
                key_bg = tk.Canvas(key_frame, bg=switch_color, highlightthickness=2, 
                                highlightbackground="#222222", relief=tk.RAISED, bd=3)
                key_bg.place(relwidth=1, relheight=1)
                
                r, g, b = self.hex_to_rgb(switch_color)
                brightness = (r * 299 + g * 587 + b * 114) / 1000
                text_color = "black" if brightness > 128 else "white"
                
                key_label = tk.Label(key_frame, text=key_text, font=("Arial", 9, "bold"),
                                  bg=switch_color, fg=text_color)
                key_label.place(relwidth=1, relheight=0.7)
                
                switch_label = tk.Label(key_frame, text=switch_type, font=("Arial", 7),
                                     bg=switch_color, fg=text_color)
                switch_label.place(relwidth=1, relheight=0.3, rely=0.7)
                
                key_bg.bind("<Button-1>", lambda e, kid=key_id: self.assign_switch_to_key(kid))
                key_label.bind("<Button-1>", lambda e, kid=key_id: self.assign_switch_to_key(kid))
                switch_label.bind("<Button-1>", lambda e, kid=key_id: self.assign_switch_to_key(kid))
                
                current_x += key_width + padding
    
    def assign_switch_to_key(self, key_id):
        self.keyboard_layout[key_id] = self.active_switch_type
        self.draw_keyboard()

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyboardSwitchMapper(root)
    root.mainloop()
