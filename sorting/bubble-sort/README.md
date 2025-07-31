# Bubble Sort Algorithm

Bubble Sort, en basit sıralama algoritmalarından biridir. Komşu elemanları karşılaştırarak çalışır.

## Algoritma Açıklaması

1. Dizinin başından itibaren komşu elemanları karşılaştır
2. Eğer sol eleman sağ elemandan büyükse, yerlerini değiştir
3. Dizinin sonuna kadar bu işlemi tekrarla
4. Her geçişte en büyük eleman sonuna "kabarcık" gibi çıkar
5. Dizi sıralanana kadar bu işlemi tekrarla

## Complexity Analysis

- **Time Complexity:** 
  - Best Case: O(n) - Dizi zaten sıralıysa
  - Average Case: O(n²)
  - Worst Case: O(n²) - Dizi ters sıralıysa
  
- **Space Complexity:** O(1) - In-place sıralama

## Avantajları
- Basit implementasyon
- In-place sıralama (ek alan gerektirmez)
- Stable algorithm (eşit elemanların sırası korunur)

## Dezavantajları
- Büyük dizilerde çok yavaş
- O(n²) complexity
- Pratik kullanım için uygun değil
