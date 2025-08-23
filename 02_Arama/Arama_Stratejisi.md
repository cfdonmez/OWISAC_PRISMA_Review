# Arama Stratejisi (PRISMA-S uyumlu)

## Ortak filtreler
- Yıllar: 2005–2025
- Dil: English
- Belge türü: Article, Proceedings/Conference, Review
- Kapsam dışı: fiber/fibre-only (NOT filtresi)

---

## IEEE Xplore — Advanced Search (All Metadata)
(("optical integrated sensing and communication" OR "optical ISAC" OR OW-ISAC)
 AND ("reconfigurable intelligent surface" OR RIS OR metasurface OR "programmable metasurface"
      OR "spatial light modulator" OR SLM OR "optical phased array" OR OPA)
 AND ("non-line-of-sight" OR NLoS OR "beyond line of sight")
 AND (turbulence OR Kolmogorov OR Rytov OR scintillation OR Fresnel OR "angular spectrum"))
 NOT (fiber OR fibre)

---

## Optica Publishing (OSA)
(("optical integrated sensing and communication" OR "optical ISAC" OR OW-ISAC)
 AND ("reconfigurable optical surface" OR "optical RIS" OR metasurface OR "spatial light modulator" OR SLM
      OR "optical phased array" OR OPA)
 AND (NLoS OR "non-line-of-sight")
 AND (turbulence OR Kolmogorov OR Rytov OR scintillation OR Fresnel OR "angular spectrum"))
 NOT fiber

---

## ScienceDirect — TITLE-ABSTR-KEY
TITLE-ABSTR-KEY(
 ("optical integrated sensing and communication" OR "optical ISAC" OR OW-ISAC)
 AND ("reconfigurable intelligent surface" OR RIS OR metasurface OR "spatial light modulator" OR SLM
      OR "optical phased array" OR OPA)
 AND ("non-line-of-sight" OR NLoS)
 AND (turbulence OR Kolmogorov OR Rytov OR scintillation OR Fresnel OR "angular spectrum")
)
 AND NOT TITLE-ABSTR-KEY(fiber OR fibre)

---

## arXiv — Advanced
(all:"optical integrated sensing and communication" OR all:"optical ISAC" OR all:OW-ISAC)
 AND (all:"reconfigurable intelligent surface" OR all:RIS OR all:metasurface OR all:"optical RIS"
      OR all:"spatial light modulator" OR all:SLM OR all:"optical phased array" OR all:OPA)
 AND (all:NLoS OR all:"non-line-of-sight")
 AND (all:turbulence OR all:Kolmogorov OR all:Rytov OR all:scintillation OR all:Fresnel OR all:"angular spectrum")
 NOT (all:fiber OR all:fibre)

Kategoriler: physics.optics, eess.SP (ops: cs.IT).

---

## 2. Koşu — Algoritma bloğu
("Gerchberg-Saxton" OR IFTA OR "phase retrieval" OR adjoint OR Wirtinger OR "manifold" OR "projected gradient"
 OR ADMM OR SPSA OR "zero-order")

Bu blok, yukarıdaki çekirdek dizgeler ile **AND** edilerek algoritma-odaklı alt küme çıkarılır.
