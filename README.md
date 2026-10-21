# The crash test skill

Most business plans are only ever tested by the person who wrote them. This skill crash tests yours first: seven
Claude crash dummies each hit your idea with a different disaster and report the exact crack they found, then a lead
engineer ranks the cracks and gives you the fix plan that makes it bulletproof. Free, MIT, no signup, no API key.

Made by **Alex Chen** ([@nocodealex](https://instagram.com/nocodealex)), an AI creator who builds free Claude Code skills. Full guide: [chen.media](https://chen.media/guides/crash-test-your-business-idea-with-7-claudes-free-crash-test-skill).

## The crash test

1. **The crash driver** loads your plan into the car: what you sell, who pays, the price, what one sale costs, how
   customers find you, and what you depend on. Every gap gets a guess marked `(assumed)` so you can correct it.
2. **Seven crash dummies, alone.** Nobody sees anybody else's notes. Each one plays one disaster at full strength:
   - **The Recession:** customers cut spending by a third
   - **The Copycat:** a funded rival copies you in 90 days and sells cheaper
   - **The Lawsuit:** a customer, rival or regulator comes after you
   - **Bad Reviews:** your first hundred customers have a bad time, in public
   - **The Price War:** a rival halves its price (it works the margin math)
   - **No Customers:** launch day comes and nobody buys
   - **The Broken Link:** the supplier, platform or person you can't run without disappears

   Each answers SURVIVES, DENTED or TOTALED, quotes the part of your plan that cracked, says what happens next, and
   gives you one cheap test to run this week.
3. **The lead engineer** merges the cracks into one list, worst first (NO MOAT, PRICING, LEGAL, NO CUSTOMERS...),
   writes the fix plan with a pass mark for each test, and rewrites your plan with the fixes in.
4. **Re-test.** Every dummy that did damage crashes the new plan again, and you see before and after. It only says
   BULLETPROOF when every dummy survives.

Everything goes in `.crash-test/` where you run it: `CRASH-REPORT.md` and `PLAN-BULLETPROOF.md`.

## Install

Paste this into Claude Code:

```
https://github.com/alexyc9381/crash-test-skill
Install this skill, then confirm /crash-test works.
```

Or as a plugin:

```
/plugin marketplace add alexyc9381/crash-test-skill
/plugin install crash-test-skill@crash-test-skill
```

Or copy `skills/crash-test` into `~/.claude/skills/`. Open a new Claude Code session afterwards.

## Use

```
/crash-test A $49/month houseplant subscription box for apartment renters who keep killing plants
```

Or point it at a file: `/crash-test my-plan.md`. Works on anything from a side hustle to a full startup. Give it
real numbers (price, cost per sale, savings, hours a week) for the sharpest read. One run is about nine to fifteen
sub-agent calls and counts toward your Claude plan's usage.

## Example run

A real run, unedited apart from shortening, on this idea: *a $49/month houseplant subscription box for US apartment
renters who keep killing plants, plants from two Florida wholesale nurseries, UPS Ground, Instagram ads and plant
influencers, a solo founder with $15,000 and 20 hours a week.* The full files are in
[`examples/houseplant-box/`](examples/houseplant-box/).

**The seven, first crash**

| Dummy | Verdict | The crack it found |
|---|---|---|
| Recession | TOTALED | "$49/month" + cancel anytime: a $49 plant habit gets cut before rent or food |
| Copycat | TOTALED | Nurseries, UPS, ads, influencers: anyone can rent every one of these |
| Lawsuit | DENTED | Packing plants at home and shipping to 48 states may need plant-dealer registration and inspections |
| Bad Reviews | DENTED | Ground shipping year-round, no live-arrival guarantee: frozen plants in winter, cooked in summer |
| Price War | DENTED | Matching a $25 rival leaves +$1.50 to -$10 per box (estimate), before ads |
| No Customers | TOTALED | No proof anyone pays $49, and it sends more plants to people who kill plants |
| Broken Link | DENTED | Both nurseries sit in one weather zone: one hurricane shuts down supply |

**The cracks, worst first:** NO CUSTOMERS (fatal x likely), PRICING / CHURN (fatal x likely), QUALITY / DEAD ON
ARRIVAL, NO MOAT, DEPENDENCY: ONE-REGION SUPPLY, LEGAL: PLANT-SHIPPING RULES.

**The fix plan, first three tests**

1. Real checkout: take a refundable $147 for a 3-month plan, ads only near the nurseries. Pass: 10+ strangers pay in
   7 days at $63 or less of ads per buyer. If this fails, stop.
2. Shipping test: send 6 boxes to the hottest and coldest places you can reach. Pass: all 6 healthy on day 7, each $36
   or less to deliver.
3. Supply and rules: call 3 nurseries, one outside Florida, and email the state plant inspection office. Pass: a backup
   nursery at $12 or less a plant, and compliance under ~$500.

**Re-test on the fixed plan**

Recession TOTALED -> DENTED · Copycat TOTALED -> DENTED · No Customers TOTALED -> DENTED · Lawsuit, Bad Reviews and
Price War stay DENTED · Broken Link DENTED -> **TOTALED**.

> **Not bulletproof.** It went from 3 TOTALED and 4 DENTED to 1 TOTALED and 6 DENTED. The care-text fix moved the
> Broken Link from the nurseries to the founder. Most of what's left can only be closed by running the tests, not by
> more planning: nobody has paid yet.

That last line is the point: it tells you when an idea is not ready, and exactly which test to run next.

## Good to know

- It's a thinking aid made by language models, not a forecast. It can't tell you whether a business will work.
- It can't see your real numbers, market or customers unless you paste them in. Guesses are marked `(assumed)` and
  worked-out numbers `(estimate)`. It never invents market sizes, statistics or competitor names.
- It is not financial, legal or tax advice. The Lawsuit dummy flags risks to check with a professional.
- It is not made by Anthropic.

Run the tests with `python3 -m unittest discover -s tests`.

## Making a video or post about this?

Go ahead. Credit it like this, in your caption or description:

```text
/crash-test skill by Alex Chen (@nocodealex): github.com/alexyc9381/crash-test-skill
```

Tag [@nocodealex](https://instagram.com/nocodealex) so I can see it. Every file the skill writes already ends with
the same credit, so leave it in the shot.

Writing about it or citing it in a paper? Use **Cite this repository** in the sidebar on GitHub.
