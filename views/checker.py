from pathlib import Path
import tempfile

import streamlit as st

from src.pipeline import check_message, transcribe_voice_note

from ui.components import (
    brand_header,
    empty_state,
    render_html,
    render_results,
    section_intro,
)


brand_header(compact=True)

section_intro(
    eyebrow="أداة التحقق",
    title="ما المعلومة التي تريد التحقق منها؟",
    description=(
        "أرسل نصًا أو ملاحظة صوتية باللغة العربية. "
        "سنفصل الادعاءات الصحية ونقيّم كل واحد منها على حدة."
    ),
)


text_tab, voice_tab = st.tabs(
    [
        "⌨️  لصق نص",
        "🎙️  رفع ملاحظة صوتية",
    ]
)


# =========================================================
# TEXT TAB
# =========================================================

with text_tab:
    with st.container(border=True):

        arabic_text = st.text_area(
            "النص المراد التحقق منه",
            height=190,
            placeholder=(
                "مثال: شرب الماء الدافئ على الريق يعالج السكري، "
                "ولقاح الإنفلونزا يسبب الإنفلونزا."
            ),
            label_visibility="collapsed",
        )

        char_count = len(arabic_text.strip())

        render_html(
            f"""
            <div class="input-meta">
                اكتب الادعاء كما وصل إليك • {char_count} حرف
            </div>
            """
        )

        check_text = st.button(
            "تحقق من النص",
            type="primary",
            use_container_width=True,
            disabled=not arabic_text.strip(),
            key="check_text",
        )

    if check_text:
        try:
            with st.spinner(
                "جارٍ تحليل الادعاءات والبحث في المصادر الطبية..."
            ):
                results = check_message(
                    arabic_text.strip()
                )

            st.session_state["text_results"] = results

        except Exception as exc:
            st.error(
                "تعذّر إكمال التحقق الآن. "
                "يرجى المحاولة مرة أخرى."
            )

            st.caption(
                f"تفاصيل تقنية: {exc}"
            )

    if "text_results" in st.session_state:
        render_results(
            st.session_state["text_results"]
        )

    else:
        empty_state(
            "ستظهر نتائج الادعاءات هنا بعد التحقق."
        )


# =========================================================
# VOICE TAB
# =========================================================

with voice_tab:

    with st.container(border=True):

        uploaded_audio = st.file_uploader(
            "ارفع ملاحظة صوتية",
            type=["mp3", "wav", "m4a"],
            help="الصيغ المدعومة: MP3، WAV، M4A",
            label_visibility="collapsed",
        )

        if uploaded_audio is not None:
            st.audio(uploaded_audio)

            size_mb = (
                uploaded_audio.size
                / (1024 * 1024)
            )

            render_html(
                f"""
                <div class="file-chip">

                    <span class="file-chip-icon">
                        ♪
                    </span>

                    <span>
                        <strong>
                            {uploaded_audio.name}
                        </strong>

                        <small>
                            {size_mb:.1f} MB
                        </small>
                    </span>

                </div>
                """
            )

        transcribe_button = st.button(
            "تحويل الصوت إلى نص",
            type="primary",
            use_container_width=True,
            disabled=uploaded_audio is None,
            key="transcribe_voice",
        )


    # -----------------------------------------------------
    # TRANSCRIBE AUDIO
    # -----------------------------------------------------

    if (
        transcribe_button
        and uploaded_audio is not None
    ):

        suffix = (
            Path(uploaded_audio.name)
            .suffix
            .lower()
            or ".wav"
        )

        temp_path = None

        try:
            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=suffix,
            ) as tmp:

                tmp.write(
                    uploaded_audio.getbuffer()
                )

                temp_path = tmp.name


            with st.spinner(
                "جارٍ تحويل الملاحظة الصوتية إلى نص..."
            ):

                transcription = (
                    transcribe_voice_note(
                        temp_path
                    )
                )


            st.session_state[
                "voice_transcription"
            ] = transcription

            # Remove previous results when a new
            # voice note is processed.
            st.session_state.pop(
                "voice_results",
                None,
            )


        except Exception as exc:

            st.error(
                "تعذّر معالجة الملاحظة الصوتية. "
                "يرجى التأكد من أن الملف بصيغة "
                "MP3 أو WAV أو M4A ثم المحاولة مرة أخرى."
            )

            st.caption(
                f"تفاصيل تقنية: {exc}"
            )


        finally:
            if temp_path:
                Path(
                    temp_path
                ).unlink(
                    missing_ok=True
                )


    # -----------------------------------------------------
    # DISPLAY + EDIT TRANSCRIPTION
    # -----------------------------------------------------

    if "voice_transcription" in st.session_state:

        render_html(
            """
            <div class="transcription-heading">
                <span class="mini-label">
                    النص المستخرج من الصوت
                </span>

                <h3>
                    راجع النص قبل التحقق
                </h3>

                <p>
                    يمكنك تعديل أي كلمة لم يتم تحويلها
                    بشكل صحيح قبل إرسال النص للتحقق.
                </p>
            </div>
            """
        )


        corrected_text = st.text_area(
            "النص المستخرج من الملاحظة الصوتية",
            value=st.session_state[
                "voice_transcription"
            ],
            height=160,
            key="voice_corrected_text",
            label_visibility="collapsed",
        )


        verify_voice_text = st.button(
            "متابعة التحقق",
            type="primary",
            use_container_width=True,
            disabled=not corrected_text.strip(),
            key="verify_voice_text",
        )


        # -------------------------------------------------
        # RUN NORMAL TEXT PIPELINE
        # -------------------------------------------------

        if verify_voice_text:

            try:
                with st.spinner(
                    "جارٍ تحليل الادعاءات "
                    "والبحث في المصادر الطبية..."
                ):

                    results = check_message(
                        corrected_text.strip()
                    )


                st.session_state[
                    "voice_results"
                ] = results


            except Exception as exc:

                st.error(
                    "تعذّر التحقق من النص المستخرج. "
                    "يرجى المحاولة مرة أخرى."
                )

                st.caption(
                    f"تفاصيل تقنية: {exc}"
                )


    # -----------------------------------------------------
    # RESULTS
    # -----------------------------------------------------

    if "voice_results" in st.session_state:

        render_results(
            st.session_state[
                "voice_results"
            ]
        )

    elif (
        "voice_transcription"
        not in st.session_state
    ):

        empty_state(
            "ارفع ملاحظة صوتية لتحويلها "
            "إلى نص ثم التحقق منها."
        )


# =========================================================
# MEDICAL DISCLAIMER
# =========================================================

render_html(
    """
    <div class="medical-disclaimer">

        <strong>
            تنبيه طبي:
        </strong>

        هذه الأداة للتثقيف والتحقق من المعلومات العامة،
        ولا تُعد تشخيصًا أو وصفة علاجية.

        في الحالات العاجلة أو عند وجود أعراض مقلقة،
        تواصل مع جهة طبية مؤهلة.

    </div>
    """
)