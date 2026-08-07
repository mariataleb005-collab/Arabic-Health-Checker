from html import escape
from pathlib import Path
import base64
from textwrap import dedent

import streamlit as st

def image_to_base64(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def render_html(content: str) -> None:
    """Render raw HTML without Markdown interpretation."""
    st.html(dedent(content).strip())


VERDICT_META = {
    "مؤكد صحيح": {
        "class": "verdict-correct",
        "icon": "✓",
        "label": "مؤكد صحيح",
    },
    "مؤكد خاطئ": {
        "class": "verdict-wrong",
        "icon": "×",
        "label": "مؤكد خاطئ",
    },
    "صحيح جزئيًا": {
        "class": "verdict-partial",
        "icon": "≈",
        "label": "صحيح جزئيًا",
    },
    "معلومات غير كافية": {
        "class": "verdict-unknown",
        "icon": "?",
        "label": "معلومات غير كافية",
    },
}

RISK_META = {
    "منخفض": {
        "class": "risk-low",
        "label": "خطورة منخفضة",
    },
    "متوسط": {
        "class": "risk-medium",
        "label": "خطورة متوسطة",
    },
    "عالي": {
        "class": "risk-high",
        "label": "خطورة عالية",
    },
}


def brand_header(compact: bool = False) -> None:
    compact_class = " brand-compact" if compact else ""

    logo_path = Path("assets/bayyinah_logo.png")
    logo_base64 = image_to_base64(str(logo_path))

    render_html(
        f"""
        <header class="brand-row{compact_class}">
            <div class="brand-lockup">

                <img
                    src="data:image/png;base64,{logo_base64}"
                    class="brand-logo-image"
                    alt="Bayyinah logo"
                >

                <div class="brand-copy">
                    <div class="brand-name">بَيِّنة</div>
                    <div class="brand-subtitle">BAYYINAH HEALTH</div>
                </div>

            </div>

            <div class="brand-trust">
                <span class="brand-trust-dot"></span>
                مدعوم بمصادر صحية موثوقة
            </div>
        </header>
        """
    )


def trust_strip() -> None:
    render_html(
        """
        <div class="trust-strip">
            <span class="trust-title">مصادر المعرفة</span>
            <span class="trust-item">WHO EMRO</span>
            <span class="trust-divider"></span>
            <span class="trust-item">UAE MOHAP</span>
            <span class="trust-divider"></span>
            <span class="trust-item">RAG + AI</span>
        </div>
        """
    )


def section_intro(eyebrow: str, title: str, description: str) -> None:
    render_html(
        f"""
        <div class="checker-intro">
            <div class="mini-label">{escape(eyebrow)}</div>
            <h1>{escape(title)}</h1>
            <p>{escape(description)}</p>
        </div>
        """
    )


def _friendly_source_name(filename: str) -> str:
    stem = Path(filename).stem
    cleaned = stem.replace("_", " ").replace("-", " ").strip()
    return cleaned or filename


def _render_source_chips(sources: list[str]) -> str:
    if not sources:
        return """
        <div class="no-source-note">
            <span>ℹ</span>
            لم يُستخدم مصدر لأن الدليل المتاح لم يكن كافيًا أو مرتبطًا بما يكفي بهذا الادعاء.
        </div>
        """

    chips = "".join(
        (
            '<span class="source-chip">'
            '<span class="source-doc">↗</span>'
            f'{escape(_friendly_source_name(source))}'
            '</span>'
        )
        for source in sources
    )

    return (
        '<div class="sources-block">'
        '<div class="sources-title">المصادر المستخدمة</div>'
        f'<div class="source-chips">{chips}</div>'
        '</div>'
    )


def render_results(results: list[dict]) -> None:
    render_html(
        f"""
        <div class="results-heading">
            <div>
                <span class="mini-label">النتائج</span>
                <h2>تم تحليل {len(results)} ادعاء</h2>
            </div>
            <div class="results-count">{len(results):02d}</div>
        </div>
        """
    )

    if not results:
        st.warning("لم نتمكن من استخراج ادعاء صحي واضح من المحتوى المرسل.")
        return

    for index, item in enumerate(results, start=1):
        claim = escape(str(item.get("claim", "")).strip())
        verdict_data = item.get("verdict") or {}

        verdict = str(verdict_data.get("verdict", "معلومات غير كافية"))
        explanation = escape(str(verdict_data.get("explanation", "")).strip())
        risk = str(verdict_data.get("risk_level", "منخفض"))
        sources = verdict_data.get("sources_used") or []

        verdict_meta = VERDICT_META.get(
            verdict,
            VERDICT_META["معلومات غير كافية"],
        )
        risk_meta = RISK_META.get(
            risk,
            {
                "class": "risk-low",
                "label": f"الخطورة: {escape(risk)}",
            },
        )

        sources_html = _render_source_chips([str(source) for source in sources])

        render_html(
            f"""
            <article class="result-card">
                <div class="result-topline">
                    <span class="claim-index">الادعاء {index:02d}</span>

                    <div class="badge-group">
                        <span class="badge {verdict_meta['class']}">
                            <span>{verdict_meta['icon']}</span>
                            {verdict_meta['label']}
                        </span>

                        <span class="badge {risk_meta['class']}">
                            {risk_meta['label']}
                        </span>
                    </div>
                </div>

                <h3 class="claim-text">{claim}</h3>

                <div class="explanation-block">
                    <div class="explanation-label">التوضيح</div>
                    <p>{explanation}</p>
                </div>

                {sources_html}
            </article>
            """
        )


def empty_state(message: str) -> None:
    render_html(
        f"""
        <div class="empty-state">
            <div class="empty-icon">✦</div>
            <strong>جاهز للتحقق</strong>
            <span>{escape(message)}</span>
        </div>
        """
    )
