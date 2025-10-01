# PRISMA 2020 Flow — Diagram

```mermaid
flowchart TD
  A[Records identified (databases and registers): n=128]:::box
  R[Records removed before screening: duplicates 0, automated 0, other 0]:::box
  S[Records screened (title/abstract): n=1]:::box
  X[Records excluded (title/abstract): n=1]:::box
  E[Reports assessed for eligibility (full-text): n=3]:::box
  F[Reports excluded (full-text, with reasons): n=2]:::box
  I[Studies included in review: total 1; qual 1; quant 0]:::box

  A --> R --> S -->|screened| E --> I
  S --> X
  E --> F

  classDef box fill:#f9f9f9,stroke:#999,stroke-width:1px,color:#000;
```

## Full-text exclusion reasons
    - out_of_scope: **1**
    - reason_unclassified: **1**