
---

# Extraction Codebook — Cascaded OPA→RIS OW-ISAC Review

All entries must be **structured lines** with fixed fields, units, and an **evidence anchor** (page/figure/section). Leave blanks as “Not specified” if absent.

---

### 1. OWC Cascaded Topology & Hardware Profile

**Instruction:** Extract the cascaded optical architecture and hardware profile in one line.
**Format:**

```
Topology=<OPA->RIS | OPA<->RIS | multi-hop | hybrid>; 
OPA=<tech, phase_bits, ±scan_deg, HPBW_deg, rate_kHz, channels>; 
RIS=<class, pixels, phase_bits, switch_time, efficiency%, aperture_cm2>; 
ISAC=<mode>; 
(Anchor)
```

**Example:**
`Topology=OPA->RIS; OPA=SiPh, 6-bit, ±60 deg, HPBW=0.8 deg, 1.2 kHz, 512 ch; RIS=LCoS, 16000 px, 8-bit, 3 ms, 42%, 25 cm^2; ISAC=OFDM waveform-reuse (p.7, Fig.3)`

---

### 2. Technical Challenges Identified

**Instruction:** Record explicit or strongly implied technical challenges. Use controlled categories.
**Categories:** alignment/calibration; phase retrieval/channel estimation; turbulence/scintillation; NLoS multipath/blockage; grating lobes/aliasing; hardware limits; computational cost/latency/memory; dataset/ground-truth.
**Format:**

```
Challenge=<category>: <description> 
(Context=<λ, z, LoS/NLoS, r0/Cn^2/σR^2, HW>) 
(Impact=<metric shift with units>) 
(Mitigation=<method or NA>) 
(Anchor)
```

**Example:**
`Challenge=Turbulence: r0 reduction 12→6 cm increases scintillation, BER +2e−3 @15 dB SNR (Context=λ=1550 nm, 1 km NLoS; Cn^2≈1e−14) (Mitigation=robust pre-shaping E−αVar) (Sec.4.2)`

---

### 3. Signal Processing & Targeting Capabilities

**Instruction:** Summarize dynamic targeting and signal processing.
**Format:**

```
Capability=<module>: <OPA range ±deg, rate_kHz, accuracy, RIS switch_time, constraints, algorithms, ISAC coupling, improvements> 
(Context=<λ, z, LoS/NLoS, r0/Cn^2 if relevant>) 
(Anchor)
```

**Example:**
`Capability=Targeting: OPA ±50 deg @1.5 kHz, accuracy 0.3 deg; RIS=2.8 ms; Algorithms=GS + RIS-coded PR; ISAC=reuse-OFDM (p.6, Fig.4)`

---

### 4. Metrics & Evaluation

**Instruction:** Extract primary comm/sensing metrics with absolute values and improvements vs baseline.
**Format:**

```
Metric=<name>: <value units> 
(Context=<λ, z, LoS/NLoS, r0/Cn^2, setup>) 
(Improvement=<%/dB vs baseline>) 
(Anchor)
```

**Example:**
`Metric=Data rate: 3.2 Gbps (Context=λ=1550 nm, indoor LoS) (Improvement=+23% vs prior design) (Fig.5)`

---

### 5. Solutions / Innovations

**Instruction:** Record novel solutions tied to challenges, with mechanism + metric gain.
**Format:**

```
Innovation=<type>: <mechanism> 
(Benefit=<metric change with units or expected effect>) 
(Anchor)
```

**Example:**
`Innovation=BN-RIS placement: Poisson-disk sampling (Benefit=PSL −7 dB) (Sec.4.2)`

---

### 6. Wavelength / Band (λ)

**Format:**
`λ=<value(s) with units> (Anchor)`
**Example:** `λ=1550 nm (p.3)`

---

### 7. Range & Environment

**Format:**
`z=<distance with units>, Environment=<indoor/outdoor+scene>, Path=<LoS/NLoS> (Anchor)`
**Example:** `z=500 m, Environment=outdoor urban, Path=NLoS (Sec.2.1)`

---

### 8. Channel Impairment Focus

**Format:**
`Impairment=<type+mechanism> (Scope=<qual/quant>) (Anchor)`
**Example:** `Impairment=NLoS (single-bounce specular) (Scope=quantitative) (Fig.2)`

---

### 9. Turbulence Parameters

**Format:**
`r0=<value>; Cn^2=<value>; σR^2=<value>; Model=<name>; z=<distance> (Anchor)`
**Example:** `r0=8–12 cm; Cn^2=1e−14–1e−15 m−2/3; Model=Kolmogorov; z=1 km (p.5)`

---

### 10. Phase Retrieval / Channel Estimation

**Format:**
`PR/CE=<family>; M=<#>; Init=<type>; Iters=<# or NA> (Anchor)`
**Example:** `PR/CE=RIS-coded GS; M=8; Init=spectral; Iters=200 (Sec.4.3)`

---

### 11. Beam Quality Metrics

**Format:**
`PSL=<dB>; ISLR=<dB>; HPBW=<deg>; contrast=<value> (Context=<ROI, sim/testbed>) (Anchor)`
**Example:** `PSL=−13.2 dB; HPBW=0.9 deg (Context=simulated far field) (Fig.4)`

---

### 12. ISAC Coupling & Metrics

**Format:**
`Coupling=<mode>; Metrics=<rate; res; ROC; CRB> (Anchor)`
**Example:** `Coupling=reuse-OFDM; Metrics=3.2 Gbps; range 7.5 cm; ROC PD=0.92@PFA=1e−3 (Sec.5)`

---

### 13. Hardware Maturity & Safety/Power

**Format:**
`Maturity=<sim/prototype/field/product>; Safety=<IEC class or NA>; Power=<value or NA> (Anchor)`
**Example:** `Maturity=prototype (lab); Safety=IEC 60825-1M; Power=350 mW (p.2)`

---

### 14. Evaluation Setup Notes

**Format:**
`Tx=<source>; Rx=<detector>; Optics=<aperture/lens>; Waveform=<scheme>; Setup=<sim/testbed>; Dataset=<name or NA> (Anchor)`
**Example:** `Tx=1550 nm DFB; Rx=APD; Optics=25 mm aperture; Waveform=OFDM; Setup=testbed indoor; Dataset=NA (p.10)`

---

### 15. Risk of Bias & Normalization Notes

**Format:**
`ROB=<low/some/high>; Normalization_notes=<any rescaling or assumptions>`

---

This codebook guarantees:

* **Consistency** (structured lines → machine parseable).
* **Transparency** (anchors for every claim).
* **Coverage** (physics, systems, hardware, metrics, ISAC).

---

