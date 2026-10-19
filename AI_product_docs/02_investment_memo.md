# 02 — Investment memo (one page) · CyberSLA, SLA-aware alert prioritisation

**Recommendation: NO-GO on the build as sized with our 01 numbers (10 analysts) — CONDITIONAL GO only if (1) the real team is ≥ 20 analysts (cost per alert ≥ €16, the flip point) and (2) the S4 prototype measures ≥ 45 % triage time saved on noise alerts with critical-alert recall ≥ 99 % on 200 alerts. Ship the SLA-timer rule first.**

> Line one is the decision. Everything below is evidence for that line. Same base case as `02_sizing.xlsx`.

| €/year, year 1 | Pessimistic | Base | Optimistic | Expected value |
|---|---|---|---|---|
| Net annual value | −524k | −79k | +709k | **−55k** |
| Probability | 0.30 | 0.50 | 0.20 | — |
| Do-nothing (value of the current process improving on its own) | 43k | 138k | 207k | 138k (base) |
| Next-best project: SLA-timer rule in the SOAR, no AI (the hurdle) | 100k | 100k | 100k | 100k |

## 1. How much?
Company (01, benchmarks): 500 enterprise customers, **28,800 alerts/month** (960/day, Prophet Security 2025), **10 analysts** for 24×7 (Expel 2026) at **€270k** fully loaded → **€8 of analyst time per alert**. The agent is a **copilot**: it ranks every alert by time-to-SLA-breach × severity and explains why (L4 internal); the analyst decides. Base-case value: triage time saved on **noise alerts** (60 % of volume) **€248k**, on **investigations** (35 %) **€57k**, **SLA penalties & churn avoided** on critical alerts **€83k** (35 % of the €500k breach cost in 01, year-1 ramp) → €388k; minus wrong rankings **€118k** and the **tail-risk line €15k** → **€254k**; minus fixed costs **€333k** = **−€79k**. Measured (benchmarks): volume, team size, breach rate. Analogies: cost per alert, €500k breach cost. **The one guess that matters: the share of triage time saved (45 % base on noise).**

## 2. How sure?
Not at all: EV **−€55k**, spread **−€524k to +€709k**. Two flip points:
- **Team size (the big one).** At €8/alert even 75 % time saved stays below do-nothing (sensitivity table). The decision flips at **≈ €16/alert ≈ 20 analysts**: EV **+€286k**, CONDITIONAL GO. With the README's **40 analysts** (€31/alert) EV is **+€926k**. 01 says 8–10, README says 40 — **we must agree on one number before S3.**
- **Time saved**, measured by the S4 prototype: 200 alerts from the Kaggle incident logs (00_datasource_links.md), triaged with vs without the ranked queue, plus critical-alert recall. A 50 % saving with one missed critical alert is still a NO-GO.

## 3. What if we're wrong?
The dominant costs are **not the model** (inference ≈ €17k/yr on all alerts): **supervision €150k** (a detection engineer owns the ranking rules), **integration €50k/yr** (SIEM/SOAR + SLA contracts + private inference — logs cannot leave our perimeter), **evaluation €50k**, monitoring €55k. **The governance line** (governance.md, Session 2): an under-prioritised critical alert is a missed contractual SLA *and* a customer exposed during an attack — the average incident costs $3.7M (Red Canary/Zscaler 2025). We price it as a mean (row 68: 1 % × €1.5M = −€15k) but it is a heavy tail, so **critical alerts are excluded from AI ranking** in every scenario, and the agent may **raise** a priority but **never lower** it. Owner: the customer's CISO (operational risk) and our product owner (technical/reputational risk). Rollback: critical recall < 99 % on the weekly replay → queue back to severity-only that day.

## 4. Compared to what?
Do-nothing is worth **€138k/yr** (01: SOAR playbooks bring breaches from 81 % to ~75 % without AI). The next-best project is an **SLA-timer rule**: sort the queue by time-to-breach and auto-escalate at 50 % of the SLA — it fixes 01's root cause #5 (*SLA data not integrated into triage*) with no model risk, ≈ €100k/yr. EV (−€55k) beats neither, and **the pessimistic case does not clear the hurdle**. Our ask: ship the timer rule this quarter, fund only the S4 prototype, re-size with the real headcount and measured time saved.

## 5. Build, buy or orchestrate?
**We orchestrate** — open-weights model in our EU VPC + our SOAR + customers' SLA contracts — because alerts and logs cannot go to a third-party API. Weighted scores (`Build or buy` tab): **Build 3.45 · Buy 2.30 · Orchestrate 4.10**. On price alone buying is cheaper at our volume (≈ €19k fees vs ≈ €130k to run it), so **we would change our mind if an AI-SOC vendor offers in-VPC deployment, no training on our data, and exportable logs and eval-sets.**

*Sources: team 01_problem_statement.md and its references (HiveWatch 2026, Prophet Security 2025, Expel 2026, DVF Recruitment 2025, Gurucul 2025, N-able 2026, Red Canary/Zscaler 2025) · Session 2 slides, 14 Oct 2026 (retry overhead, do-nothing 3–5 %/yr, staged ramp) · 02_sizing template "How to fill it" (P7 = time saved + penalties avoided). Every "guess" in the sheet says in column G how we will check it.*
