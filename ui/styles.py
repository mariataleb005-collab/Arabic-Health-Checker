from textwrap import dedent

import streamlit as st


GLOBAL_CSS = r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;600;700;800&display=swap');

:root {
    --ink: #102724;
    --muted: #647773;
    --teal-950: #062f2c;
    --teal-900: #073c38;
    --teal-800: #0a4f49;
    --teal-700: #0b665d;
    --teal-600: #0b7a6c;
    --mint-50: #eef9f6;
    --surface: #ffffff;
    --line: #dfe9e5;

    --green: #16785e;
    --green-bg: #e7f5ef;
    --red: #b13c43;
    --red-bg: #faecee;
    --orange: #a86114;
    --orange-bg: #fff3df;
    --gray: #66726f;
    --gray-bg: #eef1f0;
}

html,
body,
.stApp,
[data-testid="stAppViewContainer"] {
    direction: rtl;
    font-family: "Tajawal", "Segoe UI", Tahoma, sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 80% 0%, rgba(161, 218, 200, .16), transparent 28%),
        linear-gradient(180deg, #fbfcf9 0%, #f7faf8 100%);
    color: var(--ink);
}

# .block-container {
#     max-width: 1180px;
#     padding-top: 1.15rem;
#     padding-bottom: 4rem;
# }
.block-container {
    padding-top: 0.75rem !important;
}

#MainMenu,
footer,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
[data-testid="manage-app-button"] {
    display: none !important;
}

# header[data-testid="stHeader"] {
#     background: rgba(251, 252, 249, .90);
#     backdrop-filter: blur(14px);
#     border-bottom: 1px solid rgba(10, 79, 73, .07);
# }

header[data-testid="stHeader"] {
    display: none !important;
}

# [data-testid="stNavigation"] {
#     direction: rtl;
# }

[data-testid="stMainBlockContainer"] {
    padding-top: 0.75rem !important;
}

[data-testid="stNavigation"] a,
[data-testid="stNavigation"] button {
    font-family: "Tajawal", sans-serif !important;
    font-weight: 700 !important;
}

.brand-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 24px;
    margin: 1.25rem 0 4.6rem;
}

.brand-compact {
    margin-bottom: 2.6rem;
}

.brand-lockup {
    display: flex;
    align-items: center;
    gap: 12px;
}

# .brand-mark {
#     position: relative;
#     width: 46px;
#     height: 46px;
#     border-radius: 15px;
#     background: var(--teal-900);
#     display: grid;
#     place-items: center;
#     box-shadow: 0 10px 25px rgba(7, 60, 56, .18);
# }

# .brand-check {
#     color: white;
#     font-size: 22px;
#     font-weight: 800;
# }

# .brand-pulse {
#     position: absolute;
#     width: 12px;
#     height: 12px;
#     background: #8bd5bb;
#     border: 3px solid var(--teal-900);
#     border-radius: 50%;
#     left: -3px;
#     top: -3px;
# }

.brand-copy {
    line-height: 1;
}

.brand-logo-image {
    width: 68px;
    height: 68px;
    object-fit: cover;
    border-radius: 50%;
    display: block;
    box-shadow: 0 10px 26px rgba(7, 60, 56, .18);
}

.brand-name {
    font-size: 1.45rem;
    font-weight: 800;
    color: var(--teal-950);
}

.brand-subtitle {
    font-size: .58rem;
    letter-spacing: .15em;
    color: #7b8d89;
    margin-top: 6px;
    direction: ltr;
    text-align: right;
    font-weight: 700;
}

.brand-trust {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    color: #60736f;
    font-size: .82rem;
    font-weight: 600;
    background: rgba(255, 255, 255, .74);
    border: 1px solid #e3ebe8;
    border-radius: 999px;
    padding: 8px 12px;
}

.brand-trust-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #25a47d;
    box-shadow: 0 0 0 4px rgba(37, 164, 125, .10);
}

.hero {
    max-width: 860px;
    margin: 0 auto;
    text-align: center;
}

.hero-eyebrow,
.mini-label {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    color: var(--teal-700);
    font-size: .78rem;
    font-weight: 800;
}

.hero-eyebrow {
    background: var(--mint-50);
    border: 1px solid #d9eee7;
    border-radius: 999px;
    padding: 8px 12px;
}

.status-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #1e9c76;
}

.hero h1 {
    font-size: clamp(2.75rem, 6vw, 5.2rem);
    line-height: 1.13;
    color: var(--teal-950);
    margin: 1.35rem auto 1.2rem;
    letter-spacing: -.035em;
    font-weight: 800;
}

.hero h1 span {
    color: var(--teal-600);
}

.hero-copy {
    max-width: 720px;
    margin: 0 auto 2rem;
    color: var(--muted);
    font-size: 1.13rem;
    line-height: 2;
}

div.stButton > button {
    min-height: 50px;
    border-radius: 14px;
    font-family: "Tajawal", sans-serif;
    font-size: .98rem;
    font-weight: 700;
}

div.stButton > button[kind="primary"] {
    background: var(--teal-900);
    border: 1px solid var(--teal-900);
    box-shadow: 0 9px 25px rgba(7, 60, 56, .15);
}

div.stButton > button[kind="primary"]:hover {
    background: var(--teal-800);
    border-color: var(--teal-800);
}

.hero-note {
    color: #71817e;
    font-size: .83rem;
    line-height: 1.7;
    padding-right: 8px;
}

.trust-strip {
    margin: 3.8rem 0 6rem;
    min-height: 62px;
    border-top: 1px solid var(--line);
    border-bottom: 1px solid var(--line);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 22px;
    color: #6b7d79;
}

.trust-title {
    font-size: .72rem;
    color: #9aa7a4;
}

.trust-item {
    font-size: .77rem;
    font-weight: 800;
    direction: ltr;
}

.trust-divider {
    width: 4px;
    height: 4px;
    background: #b9c7c3;
    border-radius: 50%;
}

.section-heading {
    max-width: 730px;
    margin-bottom: 2.3rem;
}

.section-heading > span {
    color: var(--teal-700);
    font-size: .78rem;
    font-weight: 800;
}

.section-heading h2,
.source-section h2,
.checker-intro h1 {
    color: var(--teal-950);
    font-weight: 800;
    letter-spacing: -.025em;
}

.section-heading h2 {
    margin: .65rem 0 .6rem;
    font-size: 2.2rem;
}

.section-heading p,
.source-section p,
.checker-intro p {
    color: var(--muted);
    line-height: 1.9;
}

.step-card {
    min-height: 260px;
    border: 1px solid var(--line);
    border-radius: 22px;
    padding: 27px;
    background: rgba(255,255,255,.86);
    box-shadow: 0 12px 35px rgba(15, 66, 61, .045);
}

.step-number {
    color: #9ab0aa;
    font-size: .72rem;
    font-weight: 800;
}

.step-icon {
    width: 42px;
    height: 42px;
    display: grid;
    place-items: center;
    background: var(--mint-50);
    color: var(--teal-700);
    border: 1px solid #dbede7;
    border-radius: 13px;
    margin: 27px 0 20px;
    font-size: 1.1rem;
    font-weight: 800;
}

.step-card h3 {
    margin: 0 0 10px;
    font-size: 1.14rem;
    color: var(--teal-950);
}

.step-card p {
    color: #6d7e7a;
    line-height: 1.8;
    font-size: .92rem;
}

.source-section {
    margin: 6rem 0 1rem;
    padding: 36px 38px;
    border-radius: 24px;
    background: var(--teal-950);
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 50px;
    align-items: center;
}

.source-section .mini-label {
    color: #93d6c1;
}

.source-section h2 {
    color: white;
    margin: .6rem 0 0;
    font-size: 1.8rem;
}

.source-section p {
    color: #c0d2ce;
    margin: 0;
}

.checker-intro {
    max-width: 760px;
    margin-bottom: 2.2rem;
}

.checker-intro h1 {
    margin: .6rem 0 .75rem;
    font-size: clamp(2rem, 4vw, 3.25rem);
}

.checker-intro p {
    max-width: 650px;
}

[data-testid="stTabs"] {
    direction: rtl;
}

[data-testid="stTabs"] [data-baseweb="tab-list"] {
    gap: 8px;
    background: #eef5f2;
    padding: 6px;
    border-radius: 14px;
    width: fit-content;
    margin-bottom: 1.2rem;
}

[data-testid="stTabs"] [data-baseweb="tab"] {
    border-radius: 10px;
    min-width: 165px;
    font-family: "Tajawal", sans-serif;
    font-weight: 700;
    color: #60736f;
}

[data-testid="stTabs"] [aria-selected="true"] {
    background: white;
    color: var(--teal-900);
}

[data-testid="stTextArea"] textarea {
    direction: rtl;
    text-align: right;
    border-radius: 16px;
    border: 1px solid #dce7e3;
    background: white;
    padding: 18px;
    line-height: 1.8;
    font-family: "Tajawal", sans-serif;
    font-size: 1rem;
}

.input-meta {
    color: #97a5a1;
    font-size: .74rem;
    margin: 0 3px 12px;
}

[data-testid="stFileUploader"] {
    direction: rtl;
}

.file-chip {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    margin: 10px 0 14px;
    background: var(--mint-50);
    border: 1px solid #d9ebe5;
    border-radius: 12px;
    padding: 9px 12px;
    color: var(--teal-900);
}

.file-chip-icon {
    width: 30px;
    height: 30px;
    display: grid;
    place-items: center;
    border-radius: 9px;
    background: white;
}

.file-chip span:last-child {
    display: flex;
    flex-direction: column;
}

.file-chip small {
    color: #7f918c;
    font-size: .68rem;
    margin-top: 2px;
    direction: ltr;
    text-align: right;
}

.results-heading {
    margin: 3.2rem 0 1.2rem;
    display: flex;
    justify-content: space-between;
    align-items: end;
}

.results-heading h2 {
    margin: .4rem 0 0;
    color: var(--teal-950);
    font-size: 1.65rem;
}

.results-count {
    color: #b7c9c4;
    font-size: 2rem;
    font-weight: 800;
}

.result-card {
    background: white;
    border: 1px solid var(--line);
    border-radius: 22px;
    padding: 24px 26px;
    margin-bottom: 18px;
    box-shadow: 0 10px 30px rgba(14, 70, 64, .055);
}

.result-topline {
    display: flex;
    gap: 16px;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
}

.claim-index {
    color: #8b9a96;
    font-size: .72rem;
    font-weight: 800;
}

.badge-group {
    display: flex;
    gap: 7px;
    flex-wrap: wrap;
}

.badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 10px;
    border-radius: 999px;
    font-size: .72rem;
    font-weight: 800;
    border: 1px solid transparent;
}

.verdict-correct {
    color: var(--green);
    background: var(--green-bg);
}

.verdict-wrong {
    color: var(--red);
    background: var(--red-bg);
}

.verdict-partial {
    color: var(--orange);
    background: var(--orange-bg);
}

.verdict-unknown {
    color: var(--gray);
    background: var(--gray-bg);
}

.risk-low {
    color: #25745f;
    background: #eef8f4;
}

.risk-medium {
    color: #9b641b;
    background: #fff7e9;
}

.risk-high {
    color: #a53a41;
    background: #fff0f1;
}

.claim-text {
    color: var(--teal-950);
    font-size: 1.22rem;
    line-height: 1.8;
    margin: 22px 0 19px;
    font-weight: 700;
}

.explanation-block {
    background: #f8faf9;
    border-right: 3px solid #c3ddd5;
    border-radius: 12px;
    padding: 14px 16px;
}

.explanation-label,
.sources-title {
    color: #81918d;
    font-size: .69rem;
    font-weight: 800;
    margin-bottom: 6px;
}

.explanation-block p {
    margin: 0;
    color: #455b56;
    line-height: 1.85;
    font-size: .94rem;
}

.sources-block {
    margin-top: 18px;
}

.source-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.source-chip {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    border: 1px solid #dfe8e5;
    color: #58706a;
    border-radius: 9px;
    padding: 7px 9px;
    font-size: .72rem;
    background: #fcfdfc;
}

.source-doc {
    color: var(--teal-600);
    font-weight: 800;
}

.no-source-note {
    display: flex;
    align-items: flex-start;
    gap: 8px;
    margin-top: 18px;
    color: #7f8e8a;
    font-size: .78rem;
    line-height: 1.7;
}

.empty-state {
    margin: 2rem 0 1rem;
    min-height: 170px;
    border: 1px dashed #cbdad6;
    border-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 5px;
    color: #8a9a96;
    background: rgba(255,255,255,.42);
    text-align: center;
}

.empty-state strong {
    color: #657a75;
    font-size: .92rem;
}

.empty-state span {
    font-size: .78rem;
}

.empty-icon {
    width: 38px;
    height: 38px;
    border-radius: 12px;
    background: var(--mint-50);
    color: var(--teal-700);
    display: grid;
    place-items: center;
    margin-bottom: 5px;
}

.medical-disclaimer {
    margin-top: 3rem;
    padding: 16px 18px;
    border-radius: 14px;
    background: #f5f7f6;
    color: #70807c;
    font-size: .76rem;
    line-height: 1.8;
    border: 1px solid #e5eae8;
}

[data-testid="stSpinner"],
[data-testid="stAlert"] {
    direction: rtl;
    text-align: right;
}

@media (max-width: 760px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .brand-trust {
        display: none;
    }

    .hero h1 {
        font-size: 2.55rem;
    }

    .trust-strip {
        gap: 11px;
        margin: 2.8rem 0 4rem;
        overflow-x: auto;
        justify-content: flex-start;
    }

    .source-section {
        grid-template-columns: 1fr;
        gap: 22px;
        padding: 28px 24px;
    }

    .result-card {
        padding: 20px;
    }

    .result-topline {
        align-items: flex-start;
        flex-direction: column;
    }
}
</style>
"""


def inject_global_styles() -> None:
    st.html(dedent(GLOBAL_CSS).strip())
