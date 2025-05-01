import tkinter as tk
from tkinter import messagebox
import time
import pygame

def predict_age():
    try:
        user_age = int(age_entry.get())
        if user_age < 0 or user_age > 150:
            messagebox.showerror("Hata", "Lütfen gerçekçi bir yaş girin, uzaylı mısınız? 😜")
            return
        predict_button.config(state="disabled")
        result_label.config(text="Yaşınız tahmin ediliyor... Lütfen bekleyin!")
        root.update()
        time.sleep(2)  # Trollemek için 2 saniye bekletiyoruz
        
        # Ses çalma
        pygame.mixer.init()
        pygame.mixer.music.load("pode-pode-pode-sentar.mp3")  # Kendi ses dosyanızın adını buraya yazın
        pygame.mixer.music.set_volume(0.01)  # Ses seviyesini düşür (0.0 - 1.0 arası)
        pygame.mixer.music.play()
        
        # Tahmin popup
        messagebox.showinfo("Tahmin Sonucu", f"Galiba yaşınız: {user_age}! 😎\nNasıl bildik ama? Hihihi!")
        
        # Ses durdurma (opsiyonel, döngü yoksa gerekmeyebilir)
        pygame.mixer.music.stop()
        
        result_label.config(text="")
        predict_button.config(state="normal")
        age_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin, harflerle yaş mı olur? 😜")
    except pygame.error as e:
        messagebox.showerror("Hata", f"Ses dosyası yüklenemedi: {e}\nLütfen 'troll_sound.mp3' dosyasının doğru yerde olduğundan emin olun!")

# Ana pencere
root = tk.Tk()
root.title("Süper Trol Yaş Tahmin Uygulaması")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Başlık
title_label = tk.Label(root, text="Yaş Tahmin Ustası!", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#ff4500")
title_label.pack(pady=20)

# Yaş girişi
age_label = tk.Label(root, text="Yaşınızı Girin:", font=("Arial", 14), bg="#f0f0f0")
age_label.pack(pady=10)
age_entry = tk.Entry(root, font=("Arial", 14), width=10)
age_entry.pack(pady=10)

# Tahmin butonu
predict_button = tk.Button(root, text="Yaşı Tahmin Et!", font=("Arial", 14), bg="#32cd32", fg="white", command=predict_age)
predict_button.pack(pady=20)

# Sonuç etiketi
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0", fg="#0000ff")
result_label.pack(pady=10)

# Footer
footer_label = tk.Label(root, text="Trol Teknolojileri A.Ş. © 2025", font=("Arial", 10), bg="#f0f0f0")
footer_label.pack(side="bottom", pady=10)

# Ana döngü
root.mainloop()