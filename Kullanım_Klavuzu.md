# OWISAC PRISMA İncelemesi Kullanım Kılavuzu

Bu kılavuz, OWISAC PRISMA incelemesi sürecinde oluşturulan dosyaların kullanımını açıklamaktadır.

## 1. Arama Stratejisi ve Kayıtları

### `02_Arama/Arama_Stratejisi.md`
Bu dosya, farklı veritabanları (IEEE Xplore, Optica Publishing, ScienceDirect, arXiv) için kullanılan arama stratejilerini ve filtrelerini detaylandırır. Optik ISAC, NLoS senaryoları, OPA/RIS/SLM/metasurface teknolojileri ve ilgili algoritmalar üzerine odaklanılmıştır.

### `02_Arama/Arama_Log.csv`
Bu CSV dosyası, yapılan arama sorgularının ve uygulanan filtrelerin bir kaydını tutar. Hangi veritabanında hangi sorgunun kullanıldığı ve uygulanan filtreler burada listelenir.

## 2. Tarama ve Dışlama Kriterleri

### `03_Tarama/Uygunluk_Ölçütleri.md`
Bu dosya, inceleme sürecinde makalelerin dahil edilme ve hariç tutulma kriterlerini (PRISMA dilinde operasyonel olarak) tanımlar. Konu, metrikler, yayın türü, dil, yıl ve ortam gibi faktörler belirtilmiştir.

### `03_Tarama/Dışlama_Kodları.md`
Bu dosya, tarama sürecinde kullanılan dışlama kodlarını ve anlamlarını listeler. Bu kodlar, makalelerin neden elendiğini belirtmek için kullanılır (örn. N1: Optik alan dışı, N5: Metrik yok).

### `03_Tarama/Screening_Log.csv`
Bu CSV dosyası, başlık ve özet taramasının (T/A) sonuçlarını kaydeder. Her bir kaydın kararını (Include, Exclude, Maybe) ve ilgili dışlama kodunu içerir.

### `03_Tarama/FullText_Dışlama_Nedenleri.csv`
Bu CSV dosyası, tam metin incelemesi sonrasında elenen makalelerin nedenlerini detaylandırır. Hangi dışlama kodunun uygulandığı ve kısa bir gerekçesi burada belirtilir.

## 3. PRISMA Akış Sayıları

### `03_Tarama/PRISMA_Akış_Sayıları.csv`
Bu CSV dosyası, PRISMA akış şemasına uygun olarak, inceleme sürecinin her aşamasındaki kayıt sayısını özetler. Veritabanı aramalarından başlayarak nihai olarak dahil edilen çalışmalara kadar olan süreci gösterir.

Bu dosyalar, OWISAC PRISMA incelemesinin sistematik bir şekilde yürütülmesine ve belgelenmesine yardımcı olmak için oluşturulmuştur.
