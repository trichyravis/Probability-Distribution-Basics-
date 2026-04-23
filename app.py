"""
===============================================================================
THE MOUNTAIN PATH - WORLD OF FINANCE
Probability & Distributions Interactive Learner App
Prof. V. Ravichandran  |  themountainpathacademy.com
===============================================================================

Run:   streamlit run mountain_path_prob_app.py
Deps:  pip install streamlit numpy pandas scipy plotly
"""

import math
import numpy as np
import pandas as pd
import streamlit as st
from scipy import stats
import plotly.graph_objects as go

# ============================================================================
# PAGE CONFIG
# ============================================================================
st.set_page_config(
    page_title="Mountain Path - Probability & Distributions",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================================
# MOUNTAIN PATH DESIGN SYSTEM
# ============================================================================
DARKBLUE  = "#003366"   # RGB(0,51,102)
LIGHTBLUE = "#ADD8E6"   # RGB(173,216,230)
GOLD      = "#FFD700"   # RGB(255,215,0)
ACCENTRED = "#B22234"
EXCEL_GRN = "#217346"
PY_DARK   = "#1E3250"
OFFWHITE  = "#F7FAFC"

MOUNTAIN_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Source+Serif+Pro:wght@400;600&display=swap');

html, body, [class*="css"] {{
    font-family: 'Source Serif Pro', Georgia, 'Times New Roman', serif;
}}

/* Remove Streamlit default padding a bit */
.block-container {{
    padding-top: 1rem;
    padding-bottom: 3rem;
    max-width: 1280px;
}}

/* Sidebar styling */
[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, {DARKBLUE} 0%, #001f3d 100%);
}}
[data-testid="stSidebar"] * {{
    color: #ffffff !important;
}}
[data-testid="stSidebar"] .stRadio > label > div {{
    color: #ffffff !important;
}}
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {{
    color: {GOLD} !important;
    font-family: 'Playfair Display', serif;
}}

/* Mountain Path brand banner */
.mp-brand-banner {{
    background: linear-gradient(135deg, {DARKBLUE} 0%, #001f3d 100%);
    color: #ffffff;
    padding: 22px 30px;
    border-radius: 8px;
    text-align: center;
    margin-bottom: 12px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.15);
    border-bottom: 4px solid {GOLD};
}}
.mp-brand-banner h1 {{
    font-family: 'Playfair Display', serif;
    font-weight: 900;
    margin: 0;
    font-size: 2.2rem;
    letter-spacing: 2px;
    color: #ffffff;
}}
.mp-brand-banner .sub {{
    font-style: italic;
    color: {LIGHTBLUE};
    font-size: 1.05rem;
}}
.mp-brand-banner .dot {{
    color: {GOLD};
    font-weight: bold;
}}

/* Page title */
.mp-title {{
    font-family: 'Playfair Display', serif;
    color: {DARKBLUE};
    font-size: 2.0rem;
    font-weight: 900;
    margin: 18px 0 4px 0;
    padding-bottom: 8px;
    border-bottom: 3px solid {GOLD};
}}
.mp-subtitle {{
    color: {DARKBLUE};
    font-size: 1.05rem;
    font-style: italic;
    margin-bottom: 18px;
}}

/* Section header */
.mp-section {{
    font-family: 'Playfair Display', serif;
    color: {DARKBLUE};
    font-size: 1.35rem;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 8px;
    padding-left: 10px;
    border-left: 5px solid {GOLD};
}}

/* Definition box (blue) */
.defn-box {{
    background: {LIGHTBLUE}33;
    border: 1.5px solid {DARKBLUE};
    border-radius: 8px;
    padding: 16px 20px;
    margin: 10px 0 14px 0;
}}
.defn-box .head {{
    background: {DARKBLUE};
    color: #ffffff;
    font-weight: bold;
    padding: 4px 10px;
    border-radius: 4px;
    display: inline-block;
    margin-bottom: 8px;
    font-size: 0.95rem;
    letter-spacing: 1px;
}}

/* Example / illustration box (gold) */
.ex-box {{
    background: #fffbe6;
    border: 1.5px solid {GOLD};
    border-radius: 8px;
    padding: 16px 20px;
    margin: 10px 0 14px 0;
}}
.ex-box .head {{
    background: {GOLD};
    color: {DARKBLUE};
    font-weight: bold;
    padding: 4px 10px;
    border-radius: 4px;
    display: inline-block;
    margin-bottom: 8px;
    font-size: 0.95rem;
    letter-spacing: 1px;
}}

/* Excel box (green) */
.xl-box {{
    background: #eaf7ef;
    border: 1.5px solid {EXCEL_GRN};
    border-radius: 8px;
    padding: 16px 20px;
    margin: 10px 0 14px 0;
    font-family: 'Courier New', monospace;
    font-size: 0.95rem;
}}
.xl-box .head {{
    background: {EXCEL_GRN};
    color: #ffffff;
    font-weight: bold;
    padding: 4px 10px;
    border-radius: 4px;
    display: inline-block;
    margin-bottom: 8px;
    font-family: 'Source Serif Pro', serif;
    font-size: 0.95rem;
    letter-spacing: 1px;
}}

/* Summary box (gold tint) */
.sum-box {{
    background: #fff7d1;
    border: 1.5px solid {DARKBLUE};
    border-radius: 8px;
    padding: 16px 20px;
    margin: 12px 0;
}}

/* Stat chip row */
.stat-chip {{
    background: {DARKBLUE};
    color: #ffffff;
    padding: 10px 16px;
    border-radius: 6px;
    text-align: center;
    box-shadow: 0 2px 6px rgba(0,0,0,0.12);
}}
.stat-chip .label {{
    color: {GOLD};
    font-size: 0.82rem;
    letter-spacing: 1px;
    text-transform: uppercase;
}}
.stat-chip .val {{
    font-size: 1.35rem;
    font-weight: 700;
}}

/* Footer */
.mp-footer {{
    margin-top: 40px;
    padding: 14px;
    background: {DARKBLUE};
    color: #ffffff;
    text-align: center;
    border-top: 4px solid {GOLD};
    border-radius: 6px;
    font-size: 0.9rem;
}}
.mp-footer .gold {{ color: {GOLD}; font-weight: 700; }}

/* Streamlit widget overrides */
.stRadio [role="radiogroup"] label {{
    background: transparent !important;
}}
[data-testid="stMetric"] {{
    background: #ffffff;
    border: 1px solid {DARKBLUE}33;
    border-radius: 6px;
    padding: 8px 10px;
}}
[data-testid="stMetricLabel"] {{
    color: {DARKBLUE} !important;
    font-weight: 600 !important;
}}

/* Tables */
.dataframe th {{
    background: {DARKBLUE} !important;
    color: #ffffff !important;
}}

/* Buttons */
.stButton>button {{
    background: {DARKBLUE};
    color: #ffffff;
    border: 1.5px solid {GOLD};
    border-radius: 6px;
    font-weight: 600;
}}
.stButton>button:hover {{
    background: {GOLD};
    color: {DARKBLUE};
    border: 1.5px solid {DARKBLUE};
}}
</style>
"""

st.markdown(MOUNTAIN_CSS, unsafe_allow_html=True)


# ============================================================================
# HELPERS
# ============================================================================
def brand_banner():
    st.markdown(
        f"""
        <div class="mp-brand-banner">
            <h1>THE MOUNTAIN PATH</h1>
            <div class="sub">World of Finance <span class="dot">•</span> themountainpathacademy.com</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def page_title(title, subtitle=""):
    st.markdown(f'<div class="mp-title">{title}</div>', unsafe_allow_html=True)
    if subtitle:
        st.markdown(f'<div class="mp-subtitle">{subtitle}</div>', unsafe_allow_html=True)


def section(text):
    st.markdown(f'<div class="mp-section">{text}</div>', unsafe_allow_html=True)


def defn_box(title, body_md):
    st.markdown(
        f"""<div class="defn-box"><span class="head">{title}</span><br>{body_md}</div>""",
        unsafe_allow_html=True,
    )


def ex_box(title, body_md):
    st.markdown(
        f"""<div class="ex-box"><span class="head">{title}</span><br>{body_md}</div>""",
        unsafe_allow_html=True,
    )


def xl_box(title, body_md):
    st.markdown(
        f"""<div class="xl-box"><span class="head">{title}</span><br>{body_md}</div>""",
        unsafe_allow_html=True,
    )


def sum_box(body_md):
    st.markdown(f"""<div class="sum-box">{body_md}</div>""", unsafe_allow_html=True)


def stat_chip_row(items):
    cols = st.columns(len(items))
    for c, (lbl, val) in zip(cols, items):
        with c:
            st.markdown(
                f'<div class="stat-chip"><div class="label">{lbl}</div>'
                f'<div class="val">{val}</div></div>',
                unsafe_allow_html=True,
            )


def mp_plot_layout(fig, title, xaxis="x", yaxis="y", height=420):
    fig.update_layout(
        title=dict(text=title, font=dict(family="Playfair Display", size=18, color=DARKBLUE)),
        xaxis=dict(title=xaxis, linecolor=DARKBLUE, gridcolor="#e6eaf0"),
        yaxis=dict(title=yaxis, linecolor=DARKBLUE, gridcolor="#e6eaf0"),
        plot_bgcolor="#ffffff",
        paper_bgcolor="#ffffff",
        font=dict(family="Source Serif Pro", color=DARKBLUE),
        height=height,
        margin=dict(l=60, r=20, t=60, b=50),
        showlegend=True,
        legend=dict(bgcolor="#ffffff", bordercolor=DARKBLUE, borderwidth=1),
    )
    return fig


def footer():
    st.markdown(
        f"""
        <div class="mp-footer">
            <span class="gold">The Mountain Path — World of Finance</span> &nbsp;•&nbsp;
            Prof. V. Ravichandran &nbsp;•&nbsp;
            <i>Bridging Theory with Practice</i> &nbsp;•&nbsp;
            <span class="gold">themountainpathacademy.com</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================================
# SIDEBAR NAVIGATION
# ============================================================================
with st.sidebar:
    st.markdown(
        f"""
        <div style="text-align:center; padding:16px 0; border-bottom:2px solid {GOLD};">
            <div style="font-family:'Playfair Display',serif; font-size:1.3rem; font-weight:900; color:{GOLD};">
                THE MOUNTAIN PATH
            </div>
            <div style="color:{LIGHTBLUE}; font-style:italic; font-size:0.85rem;">World of Finance</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("### Navigate")
    page = st.radio(
        "Sections",
        [
            "🏠 Home",
            "📚 Foundations",
            "🎲 Discrete: Bernoulli",
            "🎲 Discrete: Binomial",
            "🎲 Discrete: Poisson",
            "🎲 Discrete: Geometric",
            "📈 Continuous: Uniform",
            "📈 Continuous: Normal",
            "📈 Continuous: Log-Normal",
            "📈 Continuous: Exponential",
            "💼 Finance Tools (VaR / GBM)",
            "🧠 Practice Quiz",
            "📋 Excel Master Cheat Sheet",
        ],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown("**Prof. V. Ravichandran**")
    st.caption("28+ yrs Corporate Finance & Banking")
    st.caption("Financial Risk Modelling • Quant Finance")


brand_banner()


# ============================================================================
# PAGE: HOME
# ============================================================================
def page_home():
    page_title(
        "Probability & Distributions",
        "A teachable, interactive learner's studio — from first principles to financial applications",
    )

    c1, c2 = st.columns([3, 2])
    with c1:
        st.markdown(
            f"""
            #### Welcome
            This interactive studio lets you **see, touch, and compute** every
            concept in probability and distributions — with live sliders,
            plotted PDFs and CDFs, and the exact **Excel formulas** a finance
            learner needs to run on their own.

            **What you can do here:**

            - Explore the foundations (sample space, events, Kolmogorov axioms).
            - Build and inspect **discrete** distributions (Bernoulli, Binomial, Poisson, Geometric).
            - Build and inspect **continuous** distributions (Uniform, Normal, Log-Normal, Exponential).
            - Compute **Value-at-Risk**, simulate **Geometric Brownian Motion**, and practise with a quiz.
            - Copy the **Excel notation** straight from the green boxes into your own spreadsheet.
            """
        )
    with c2:
        # Hero figure - overlaid Normal + LogNormal + Exponential
        x1 = np.linspace(-4, 4, 400)
        x2 = np.linspace(0.05, 6, 400)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x1, y=stats.norm.pdf(x1), mode="lines",
                                 name="Normal N(0,1)",
                                 line=dict(color=DARKBLUE, width=3),
                                 fill="tozeroy", fillcolor="rgba(173,216,230,0.35)"))
        fig.add_trace(go.Scatter(x=x2, y=stats.lognorm.pdf(x2, s=1, scale=1),
                                 mode="lines", name="Log-Normal",
                                 line=dict(color=ACCENTRED, width=2.5, dash="dash")))
        fig.add_trace(go.Scatter(x=x2, y=stats.expon.pdf(x2, scale=1),
                                 mode="lines", name="Exponential",
                                 line=dict(color=GOLD, width=2.5)))
        mp_plot_layout(fig, "Three Continuous Distributions at a Glance", "x", "Density", height=360)
        st.plotly_chart(fig, use_container_width=True)

    section("How to use this studio")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            f"""<div class="defn-box"><span class="head">1 — EXPLORE</span><br>
            Pick a distribution from the sidebar. Drag sliders to change parameters
            and watch PMF/PDF and CDF update instantly.</div>""",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f"""<div class="ex-box"><span class="head">2 — VERIFY</span><br>
            Every panel shows the exact numerical answer so you can check
            your own Excel / Python calculation.</div>""",
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            f"""<div class="xl-box"><span class="head">3 — APPLY</span><br>
            Copy the Excel formula straight from the green boxes into
            your own workbook and replicate the result.</div>""",
            unsafe_allow_html=True,
        )


# ============================================================================
# PAGE: FOUNDATIONS
# ============================================================================
def page_foundations():
    page_title("Foundations — What is Probability?",
               "Random experiments, sample spaces, events, Kolmogorov axioms, random variables")

    section("1. Random Experiment")
    defn_box("DEFINITION",
             "A <b>random experiment</b> is any well-defined, repeatable procedure whose "
             "outcome cannot be predicted with certainty in advance. Examples: tossing a coin, "
             "rolling a die, observing tomorrow's NIFTY return, checking whether a borrower defaults.")

    section("2. Sample Space Ω and Events")
    defn_box("SAMPLE SPACE Ω",
             "The set of all possible outcomes. "
             "<br>• Coin toss: Ω = {H, T}"
             "<br>• Die roll: Ω = {1,2,3,4,5,6}"
             "<br>• Daily stock return: Ω = ℝ"
             "<br>• Time until default: Ω = [0, ∞)")
    defn_box("EVENT",
             "Any subset of Ω. For a die: A = 'even' = {2,4,6}; B = 'score > 4' = {5,6}; "
             "C = 'score = 7' = ∅ (impossible).")

    section("3. Kolmogorov Axioms")
    sum_box(
        "For any event A in a sample space Ω, the probability function P satisfies:<br>"
        "<b>Axiom 1 (non-negativity):</b> P(A) ≥ 0<br>"
        "<b>Axiom 2 (normalisation):</b> P(Ω) = 1<br>"
        "<b>Axiom 3 (countable additivity):</b> if A₁, A₂, … are disjoint, "
        "P(∪Aᵢ) = ΣP(Aᵢ)<br><br>"
        "Everything else in probability — conditional probability, Bayes' rule, "
        "distributions — is a <i>consequence</i> of these three simple rules."
    )

    section("4. Three Ways to Interpret a Probability")
    c1, c2, c3 = st.columns(3)
    with c1:
        defn_box("CLASSICAL", "Equally-likely outcomes. If Ω has n equal outcomes and A has k of them, P(A) = k/n. "
                              "Example: fair die, P(even) = 3/6.")
    with c2:
        defn_box("FREQUENTIST", "Long-run relative frequency. P(A) ≈ count(A in N trials) / N, as N → ∞. "
                                "Example: backtest of 5000 days, fraction with loss > 1%.")
    with c3:
        defn_box("BAYESIAN", "Personal degree of belief, updated via Bayes' rule as new evidence arrives. "
                             "Example: probability the Fed cuts rates next meeting.")

    section("5. Random Variable — The Bridge to Numbers")
    defn_box("RANDOM VARIABLE (RV)",
             "A function <b>X : Ω → ℝ</b> that assigns a real number to every outcome of the experiment. "
             "It converts qualitative outcomes (H/T) into quantitative values (1/0) so we can do arithmetic and statistics.")

    ex_box("ILLUSTRATION — Two-Coin Toss",
           "Ω = {HH, HT, TH, TT}, each with probability 1/4. Define X = number of heads.<br>"
           "Then X(HH)=2, X(HT)=1, X(TH)=1, X(TT)=0, so X takes values {0,1,2} with probabilities {1/4, 2/4, 1/4}. "
           "<i>That table of values and probabilities is exactly what a probability distribution is.</i>")


# ============================================================================
# GENERIC DISCRETE HELPERS
# ============================================================================
def show_discrete_plots(xs, pmf, cdf, title_pmf, title_cdf):
    c1, c2 = st.columns(2)
    with c1:
        fig = go.Figure(go.Bar(x=xs, y=pmf, marker_color=DARKBLUE, marker_line_color=GOLD,
                               marker_line_width=1.2, name="PMF"))
        mp_plot_layout(fig, title_pmf, "x", "P(X=x)", height=380)
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        # Step CDF
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=xs, y=cdf, mode="lines+markers",
                                 line=dict(color=DARKBLUE, width=2, shape="hv"),
                                 marker=dict(color=GOLD, size=8, line=dict(color=DARKBLUE, width=1)),
                                 name="CDF"))
        mp_plot_layout(fig, title_cdf, "x", "F(x) = P(X ≤ x)", height=380)
        st.plotly_chart(fig, use_container_width=True)


def show_continuous_plots(x, pdf, cdf, title_pdf, title_cdf, fill_range=None):
    c1, c2 = st.columns(2)
    with c1:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=pdf, mode="lines",
                                 line=dict(color=DARKBLUE, width=3),
                                 fill="tozeroy", fillcolor="rgba(173,216,230,0.35)",
                                 name="PDF"))
        if fill_range is not None:
            a, b = fill_range
            mask = (x >= a) & (x <= b)
            fig.add_trace(go.Scatter(x=x[mask], y=pdf[mask], mode="lines",
                                     line=dict(color=GOLD, width=0),
                                     fill="tozeroy", fillcolor="rgba(255,215,0,0.55)",
                                     name=f"P({a:.2f}≤X≤{b:.2f})"))
        mp_plot_layout(fig, title_pdf, "x", "f(x)", height=380)
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = go.Figure(go.Scatter(x=x, y=cdf, mode="lines",
                                   line=dict(color=DARKBLUE, width=3), name="CDF"))
        mp_plot_layout(fig, title_cdf, "x", "F(x) = P(X ≤ x)", height=380)
        st.plotly_chart(fig, use_container_width=True)


# ============================================================================
# PAGE: BERNOULLI
# ============================================================================
def page_bernoulli():
    page_title("Bernoulli Distribution",
               "Single yes/no trial — the atom of all discrete probability models")

    defn_box(
        "BERNOULLI(p)",
        "A single trial with two outcomes: success (X=1) with probability p, failure (X=0) with probability 1−p."
        "<br>PMF: p(x) = pˣ(1−p)¹⁻ˣ for x ∈ {0,1}"
        "<br>Mean = p, &nbsp; Variance = p(1−p)",
    )

    p = st.slider("Success probability p", 0.01, 0.99, 0.05, 0.01,
                  help="In credit risk this is typically the one-year Probability of Default (PD).")

    xs = np.array([0, 1])
    pmf = np.array([1 - p, p])
    cdf = np.cumsum(pmf)

    stat_chip_row([
        ("Mean E[X]", f"{p:.4f}"),
        ("Variance", f"{p*(1-p):.4f}"),
        ("Std Dev", f"{math.sqrt(p*(1-p)):.4f}"),
        ("Skewness", f"{(1-2*p)/math.sqrt(p*(1-p)):.4f}"),
    ])

    show_discrete_plots(xs, pmf, cdf, f"Bernoulli({p:.2f}) PMF", f"Bernoulli({p:.2f}) CDF")

    ex_box("FINANCE ILLUSTRATION — 1-Year Default",
           f"If PD = {p:.2%}, then E[X] = {p:.4f} (expected default rate) "
           f"and σ = {math.sqrt(p*(1-p)):.4f} — the default indicator is very noisy relative to its mean.")

    xl_box("EXCEL NOTATION",
           f"<b>P(X=1)</b>: <code>=BINOM.DIST(1,1,{p},FALSE)</code> → {p:.4f}"
           f"<br><b>P(X=0)</b>: <code>=BINOM.DIST(0,1,{p},FALSE)</code> → {1-p:.4f}"
           f"<br><b>Mean</b>: <code>={p}</code>"
           f"<br><b>Variance</b>: <code>={p}*{1-p}</code> → {p*(1-p):.4f}"
           f"<br><b>Std Dev</b>: <code>=SQRT({p}*{1-p})</code> → {math.sqrt(p*(1-p)):.4f}"
           f"<br><b>Simulate one trial</b>: <code>=IF(RAND()&lt;{p},1,0)</code>")


# ============================================================================
# PAGE: BINOMIAL
# ============================================================================
def page_binomial():
    page_title("Binomial Distribution",
               "Counting successes in n independent Bernoulli trials")

    defn_box(
        "BINOMIAL(n, p)",
        "X = number of successes in n independent trials, each success probability p."
        "<br>PMF: p(x) = C(n,x) · pˣ · (1−p)ⁿ⁻ˣ, for x = 0,1,…,n"
        "<br>Mean = np, &nbsp; Variance = np(1−p)",
    )

    c1, c2 = st.columns(2)
    with c1:
        n = st.slider("n — number of trials", 1, 200, 10, 1)
    with c2:
        p = st.slider("p — success probability", 0.01, 0.99, 0.05, 0.01)

    xs = np.arange(0, n + 1)
    pmf = stats.binom.pmf(xs, n, p)
    cdf = stats.binom.cdf(xs, n, p)

    stat_chip_row([
        ("Mean", f"{n*p:.4f}"),
        ("Variance", f"{n*p*(1-p):.4f}"),
        ("Std Dev", f"{math.sqrt(n*p*(1-p)):.4f}"),
        ("Mode", f"{int(np.floor((n+1)*p))}"),
    ])

    show_discrete_plots(xs, pmf, cdf, f"Binomial({n}, {p:.2f}) PMF", f"Binomial({n}, {p:.2f}) CDF")

    st.markdown("#### Query probabilities")
    c1, c2, c3 = st.columns(3)
    with c1:
        k = st.number_input("k (specific value)", 0, n, min(1, n), 1)
        st.metric("P(X = k)", f"{stats.binom.pmf(k, n, p):.6f}")
    with c2:
        st.metric("P(X ≤ k)", f"{stats.binom.cdf(k, n, p):.6f}")
    with c3:
        st.metric("P(X ≥ k)", f"{1-stats.binom.cdf(k-1, n, p):.6f}")

    xl_box("EXCEL NOTATION",
           f"<b>P(X = k)</b>: <code>=BINOM.DIST(k, {n}, {p}, FALSE)</code>"
           f"<br><b>P(X ≤ k)</b>: <code>=BINOM.DIST(k, {n}, {p}, TRUE)</code>"
           f"<br><b>P(X ≥ k)</b>: <code>=1 - BINOM.DIST(k-1, {n}, {p}, TRUE)</code>"
           f"<br><b>P(a ≤ X ≤ b)</b>: <code>=BINOM.DIST.RANGE({n}, {p}, a, b)</code>"
           f"<br><b>α-quantile</b>: <code>=BINOM.INV({n}, {p}, alpha)</code>"
           f"<br><b>Mean</b>: <code>={n}*{p}</code> → {n*p:.4f}"
           f"<br><b>Variance</b>: <code>={n}*{p}*{1-p}</code> → {n*p*(1-p):.4f}"
           f"<br><b>Simulate</b>: <code>=BINOM.INV({n}, {p}, RAND())</code>")


# ============================================================================
# PAGE: POISSON
# ============================================================================
def page_poisson():
    page_title("Poisson Distribution",
               "Events in a fixed interval — rare-event / operational-risk modelling")

    defn_box(
        "POISSON(λ)",
        "X = number of events per interval when events occur independently at constant rate λ."
        "<br>PMF: p(x) = e^(−λ) · λˣ / x!, for x = 0,1,2,…"
        "<br>Mean = λ, &nbsp; Variance = λ (a defining feature)"
        "<br><i>Law of rare events:</i> Binomial(n,p) → Poisson(λ=np) as n→∞, p→0.",
    )

    lam = st.slider("λ — average events per interval", 0.1, 30.0, 3.0, 0.1)
    upper = int(max(15, lam * 3))
    xs = np.arange(0, upper + 1)
    pmf = stats.poisson.pmf(xs, lam)
    cdf = stats.poisson.cdf(xs, lam)

    stat_chip_row([
        ("Mean", f"{lam:.3f}"),
        ("Variance", f"{lam:.3f}"),
        ("Std Dev", f"{math.sqrt(lam):.4f}"),
        ("Mode", f"{int(np.floor(lam))}"),
    ])

    show_discrete_plots(xs, pmf, cdf, f"Poisson({lam}) PMF", f"Poisson({lam}) CDF")

    c1, c2, c3 = st.columns(3)
    with c1:
        k = st.number_input("k", 0, upper, min(3, upper), 1)
        st.metric("P(X = k)", f"{stats.poisson.pmf(k, lam):.6f}")
    with c2:
        st.metric("P(X ≤ k)", f"{stats.poisson.cdf(k, lam):.6f}")
    with c3:
        st.metric("P(X ≥ k)", f"{1-stats.poisson.cdf(k-1, lam):.6f}")

    ex_box("FINANCE ILLUSTRATION — Fraud Desk",
           f"λ = {lam} fraud cases/day. P(zero tomorrow) = {math.exp(-lam):.4f}. "
           f"P(at least 5) = {1-stats.poisson.cdf(4, lam):.4f}. This drives operational-risk capital.")

    xl_box("EXCEL NOTATION",
           f"<b>P(X = k)</b>: <code>=POISSON.DIST(k, {lam}, FALSE)</code>"
           f"<br><b>P(X ≤ k)</b>: <code>=POISSON.DIST(k, {lam}, TRUE)</code>"
           f"<br><b>P(X ≥ k)</b>: <code>=1 - POISSON.DIST(k-1, {lam}, TRUE)</code>"
           f"<br><b>Mean / Variance</b>: <code>={lam}</code>")


# ============================================================================
# PAGE: GEOMETRIC
# ============================================================================
def page_geometric():
    page_title("Geometric Distribution",
               "Number of trials until the first success")

    defn_box(
        "GEOMETRIC(p)  [support x = 1, 2, 3, …]",
        "PMF: p(x) = (1−p)ˣ⁻¹ · p"
        "<br>Mean = 1/p, &nbsp; Variance = (1−p)/p²"
        "<br><i>Memoryless:</i> P(X > s+t | X > s) = P(X > t)",
    )

    p = st.slider("p — success probability per trial", 0.01, 0.99, 0.2, 0.01)
    upper = int(min(50, 6 / p))
    xs = np.arange(1, upper + 1)
    pmf = p * (1 - p) ** (xs - 1)
    cdf = 1 - (1 - p) ** xs

    stat_chip_row([
        ("Mean", f"{1/p:.4f}"),
        ("Variance", f"{(1-p)/p**2:.4f}"),
        ("Std Dev", f"{math.sqrt((1-p)/p**2):.4f}"),
        ("Median", f"{math.ceil(math.log(0.5)/math.log(1-p))}"),
    ])

    show_discrete_plots(xs, pmf, cdf, f"Geometric({p}) PMF", f"Geometric({p}) CDF")

    xl_box("EXCEL NOTATION",
           f"<b>P(X = k)</b>: <code>={p}*(1-{p})^(k-1)</code>"
           f"<br><b>P(X ≤ k)</b>: <code>=1-(1-{p})^k</code>"
           f"<br><b>Mean</b>: <code>=1/{p}</code> → {1/p:.4f}"
           f"<br><b>Variance</b>: <code>=(1-{p})/{p}^2</code> → {(1-p)/p**2:.4f}"
           f"<br><b>Simulate</b>: <code>=CEILING(LN(1-RAND())/LN(1-{p}),1)</code>")


# ============================================================================
# PAGE: UNIFORM
# ============================================================================
def page_uniform():
    page_title("Uniform Distribution",
               "Every sub-interval of equal length has equal probability — the workhorse of Monte Carlo")

    defn_box(
        "UNIFORM(a, b)",
        "PDF: f(x) = 1/(b−a) for a ≤ x ≤ b, else 0."
        "<br>CDF: F(x) = (x−a)/(b−a) for a ≤ x ≤ b."
        "<br>Mean = (a+b)/2, &nbsp; Variance = (b−a)²/12",
    )

    c1, c2 = st.columns(2)
    with c1:
        a = st.number_input("a (lower)", -100.0, 100.0, 0.0, 0.5)
    with c2:
        b = st.number_input("b (upper)", -100.0, 1000.0, 1.0, 0.5)
    if b <= a:
        st.error("b must be greater than a."); return

    x = np.linspace(a - 0.2 * (b - a), b + 0.2 * (b - a), 400)
    pdf = np.where((x >= a) & (x <= b), 1 / (b - a), 0)
    cdf = np.clip((x - a) / (b - a), 0, 1)

    stat_chip_row([
        ("Mean", f"{(a+b)/2:.4f}"),
        ("Variance", f"{(b-a)**2/12:.4f}"),
        ("Std Dev", f"{(b-a)/math.sqrt(12):.4f}"),
        ("Range", f"[{a}, {b}]"),
    ])

    show_continuous_plots(x, pdf, cdf, f"Uniform({a}, {b}) PDF", f"Uniform({a}, {b}) CDF")

    xl_box("EXCEL NOTATION",
           f"<b>PDF</b>: <code>=IF(AND(x&gt;={a},x&lt;={b}),1/({b}-{a}),0)</code>"
           f"<br><b>CDF</b>: <code>=MEDIAN(0,(x-{a})/({b}-{a}),1)</code>"
           f"<br><b>Mean</b>: <code>=({a}+{b})/2</code>"
           f"<br><b>Variance</b>: <code>=({b}-{a})^2/12</code>"
           f"<br><b>Simulate U(0,1)</b>: <code>=RAND()</code>"
           f"<br><b>Simulate U({a},{b})</b>: <code>={a}+({b}-{a})*RAND()</code>")


# ============================================================================
# PAGE: NORMAL
# ============================================================================
def page_normal():
    page_title("Normal (Gaussian) Distribution",
               "The bell curve — central to Black-Scholes, VaR, portfolio theory, and the Central Limit Theorem")

    defn_box(
        "NORMAL(μ, σ²)",
        "PDF: f(x) = 1/(σ√(2π)) · exp(−(x−μ)²/(2σ²))"
        "<br>Mean = μ, Variance = σ²"
        "<br>68–95–99.7 rule: ~68% within ±σ, ~95% within ±2σ, ~99.7% within ±3σ.",
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        mu = st.slider("μ (mean)", -5.0, 5.0, 0.0, 0.1)
    with c2:
        sigma = st.slider("σ (std dev)", 0.1, 5.0, 1.0, 0.1)
    with c3:
        fill_mode = st.selectbox("Shade region", ["None", "P(X ≤ a)", "P(X ≥ a)", "P(a ≤ X ≤ b)"])

    x = np.linspace(mu - 5 * sigma, mu + 5 * sigma, 500)
    pdf = stats.norm.pdf(x, mu, sigma)
    cdf = stats.norm.cdf(x, mu, sigma)

    stat_chip_row([
        ("Mean", f"{mu:.4f}"),
        ("Variance", f"{sigma**2:.4f}"),
        ("Std Dev", f"{sigma:.4f}"),
        ("Skew / Kurt", "0 / 3"),
    ])

    fill_range = None
    if fill_mode == "P(X ≤ a)":
        a_ = st.number_input("a", float(mu - 3 * sigma), float(mu + 3 * sigma), float(mu - sigma))
        fill_range = (x.min(), a_)
        st.metric("P(X ≤ a)", f"{stats.norm.cdf(a_, mu, sigma):.6f}")
    elif fill_mode == "P(X ≥ a)":
        a_ = st.number_input("a", float(mu - 3 * sigma), float(mu + 3 * sigma), float(mu + sigma))
        fill_range = (a_, x.max())
        st.metric("P(X ≥ a)", f"{1 - stats.norm.cdf(a_, mu, sigma):.6f}")
    elif fill_mode == "P(a ≤ X ≤ b)":
        c1, c2 = st.columns(2)
        with c1:
            a_ = st.number_input("a", float(mu - 3 * sigma), float(mu + 3 * sigma), float(mu - sigma))
        with c2:
            b_ = st.number_input("b", float(mu - 3 * sigma), float(mu + 3 * sigma), float(mu + sigma))
        if b_ > a_:
            fill_range = (a_, b_)
            st.metric("P(a ≤ X ≤ b)", f"{stats.norm.cdf(b_, mu, sigma) - stats.norm.cdf(a_, mu, sigma):.6f}")

    show_continuous_plots(x, pdf, cdf, f"Normal({mu}, {sigma}²) PDF",
                          f"Normal({mu}, {sigma}²) CDF", fill_range)

    xl_box("EXCEL NOTATION",
           f"<b>PDF</b>: <code>=NORM.DIST(x, {mu}, {sigma}, FALSE)</code>"
           f"<br><b>CDF</b>: <code>=NORM.DIST(x, {mu}, {sigma}, TRUE)</code>"
           f"<br><b>Standard Normal CDF</b>: <code>=NORM.S.DIST(z, TRUE)</code>"
           f"<br><b>Inverse CDF</b>: <code>=NORM.INV(p, {mu}, {sigma})</code>"
           f"<br><b>Standard Normal inverse</b>: <code>=NORM.S.INV(p)</code>"
           f"<br><b>Simulate</b>: <code>=NORM.INV(RAND(), {mu}, {sigma})</code>")


# ============================================================================
# PAGE: LOG-NORMAL
# ============================================================================
def page_lognormal():
    page_title("Log-Normal Distribution",
               "Asset prices, loss severities — right-skewed, strictly positive")

    defn_box(
        "LOG-NORMAL(μ, σ²)  where ln X ~ N(μ, σ²)",
        "PDF (x > 0): f(x) = 1/(xσ√(2π)) · exp(−(ln x − μ)²/(2σ²))"
        "<br>E[X] = exp(μ + σ²/2), &nbsp; Var(X) = (exp(σ²) − 1)·exp(2μ + σ²)"
        "<br>Median = e^μ, Mode = e^(μ−σ²)",
    )

    c1, c2 = st.columns(2)
    with c1:
        mu = st.slider("μ (mean of ln X)", -2.0, 5.0, 0.0, 0.1)
    with c2:
        sigma = st.slider("σ (std dev of ln X)", 0.05, 2.0, 0.5, 0.05)

    x = np.linspace(0.001, math.exp(mu + 4 * sigma), 500)
    pdf = stats.lognorm.pdf(x, s=sigma, scale=math.exp(mu))
    cdf = stats.lognorm.cdf(x, s=sigma, scale=math.exp(mu))
    mean_X = math.exp(mu + sigma ** 2 / 2)
    var_X = (math.exp(sigma ** 2) - 1) * math.exp(2 * mu + sigma ** 2)

    stat_chip_row([
        ("E[X]", f"{mean_X:.4f}"),
        ("Var(X)", f"{var_X:.4f}"),
        ("Median", f"{math.exp(mu):.4f}"),
        ("Mode", f"{math.exp(mu - sigma**2):.4f}"),
    ])

    show_continuous_plots(x, pdf, cdf, f"Log-Normal(μ={mu}, σ={sigma}) PDF",
                          f"Log-Normal(μ={mu}, σ={sigma}) CDF")

    xl_box("EXCEL NOTATION",
           f"<b>PDF</b>: <code>=LOGNORM.DIST(x, {mu}, {sigma}, FALSE)</code>"
           f"<br><b>CDF</b>: <code>=LOGNORM.DIST(x, {mu}, {sigma}, TRUE)</code>"
           f"<br><b>Inverse</b>: <code>=LOGNORM.INV(p, {mu}, {sigma})</code>"
           f"<br><b>E[X]</b>: <code>=EXP({mu}+{sigma}^2/2)</code> → {mean_X:.4f}"
           f"<br><b>Var(X)</b>: <code>=(EXP({sigma}^2)-1)*EXP(2*{mu}+{sigma}^2)</code> → {var_X:.4f}"
           f"<br><b>GBM stock price</b>: <code>=S0*EXP((r-0.5*v^2)*T + v*SQRT(T)*NORM.S.INV(RAND()))</code>")


# ============================================================================
# PAGE: EXPONENTIAL
# ============================================================================
def page_exponential():
    page_title("Exponential Distribution",
               "Waiting time until the next event — foundation of reduced-form credit risk")

    defn_box(
        "EXPONENTIAL(λ)",
        "PDF: f(x) = λ·e^(−λx), x ≥ 0."
        "<br>CDF: F(x) = 1 − e^(−λx)."
        "<br>Mean = 1/λ, &nbsp; Variance = 1/λ²"
        "<br><i>Memoryless:</i> P(X > s+t | X > s) = P(X > t)",
    )

    lam = st.slider("λ — hazard rate (events per unit time)", 0.01, 5.0, 0.5, 0.01)
    x = np.linspace(0, 6 / lam, 500)
    pdf = lam * np.exp(-lam * x)
    cdf = 1 - np.exp(-lam * x)

    stat_chip_row([
        ("Mean", f"{1/lam:.4f}"),
        ("Variance", f"{1/lam**2:.4f}"),
        ("Median", f"{math.log(2)/lam:.4f}"),
        ("Std Dev", f"{1/lam:.4f}"),
    ])

    show_continuous_plots(x, pdf, cdf, f"Exponential(λ={lam}) PDF", f"Exponential(λ={lam}) CDF")

    ex_box("FINANCE ILLUSTRATION — Time to Default",
           f"Hazard rate λ = {lam}: expected time to default = {1/lam:.2f} years. "
           f"1-year PD = {1 - math.exp(-lam):.4f}; 5-year survival = {math.exp(-5*lam):.4f}.")

    xl_box("EXCEL NOTATION",
           f"<b>PDF</b>: <code>=EXPON.DIST(x, {lam}, FALSE)</code>"
           f"<br><b>CDF</b>: <code>=EXPON.DIST(x, {lam}, TRUE)</code>"
           f"<br><b>Survival 1-F(x)</b>: <code>=1 - EXPON.DIST(x, {lam}, TRUE)</code>"
           f"<br><b>Mean</b>: <code>=1/{lam}</code>"
           f"<br><b>Simulate</b>: <code>=-LN(1-RAND())/{lam}</code>")


# ============================================================================
# PAGE: FINANCE TOOLS (VaR + GBM)
# ============================================================================
def page_finance_tools():
    page_title("Finance Tools",
               "Parametric Value-at-Risk and a Geometric Brownian Motion price simulator")

    t1, t2 = st.tabs(["🎯 Value-at-Risk (Normal)", "🌀 GBM Monte Carlo"])

    with t1:
        section("Parametric VaR (Normal)")
        c1, c2, c3 = st.columns(3)
        with c1:
            port = st.number_input("Portfolio value ($)", 10_000, 10_000_000_000, 10_000_000, 10_000)
        with c2:
            vol = st.number_input("Daily volatility σ (decimal)", 0.0001, 0.2, 0.01, 0.0001, format="%.4f")
        with c3:
            conf = st.slider("Confidence level (%)", 90, 99, 99, 1)

        alpha = 1 - conf / 100
        z = stats.norm.ppf(alpha)
        var_1d = -z * vol * port
        var_10d = var_1d * math.sqrt(10)

        stat_chip_row([
            ("Quantile z", f"{z:.4f}"),
            ("1-day σ (₹)", f"{vol*port:,.0f}"),
            ("1-day VaR", f"${var_1d:,.0f}"),
            ("10-day VaR (√10)", f"${var_10d:,.0f}"),
        ])

        # Plot the loss distribution
        x = np.linspace(-4 * vol, 4 * vol, 500)
        pdf = stats.norm.pdf(x, 0, vol)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x * 100, y=pdf, mode="lines",
                                 line=dict(color=DARKBLUE, width=3),
                                 fill="tozeroy", fillcolor="rgba(173,216,230,0.35)",
                                 name="Return density"))
        cut = z * vol
        mask = x <= cut
        fig.add_trace(go.Scatter(x=(x[mask]) * 100, y=pdf[mask], mode="lines",
                                 line=dict(color=ACCENTRED, width=0),
                                 fill="tozeroy", fillcolor="rgba(178,34,52,0.55)",
                                 name=f"{100-conf}% tail"))
        mp_plot_layout(fig, f"Daily Return Density — {conf}% VaR",
                       "Daily return (%)", "Density", height=380)
        st.plotly_chart(fig, use_container_width=True)

        xl_box("EXCEL NOTATION",
               f"<b>z-quantile</b>: <code>=NORM.S.INV({alpha:.4f})</code> → {z:.4f}"
               f"<br><b>1-day VaR</b>: <code>=-NORM.S.INV({alpha:.4f})*{vol}*{port}</code> → ${var_1d:,.0f}"
               f"<br><b>10-day VaR</b>: <code>=-NORM.S.INV({alpha:.4f})*{vol}*{port}*SQRT(10)</code> → ${var_10d:,.0f}")

    with t2:
        section("Geometric Brownian Motion — Monte Carlo Stock Paths")
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            S0 = st.number_input("S₀ (spot)", 1.0, 10000.0, 100.0, 1.0)
        with c2:
            r = st.number_input("μ / r (annual drift)", -0.5, 0.5, 0.08, 0.01)
        with c3:
            sig = st.number_input("σ (annual volatility)", 0.01, 1.0, 0.20, 0.01)
        with c4:
            T = st.number_input("T (years)", 0.01, 10.0, 1.0, 0.1)
        n_paths = st.slider("Number of simulated paths", 5, 500, 50, 5)
        n_steps = 252  # daily

        dt = T / n_steps
        rng = np.random.default_rng()
        Z = rng.standard_normal((n_paths, n_steps))
        increments = (r - 0.5 * sig ** 2) * dt + sig * math.sqrt(dt) * Z
        log_paths = np.cumsum(increments, axis=1)
        paths = S0 * np.exp(log_paths)
        paths = np.hstack([np.full((n_paths, 1), S0), paths])
        t_axis = np.linspace(0, T, n_steps + 1)

        fig = go.Figure()
        for i in range(n_paths):
            fig.add_trace(go.Scatter(x=t_axis, y=paths[i], mode="lines",
                                     line=dict(color=DARKBLUE, width=1),
                                     opacity=0.3, showlegend=False))
        mean_path = paths.mean(axis=0)
        fig.add_trace(go.Scatter(x=t_axis, y=mean_path, mode="lines",
                                 line=dict(color=GOLD, width=3),
                                 name="Mean of paths"))
        mp_plot_layout(fig, "GBM Monte Carlo Paths", "t (years)", "Price", height=420)
        st.plotly_chart(fig, use_container_width=True)

        ST = paths[:, -1]
        stat_chip_row([
            ("Mean Sₜ", f"{ST.mean():.2f}"),
            ("5th percentile", f"{np.percentile(ST, 5):.2f}"),
            ("95th percentile", f"{np.percentile(ST, 95):.2f}"),
            ("Theoretical E[Sₜ]", f"{S0*math.exp(r*T):.2f}"),
        ])

        xl_box("EXCEL NOTATION",
               f"<b>Simulate one terminal price</b>: "
               f"<code>={S0}*EXP(({r}-0.5*{sig}^2)*{T} + {sig}*SQRT({T})*NORM.S.INV(RAND()))</code>"
               f"<br><b>Theoretical E[Sₜ]</b>: <code>={S0}*EXP({r}*{T})</code> → {S0*math.exp(r*T):.2f}")


# ============================================================================
# PAGE: PRACTICE QUIZ
# ============================================================================
QUIZ = [
    ("In Excel, which formula gives P(X ≤ 3) for X ~ Binomial(10, 0.5)?",
     [
         "=BINOM.DIST(3, 10, 0.5, TRUE)",
         "=BINOM.DIST(3, 10, 0.5, FALSE)",
         "=BINOM.INV(10, 0.5, 3)",
         "=NORM.S.DIST(3, TRUE)",
     ],
     0,
     "TRUE returns the cumulative CDF. FALSE returns just the PMF value at k."),
    ("For a continuous random variable X, what is P(X = a)?",
     ["1", "Always 0", "f(a)", "F(a) − F(a−1)"], 1,
     "Point probabilities are zero for continuous RVs; only intervals (areas) carry probability."),
    ("Which statement about the PDF f(x) is FALSE?",
     ["f(x) ≥ 0 always",
      "∫f(x)dx = 1 over the support",
      "f(x) is itself a probability and must be ≤ 1",
      "P(a ≤ X ≤ b) = ∫ₐᵇ f(x)dx"], 2,
     "f(x) is a density, not a probability; it can exceed 1 (only the integral must be 1)."),
    ("E[X] and Var(X) for Poisson(λ) are:",
     ["both λ", "λ and λ²", "1/λ and 1/λ²", "λ and √λ"], 0,
     "Poisson has mean = variance = λ — a defining feature used as a quick sanity check."),
    ("In Excel, =NORM.S.INV(0.01) returns approximately:",
     ["2.3263", "−2.3263", "0.9900", "0.0100"], 1,
     "NORM.S.INV gives the standard-normal quantile; at α=0.01 it is ≈ −2.3263 (the 1% VaR z-score)."),
    ("The 1-day 99% VaR on a portfolio with daily σ = ₹1 mn is closest to:",
     ["₹1.00 mn", "₹1.64 mn", "₹2.33 mn", "₹3.00 mn"], 2,
     "VaR ≈ 2.3263 × σ (normal assumption). 2.3263 × ₹1 mn ≈ ₹2.33 mn."),
    ("Which distribution is used to model the waiting time until the next default event?",
     ["Binomial", "Normal", "Exponential", "Uniform"], 2,
     "Exponential models the time until the next event in a Poisson process — foundation of reduced-form credit models."),
    ("Under Geometric Brownian Motion the terminal price Sₜ is:",
     ["Normal", "Log-normal", "Uniform", "Exponential"], 1,
     "Because ln Sₜ is Normal, Sₜ itself is Log-normal — guaranteeing prices stay positive."),
    ("What does =BINOM.INV(10, 0.5, 0.95) return?",
     ["P(X ≤ 10)",
      "Smallest k with P(X ≤ k) ≥ 0.95",
      "The 95th value of PMF",
      "Random Binomial sample"], 1,
     "BINOM.INV is the discrete quantile: smallest integer k whose CDF is ≥ the probability argument."),
    ("Which Excel formula simulates one realisation of Exponential(λ = 0.5)?",
     ["=EXPON.DIST(0.5, RAND(), TRUE)",
      "=RAND()*0.5",
      "=-LN(1-RAND())/0.5",
      "=NORM.S.INV(RAND())*0.5"], 2,
     "Inverse-CDF method: if U~U(0,1), then X = −ln(1−U)/λ ~ Exp(λ)."),
]


def page_quiz():
    page_title("Practice Quiz", "Ten multiple-choice questions to test your understanding")

    if "quiz_answers" not in st.session_state:
        st.session_state.quiz_answers = [None] * len(QUIZ)

    for i, (q, opts, correct, expl) in enumerate(QUIZ):
        st.markdown(f"**Q{i+1}. {q}**")
        chosen = st.radio(f"Answer {i+1}", opts, index=None, key=f"q_{i}", label_visibility="collapsed")
        st.session_state.quiz_answers[i] = chosen
        st.markdown("---")

    if st.button("📊 Submit & Score", use_container_width=False):
        score = 0
        for i, (q, opts, correct, expl) in enumerate(QUIZ):
            if st.session_state.quiz_answers[i] == opts[correct]:
                score += 1
                st.success(f"Q{i+1} ✓ correct — {expl}")
            else:
                chosen = st.session_state.quiz_answers[i]
                if chosen is None:
                    st.warning(f"Q{i+1} not answered. Correct: **{opts[correct]}** — {expl}")
                else:
                    st.error(f"Q{i+1} ✗ you chose: {chosen}. Correct: **{opts[correct]}** — {expl}")
        st.markdown(f"<div class='sum-box'><b>Final score: {score} / {len(QUIZ)}</b></div>", unsafe_allow_html=True)


# ============================================================================
# PAGE: EXCEL CHEAT SHEET
# ============================================================================
def page_cheat_sheet():
    page_title("Excel Master Cheat Sheet", "Every distribution, every function — at a glance")

    section("Distribution functions (PDF/PMF ↔ CDF ↔ Inverse)")
    df1 = pd.DataFrame(
        [
            ["Bernoulli(p)",        "=BINOM.DIST(x,1,p,FALSE)",    "=BINOM.DIST(x,1,p,TRUE)",     "—"],
            ["Binomial(n,p)",       "=BINOM.DIST(x,n,p,FALSE)",    "=BINOM.DIST(x,n,p,TRUE)",     "=BINOM.INV(n,p,α)"],
            ["Poisson(λ)",          "=POISSON.DIST(x,λ,FALSE)",    "=POISSON.DIST(x,λ,TRUE)",     "—"],
            ["Geometric(p)",        "=p*(1-p)^(x-1)",              "=1-(1-p)^x",                  "=CEILING(LN(1-α)/LN(1-p),1)"],
            ["Uniform(a,b)",        "=1/(b-a)",                    "=(x-a)/(b-a)",                "=a+α*(b-a)"],
            ["Normal(μ,σ)",         "=NORM.DIST(x,μ,σ,FALSE)",    "=NORM.DIST(x,μ,σ,TRUE)",     "=NORM.INV(α,μ,σ)"],
            ["Std Normal(0,1)",     "=NORM.S.DIST(z,FALSE)",       "=NORM.S.DIST(z,TRUE)",        "=NORM.S.INV(α)"],
            ["Log-Normal(μ,σ)",    "=LOGNORM.DIST(x,μ,σ,FALSE)", "=LOGNORM.DIST(x,μ,σ,TRUE)",  "=LOGNORM.INV(α,μ,σ)"],
            ["Exponential(λ)",      "=EXPON.DIST(x,λ,FALSE)",      "=EXPON.DIST(x,λ,TRUE)",       "=-LN(1-α)/λ"],
        ],
        columns=["Distribution", "PDF / PMF", "CDF", "Inverse / quantile"],
    )
    st.dataframe(df1, use_container_width=True, hide_index=True)

    section("Descriptive statistics")
    df2 = pd.DataFrame(
        [
            ["Arithmetic mean", "=AVERAGE(range)"],
            ["Median", "=MEDIAN(range)"],
            ["Mode", "=MODE.SNGL(range)"],
            ["Sample variance", "=VAR.S(range)"],
            ["Population variance", "=VAR.P(range)"],
            ["Sample std deviation", "=STDEV.S(range)"],
            ["Population std deviation", "=STDEV.P(range)"],
            ["Skewness", "=SKEW(range)"],
            ["Kurtosis (excess)", "=KURT(range)"],
            ["k-th percentile", "=PERCENTILE.INC(range, k)"],
            ["Correlation", "=CORREL(r1, r2)"],
            ["Sample covariance", "=COVARIANCE.S(r1, r2)"],
            ["SUMPRODUCT for E[X]", "=SUMPRODUCT(x_range, p_range)"],
        ],
        columns=["Statistic", "Excel formula"],
    )
    st.dataframe(df2, use_container_width=True, hide_index=True)

    section("Monte Carlo quick-reference")
    df3 = pd.DataFrame(
        [
            ["U(0,1)",              "=RAND()"],
            ["Integer in [a,b]",    "=RANDBETWEEN(a,b)"],
            ["Bernoulli(p)",        "=IF(RAND()<p,1,0)"],
            ["Binomial(n,p)",       "=BINOM.INV(n,p,RAND())"],
            ["Normal(μ,σ)",         "=NORM.INV(RAND(),μ,σ)"],
            ["Standard Normal",     "=NORM.S.INV(RAND())"],
            ["Log-Normal",          "=LOGNORM.INV(RAND(),μ,σ)"],
            ["Exponential(λ)",      "=-LN(1-RAND())/λ"],
            ["GBM terminal Sₜ",     "=S0*EXP((r-0.5*v^2)*T+v*SQRT(T)*NORM.S.INV(RAND()))"],
        ],
        columns=["Target distribution", "Excel formula"],
    )
    st.dataframe(df3, use_container_width=True, hide_index=True)


# ============================================================================
# ROUTER
# ============================================================================
PAGES = {
    "🏠 Home": page_home,
    "📚 Foundations": page_foundations,
    "🎲 Discrete: Bernoulli": page_bernoulli,
    "🎲 Discrete: Binomial": page_binomial,
    "🎲 Discrete: Poisson": page_poisson,
    "🎲 Discrete: Geometric": page_geometric,
    "📈 Continuous: Uniform": page_uniform,
    "📈 Continuous: Normal": page_normal,
    "📈 Continuous: Log-Normal": page_lognormal,
    "📈 Continuous: Exponential": page_exponential,
    "💼 Finance Tools (VaR / GBM)": page_finance_tools,
    "🧠 Practice Quiz": page_quiz,
    "📋 Excel Master Cheat Sheet": page_cheat_sheet,
}

PAGES[page]()

footer()
