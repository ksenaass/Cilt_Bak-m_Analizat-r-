import tkinter as tk
from tkinter import messagebox

# Renk ayarları
ARKA_PLAN = "#FCE4EC"  # Ana pencerenin arka planını pastel pembe yapar.
KUTU_RENGI = "#F8DDE6"  # İçerik kutularını açık pembe yapar.
YAZI_RENGI = "#304540"
DUZME_RENGI = "#54735F"

# Seçilebilir cilt bakım içerikleri
ICERIKLER = [
    "Retinoid / retinol",
    "Glikolik asit",
    "Laktik asit",
    "Mandelik asit",
    "Malik asit",
    "Sitrik asit",
    "Tartarik asit",
    "Salisilik asit (BHA)",
    "Diğer BHA / LHA",
    "PHA (gluconolactone vb.)",
    "Azelaik asit",
    "Traneksamik asit",
    "Askorbik asit / C vitamini",
    "Kojik asit",
    "Ferulik asit",
    "Fitik asit",
    "Süksinik asit",
    "Hyaluronik asit",
    "Poliglutamik asit",
    "Alfa arbutin",
    "Arbutin",
    "Benzoyl peroksit",
    "Niasinamid",
    "Peptitler",
]

# Tahriş riski eşleşmelerinde kullanılacak eksfoliyanlar
EKSFOLIYANLAR = {
    "Glikolik asit",
    "Laktik asit",
    "Mandelik asit",
    "Malik asit",
    "Sitrik asit",
    "Tartarik asit",
    "Salisilik asit (BHA)",
    "Diğer BHA / LHA",
    "PHA (gluconolactone vb.)",
}

# Bu içerikler eksfoliyanlarla seçildiğinde uyarı gösterilir
UYARI_ICERIKLERI = {
    "Retinoid / retinol",
    "Benzoyl peroksit",
}

# Ana pencereyi oluşturur
pencere = tk.Tk()
pencere.title("Cilt Bakımı Analizötörü")
pencere.geometry("700x700")
pencere.configure(bg=ARKA_PLAN)

# Başlığı gösterir
tk.Label(
    pencere,
    text="Cilt Bakımı Analizörü",
    font=("Arial", 18, "bold"),
    bg=ARKA_PLAN,
    fg=YAZI_RENGI,
).pack(pady=(20, 8))

# Salisilik asidin BHA ailesinden olduğunu açıklar
tk.Label(
    pencere,
    text="Salisilik asit ayrı listelenir; diğer BHA/LHA türevleri ayrı seçenektir.",
    font=("Arial", 10),
    bg=ARKA_PLAN,
    fg=YAZI_RENGI,
).pack(pady=(0, 14))

# İçerikleri iki sütun halinde gösterir
liste = tk.Frame(pencere, bg=ARKA_PLAN)
liste.pack(padx=24, pady=4, fill="both", expand=True)

liste.columnconfigure(0, weight=1)
liste.columnconfigure(1, weight=1)

secimler = {}

# Her içerik için bir seçim kutusu oluşturur
for sira, icerik in enumerate(ICERIKLER):
    secim = tk.BooleanVar()
    secimler[icerik] = secim

    tk.Checkbutton(
        liste,
        text=icerik,
        variable=secim,
        bg=KUTU_RENGI,
        fg=YAZI_RENGI,
        activebackground=KUTU_RENGI,
        selectcolor="white",
        anchor="w",
        font=("Arial", 10),
        padx=8,
        pady=5,
    ).grid(
        row=sira // 2,
        column=sira % 2,
        sticky="ew",
        padx=5,
        pady=4,
    )


def analiz_et():
    # İşaretlenen içerikleri bir listeye alır
    secilenler = [
        icerik
        for icerik, secim in secimler.items()
        if secim.get()
    ]

    # İçerik seçilmediyse bilgi verir
    if not secilenler:
        messagebox.showinfo("Analiz", "Önce içerik seç.")
        return

    uyarilar = []

    # Retinoid veya benzoyl peroksiti seçili eksfoliyanlarla karşılaştırır
    for uyari_icerigi in UYARI_ICERIKLERI:
        if uyari_icerigi in secilenler:
            for asit in EKSFOLIYANLAR:
                if asit in secilenler:
                    uyarilar.append(f"{uyari_icerigi} + {asit}")

    # Sonuç penceresinin mesajını hazırlar
    if uyarilar:
        mesaj = (
            "Olası tahriş eşleşmeleri:\n\n"
            + "\n".join(f"• {uyari}" for uyari in uyarilar)
        )
    else:
        mesaj = "Seçilen içerikler için belirgin bir tahriş uyarısı bulunamadı."

    # Birden fazla eksfoliyan seçildiyse ek uyarı ekler
    secilen_asitler = [
        icerik for icerik in secilenler
        if icerik in EKSFOLIYANLAR
    ]

    if len(secilen_asitler) > 1:
        mesaj += (
            "\n\nBirden fazla eksfoliyan asit seçildi. "
            "Birlikte kullanım tahriş ihtimalini artırabilir."
        )

    mesaj += "\n\nBu uyarılar kesin bir kimyasal uyumsuzluk anlamına gelmez."

    # Sonucu açılır pencerede gösterir
    messagebox.showinfo("Analiz sonucu", mesaj)


# Analiz düğmesini ekler
tk.Button(
    pencere,
    text="Analiz et",
    command=analiz_et,
    bg=DUZME_RENGI,
    fg="white",
    activebackground="#466653",
    font=("Arial", 11, "bold"),
    padx=24,
    pady=10,
).pack(pady=18)

# Uygulamanın açık kalmasını sağlar
pencere.mainloop()