#!/usr/bin/env python3
# Kahve Fincanında Yüzme Yapan Kedi Simülatörü
# Bu kod gerçekten çalışır. Gerçekten.

import random
import time

def yuzme_simule_et():
    print("\n🐱 Kahve fincanına giriyor...")
    time.sleep(1)
    
    ascii_kedi = """
      /\\_/\\
     ( o.o )
      > ^ <
     /|   |\\
    (_|   |_)
    """
    print(ascii_kedi)
    print("Yüzüyor... yüzüyor... kahve sıçratıyor...")
    time.sleep(2)
    
    sonuc = random.choice([
        "BAŞARILI: Kedi kahveyi içti, sen kaldın.",
        "FELAKET: Kedi boğuldu ama gülüyor. İmkansız.",
        "ORTA: Kedi çıktı, fincan boş, hayat boş.",
        "SÜRPRİZ: Kedi artık kahve kokuyor. Sonsuza dek."
    ])
    print(f"\nSonuç: {sonuc}")
    
    # Gizli şey: hiçbir şey gizli değil. Tamamen değil.
    # kayyum_onayli = True  # sadece yorum

if __name__ == "__main__":
    print("Dünyanın en ciddi kedi yüzme simülatörü başlatılıyor...")
    yuzme_simule_et()
    print("\nTeşekkürler. Bilim kazandı.")