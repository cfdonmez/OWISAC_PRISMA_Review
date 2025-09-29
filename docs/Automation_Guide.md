# 🚀 OWISAC PRISMA Review - Automation Guide

Bu kılavuz, kurduğumuz **Writer-First** otomasyon sistemlerini kullanmanıza yardımcı olur. Şu anda **4 güçlü otomasyon** sistemimiz var ve hepsi **pipeline'a entegre** edilmiş durumda.

## 📋 İçindekiler

- [Genel Bakış](#genel-bakış)
- [Quick Start](#quick-start)
- [Tek Tek Script Kullanımı](#tek-tek-script-kullanımı)
- [Pipeline Kullanımı](#pipeline-kullanımı)
- [CI/CD Entegrasyonu](#cicd-entegasyonu)
- [Özelleştirme](#özelleştirme)
- [Sorun Giderme](#sorun-giderme)

## 🎯 Genel Bakış

### Kurduğumuz Otomasyon Sistemleri:

| Sistem | Script | Amaç | Çıktı |
|--------|--------|------|-------|
| **PRISMA Sayımları** | `insert_counts_snippet.py` | Kayıt sayıları ve eleme gerekçeleri | `results/snippets/prisma_counts.md` |
| **Beamforming Kırılımı** | `synth_build_subgroups.py` | Beamforming stratejilerine göre metrik ortalaması | `results/synthesis_tables/subgroups.md` |
| **Architecture Kırılımı** | `synth_build_architectures.py` | Mimari bileşenlere göre metrik ortalaması | `results/synthesis_tables/architectures.md` |
| **Risk of Bias** | `rob_build_summary.py` | Çalışma kalitesi değerlendirme özeti | `results/synthesis_tables/rob_summary.md` |

### Writer-First Yaklaşım:

✅ **Senin yapacağın:** İçerik yazmak, yorum yapmak, bilimsel tartışma yürütmek
✅ **Otomasyonun yapacağı:** Sayıları otomatik çekip, doğru yere yerleştirmek

## 🚀 Quick Start

### Tüm Sistemi Tek Komutla Çalıştır:

```bash
# Tüm otomasyon sistemlerini çalıştır
python scripts/run_pipeline.py

# Manuscript'i derle (tablolar otomatik dahil olur)
python scripts/analysis/build_manuscript.py

# Sonucu kontrol et
grep -n "Synthesis" manuscript/full_article.md
```

### Sadece İhtiyacın Olan Script'i Çalıştır:

```bash
# Sadece PRISMA sayımlarını güncelle
python scripts/analysis/insert_counts_snippet.py

# Sadece alt-grup özetini güncelle
python scripts/analysis/synth_build_subgroups.py

# Sadece architecture kırılımını güncelle
python scripts/analysis/synth_build_architectures.py

# Sadece RoB assessment'ı güncelle
python scripts/analysis/rob_build_summary.py
```

## 🔧 Tek Tek Script Kullanımı

### 1. PRISMA Sayım Otomasyonu

```bash
python scripts/analysis/insert_counts_snippet.py
```

**Ne Yapar:**
- `results/prisma_counts.json` dosyasını okur
- PRISMA sayımlarını otomatik formatlar
- `results/snippets/prisma_counts.md` dosyasına yazar

**Çıktı:**
```markdown
### PRISMA Counts Summary (auto)

We identified **3** records; screened **1**; assessed **1** full texts;
excluded **1** at title/abstract; and included **1** qualitatively and **0** quantitatively.
```

### 2. Beamforming Alt-grup Özeti

```bash
python scripts/analysis/synth_build_subgroups.py
```

**Ne Yapar:**
- `data/extraction/synthesis_input_demo.csv` dosyasını okur
- Beamforming stratejilerine göre metrikleri gruplar
- Ortalama değerleri hesaplar

**Çıktı:**
```markdown
| Beamforming | Metric | Mean value |
|---|---|---:|
| hybrid (ampl+phase) | HPBW | 0.8 |
| phase-only | BER | 1e-05 |
| phase-only | SINR_dB | 18.5 |
```

### 3. Architecture Components Kırılımı

```bash
python scripts/analysis/synth_build_architectures.py
```

**Ne Yapar:**
- Aynı CSV dosyasını okur
- Architecture bileşenlerine göre metrikleri gruplar
- Ortalama değerleri hesaplar

**Çıktı:**
```markdown
| Architecture | Metric | Mean value |
|---|---|---:|
| OPA+RIS | BER | 1e-05 |
| OPA+RIS | SINR_dB | 18.5 |
| OPA→RIS cascade | HPBW | 0.8 |
```

### 4. Risk of Bias Assessment

```bash
python scripts/analysis/rob_build_summary.py
```

**Ne Yapar:**
- Çalışma verilerini analiz eder
- 5 domain'de risk değerlendirmesi yapar:
  - Randomization
  - Deviations from intended interventions
  - Missing outcome data
  - Measurement of outcome
  - Selection of reported result

**Çıktı:**
```markdown
| Study ID | Randomization | Deviations | Missing Data | Measurement | Selection | Overall |
|----------|---------------|------------|--------------|-------------|-----------|---------|
| R003 | Low | Low | Low | Low | Low | **Low** |
```

## 🔄 Pipeline Kullanımı

### Tüm Süreci Otomatik Çalıştır:

```bash
python scripts/run_pipeline.py
```

**Pipeline Adımları:**
1. **Validate data files** → Veri dosyalarını doğrula
2. **Compute PRISMA counts** → PRISMA sayımlarını hesapla
3. **Validate PRISMA counts** → Sayımları doğrula
4. **Build PRISMA flow figure** → Flow diagram üret (Pillow eksik)
5. **Synthesis validate** → Sentez verilerini doğrula
6. **Synthesis build tables** → Ana sentez tablolarını oluştur
7. **Synthesis build subgroups** → Alt-grup özetini oluştur
8. **Synthesis build architectures** → Architecture kırılımını oluştur
9. **Build RoB summary** → Risk of bias özetini oluştur
10. **Build manuscript** → Tüm içeriği birleştir

### Sadece Sentez Kısımını Çalıştır:

```bash
# Sadece sentez ve tablo oluşturma
python -c "
import subprocess, sys
steps = [
    ('Validate data files', [sys.executable, 'scripts/analysis/validate_data_files.py']),
    ('Compute PRISMA counts', [sys.executable, 'scripts/analysis/compute_prisma_counts.py']),
    ('Synthesis build subgroups', [sys.executable, 'scripts/analysis/synth_build_subgroups.py']),
    ('Synthesis build architectures', [sys.executable, 'scripts/analysis/synth_build_architectures.py']),
    ('Build RoB summary', [sys.executable, 'scripts/analysis/rob_build_summary.py']),
    ('Build manuscript', [sys.executable, 'scripts/analysis/build_manuscript.py']),
]
for name, cmd in steps:
    print(f'=== {name} ===')
    subprocess.run(cmd, text=True).returncode == 0 and print(f'[ok] {name}')
"
```

## 🔄 CI/CD Entegrasyonu

### GitHub Actions Workflow:

Her `git push` ve `pull request`'te otomatik çalışır:

```yaml
- name: Synthesis validate & build
  run: |
    python scripts/analysis/synth_build_subgroups.py
    python scripts/analysis/synth_build_architectures.py
    python scripts/analysis/rob_build_summary.py
    # Tüm tabloları kontrol et
    sed -n "1,80p" results/synthesis_tables/*.md
```

### Manuel Trigger:

```bash
# GitHub Actions tab'ında manuel çalıştır
# Veya VSCode'da terminalden
python scripts/run_pipeline.py
```

## 🎨 Özelleştirme

### Yeni Kırılım Tablosu Eklemek:

1. **Script oluştur:**
```python
# scripts/analysis/synth_build_[yeni_kırılım].py
key = (r["yeni_sütun"], r["metric"])
```

2. **Pipeline'a ekle:**
```python
# scripts/run_pipeline.py
("Synthesis build [yeni_kırılım]", [sys.executable, "scripts/analysis/synth_build_[yeni_kırılım].py"]),
```

3. **CI'ya ekle:**
```yaml
# .github/workflows/prisma.yml
python scripts/analysis/synth_build_[yeni_kırılım].py
```

4. **Results'a dahil et:**
```markdown
<!-- INCLUDE: results/synthesis_tables/[yeni_kırılım].md -->
```

### Mevcut Kırılımları Değiştirmek:

**Örnek - Turbulence Parameters Kırılımı:**
```python
# scripts/analysis/synth_build_turbulence.py
key = (r["turbulence_params"], r["metric"])
```

## 🛠️ Sorun Giderme

### Yaygın Hatalar:

**1. "Missing data/extraction/synthesis_input_demo.csv"**
```bash
# Çözüm: Veri dosyasını kontrol et
ls -la data/extraction/synthesis_input_demo.csv
```

**2. "Pillow missing"**
```bash
# Çözüm: Pillow'u yükle (flow diagram için)
pip install pillow
```

**3. "Module not found"**
```bash
# Çözüm: Requirements'ı yükle
pip install -r requirements.txt
```

**4. "Permission denied"**
```bash
# Çözüm: Yazma izinlerini kontrol et
chmod 666 results/synthesis_tables/*.md
```

### Debug Modu:

```bash
# Verbose output için
python -c "
import sys
sys.path.append('.')
from scripts.analysis.synth_build_subgroups import main
main()
"
```

### Log Kontrolü:

```bash
# Son çalıştırma loglarını kontrol et
tail -20 results/qa_data_report.txt
```

## 📈 İleri Seviye Kullanım

### Çoklu Kırılım (Intersection):

```python
# Beamforming + Architecture birlikte
key = (r["beamforming_strategy"], r["architecture_components"], r["metric"])
```

### Zaman Serisi Analizi:

```python
# Yıla göre kırılım
key = (r["year"], r["metric"])
```

### Özel Metrik Filtreleme:

```python
# Sadece belirli metrikler
if r["metric"] in ["SINR_dB", "BER", "HPBW"]:
    # İşleme al
```

## 🎯 Best Practices

### Writer-First Workflow:

1. **İçeriğini yaz:** `manuscript/sections/03_results.md`
2. **Veri tablolarını güncelle:** `python scripts/run_pipeline.py`
3. **Sonucu kontrol et:** `grep -n "Synthesis" manuscript/full_article.md`
4. **Gerekirse düzenle:** Tekrar 1. adıma dön

### Version Control:

```bash
# Her büyük değişiklikten önce
git add .
git commit -m "feat: add new [kırılım] automation"

# Pipeline sonuçlarını kontrol et
git diff results/synthesis_tables/
```

### Performance:

```bash
# Büyük veri setleri için
import pandas as pd  # Daha hızlı CSV işleme
```

## 📞 Destek

Bu otomasyon sistemleri hakkında sorularınız için:
- Bu kılavuzu güncelleyin
- Yeni kırılım önerilerinizi ekleyin
- Sorun giderme bölümünü genişletin

---

**Son Güncelleme:** Otomasyon sistemleri sürekli geliştiriliyor. En güncel kullanım için `python scripts/run_pipeline.py` komutunu çalıştırın ve çıktıları kontrol edin.
