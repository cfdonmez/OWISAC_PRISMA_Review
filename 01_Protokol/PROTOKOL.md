# PROTOKOL (PRISMA-P — Systematic Scoping Review)

## 1) Arka plan ve amaç
- Konu: [NLoS optik ISAC; OPA→RIS kaskadı; türbülans ve quantization-aware tasarım]
- Neden: [Literatür parçalı; SINR–MTF birlikte rapor az; kalibrasyon/algoritmalar dağınık]
- Amaç: [Literatürü SINR–MTF Pareto ekseninde sınıflandırmak; benchmark önerileri]

## 2) Araştırma soruları (PICOS)
- **P:** [Serbest-uzay optik ISAC; NLoS; türbülanslı kanal]
- **I:** [RIS/SLM/metayüzey + OPA; quantization-aware]
- **C:** [LoS] • [OPA-only] • [ideal/sonsuz-bit faz] • [aktif röle (opsiyon)]
- **O:** [Algılama: MTF/Strehl/EE50; İletişim: SINR/EVM/BER]
- **S:** [sim/lab/field; ASM/Fresnel; Cn²; 1–3 bit faz]

## 3) Uygunluk ölçütleri
- **Dahil:** [NLoS veya OPA/RIS/SLM] VE [SINR/EVM/BER veya MTF/Strehl/EE50]; [2005–2025]; [EN]; [makale/konferans/review]
- **Hariç:** [fiber-only] • [yalnız RF-ISAC] • [salt malzeme/kimya] • [metrik yok] • [patent]
- Gri literatür / preprint: [dahil/hariç]

## 4) Bilgi kaynakları ve arama özeti
- Veri tabanları: [IEEE Xplore, Optica, ScienceDirect, arXiv (+WoS/Scopus ops.)]
- Ortak filtreler: [2005–2025; EN; Article/Proceedings/Review; NOT fiber/fibre]
- Çekirdek dizge: ["optical ISAC/OW-ISAC" AND (OPA/RIS/SLM/metasurface) AND (NLoS) AND (turbulence/Fresnel/ASM)]
- 2. koşu (algoritma): [AND ("Gerchberg-Saxton" OR IFTA OR adjoint OR manifold OR ADMM OR SPSA ...)]
- Kayıt: Her koşu → 02_Arama/Arama_Log.xlsx

## 5) Çalışma seçimi (tarama)
- Aşama-1: Başlık–özet • Aşama-2: Tam metin
- Karar modeli: [Tek tarayıcı + ikinci doğrulama] / [İki bağımsız tarayıcı]
- Dışlama kodları: N1 Optik dışı/RF, N2 fiber-only, N3 RIS/OPA yok, N4 NLoS yok, N5 metrik yok, N6 malzeme-only, N7 yinelenen, N8 tam metin yok, N9 dil/yıl/tür

## 6) Veri çıkarımı
- Form: 04_Çıkarma/Charting_Form.xlsx • Sözlük: 04_Çıkarma/Codebook.md
- Normalizasyon: MTF(0)=1; SINR dB; EE50 birimi (µrad/pixel)

## 7) Sentez ve analiz
- Yaklaşım: Nitel sentez + taksonomi • Görseller: SINR–MTF Pareto; donanım radar
- Alt grup/duyarlılık: bit derinliği, Cn², OPA/RIS boyutu, sim vs lab

## 8) Kayıt ve değişiklikler
- Protokol kaydı: [OSF (link) / yok]
- Değişiklik günlüğü: 01_Protokol/DEĞİŞİKLİK_GÜNLÜĞÜ.md
