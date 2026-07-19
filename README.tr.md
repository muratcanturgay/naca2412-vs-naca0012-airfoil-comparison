# Kanat Profili Aerodinamik Analizi: NACA 2412 vs NACA 0012

*(English version: [README.md](README.md))*

## Genel Bakış
Bu proje, iki iyi bilinen kanat profilinin — **kavisli NACA 2412** ve **simetrik NACA 0012** — farklı hücum açılarındaki aerodinamik performansını XFOIL ile hesaplayıp Python/Matplotlib ile görselleştirerek karşılaştırıyor.

## Yöntem
- **Araç:** XFOIL (Mark Drela, MIT) — kanat geometrisi ve akış koşullarından kaldırma/sürükleme karakteristiklerini hesaplayan 2 boyutlu bir kanat analiz programı.
- **Koşullar:** Reynolds sayısı = 200.000 (küçük İHA/model uçak ölçeğini temsil eder), Mach = 0 — doğrudan karşılaştırma yapabilmek için her iki kanat için de aynı.
- **Hücum açısı aralığı:** NACA 2412: -5° ile 15°. NACA 0012: -5° ile 14°. (Küçük farklar, XFOIL'in her kanat için sonuç üretebildiği gerçek açı aralığını yansıtıyor.)

## Sonuçlar — NACA 2412 (kavisli)
- Kaldırma katsayısı (CL), açı arttıkça düzenli şekilde artıyor, 9-11° civarında yavaşlıyor, bu da stall'a yaklaşıldığını gösteriyor.
- Sürükleme katsayısı (CD), -1° ile 5° arasında düşük kalıyor, 7°'den sonra hızla artıyor.
- **En yüksek verimlilik (CL/CD ≈ 67), yaklaşık 6-7°'de elde ediliyor.**

## Sonuçlar — NACA 0012 (simetrik)
- Simetrik bir kanat için beklendiği gibi, 0° hücum açısında CL tam olarak sıfır (kavisli 2412 kanadı ise, kavisi sayesinde 0°'de bile kaldırma üretiyordu).
- **En yüksek verimlilik (CL/CD ≈ 47), yaklaşık 5°'de elde ediliyor** — 2412'nin en yüksek verimliliğinden belirgin şekilde daha düşük.

## Karşılaştırma — Hangi Kanat "Daha İyi"?
Kavisli NACA 2412, simetrik NACA 0012'ye göre **daha yüksek maksimum verimlilik** elde ediyor — yani en verimli açısında, sürüklemeye kıyasla daha fazla kaldırma üretiyor. Bu yüzden kavisli kanatlar, verimli kaldırma üretiminin öncelikli olduğu ana kanatlarda tipik olarak tercih ediliyor.

Ancak NACA 0012 gibi simetrik kanatların kendine has bir avantajı var: **her iki yönde (pozitif ve negatif açı) aynı performansı gösteriyorlar** — bu, kuyruk yüzeyleri ve dengeleyiciler gibi kontrol yüzeylerinde, ya da ters uçarken de eşit performans gerektiren akrobasi uçaklarında değerli. Kavis, bu simetriyi tek yönlü daha yüksek verimlilikle takas ediyor.

## Kullanılan Araçlar
- XFOIL (aerodinamik hesaplama)
- Python 3 + Matplotlib (veri görselleştirme)

## Dosyalar
- `naca2412_naca0012_comparison_en.py` / `naca2412_naca0012_comparison_tr.py` — birleştirilmiş analiz ve karşılaştırma scriptleri (İngilizce/Türkçe yorum satırlarıyla)
- `data/naca2412_xfoil_output.txt`, `data/naca0012_xfoil_output.txt` — her iki kanat için ham XFOIL çıktısı (polar veri)
- Grafik görselleri — kaldırma, sürükleme ve verimlilik için tekil ve karşılaştırmalı grafikler
