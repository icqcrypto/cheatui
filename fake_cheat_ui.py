#!/usr/bin/env python3
# fake_cheat_ui.py
# Zararsız sahte "hile arayüzü" demo — sadece görsel simülasyon ve log üretir.

import tkinter as tk
from tkinter import ttk, messagebox
import random
import time

class FakeCheatUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("UltraHack 9000 - Demo (Fake)")
        self.geometry("640x440")
        self.resizable(False, False)

        # Üst başlık
        header = ttk.Label(self, text="UltraHack 9000 — Demo Interface", font=("Segoe UI", 16, "bold"))
        header.pack(pady=10)

        # Sağ / sol frame
        main_frame = ttk.Frame(self)
        main_frame.pack(fill="both", expand=True, padx=12, pady=6)

        left = ttk.Frame(main_frame, width=320)
        left.pack(side="left", fill="y", padx=(0,8))
        right = ttk.Frame(main_frame)
        right.pack(side="right", fill="both", expand=True)

        # Sahte seçenekler (toggles)
        ttk.Label(left, text="Hile Seçenekleri", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(0,6))
        self.options = {}
        for name in ["Aimbot", "Wallhack", "NoRecoil", "SpeedHack", "AutoLoot"]:
            var = tk.BooleanVar(value=False)
            cb = ttk.Checkbutton(left, text=name, variable=var)
            cb.pack(anchor="w", pady=2)
            self.options[name] = var

        ttk.Separator(left, orient="horizontal").pack(fill="x", pady=8)
        ttk.Label(left, text="Ayarlar", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(0,6))

        # Slider örneği (sadece görsel)
        ttk.Label(left, text="Aimbot Hassasiyeti").pack(anchor="w")
        self.aim_slider = ttk.Scale(left, from_=1, to=10, orient="horizontal")
        self.aim_slider.set(5)
        self.aim_slider.pack(fill="x", pady=4)

        ttk.Label(left, text="Speed Factor").pack(anchor="w")
        self.speed_spin = ttk.Spinbox(left, from_=1, to=5, width=5)
        self.speed_spin.set("1")
        self.speed_spin.pack(anchor="w", pady=4)

        # Start / Stop butonları
        btn_frame = ttk.Frame(left)
        btn_frame.pack(fill="x", pady=(10,0))
        self.start_btn = ttk.Button(btn_frame, text="Başlat", command=self.start_fake)
        self.start_btn.pack(side="left", expand=True, fill="x", padx=(0,4))
        self.stop_btn = ttk.Button(btn_frame, text="Durdur", command=self.stop_fake, state="disabled")
        self.stop_btn.pack(side="right", expand=True, fill="x", padx=(4,0))

        # Sağ tarafta log ve süslü bilgiler
        ttk.Label(right, text="Sistem Çıktısı", font=("Segoe UI", 12, "bold")).pack(anchor="w")
        self.log = tk.Text(right, height=18, state="disabled", wrap="word")
        self.log.pack(fill="both", expand=True, pady=(4,6))

        # Durum çubuğu
        self.status_var = tk.StringVar(value="Hazır — Demo (zararsız)")
        status = ttk.Label(self, textvariable=self.status_var, relief="sunken", anchor="w")
        status.pack(fill="x", side="bottom")

        # İç durum
        self.running = False
        self.after_id = None

        # Açıklama uyarısı
        ttk.Label(self, text="(Bu bir demo. Gerçek hile yapmaz — sadece simülasyon.)", font=("Segoe UI", 8, "italic")).pack(side="bottom", pady=4)

    def append_log(self, text):
        self.log.configure(state="normal")
        timestamp = time.strftime("%H:%M:%S")
        self.log.insert("end", f"[{timestamp}] {text}\n")
        self.log.see("end")
        self.log.configure(state="disabled")

    def start_fake(self):
        selected = [k for k,v in self.options.items() if v.get()]
        if not selected:
            if not messagebox.askyesno("Uyarı", "Hiçbir seçenek seçilmedi. Devam edilsin mi?"):
                return
        self.running = True
        self.start_btn.configure(state="disabled")
        self.stop_btn.configure(state="normal")
        self.status_var.set("Çalışıyor — Simülasyon aktif")
        self.append_log("Simülasyon başlatıldı.")
        self.cycle_simulation()

    def stop_fake(self):
        if self.after_id:
            self.after_cancel(self.after_id)
            self.after_id = None
        self.running = False
        self.start_btn.configure(state="normal")
        self.stop_btn.configure(state="disabled")
        self.status_var.set("Durduruldu — Hazır")
        self.append_log("Simülasyon durduruldu.")

    def cycle_simulation(self):
        # Bu fonksiyon sadece rastgele "etki" ve log üretir — hiçbir şey değiştirmez.
        if not self.running:
            return
        actions = [
            "Tarama tamamlandı: 42 hedef bulundu (sadece demo).",
            "Çekirdek modül yükleniyor... (simülasyon)",
            "Aimbot hedef kilitlendi: oyuncu_{}".format(random.randint(100,999)),
            "Wallhack: gizli nesneler gösteriliyor (görsel).",
            "NoRecoil aktif — geri tepme %{} azaltıldı (sahte değer).".format(random.randint(70,95)),
            "SpeedHack: hız faktörü set edildi → x{}".format(self.speed_spin.get()),
            "AutoLoot: etraftan 12 eşya toplandı (simülasyon).",
            "Güncelleme kontrolü: yeni demo modülü bulunmadı."
        ]
        msg = random.choice(actions)
        # Hafifçe değiştir ki daha canlı olsun
        if random.random() < 0.15:
            msg += " ✔"
        elif random.random() < 0.10:
            msg += " ✖ (simulated fail)"
        self.append_log(msg)

        # Duruma göre sahte istatistik güncelle
        fake_stat = f"FPS boost: +{random.randint(1,8)} | Ping: {random.randint(20,80)}ms"
        self.status_var.set(fake_stat)

        # tekrar zamanla çağır
        self.after_id = self.after(1500 + random.randint(0,2000), self.cycle_simulation)

if __name__ == "__main__":
    app = FakeCheatUI()
    app.mainloop()
