# Veri Çıkarma (Data Extraction) Süreci

Bu dizin (`/data/extraction/`), "Cascaded OPA–RIS Architectures for NLoS Optical Wireless ISAC" sistematik derlemesinin **veri çıkarma** aşamasıyla ilgili tüm dosyaları ve dokümantasyonu içerir.

## 1. Amaç ve Kapsam

Bu aşamanın temel amacı, tarama (screening) sürecinden sonra "dahil edilen" (included) olarak işaretlenmiş tüm çalışmalardan, önceden tanımlanmış veri alanlarını sistematik bir şekilde çıkarmaktır. Bu veriler, nihai makalede sunulacak olan tematik sentezin, analizlerin ve karşılaştırma tablolarının temelini oluşturur.

Süreç, `/protocol/data_extraction_form.xlsx`'te tanımlanan veri çıkarma formuna ve projenin beş ana teknik eksenine (WD-JD, RC-PR-T, BN-RIS, RPB-Kol, HW-Q/CTRL) sıkı sıkıya bağlıdır.

## 2. İş Akışı (Workflow)

Veri çıkarma süreci aşağıdaki adımları izler:

1.  **Girdi Belirleme:** `/data/screening_log.csv` dosyasında `decision` sütunu `Include` olarak işaretlenmiş tüm çalışmalar bu aşamanın girdisini oluşturur.
2.  **Ana Veritabanını Doldurma:** Dahil edilen her bir çalışma için `/data/included_studies.csv` ana veritabanı dosyasına yeni bir satır eklenir.
3.  **Manuel Veri Çıkarma:** Bir araştırmacı, her bir çalışma için ilgili alanları `/protocol/data_extraction_form.xlsx` şablonuna ve `/protocol/codebook.md`'deki kodlama kurallarına göre manuel olarak doldurur.
    *   **Öncelik:** Her çalışma için en az bir birincil sonuç metriği (primary outcome) kaydedilmelidir.
    *   **Teknik Eksen Haritalama:** Her çalışma, tematik sentezi kolaylaştırmak amacıyla beş teknik eksenden hangilerine katkıda bulunduğuna göre etiketlenir.
4.  **Kalite Güvencesi (QA):** İkinci bir araştırmacı, çıkarılan verilerin bir alt kümesini doğruluk, tutarlılık ve eksiksizlik açısından kontrol eder. Tespit edilen tüm sorunlar ve notlar `/data/qa_logs/qa_log.csv` dosyasına kaydedilir.
5.  **Otomatik Doğrulama:** Analiz aşamasına geçmeden önce, `included_studies.csv` dosyası `scripts/analysis/validate_included_studies.py` betiği kullanılarak projenin veri şemasına göre otomatik olarak doğrulanır.

## 3. Temel Dosyalar ve Anlamları

*   **/data/included\_studies.csv**: Dahil edilen tüm çalışmalardan çıkarılan verileri içeren **ana ve tekil doğruluk kaynağı** olan CSV dosyasıdır. Tüm analizler bu dosya üzerinden yürütülür.
*   **/protocol/data\_extraction\_form.xlsx**: Veri alanlarını, açıklamalarını ve beklenen veri türlerini tanımlayan Excel şablonudur. Veri çıkarma sürecinde bir rehber görevi görür.
*   **/protocol/codebook.md**: Tutarlılığı sağlamak amacıyla `enum` (sınıflandırılmış) alanlar için kontrollü kelime dağarcığını ve tanımları içerir (örn: `architecture`, `channel_regime`).
*   **Bu Dizin (`/data/extraction/`)**: Veri çıkarma sürecinde kullanılan ara dosyaları (örn: referans yöneticisinden ham dışa aktarımlar, geçici analiz sayfaları) barındırabilir. Bu dosyalar çalışma dosyaları olarak kabul edilir ve ana `included_studies.csv` dosyasına göre ikincil öneme sahiptir.

## 4. Veri Alanları ve Kodlama Kuralları

Veri alanlarının tam listesi ana `README.md` dosyasında ve veri çıkarma formunda detaylandırılmıştır. Süreç boyunca uyulması gereken temel ilkeler şunlardır:

*   **Birim Tutarlılığı:** Belirtilen birimlere (örn: `nm`, `m`, `dB`, `deg`) harfiyen uyulmalıdır.
*   **Kontrollü Kelime Dağarcığı:** `codebook.md`'de tanımlanan `enum` değerleri tam olarak kullanılmalıdır.
*   **Eksik Veri Yönetimi:** Eğer bir makalede ilgili veri bulunmuyorsa, alan boş bırakılmalı ve `notes` sütununda bir açıklama yapılmalıdır.
*   **Normalizasyon:** Veriler orijinal birimlerinden dönüştürülürse (örn: inç'ten metreye), bu dönüşüm `normalization_notes` sütununda mutlaka belirtilmelidir.
