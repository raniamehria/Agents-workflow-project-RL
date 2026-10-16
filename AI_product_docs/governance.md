# Governance — our living file

> Created for Assignment 1, one line added every session. One question at the oral is drawn from this file.
> Answers are provisional: write what you know today, and mark what you still have to check.

## Session 1 — the six questions
| # | Question | Our answer (provisional) | To check with |
|---|---|---|---|
| 1 | **EU AI Act:** which risk tier is our agent in, and why? (minimal · limited — transparency: tell the user it is an AI · high-risk · prohibited) | **Limited risk — transparency.** The agent is a support/triage tool for a B2B cybersecurity SaaS. It does not decide access to essential services, but it interacts with users and must disclose it is an AI. If it ever autonomously blocks or degrades a security control, it could become high-risk; we must keep that out of scope. | Legal / DPO |
| 2 | **Data:** whose data does it use, and on what legal basis? (GDPR art. 6; what the B2B contract allows) | **Data:** The agent processes support ticket content (e.g., error logs, user descriptions) and telemetry from the cybersecurity SaaS. This may include personal data of the SaaS customer's employees. **Legal Basis:** Primarily Contract Performance (GDPR Art. 6(1)(b)) — processing is necessary to provide the SaaS service, including support. Legitimate Interest (Art. 6(1)(f)) may also apply for security monitoring and product improvement. | DPO / Legal |
| 3 | **Accountability:** who is accountable when it is wrong — and where is the human? | **Accountable owner:** the customer’s CISO / Head of Security. **Human in the loop:** L2 outside — human analyst approves all AI-drafted customer responses; L4 inside — AI may reorder internal triage queue by SLA risk, but a human must confirm severity and closure. | Head of Support / CISO |
| 4 | **Never:** what must it never do? (our first guardrail) | Never autonomously close a security incident, mark an alert as a false positive, or deprioritise an alert whose SLA deadline is within 4 hours without human confirmation. In security, a false negative can be catastrophic. | Security Team |
| 5 | **Explainability:** explainable to whom — the customer, the support agent, the auditor? | **To the security analyst:** evidence-based reason for prioritisation (e.g., “P1 because asset=production, CVSS=9.8, SLA deadline in 2h”). **To the auditor:** full trace of data seen, rule triggered, confidence score. **To the customer:** plain-language explanation that an AI assisted and a human approved. | Engineering / Security |
| 6 | **The people it cannot serve:** what happens to them? | One-click escalation to a human that preserves all context. If the agent cannot diagnose an alert, it must fail secure: escalate immediately to a human analyst. Track “could not reach a person” as a counter-metric. | Support Operations |

## Session 2 — the cost of error
- Which cost-of-error line is a **legal or reputational** risk, not just money? …
	**The legal/reputational risk is a missed SLA on a critical security incident.** In cybersecurity SaaS, an SLA (Service Level Agreement) is a contractual commitment, e.g., “create a Security Incident Case within 3 hours for Critical alerts.” An SLA-aware prioritisation agent ranks alerts by time-to-SLA-breach, not just severity. Example: Palo Alto Cortex assigns remediation deadlines (Critical = 7 days, High = 14 days); Forescout commits to 3-hour case creation for Critical. If the AI misses or deprioritises such an alert — a “rare but catastrophic miss” — the result can be a breach, service credits, regulatory penalties, and lost trust. This is the tail risk that must be priced.
- Who in the company **owns** that risk? …
	 **The customer’s CISO / Head of Security owns the operational risk; our product owner owns the technical/reputational risk.** The investment memo must include a tail-risk line: probability of a catastrophic miss × cost of breach/penalty/reputational damage. The agent’s guardrails and L2/L4 design are the mitigation.

## Session 3 — data (to come)
## Session 4 — human-in-the-loop points and the override switch (to come)
## Session 5 — counter-metrics and the segments we report (to come)
## Session 6 — protected segments and the harm threshold that stops an experiment (to come)
## Session 7 — accountable owner, rollback authority, incident path (to come)
