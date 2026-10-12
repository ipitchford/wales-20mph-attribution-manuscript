"""Figure 1: plot the frozen derived quarterly event series (no new analysis).

Input: cases/wales-20mph-casualty-attribution/derived/quarterly_event_series.csv
(SHA-256 192401637ebdeaff83c983472591fd968c12feb8cc184d6aea7161f9b12f077f).
Usage: python make_figure1.py <path-to-csv> <output.pdf>
"""
import csv
import hashlib
import sys

EXPECTED = "192401637ebdeaff83c983472591fd968c12feb8cc184d6aea7161f9b12f077f"
src, out = sys.argv[1], sys.argv[2]
digest = hashlib.sha256(open(src, "rb").read()).hexdigest()
if digest != EXPECTED:
    raise SystemExit(f"input digest {digest} does not match registered {EXPECTED}")

import matplotlib  # imported only after the input digest check

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

rows = list(csv.DictReader(open(src, newline="")))
q = [r["quarter"] for r in rows]
x = list(range(len(q)))


def series(col):
    return [int(r[col]) if r[col] else None for r in rows]


def pts(col):
    ys = series(col)
    return [i for i, y in zip(x, ys) if y is not None], [y for y in ys if y is not None]


plt.rcParams.update({"font.family": "serif", "font.serif": ["Linux Libertine O", "Libertinus Serif", "DejaVu Serif"], "pdf.fonttype": 42, "font.size": 8.5, "axes.spines.top": False,
                     "axes.spines.right": False})
fig, (a, b) = plt.subplots(2, 1, figsize=(6.3, 5.4), sharex=True,
                           gridspec_kw={"height_ratios": [1.25, 1]})
impl = q.index("2023Q3")
for ax in (a, b):
    ax.axvspan(impl - 0.5, impl + 0.5, color="0.88", lw=0)
    ax.axvspan(q.index("2022Q4") - 0.5, q.index("2023Q3") + 0.5, color="0.95", lw=0, zorder=0)
    ax.axvspan(q.index("2023Q4") - 0.5, q.index("2024Q3") + 0.5, color="#e6eef6", lw=0, zorder=0)
    ax.grid(axis="y", color="0.9", lw=0.6)

for col, lab, st in [("svg_provisional_combined", "Provisional WG figure (reconstructed)", dict(color="#1f3a5f", lw=1.6)),
                     ("statswales_combined", "Current StatsWales extract", dict(color="#b5651d", lw=1.1, ls="--")),
                     ("dft_wales_combined", "Current DfT collision rows (summed casualties)", dict(color="#4a7c59", lw=1.1, ls=":"))]:
    xs, ys = pts(col)
    a.plot(xs, ys, label=lab, **st)
a.set_ylabel("Casualties per quarter")
a.set_title("(a) Wales, roads recorded as 20 or 30 mph, three frozen routes", loc="left", fontsize=8.5)
a.legend(frameon=False, fontsize=7.5, loc="upper right")
a.text(impl, a.get_ylim()[0] + 15, "2023 Q3\n(17 Sep)", ha="center", va="bottom", fontsize=7)

for col, lab, st in [("statswales_20", "Recorded 20 mph", dict(color="#7a1f1f", lw=1.3)),
                     ("statswales_30", "Recorded 30 mph", dict(color="0.35", lw=1.3, ls="--"))]:
    xs, ys = pts(col)
    b.plot(xs, ys, label=lab, **st)
b.set_ylabel("Casualties per quarter")
b.set_title("(b) Current StatsWales extract split by recorded speed limit", loc="left", fontsize=8.5)
b.legend(frameon=False, fontsize=7.5, loc="center left")
ticks = [i for i, s in enumerate(q) if s.endswith("Q1")]
b.set_xticks(ticks)
b.set_xticklabels([q[i][:4] for i in ticks], rotation=0)
b.set_xlim(-0.5, len(q) - 0.5)
fig.tight_layout()
fig.savefig(out, metadata={"Creator": "make_figure1.py", "Author": "Anonymous"})
print("wrote", out, "from", digest)
