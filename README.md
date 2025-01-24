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

