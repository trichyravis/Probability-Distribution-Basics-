
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


def prob_card(n, title, setup, formula, answer):
    """Render one solved-problem card (used by every distribution page)."""
    st.markdown(
        f"<div class='ex-box'><span class='head'>Problem {n}. {title}</span><br>"
        f"<b>Setup:</b> {setup}<br>"
        f"<b>Excel:</b> <code>{formula}</code><br>"
        f"<b>Answer:</b> {answer}</div>",
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


# -- Author / contact links (update handles here) -----------------------------
LINKEDIN_URL = "https://www.linkedin.com/in/trichyravis/"
GITHUB_URL   = "https://github.com/trichyravis"
EMAIL        = "trichyravis@gmail.com"


def footer():
    st.markdown(
        f"""
        <div class="mp-footer">
            <span class="gold">The Mountain Path — World of Finance</span> &nbsp;•&nbsp;
            Prof. V. Ravichandran &nbsp;•&nbsp;
            <i>Bridging Theory with Practice</i> &nbsp;•&nbsp;
            <a href="https://themountainpathacademy.com" target="_blank" style="color:#FFD700;text-decoration:none;">themountainpathacademy.com</a> &nbsp;•&nbsp;
            <a href="{LINKEDIN_URL}" target="_blank" style="color:#FFD700;text-decoration:none;">LinkedIn</a> &nbsp;•&nbsp;
            <a href="{GITHUB_URL}" target="_blank" style="color:#FFD700;text-decoration:none;">GitHub</a> &nbsp;•&nbsp;
            <a href="mailto:{EMAIL}" style="color:#FFD700;text-decoration:none;">{EMAIL}</a>
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
            "📈 Continuous: Triangular",
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

    # ---- 10 SOLVED PROBLEMS ------------------------------------------------
    section("10 Solved problems (Excel notation) — fixed at p = 0.30")
    P = 0.30
    prob_card(1, "P(X = 1)",  "Probability of a success in one trial.",
              f"=BINOM.DIST(1,1,{P},FALSE)", f"<b>{P:.4f}</b>")
    prob_card(2, "P(X = 0)",  "Probability of a failure.",
              f"=BINOM.DIST(0,1,{P},FALSE)", f"<b>{1-P:.4f}</b>")
    prob_card(3, "Mean",      "Expected value of a single Bernoulli trial.",
              f"={P}", f"E[X] = <b>{P:.4f}</b>")
    prob_card(4, "Variance",  "Var(X) = p(1−p).",
              f"={P}*{1-P}", f"<b>{P*(1-P):.4f}</b>")
    prob_card(5, "Std deviation", "σ = √(p(1−p)).",
              f"=SQRT({P}*{1-P})", f"<b>{math.sqrt(P*(1-P)):.4f}</b>")
    prob_card(6, "Skewness",  "Closed form (1−2p)/√(p(1−p)).",
              f"=(1-2*{P})/SQRT({P}*{1-P})", f"<b>{(1-2*P)/math.sqrt(P*(1-P)):.4f}</b> (right-skewed)")
    prob_card(7, "CDF F(0)",  "Cumulative at 0.",
              f"=BINOM.DIST(0,1,{P},TRUE)", f"<b>{1-P:.4f}</b>")
    prob_card(8, "CDF F(1)",  "Cumulative at 1 = 1.",
              f"=BINOM.DIST(1,1,{P},TRUE)", "<b>1.0000</b>")
    prob_card(9, "Simulate one trial", "Inverse-CDF via RAND.",
              f"=IF(RAND()&lt;{P},1,0)", "Returns 1 with prob 0.30, else 0.")
    prob_card(10, "Sum of N independent Bernoullis = Binomial",
              "If we run N=100 such trials, the count of successes follows Binomial(N=100, p=0.30).",
              f"=BINOM.DIST(35,100,{P},FALSE)",
              f"P(X = 35 in 100) = <b>{stats.binom.pmf(35,100,P):.6f}</b>")


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

    # ---- 10 SOLVED PROBLEMS ------------------------------------------------
    section("10 Solved problems (Excel notation) — Loan portfolio of n=20, PD=0.10")
    N, P = 20, 0.10
    rv = stats.binom(N, P)
    prob_card(1, "Mean & variance", "Expected number of defaults and its variance.",
              f"=20*0.10 ; =20*0.10*0.90", f"E[X]=<b>2.0</b>, Var=<b>1.8</b>, σ=<b>{math.sqrt(20*0.10*0.90):.4f}</b>")
    prob_card(2, "P(X = 0) — zero defaults",
              "Probability the entire portfolio survives the year.",
              "=BINOM.DIST(0,20,0.10,FALSE)", f"<b>{rv.pmf(0):.6f}</b>")
    prob_card(3, "P(X = 2) — exactly 2 defaults",
              "Most-likely outcome (mode).", "=BINOM.DIST(2,20,0.10,FALSE)",
              f"<b>{rv.pmf(2):.6f}</b>")
    prob_card(4, "P(X ≤ 2) — at most 2 defaults",
              "Cumulative probability up to 2.", "=BINOM.DIST(2,20,0.10,TRUE)",
              f"<b>{rv.cdf(2):.6f}</b>")
    prob_card(5, "P(X ≥ 3) — tail-loss event",
              "1 − P(X ≤ 2). The downside-risk side.",
              "=1 - BINOM.DIST(2,20,0.10,TRUE)",
              f"<b>{1-rv.cdf(2):.6f}</b>")
    prob_card(6, "P(2 ≤ X ≤ 5) — central-mass band",
              "Range probability via BINOM.DIST.RANGE.",
              "=BINOM.DIST.RANGE(20,0.10,2,5)",
              f"<b>{rv.cdf(5)-rv.cdf(1):.6f}</b>")
    prob_card(7, "95-percentile loss-count VaR",
              "Inverse CDF — most defaults you would expect at the 95% level.",
              "=BINOM.INV(20,0.10,0.95)",
              f"<b>{int(rv.ppf(0.95))}</b> defaults")
    prob_card(8, "Mode = ⌊(n+1)p⌋",
              "Closed-form mode of a Binomial.",
              "=FLOOR((20+1)*0.10,1)",
              f"<b>{int((N+1)*P)}</b>")
    prob_card(9, "Normal approximation P(X ≤ 4)",
              "Use NORM.DIST with μ=np, σ=√(npq) and continuity correction.",
              "=NORM.DIST(4.5, 2, SQRT(1.8), TRUE)",
              f"Approx <b>{stats.norm.cdf(4.5, 2, math.sqrt(1.8)):.6f}</b>; exact = <b>{rv.cdf(4):.6f}</b>")
    prob_card(10, "Simulate one portfolio loss-count",
              "Inverse-CDF via RAND.", "=BINOM.INV(20,0.10,RAND())",
              "Returns 0–20; long-run average ≈ 2.")


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

    # ---- 10 SOLVED PROBLEMS ------------------------------------------------
    section("10 Solved problems (Excel notation) — Insurance claims, λ = 4 / day")
    L = 4
    rv = stats.poisson(L)
    prob_card(1, "Mean and variance",
              "Both equal λ — defining feature of Poisson.",
              "=4 ; =4", "<b>Mean = Var = 4</b>, σ = <b>2</b>")
    prob_card(2, "P(X = 0) — quiet day",
              "Probability of zero claims today.",
              "=POISSON.DIST(0,4,FALSE)", f"<b>{rv.pmf(0):.6f}</b>")
    prob_card(3, "P(X = 3) — modal-ish day",
              "Probability of exactly 3 claims.",
              "=POISSON.DIST(3,4,FALSE)", f"<b>{rv.pmf(3):.6f}</b>")
    prob_card(4, "P(X ≤ 2)",
              "At most 2 claims today.",
              "=POISSON.DIST(2,4,TRUE)", f"<b>{rv.cdf(2):.6f}</b>")
    prob_card(5, "P(X ≥ 5) — busy-day risk",
              "Tail probability used for staffing capacity.",
              "=1 - POISSON.DIST(4,4,TRUE)",
              f"<b>{1-rv.cdf(4):.6f}</b>")
    prob_card(6, "P(2 ≤ X ≤ 6) — central band",
              "= F(6) − F(1).",
              "=POISSON.DIST(6,4,TRUE) - POISSON.DIST(1,4,TRUE)",
              f"<b>{rv.cdf(6)-rv.cdf(1):.6f}</b>")
    prob_card(7, "Weekly aggregate (λ_week = 28)",
              "Sum of independent Poissons is Poisson with sum of rates.",
              "=POISSON.DIST(35,28,TRUE) - POISSON.DIST(20,28,TRUE)",
              f"P(20 < X ≤ 35) = <b>{stats.poisson.cdf(35,28)-stats.poisson.cdf(20,28):.6f}</b>")
    prob_card(8, "Mode = ⌊λ⌋",
              "Closed-form Poisson mode.",
              "=FLOOR(4,1)", "<b>4</b>")
    prob_card(9, "Normal approximation P(X ≤ 6)",
              "When λ ≥ 10, X ≈ Normal(λ, λ); for λ=4 it is rough but illustrative.",
              "=NORM.DIST(6.5, 4, SQRT(4), TRUE)",
              f"Approx <b>{stats.norm.cdf(6.5, 4, 2):.6f}</b>; exact <b>{rv.cdf(6):.6f}</b>")
    prob_card(10, "Operational-risk capital (frequency leg)",
              "Expected annual claim count and 99.9% VaR claim count "
              "(use scipy / inverse search; Excel needs an inverse table).",
              "Use lookup against POISSON.DIST(k,λ_year,TRUE) until 0.999",
              f"Annual mean = <b>{4*250}</b>, 99.9% VaR claims/year ≈ <b>{int(stats.poisson.ppf(0.999, 4*250))}</b> "
              "(assuming 250 trading days)")


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

    # ---- 10 SOLVED PROBLEMS ------------------------------------------------
    section("10 Solved problems (Excel notation) — Sales calls, p = 0.20 per call")
    Pp = 0.20
    rv = stats.geom(Pp)
    prob_card(1, "P(X = 1)", "Convert on the very first call.",
              "=0.20*(1-0.20)^(1-1)", f"<b>{rv.pmf(1):.4f}</b>")
    prob_card(2, "P(X = 3)", "First conversion happens on the 3rd call.",
              "=0.20*(1-0.20)^(3-1)", f"<b>{rv.pmf(3):.4f}</b>")
    prob_card(3, "P(X ≤ 5)", "Convert within the first 5 calls.",
              "=1-(1-0.20)^5", f"<b>{rv.cdf(5):.6f}</b>")
    prob_card(4, "P(X > 10)", "More than 10 calls without success.",
              "=(1-0.20)^10", f"<b>{(1-Pp)**10:.6f}</b>")
    prob_card(5, "Mean number of calls", "1/p = 5 calls on average.",
              "=1/0.20", "<b>5.0</b>")
    prob_card(6, "Variance", "(1−p)/p².",
              "=(1-0.20)/0.20^2", f"<b>{(1-Pp)/Pp**2:.4f}</b>")
    prob_card(7, "Median number of calls",
              "Smallest k such that 1−(1−p)^k ≥ 0.5.",
              "=CEILING(LN(0.5)/LN(1-0.20),1)",
              f"<b>{math.ceil(math.log(0.5)/math.log(1-Pp))}</b>")
    prob_card(8, "Memoryless check",
              "Given 4 failures already, P(2 more failures, then success) = same as starting fresh.",
              "=(1-0.20)^2 * 0.20",
              f"<b>{(1-Pp)**2 * Pp:.6f}</b> — independent of history.")
    prob_card(9, "Simulate one path",
              "Inverse-CDF for Geometric.",
              "=CEILING(LN(1-RAND())/LN(1-0.20),1)",
              "Returns a positive integer; long-run mean = 5.")
    prob_card(10, "Survival until success",
              "P(X > 7) = (1-p)^7 — probability salesperson is still pitching after 7 calls.",
              "=(1-0.20)^7", f"<b>{(1-Pp)**7:.6f}</b>")


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

    # ---- 10 SOLVED PROBLEMS ------------------------------------------------
    section("10 Solved problems (Excel notation) — Loan recovery rate U(10%, 50%)")
    A_, B_ = 10, 50
    rv = stats.uniform(A_, B_-A_)
    prob_card(1, "PDF height", "Constant 1/(b−a) over [a, b].",
              "=1/(50-10)", "<b>0.025</b>")
    prob_card(2, "Mean", "(a+b)/2.",
              "=(10+50)/2", "<b>30</b>%")
    prob_card(3, "Variance & σ",
              "(b−a)²/12 and √Var.", "=(50-10)^2/12 ; =(50-10)/SQRT(12)",
              f"Var = <b>{(B_-A_)**2/12:.4f}</b>, σ = <b>{(B_-A_)/math.sqrt(12):.4f}</b>")
    prob_card(4, "P(X ≤ 20)", "(20−10)/(50−10).",
              "=(20-10)/(50-10)", f"<b>{rv.cdf(20):.4f}</b>")
    prob_card(5, "P(20 ≤ X ≤ 35)",
              "Length of sub-interval ÷ length of support.",
              "=(35-20)/(50-10)", f"<b>{rv.cdf(35)-rv.cdf(20):.4f}</b>")
    prob_card(6, "P(X > 40) — high-recovery", "(50−40)/(50−10).",
              "=(50-40)/(50-10)", f"<b>{1-rv.cdf(40):.4f}</b>")
    prob_card(7, "Median",
              "Symmetric → median = mean.", "=(10+50)/2", "<b>30</b>")
    prob_card(8, "90th percentile (haircut planning)",
              "a + α(b−a).", "=10+0.90*(50-10)", f"<b>{rv.ppf(0.90):.2f}</b>")
    prob_card(9, "Simulate one recovery rate",
              "Inverse-CDF for Uniform.", "=10+(50-10)*RAND()",
              "Returns a number in [10, 50]; long-run mean = 30.")
    prob_card(10, "Expected loss given default",
              "If LGD = 1 − recovery, E[LGD] = 1 − E[recovery]/100.",
              "=1 - ((10+50)/2)/100", "<b>0.70</b> = 70%")


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

    # ---- 10 SOLVED PROBLEMS ------------------------------------------------
    section("10 Solved problems (Excel notation) — Daily P&L μ = 0, σ = 1.5%, MV = ₹10 cr")
    M_, S_ = 100, 15  # use IQ-style centred example for first set, then VaR set
    rv = stats.norm(M_, S_)
    prob_card(1, "P(X ≤ 130) for N(100, 15)",
              "CDF at 130.", "=NORM.DIST(130,100,15,TRUE)",
              f"<b>{rv.cdf(130):.6f}</b>")
    prob_card(2, "P(X > 120)",
              "1 − CDF.", "=1 - NORM.DIST(120,100,15,TRUE)",
              f"<b>{1-rv.cdf(120):.6f}</b>")
    prob_card(3, "P(85 ≤ X ≤ 115) — within ±1σ band",
              "= F(115) − F(85). Should be ≈ 68%.",
              "=NORM.DIST(115,100,15,TRUE)-NORM.DIST(85,100,15,TRUE)",
              f"<b>{rv.cdf(115)-rv.cdf(85):.6f}</b> (≈ 68% rule)")
    prob_card(4, "Standardise to z",
              "z = (x − μ)/σ.", "=(130-100)/15 ; =NORM.S.DIST(2,TRUE)",
              f"z = 2.0; Φ(2) = <b>{stats.norm.cdf(2):.6f}</b>")
    prob_card(5, "95th percentile",
              "Inverse CDF at 0.95.", "=NORM.INV(0.95,100,15)",
              f"<b>{rv.ppf(0.95):.4f}</b>")
    prob_card(6, "99.5th percentile (right tail)",
              "Capital VaR-style quantile.", "=NORM.INV(0.995,100,15)",
              f"<b>{rv.ppf(0.995):.4f}</b>")
    prob_card(7, "Standard Normal critical z",
              "z₀.₉₇₅ used in 95% CI.", "=NORM.S.INV(0.975)",
              f"<b>{stats.norm.ppf(0.975):.4f}</b>")
    prob_card(8, "1-day 95% VaR (μ=0, σ=1.5%, MV=₹10 cr)",
              "Parametric VaR = MV·σ·z₀.₉₅.",
              "=10E7 * 0.015 * NORM.S.INV(0.95)",
              f"<b>₹{10e7*0.015*stats.norm.ppf(0.95):,.0f}</b>")
    prob_card(9, "10-day 99% VaR — Basel scaling",
              "VaR scales with √T and uses 99% quantile.",
              "=10E7 * 0.015 * SQRT(10) * NORM.S.INV(0.99)",
              f"<b>₹{10e7*0.015*math.sqrt(10)*stats.norm.ppf(0.99):,.0f}</b>")
    prob_card(10, "Simulate one daily return",
              "Inverse-CDF Monte Carlo.", "=NORM.INV(RAND(),0,0.015)",
              "Returns a normal draw with mean 0, σ = 1.5%.")


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

    # ---- 10 SOLVED PROBLEMS ------------------------------------------------
    section("10 Solved problems (Excel notation) — Stock price model μ_lnX = 5, σ_lnX = 0.40")
    M_, S_ = 5.0, 0.40
    rv = stats.lognorm(s=S_, scale=math.exp(M_))
    prob_card(1, "E[X] = exp(μ + σ²/2)",
              "Mean of a Log-Normal.", f"=EXP({M_}+{S_}^2/2)",
              f"<b>{math.exp(M_+S_**2/2):.4f}</b>")
    prob_card(2, "Var(X) = (exp(σ²)−1)·exp(2μ+σ²)",
              "Variance closed form.",
              f"=(EXP({S_}^2)-1)*EXP(2*{M_}+{S_}^2)",
              f"<b>{(math.exp(S_**2)-1)*math.exp(2*M_+S_**2):.4f}</b>")
    prob_card(3, "Median = exp(μ)",
              "Median is below the mean (right-skew).",
              f"=EXP({M_})", f"<b>{math.exp(M_):.4f}</b>")
    prob_card(4, "Mode = exp(μ − σ²)",
              "Mode is below the median.",
              f"=EXP({M_}-{S_}^2)", f"<b>{math.exp(M_-S_**2):.4f}</b>")
    prob_card(5, "P(X ≤ 200)",
              "Probability price stays under 200.",
              f"=LOGNORM.DIST(200,{M_},{S_},TRUE)",
              f"<b>{rv.cdf(200):.6f}</b>")
    prob_card(6, "P(X ≥ 150)",
              "Right-tail probability.",
              f"=1 - LOGNORM.DIST(150,{M_},{S_},TRUE)",
              f"<b>{1-rv.cdf(150):.6f}</b>")
    prob_card(7, "95th percentile",
              "Inverse CDF.", f"=LOGNORM.INV(0.95,{M_},{S_})",
              f"<b>{rv.ppf(0.95):.4f}</b>")
    prob_card(8, "Black-Scholes call PV factor",
              "Risk-neutral price-implied probability that S_T &gt; K = 150 "
              "(use μ = ln S₀ + (r − σ²/2)T for risk-neutral).",
              f"=1 - LOGNORM.DIST(150,{M_},{S_},TRUE)",
              f"≈ <b>{1-rv.cdf(150):.6f}</b> (illustrative; substitute risk-neutral μ in practice)")
    prob_card(9, "Simulate one terminal price",
              "Direct Log-Normal simulator.",
              f"=LOGNORM.INV(RAND(),{M_},{S_})",
              "Returns a positive number with the right Log-Normal shape.")
    prob_card(10, "GBM terminal price (S₀=100, r=5%, σ=20%, T=1)",
              "Standard Black-Scholes terminal price simulator.",
              "=100 * EXP((0.05-0.5*0.20^2)*1 + 0.20*SQRT(1)*NORM.S.INV(RAND()))",
              "Returns one realisation of S_T; average ≈ S₀·exp(rT) = 105.13.")


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

    # ---- 10 SOLVED PROBLEMS ------------------------------------------------
    section("10 Solved problems (Excel notation) — λ values vary; credit-hazard examples")
    rv_05 = stats.expon(scale=1/0.5)
    prob_card(1, "λ = 0.5/yr: P(X < 2)",
              "Probability event arrives within 2 years.",
              "=EXPON.DIST(2,0.5,TRUE)", f"<b>{rv_05.cdf(2):.6f}</b>")
    prob_card(2, "λ = 0.5/yr: Mean = 1/λ",
              "Expected waiting time.", "=1/0.5", "<b>2 years</b>")
    prob_card(3, "λ = 0.5/yr: P(X > 3)",
              "Survival past 3 years.",
              "=1 - EXPON.DIST(3,0.5,TRUE)", f"<b>{1-rv_05.cdf(3):.6f}</b>")
    prob_card(4, "λ = 0.5/yr: Median = ln(2)/λ",
              "Time by which P(X ≤ t) = 0.5.",
              "=LN(2)/0.5", f"<b>{math.log(2)/0.5:.4f}</b>")
    prob_card(5, "Credit hazard λ = 0.03: 5-year survival",
              "Reduced-form credit risk.",
              "=1 - EXPON.DIST(5,0.03,TRUE)",
              f"<b>{math.exp(-5*0.03):.6f}</b>")
    prob_card(6, "λ = 0.03: 1-year PD",
              "Default probability over the year.",
              "=EXPON.DIST(1,0.03,TRUE)",
              f"<b>{1-math.exp(-0.03):.6f}</b>")
    prob_card(7, "λ = 1: P(2 < X < 4)",
              "Probability event occurs between t=2 and t=4.",
              "=EXPON.DIST(4,1,TRUE) - EXPON.DIST(2,1,TRUE)",
              f"<b>{stats.expon.cdf(4,scale=1) - stats.expon.cdf(2,scale=1):.6f}</b>")
    prob_card(8, "λ = 2: variance = 1/λ²",
              "Variance closed form.", "=1/2^2", "<b>0.25</b>")
    prob_card(9, "λ = 0.1: 90th percentile",
              "Quantile at α=0.9.",
              "=-LN(1-0.9)/0.1", f"<b>{-math.log(1-0.9)/0.1:.4f}</b>")
    prob_card(10, "Simulate one Exponential(0.5) draw",
              "Inverse-CDF Monte Carlo.",
              "=-LN(1-RAND())/0.5",
              "Returns a positive number; long-run mean = 2.")


# ============================================================================
# PAGE: TRIANGULAR
# ============================================================================
def page_triangular():
    page_title(
        "Triangular Distribution",
        "Expert-elicited min / mode / max — the workhorse of project finance, cost modelling, and scenario analysis",
    )

    # ---- DEFINITION ---------------------------------------------------------
    defn_box(
        "TRIANGULAR(a, c, b)  —  a ≤ c ≤ b",
        "A continuous distribution on [a, b] whose density rises linearly to a peak at "
        "the <b>mode</b> c and then falls linearly to zero at b. Used when only three "
        "pieces of information are available: a <i>pessimistic</i> minimum (a), a "
        "<i>most-likely</i> value (c), and an <i>optimistic</i> maximum (b)."
        "<br><br>"
        "<b>PDF</b>:&nbsp; "
        "f(x) = 2(x−a) / [(b−a)(c−a)] &nbsp; for a ≤ x ≤ c<br>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "
        "f(x) = 2(b−x) / [(b−a)(b−c)] &nbsp; for c &lt; x ≤ b<br>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0 otherwise"
        "<br><br>"
        "<b>CDF</b>:&nbsp; "
        "F(x) = (x−a)² / [(b−a)(c−a)] &nbsp; for a ≤ x ≤ c<br>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "
        "F(x) = 1 − (b−x)² / [(b−a)(b−c)] &nbsp; for c &lt; x ≤ b"
        "<br><br>"
        "<b>Mean</b> = (a + b + c) / 3 &nbsp;&nbsp;&nbsp; "
        "<b>Variance</b> = (a² + b² + c² − ab − ac − bc) / 18 &nbsp;&nbsp;&nbsp; "
        "<b>Mode</b> = c",
    )

    # ---- PARAMETER INPUTS ---------------------------------------------------
    c1, c2, c3 = st.columns(3)
    with c1:
        a = st.number_input("a — minimum (pessimistic)", -1000.0, 1000.0, 0.0, 0.5)
    with c2:
        c = st.number_input("c — mode (most likely)",    -1000.0, 1000.0, 3.0, 0.5)
    with c3:
        b = st.number_input("b — maximum (optimistic)",  -1000.0, 1000.0, 10.0, 0.5)

    if not (a <= c <= b) or a == b:
        st.error("Parameters must satisfy a ≤ c ≤ b and a < b."); return

    # scipy parameterisation: shape = (c-a)/(b-a), loc=a, scale=b-a
    shape = (c - a) / (b - a)
    rv = stats.triang(shape, loc=a, scale=(b - a))

    # Grid
    pad = 0.1 * (b - a)
    x = np.linspace(a - pad, b + pad, 500)
    pdf = rv.pdf(x)
    cdf = rv.cdf(x)

    # ---- SUMMARY STATS ------------------------------------------------------
    mean_ = (a + b + c) / 3.0
    var_  = (a**2 + b**2 + c**2 - a*b - a*c - b*c) / 18.0
    sd_   = math.sqrt(var_) if var_ > 0 else 0.0
    # median (closed form)
    if c >= (a + b) / 2:
        median_ = a + math.sqrt((b - a) * (c - a) / 2.0)
    else:
        median_ = b - math.sqrt((b - a) * (b - c) / 2.0)
    # skewness (closed form)
    denom = (a**2 + b**2 + c**2 - a*b - a*c - b*c) ** 1.5
    skew_ = (math.sqrt(2) * (a + b - 2*c) * (2*a - b - c) * (a - 2*b + c)) / (5 * denom) if denom > 0 else 0.0

    stat_chip_row([
        ("Mean", f"{mean_:.4f}"),
        ("Median", f"{median_:.4f}"),
        ("Mode", f"{c:.4f}"),
        ("Variance", f"{var_:.4f}"),
        ("Std Dev", f"{sd_:.4f}"),
        ("Skewness", f"{skew_:.4f}"),
        ("Range", f"[{a}, {b}]"),
    ])

    # ---- PROBABILITY QUERY / SHADED REGION ---------------------------------
    section("Probability query — shade a region")
    qmode = st.selectbox(
        "Region",
        ["None", "P(X ≤ q)", "P(X ≥ q)", "P(q₁ ≤ X ≤ q₂)", "Inverse CDF  —  given α, find q"],
    )
    fill_range = None
    if qmode == "P(X ≤ q)":
        q = st.slider("q", float(a), float(b), float(c), step=(b - a) / 200)
        fill_range = (x.min(), q)
        st.metric("P(X ≤ q)", f"{rv.cdf(q):.6f}")
    elif qmode == "P(X ≥ q)":
        q = st.slider("q", float(a), float(b), float(c), step=(b - a) / 200)
        fill_range = (q, x.max())
        st.metric("P(X ≥ q)", f"{1 - rv.cdf(q):.6f}")
    elif qmode == "P(q₁ ≤ X ≤ q₂)":
        cc1, cc2 = st.columns(2)
        with cc1:
            q1 = st.slider("q₁", float(a), float(b), float(a + 0.25*(b-a)), step=(b - a) / 200)
        with cc2:
            q2 = st.slider("q₂", float(a), float(b), float(a + 0.75*(b-a)), step=(b - a) / 200)
        if q2 > q1:
            fill_range = (q1, q2)
            st.metric("P(q₁ ≤ X ≤ q₂)", f"{rv.cdf(q2) - rv.cdf(q1):.6f}")
    elif qmode == "Inverse CDF  —  given α, find q":
        alpha = st.slider("α (probability)", 0.001, 0.999, 0.5, 0.001)
        q_alpha = rv.ppf(alpha)
        st.metric(f"q such that F(q) = {alpha:.3f}", f"{q_alpha:.6f}")
        fill_range = (x.min(), q_alpha)

    # ---- PLOTS --------------------------------------------------------------
    show_continuous_plots(
        x, pdf, cdf,
        f"Triangular(a={a}, c={c}, b={b}) PDF",
        f"Triangular(a={a}, c={c}, b={b}) CDF",
        fill_range,
    )

    # ---- KEY PROPERTIES -----------------------------------------------------
    section("Key properties")
    sum_box(
        "• <b>Support</b>: bounded on [a, b] — unlike Normal or Log-Normal, no infinite tails.<br>"
        "• <b>Unimodal & continuous</b>; the density is piecewise-linear (two straight lines meeting at c).<br>"
        "• <b>Peak density</b> at the mode: f(c) = 2 / (b − a).<br>"
        "• <b>Symmetric</b> when c = (a + b)/2 (skew = 0); <b>right-skewed</b> when c is near a, <b>left-skewed</b> when c is near b.<br>"
        "• <b>F(c)</b> = (c − a) / (b − a) — this threshold drives the inverse-CDF branch used in Monte Carlo.<br>"
        "• <b>Inverse CDF</b>:<br>"
        "&nbsp;&nbsp;&nbsp;q(u) = a + √(u · (b−a)(c−a)) &nbsp;&nbsp; for &nbsp; u ≤ (c−a)/(b−a)<br>"
        "&nbsp;&nbsp;&nbsp;q(u) = b − √((1−u) · (b−a)(b−c)) &nbsp;&nbsp; for &nbsp; u &gt; (c−a)/(b−a)"
    )

    # ---- EXCEL NOTATION -----------------------------------------------------
    xl_box(
        "EXCEL NOTATION  (no native TRIANG.DIST — use IF formulas)",
        f"<b>PDF</b>:<br>"
        f"<code>=IF(AND(x&gt;={a},x&lt;={c}), 2*(x-{a})/(({b}-{a})*({c}-{a})), "
        f"IF(AND(x&gt;{c},x&lt;={b}), 2*({b}-x)/(({b}-{a})*({b}-{c})), 0))</code>"
        f"<br><br><b>CDF</b>:<br>"
        f"<code>=IF(x&lt;{a},0, IF(x&lt;={c}, (x-{a})^2/(({b}-{a})*({c}-{a})), "
        f"IF(x&lt;={b}, 1-({b}-x)^2/(({b}-{a})*({b}-{c})), 1)))</code>"
        f"<br><br><b>Mean</b>: <code>=({a}+{b}+{c})/3</code>"
        f"<br><b>Variance</b>: <code>=({a}^2+{b}^2+{c}^2-{a}*{b}-{a}*{c}-{b}*{c})/18</code>"
        f"<br><b>Std Dev</b>: <code>=SQRT(({a}^2+{b}^2+{c}^2-{a}*{b}-{a}*{c}-{b}*{c})/18)</code>"
        f"<br><b>Peak density f(c)</b>: <code>=2/({b}-{a})</code>"
        f"<br><b>Threshold F(c)</b>: <code>=({c}-{a})/({b}-{a})</code>"
        f"<br><br><b>Inverse CDF (quantile at α)</b>:<br>"
        f"<code>=IF(α&lt;=({c}-{a})/({b}-{a}), "
        f"{a}+SQRT(α*({b}-{a})*({c}-{a})), "
        f"{b}-SQRT((1-α)*({b}-{a})*({b}-{c})))</code>"
        f"<br><br><b>Monte-Carlo simulate one draw</b>  (one RAND call via LET):<br>"
        f"<code>=LET(u,RAND(), t,({c}-{a})/({b}-{a}), "
        f"IF(u&lt;=t, {a}+SQRT(u*({b}-{a})*({c}-{a})), "
        f"{b}-SQRT((1-u)*({b}-{a})*({b}-{c}))))</code>"
        f"<br><b>PERT-style mean approximation</b>: <code>=({a}+4*{c}+{b})/6</code>  "
        f"<i>(used in @Risk / Crystal Ball project models — not exact here but popular)</i>",
    )

    # ---- FINANCE ILLUSTRATION ----------------------------------------------
    ex_box(
        "FINANCE ILLUSTRATION — Project cost estimation",
        f"A project sponsor elicits from engineers: <b>pessimistic</b> cost a = {a}, "
        f"<b>most-likely</b> c = {c}, <b>optimistic</b> b = {b} (₹ crore). "
        f"Under a triangular model:<br>"
        f"• Expected cost E[X] = (a + b + c)/3 = <b>{mean_:.2f}</b>"
        f"<br>• Std dev = <b>{sd_:.2f}</b> (uncertainty band)"
        f"<br>• P(cost ≤ c) = <b>{rv.cdf(c):.4f}</b> — probability the project comes in at or below the most-likely estimate"
        f"<br>• P(cost &gt; {c + 0.25*(b-c):.1f}) = <b>{1 - rv.cdf(c + 0.25*(b-c)):.4f}</b> — right-tail overrun risk"
        f"<br>• 95th-percentile cost = <b>{rv.ppf(0.95):.2f}</b> — a VaR-style reserve for contingency budgeting."
    )

    # ---- 10 SOLVED PROBLEMS -------------------------------------------------
    section("10 Solved problems (Excel notation)")

    # Fixed parameters for the practice set — independent of slider so answers are stable
    A, C, B = 10, 15, 30  # ₹ crore project cost example
    rvP = stats.triang((C - A) / (B - A), loc=A, scale=(B - A))

    prob_card(
        1, "Expected value",
        f"Cost estimates a={A}, c={C}, b={B} (₹ crore). Find E[X].",
        f"=({A}+{B}+{C})/3",
        f"E[X] = <b>{(A+B+C)/3:.4f}</b> ₹ crore",
    )
    prob_card(
        2, "Variance & standard deviation",
        "Using the same a, c, b, find Var(X) and σ.",
        f"=({A}^2+{B}^2+{C}^2-{A}*{B}-{A}*{C}-{B}*{C})/18",
        f"Var = <b>{(A**2+B**2+C**2-A*B-A*C-B*C)/18:.4f}</b>, σ = <b>{math.sqrt((A**2+B**2+C**2-A*B-A*C-B*C)/18):.4f}</b>",
    )
    prob_card(
        3, "Peak density",
        "Height of the PDF at the mode c.",
        f"=2/({B}-{A})",
        f"f(c) = <b>{2/(B-A):.4f}</b>",
    )
    prob_card(
        4, "P(X ≤ 18)",
        "Probability that cost does not exceed ₹18 crore.",
        f"=IF(18&lt;={C}, (18-{A})^2/(({B}-{A})*({C}-{A})), 1-({B}-18)^2/(({B}-{A})*({B}-{C})))",
        f"F(18) = <b>{rvP.cdf(18):.6f}</b>",
    )
    prob_card(
        5, "P(12 ≤ X ≤ 25)",
        "Probability cost falls inside a mid-range band.",
        f"=F(25) - F(12)  (evaluate each using the CDF IF formula)",
        f"P(12 ≤ X ≤ 25) = F(25) − F(12) = <b>{rvP.cdf(25) - rvP.cdf(12):.6f}</b>",
    )
    prob_card(
        6, "P(X > 22) — cost overrun risk",
        "Right-tail probability of exceeding ₹22 crore.",
        f"=1 - IF(22&lt;={C}, (22-{A})^2/(({B}-{A})*({C}-{A})), 1-({B}-22)^2/(({B}-{A})*({B}-{C})))",
        f"P(X &gt; 22) = <b>{1 - rvP.cdf(22):.6f}</b>",
    )
    prob_card(
        7, "Median",
        "Because c < (a+b)/2 = 20, median is in the upper branch.",
        f"={B}-SQRT(({B}-{A})*({B}-{C})/2)",
        f"Median = <b>{B - math.sqrt((B-A)*(B-C)/2):.4f}</b>",
    )
    prob_card(
        8, "95th-percentile (contingency reserve)",
        "Find q such that F(q) = 0.95. Check which branch.",
        f"=IF(0.95&lt;=({C}-{A})/({B}-{A}), {A}+SQRT(0.95*({B}-{A})*({C}-{A})), "
        f"{B}-SQRT(0.05*({B}-{A})*({B}-{C})))",
        f"q₀.₉₅ = <b>{rvP.ppf(0.95):.4f}</b>",
    )
    prob_card(
        9, "Simulate one Monte-Carlo cost path",
        "One realisation via inverse-CDF with a single RAND() call.",
        f"=LET(u,RAND(), t,({C}-{A})/({B}-{A}), "
        f"IF(u&lt;=t, {A}+SQRT(u*({B}-{A})*({C}-{A})), "
        f"{B}-SQRT((1-u)*({B}-{A})*({B}-{C}))))",
        "Copy down ≥10,000 rows → empirical mean ≈ 18.33, empirical 95% ≈ 25.5.",
    )
    prob_card(
        10, "PERT vs Triangular mean",
        "Compare Triangular mean with PERT approximation (a + 4c + b)/6.",
        f"Tri: =({A}+{B}+{C})/3    |    PERT: =({A}+4*{C}+{B})/6",
        f"Triangular = <b>{(A+B+C)/3:.4f}</b>, PERT = <b>{(A + 4*C + B)/6:.4f}</b> — PERT shifts weight toward the mode.",
    )


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
            ["Triangular(a,c,b)",   "IF-branch on c (see page)",   "IF-branch on c (see page)",   "Branched on α ≤ (c-a)/(b-a)"],
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
            ["Triangular(a,c,b)",   "=LET(u,RAND(),t,(c-a)/(b-a),IF(u<=t,a+SQRT(u*(b-a)*(c-a)),b-SQRT((1-u)*(b-a)*(b-c))))"],
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
    "📈 Continuous: Triangular": page_triangular,
    "💼 Finance Tools (VaR / GBM)": page_finance_tools,
    "🧠 Practice Quiz": page_quiz,
    "📋 Excel Master Cheat Sheet": page_cheat_sheet,
}

PAGES[page]()

footer()
