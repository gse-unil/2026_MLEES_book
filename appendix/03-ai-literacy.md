# AI Literacy for Scientific Programming

AI chatbots are a powerful tool, not an oracle: excellent at producing plausible code fast, and unable to know whether that code is *right* for your data, your units, or your question. This page is a living guide — expect it to change faster than the rest of the book as models and norms evolve — built around three habits: being a precise communicator, a skeptical reviewer, and an active learner.

:::{admonition} Learning objectives
:class: tip
- Write prompts that state the goal, the environment, the data, and the task.
- Verify generated code before trusting it: understand it, test it small, question the approach.
- Use an assistant to build understanding, not just to produce code.
- Recognise a silent, unit-related bug as the archetypal failure mode of generated scientific code.
:::

## Be a precise communicator

Garbage in, garbage out. A prompt that gets a useful answer on the first try usually states four things:

1. **The goal** — the high-level scientific objective, not just the mechanical step.
2. **The environment** — language and libraries (`python`, `pandas`, `numpy`, ...).
3. **The data** — its actual structure; paste a `.head()` or `print()` output rather than describing it from memory.
4. **The task** — the precise action wanted.

Compare two prompts for the same task: averaging a temperature record by month.

A bad prompt:

> How do I average my data by month in python?

Without a description of the data, the assistant reaches for a generic example — a three-row toy table that happens to already have monthly, not daily, dates — and returns code that runs but has nothing to do with the actual station data.

A good prompt:

> I am using python with the pandas library to analyze weather station data. I have a DataFrame `df_temp` with a `DatetimeIndex` and a column `air_temp_celsius`. Here is `df_temp.head()`:
> ```
>                       air_temp_celsius
> 2024-07-01 00:00:00              15.2
> 2024-07-01 01:00:00              14.9
> ```
> Please give me code to compute the mean monthly air temperature, stored in a new DataFrame `monthly_mean_temp`.

Pinning the actual column names and structure gets `df_temp.resample("ME").mean()` — the right tool, applied to the right data — on the first try.

## Be a skeptical reviewer

Never trust, always verify. Generated code runs and looks reasonable far more often than it is actually correct — the failures that matter in science are silent, not crashes. Three checks catch most of them:

1. **Understand.** Can you explain what every line does? If not, ask for a line-by-line explanation before running it.
2. **Test.** Run it on a small, known subset first, and check one value by hand.
3. **Question.** Is this the best approach, or just *an* approach? Ask for alternatives and trade-offs.

A first request — "plot a 30-day rolling average of temperature" — gets a working but bare plot. Two follow-ups sharpen it without starting over. First:

> This code works, but the plot is not very readable. How would you modify it so it's more readable?

adds axis labels, a legend, and the raw data as context. Then:

> For climatological analysis, a centered mean is usually more appropriate. How would you modify this to use a centered 30-day window?

is the kind of correction only a reviewer who understands the *domain*, not just the syntax, would think to ask for — `rolling(window=30, center=True)` in place of the assistant's default trailing window.

## Be an active learner

Use it to build understanding, not just to produce code. Three prompt patterns are worth having ready:

- **Explain this error** — paste the full traceback and ask what it means and why, not just for a fix.
- **Compare these methods** — "what's the difference between a `for` loop and a `while` loop, and when would I use one over the other?" turns a syntax question into an understanding one.
- **Suggest a structure** — before writing a script that loads 50 files and merges them, ask for a clean approach first; you will read and adapt it faster than debugging one written top-down.

## A concrete failure: the unstated unit

Asked to flag freezing conditions, an assistant might write:

```python
def is_freezing(temperature):     # unit unspecified: the latent bug
    return temperature < 0
```

Called on a station that reports temperature in kelvin, this is wrong for every real value: `is_freezing(268.15)` — a genuine −5 °C — returns `False`, because nothing is ever below zero kelvin. The code is not wrong in isolation; it is wrong because the prompt never fixed the unit, so the assistant guessed celsius. The fix states the unit everywhere it can — the name, the type hint, the threshold:

```python
def is_freezing_kelvin(temp_kelvin: float) -> bool:
    return temp_kelvin < 273.15
```

:::{admonition} You own the code you did not write
:class: important
Generated code is a draft, and you are accountable for what it does. Two habits make that safe: state every constraint the code needs to respect — units, valid ranges, dtypes, edge cases — directly in the prompt, and never run a line you have not read and understood.
:::

## This page will change

Models, tools, and institutional norms around AI assistance are all moving faster than the rest of this book. Treat the three habits above — precise, skeptical, active — as the stable part; the specific tools and examples will be revisited as they change.
