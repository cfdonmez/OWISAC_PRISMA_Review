# PRISMA 2020 Flow — Diagram

```mermaid
flowchart TD
  A[Records identified<br/>(databases & registers)<br/>n=128]:::box
  R[Records removed before screening<br/>duplicates: 0<br/>automated: 0<br/>other: 0]:::box
  S[Records screened (title/abstract)<br/>n=1]:::box
  X[Records excluded (title/abstract)<br/>n=1]:::box
  E[Reports assessed for eligibility (full-text)<br/>n=3]:::box
  F[Reports excluded (full-text, with reasons)<br/>n=2]:::box
  I[Studies included in review<br/>total: 1<br/>qual: 1 | quant: 0]:::box

  A --> R --> S -->|screened| E --> I
  S --> X
  E --> F


  classDef box fill:#f9f9f9,stroke:#999,stroke-width:1px,color:#000;
```

## Full-text exclusion reasons
    - out_of_scope: **1**
    - reason_unclassified: **1**