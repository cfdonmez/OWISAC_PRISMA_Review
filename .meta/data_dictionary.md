# Data Dictionary (v0.2)

Bu sözlük `data/` altındaki CSV/XLSX dosyaları için PRISMA-2020 ve PRISMA-S uyumlu asgari gereksinimleri tanımlar.

## 1) Ana Veri Dosyaları

### 1.1) screening_log.csv
Tarama sürecindeki her bir karar anını kaydeder.

**Zorunlu Kolonlar:**
- `record_id` (string) — Tekil kimlik.
- `stage` (enum) — Karar aşaması: { tiab, fulltext }.
- `decision` (enum) — Verilen karar: { include, exclude, unsure }.
- `decided_by` (string) — Karar veren kişi/ekip etiketi.
- `decided_at` (datetime, ISO 8601) — Karar zamanı (örn: `2025-09-28T12:34:56Z`).

**Önerilen/Opsiyonel Kolonlar:**
- `source_db` (enum) — Veritabanı (örn: IEEE Xplore, Scopus).
- `source_id` (string) — Veritabanındaki orijinal kimlik (DOI, ArXiv ID, vb.).
- `search_run_id` (string) — `search_log.csv` ile ilişkilendirme anahtarı.
- `automation_tool` (string) — Kullanılan otomasyon aracının adı.
- `automation_flag` (enum) — Otomasyonun etkisi: { screened_out, prioritized, none }.
- `conflict` (bool) — İkili taramada uyuşmazlık olup olmadığı.
- `resolver` (string) — Uyuşmazlığı çözen kişi.
- `resolved_at` (datetime, ISO 8601) — Uyuşmazlığın çözülme zamanı.
- `status` (string) — Eski iş akışı durumu (uyumluluk için tutulabilir).

### 1.2) excluded_studies.csv
Hariç tutulan çalışmaların gerekçelerini listeler.

**Zorunlu Kolonlar:**
- `record_id` (string) — Tekil kimlik.
- `stage` (enum) — Dışlama aşaması: { tiab, fulltext }.
- `reason_code` (enum) — Standart dışlama gerekçesi.
  - **Kabul Edilen Değerler:** { out_of_scope, not_optical, no_opa_or_ris, no_nlos_or_turbulence, insufficient_methods, no_metrics, duplicate, not_substantial, **unobtainable_fulltext**, **retracted**, **wrong_pub_type** }

**Opsiyonel Kolonlar:**
- `reason` (free-text) — İnsan tarafından okunabilir ek açıklama.

### 1.3) included_studies.csv
Derlemeye dahil edilen çalışmaların özelliklerini tanımlar.

**Zorunlu Kolonlar:**
- `record_id` (string) — Tekil kimlik.
- `citation` (string) — Tam bibliyografik künye.
- `title` (string) — Çalışmanın başlığı.
- `authors` (string) — Yazar listesi.
- `year` (int) — Yayın yılı.
- `venue` (string) — Yayınlandığı yer (dergi, konferans, vb.).
- `pub_type` (enum) — Yayın türü: { journal, conference, preprint, thesis, other }.
- `peer_reviewed` (bool) — Hakem denetiminden geçip geçmediği.
- `doi` (string) — Varsa zorunlu.
- `url` (string) — DOI yoksa zorunlu.

**Kuvvetle Önerilen Kolonlar:**
- `study_design` (enum) — Çalışma tasarımı: { simulation, experiment, hybrid, review }.
- `dataset_url` (string) — Varsa veri setinin URL'si.
- `code_url` (string) — Varsa kodun URL'si.

## 2) Log Dosyaları (PRISMA-S ve Şeffaflık için)

### 2.1) search_log.csv
Yapılan her bir veritabanı aramasını kaydeder.

**Zorunlu Kolonlar:**
- `search_run_id` (string) — Bu arama işlemini tanımlayan tekil kimlik.
- `source_db` (string) — Arama yapılan veritabanı.
- `platform_interface` (string) — Arama arayüzü (örn: "IEEE Xplore Advanced Search").
- `query_string` (string) — Çalıştırılan tam arama sorgusu.
- `date_ran` (date, ISO 8601) — Aramanın yapıldığı tarih.
- `results_n` (int) — Aramadan dönen sonuç sayısı.

### 2.2) dedup_log.csv
Tekrar (duplicate) kayıtların nasıl birleştirildiğini kaydeder.

**Zorunlu Kolonlar:**
- `primary_record_id` (string) — Korunan ana kaydın kimliği.
- `merged_record_ids` (string) — Birleştirilen diğer kayıtların kimlikleri (virgülle ayrılmış).
- `method_tool` (string) — Kullanılan yöntem veya araç (örn: "Zotero", "manual").
- `decided_by` (string) — Kararı veren kişi.
- `decided_at` (datetime, ISO 8601) — Karar zamanı.

### 2.3) automation_log.csv
Otomasyon araçlarının kullanımını detaylandırır.

**Zorunlu Kolonlar:**
- `record_id` (string) — İşlem gören kaydın kimliği.
- `tool` (string) — Kullanılan araç (örn: "ASReview", "Rayyan AI").
- `version` (string) — Aracın sürümü.
- `threshold` (float) — Varsa, kullanılan karar eşiği.
- `action` (string) — Aracın yaptığı işlem (örn: "screened_out", "prioritized").
