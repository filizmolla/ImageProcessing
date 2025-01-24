# HW1
### PGM Image Processing Program
Bu program, PGM (Portable Gray Map) formatındaki görüntüleri işlemek için geliştirilmiştir. Program, kullanıcıya farklı görüntü işleme işlemleri sunar ve işlenmiş görüntüleri yeni bir dosyaya kaydeder. Hem ASCII (P2) hem de binary (P5) formatındaki PGM dosyalarını destekler.

#### Özellikler

##### PGM Dosyası Okuma
ASCII (P2) ve Binary (P5) formatlarını destekler. Yorum satırlarını (#) otomatik olarak yoksayar.

##### Negatif Görüntü
Giriş görüntüsünün negatifini oluşturur.

##### Parlaklık Değiştirme
Kullanıcı tarafından belirlenen bir değer eklenerek görüntünün parlaklığı değiştirilir.

##### Eşikleme (Thresholding)
Kullanıcı tarafından verilen eşik değerine göre görüntü, siyah-beyaz hale getirilir.

##### Maske Uygulama (Convolution)
Kullanıcı tarafından tanımlanan bir maske ile görüntü üzerinde filtreleme işlemi yapılır.

##### PGM Dosyası Yazma
İşlenmiş görüntüyü PGM formatında kaydeder.

# HW3 
## Görüntü İşleme ve K-Means Kümeleme  
Bu ödev, bir görüntü işleme görevinde renk histogramlarını kullanarak K-Means algoritması ile görüntülerin otomatik olarak gruplandırılmasını hedefler.  

### Özellikler  
- Görüntülerin RGB histogramlarını hesaplama  
- K-Means kümeleme algoritmasını sıfırdan Python ile uygulama  
- Kümeleme sonuçlarını değerlendirmek için Ayarlanmış Rand İndeksi (ARI) hesaplama  
- Görüntü kümelerini ve histogram merkezlerini görselleştirme  


### Projenin İçeriği  

#### 1. **Histogram Hesaplama**  
Her bir görüntünün RGB histogramı normalize edilerek hesaplanır. Bu histogramlar, K-Means algoritması için veri noktaları olarak kullanılır.  

#### 2. **K-Means Kümeleme Algoritması**  
Proje, K-Means algoritmasını şu şekilde uygular:  
- Rastgele seçilen **k** görüntü histogramı, başlangıç kümeleri için merkezler olarak kullanılır.  
- Her bir veri noktası (görüntü histogramı), en yakın kümeye atanır.  
- Kümelerin merkezleri, o kümedeki veri noktalarının ortalaması alınarak güncellenir.  

#### 3. **Sonuçların Değerlendirilmesi**  
Kümeleme sonuçlarını değerlendirmek için şu metrikler kullanılır:  
- **Adjusted Rand Index (ARI):** Etiketlerin ne kadar iyi eşleştiğini ölçmek için kullanılır.  
- **Confusion Matrix:** Kümeleme sonuçlarının görselleştirilmesi.  


