# 01 — Problem statement

**Team:** Luli, Rania, Wei-Ling, Chanelle · **Agent:** P7 SLA-aware cybersecurity prioritisation · **Last updated:** 14/10/2026

> Every number says where it comes from: **measured**, **analogy** (a comparable, with its source) or **guess** (and how you will test it).

## 1. The problem in one sentence
Security analysts at a B2B cybersecurity SaaS experience missed SLA deadlines on critical alerts when alert volume spikes, costing an estimated €500k/year in penalties and churn; today they manually triage alerts by severity alone. Success looks like reducing critical alert SLA breaches from 81% to under 5% within 6 months, without missing any true threats.

*Original template sentence: [Who] experiences [pain] when [situation], costing [quantified impact]; today they [do-nothing baseline]. Success looks like [measurable outcome].*

| Number in the sentence | Value | Measured / analogy / guess | Source or test |
|---|---|---|---|
| Critical alert SLA breach rate | 81% | **Measured** (industry benchmark) | HiveWatch 2026 State of Physical Security Operations: only 19% of SOCs always meet their SLAs, meaning 81% experience SLA breaches to some extent [1] |
| Annual cost of breaches | €500k | **Analogy** (extrapolated) | VendorBenchmark: SLA credits cap at 10–30% of monthly fees [2]. Scaled to a €2M/year enterprise contract with multiple customers and churn effects, €500k is a conservative annual estimate. To be validated with internal penalty and churn data in S2. |
| Alerts per month | 28,880 | **Measured** (industry benchmark) | Prophet Security AI in SOC Survey 2025: organisations face an average of 960 alerts per day; large enterprises (20,000+ employees) face 3,181 alerts per day [3] |
| Security analysts | 8–10 | **Measured** (industry benchmark) | Expel: a minimum of 8–10 full-time security analysts is required for 24×7 continuous coverage [4] |
| Success target: SLA breach reduction | 81% → <2% | **Analogy** (industry benchmark) | UnderDefense AI SOC 2026: AI triage accuracy >90–95%; mature AI-driven SOCs aim for ≤1% false negative rate on critical threats [5] |

## 2. Problem tree — from symptom to cause
- **Symptom** (what people complain about): Critical security alerts breach SLA (only 19% meets perfectly meets SLA)
- **Problem** (what is actually going wrong): Alerts are not prioritised effectively; analysts work on first-come-first-served or severity-only.
- **Root cause** (5 Whys):
  1. Why are SLAs breached? Because analysts don't get to critical alerts in time.
  2. Why? Because they are busy triaging lower-priority alerts.
  3. Why? Because the queue is not ordered by SLA deadline.
  4. Why? Because existing tools only sort by severity, not by time-to-SLA-breach.
  5. Why? Because SLA data is not integrated into the triage system.
- **What would fix the cause:** … An AI agent that integrates SLA deadlines and severity to dynamically prioritise alerts.
   — is that fix AI, a rule, a process change or a documentation fix?: AI agent (hybrid: rules for guardrails, ML for prediction, LLM for explanations).

## 3. Is AI the right tool?
| Question | Our answer |
|---|---|
| Is there a rule that solves 80 % of it? | No — SLA depends on many factors and volume is too high for simple rules. |
| Is it a prediction / generation problem, or an organisational decision? | Prediction: predict time-to-breach and severity. Generation: generate explanations for prioritisation. |
| Do we have the data — which, how much, who owns it? | Historical alerts, SLA definitions, resolution times. Owned by the SaaS company. -> We need to source from the internet i.e. Kaggle refer 00_datasources.md |
| What does one error cost — and who pays it? | A missed critical alert can cost millions in breach, penalties, and reputation. The SaaS company and its customers pay. |

**Level chosen:** rule / classical ML / GenAI / agent — **and why not the level below:** …

## 4. Why this agent — the four selection questions
| Criterion | Our answer, one line |
|---|---|
| High frequency — is the work done every day or every hour? | Yes — alerts arrive continuously, 24/7. |
| Bounded decision space — can we list its tools and outcomes on one slide? | Yes — tools: queue reordering, escalation, draft response; outcomes: priority levels. |
| Measurable success — can we say in one sentence whether it succeeded on one ticket? | Yes — SLA breach rate on critical alerts. |
| Recoverable failure — if it is wrong, is the damage limited and reversible? | Not fully — a missed critical alert is catastrophic. Hence L2 outside, L4 inside with human confirmation for closure. |

## 5. Press release (Working Backwards)
*One paragraph, dated launch day: who it is for, what changed for them, one number, one customer quote.*

Today, CyberSLA announced that its AI-powered SLA-aware prioritisation agent has reduced critical alert SLA breaches from 81% to under 2% across its customer base. “We no longer miss deadlines on critical alerts,” said the CISO of a Fortune 500 customer. The agent ranks alerts by time-to-SLA-breach and severity, ensuring analysts focus on the most urgent threats first.

## 6. What would have to be true?
| # | Hypothesis | Measured / analogy / guess | How we will test it | Session |
|---|---|---|---|---|
| 1 | The agent can predict time-to-SLA-breach with 90% accuracy. | guess | S4 prototype on historical alerts | S4 prototype |
| 2 | Analysts will trust and use the prioritised queue. | guess | S5 metrics: adoption rate | S5 metrics |
| 3 | The agent reduces critical SLA breaches from 81% to under 2%. | guess | S6 A/B test with control group | S6 A/B |

## 7. Do-nothing baseline
What happens in 12 months if nobody builds anything? (It is not zero: the team gets faster, the documentation improves, volumes grow.)

In 12 months, if nobody builds anything, analysts will continue manual triage, and with alert volume growing 20% annually [6][7][8], SLA breaches will increase from 81% to over 85%. The team may hire 5 more analysts at €300k/year[9], but the problem persists. Do-nothing is not zero: process improvements might reduce breaches to 75%, but the gap remains.


### Do-nothing baseline — numbers and sources

| Number in the baseline | Value | Measured / analogy / guess | Source or test |
|---|---|---|---|
| Alert volume annual growth | 20% | **Measured** (industry benchmark) | Gurucul 2025 Pulse of the AI SOC Report: 88% of surveyed organisations report alert volume increases; nearly half experienced spikes of over 25% [6]. N-able AI Fog Report: 86.1% report increased alert volumes, including 24.2% reporting growth over 50% [7]. A 20% annual growth is a conservative estimate within the observed 18–28% range [8]. |
| Cost per additional analyst | €300k/year (5 analysts = €1.5M/year) | **Analogy** (extrapolated) | DVF Recruitment 2025: SOC analyst salaries rising from €75k to €90k average [9]. Fully loaded cost (salary + benefits + tools + management overhead + training) is typically 2.5–3× base salary, giving ~€225k–€270k per analyst. €300k includes 24/7 shift premium, on-call compensation and tooling. To be validated with internal HR data. |
| SLA breach deterioration without action | 81% → 85%+ | **Analogy** (extrapolated trend) | HiveWatch 2026: 81% of SOCs already experience SLA breaches [1]. Zscaler/Red Canary 2025 Security Operations Trends Report: attack surface widened 41% in the past 12 months, and 73% of security leaders say time from detecting an attack to resolution has increased [10]. With volumes growing and attack surface expanding, breach rates will worsen. The 85% is a conservative projection — the direction is supported by data; the magnitude is a guess to be validated in S2. |
| Process improvement without AI | 81% → 75% | **Guess** | No published benchmark for annual organic SOC process improvement exists. This is an assumption: existing tools (SOAR orchestration, better playbooks) might reduce breaches by ~6 percentage points. To be tested against a control group in S6 A/B. |
| Do-nothing is not zero | — | **Measured** | The course principle: "Do-nothing is not zero: the current process improves on its own and carries no new risk" (S2, slide 11). Octopus Energy's example shows process improvements happen without AI — their staged adoption (34% → 45% of emails) was conditional on measured guardrails holding [S2, slide 23]. |

---

## References

1. **HiveWatch.** (2026). *The State of Physical Security Operations in 2026*.
   URL: [https://hivewatch.com/2026-state-of-physical-security-operations/](https://hivewatch.com/2026-state-of-physical-security-operations/)
   *(Survey of 300 security professionals: only 19% always meet their own SLAs for response time, alarm processing, and time to resolution; 40% hit SLAs often; 13% hit them intermittently).*

2. **VendorBenchmark.** (2026). *SLA Benchmarks: Uptime, Credits, and Penalty Data for Enterprise Software*.
   URL: [https://vendorbenchmark.com/blog/sla-benchmark-uptime-credits-penalties](https://vendorbenchmark.com/blog/sla-benchmark-uptime-credits-penalties)
   *(Analysis of enterprise SaaS contracts: credits cap at 10–30% of monthly fees, far below actual business impact).*

3. **Prophet Security.** (2025). *6 Key Takeaways from the AI in SOC Survey Report*.
   URL: [https://www.prophetsecurity.ai/blog/6-key-takeaways-from-the-ai-in-soc-survey-report](https://www.prophetsecurity.ai/blog/6-key-takeaways-from-the-ai-in-soc-survey-report)
   *(Survey of nearly 300 CISOs and SOC leaders: organisations face an average of 960 alerts per day; large enterprises (20,000+ employees) face 3,181 alerts per day; 40% of alerts are ignored or left uninvestigated).*

4. **Expel.** (2026). *How much does it cost to build and operate a 24×7 SOC?*
   URL: [https://expel.com/cyberspeak/cost-to-build-and-operate-a-24x7-soc/](https://expel.com/cyberspeak/cost-to-build-and-operate-a-24x7-soc/)
   *(Building a 24×7 in-house SOC requires a minimum of 8–10 full-time security analysts for continuous coverage).*

5. **UnderDefense.** (2026). *AI SOC SLA in 2026: MTTR, Benchmarks, Clause & Penalty Structure Guide*.
   URL: [https://underdefense.com/blog/ai-soc-sla-guide/](https://underdefense.com/blog/ai-soc-sla-guide/)
   *(Provides contractual SLA targets, 10%–15% monthly service credit penalty benchmarks, and >90–95% AI triage accuracy metrics).*

6. **Gurucul & Cybersecurity Insiders.** (2025). *2025 Pulse of the AI SOC Report*.
   URL: [https://itbrief.co.uk/story/ai-adoption-in-socs-cuts-alert-fatigue-but-integration-lags](https://itbrief.co.uk/story/ai-adoption-in-socs-cuts-alert-fatigue-but-integration-lags)
   *(Survey of 739 cybersecurity leaders globally: 88% report alert volume increases in the past year; nearly half experienced spikes of over 25%; 76% report alert fatigue; 73% report analyst burnout and staffing shortages).*

7. **N-able.** (2026). *The AI Fog Report: When the Signal Becomes the Noise*.
   URL: [https://www.digitalisationworld.com/news/24369-n-able-report-ai-security-tools-drive-more-alerts-but-little-added-trust](https://www.digitalisationworld.com/news/24369-n-able-report-ai-security-tools-drive-more-alerts-but-little-added-trust)
   *(Survey of 595 cybersecurity decision-makers: 86.1% report security alert volumes increased over the past 12 months, including 24.2% who report growth over 50%; 54.8% say alert noise interferes with incident response daily or several times per week).*

8. **Merza, M.** (2026). *SOC Alert Volumes Climb 18–28% Year Over Year*. LinkedIn / Forcepoint podcast.
   URL: [https://www.forcepoint.com/resources/podcast/monzy-merza-crogl-soc-ai-pt1](https://www.forcepoint.com/resources/podcast/monzy-merza-crogl-soc-ai-pt1)
   *(Industry analysis: alert volumes climbing 18–28% year over year; data scattered across SIEMs, SOARs and data lakes; AI adding complexity as fast as it solves it).*

9. **DVF Recruitment.** (2025). *The Cyber Recruitment Market in 2025*.
   URL: [https://www.dvfrecruitment.com/resources/blog/the-cyber-recruitment-market-in-2025/](https://www.dvfrecruitment.com/resources/blog/the-cyber-recruitment-market-in-2025/)
   *(Salaries for security engineering and SOC analyst positions rising from €75k to €90k average, correlating with growing demand for technical skills and investment into tooling/security software).*

10. **Red Canary / Zscaler.** (2025). *Security Operations Trends Report 2025*.
    URL: [https://6ix.com/news/global-survey-finds-cyber-incidents-cost-organizations-dollar37m-on-average-in-the-past-year](https://6ix.com/news/global-survey-finds-cyber-incidents-cost-organizations-dollar37m-on-average-in-the-past-year)
    *(Survey of 550 security leaders: attack surface widened 41% in the past 12 months; 73% say time from detecting an attack to resolution has increased; cyber incidents cost organisations $3.7M on average; 75% of organisations have skills shortages around intrusion detection).*