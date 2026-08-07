import streamlit as st

from ui.components import brand_header, render_html, trust_strip


brand_header()

render_html(
    """
    <section class="hero">
        <div class="hero-eyebrow">
            <span class="status-dot"></span>
            مدقق صحي عربي مدعوم بالمصادر
        </div>

        <h1>
            تحقّق من المعلومة الصحية<br>
            <span>قبل أن تصدّقها أو تشاركها.</span>
        </h1>

        <p class="hero-copy">
            بَيِّنة تساعدك على فحص الادعاءات الصحية المكتوبة أو الصوتية باللغة العربية،
            ومقارنتها بمصادر طبية موثوقة مثل منظمة الصحة العالمية ووزارة الصحة ووقاية المجتمع.
        </p>
    </section>
    """
)

cta_col, note_col = st.columns([0.36, 0.64], vertical_alignment="center")

with cta_col:
    if st.button(
        "ابدأ التحقق الآن  ←",
        type="primary",
        use_container_width=True,
        key="home_cta",
    ):
        st.switch_page("views/checker.py")

with note_col:
    render_html(
        """
        <div class="hero-note">
            لا يستبدل التشخيص أو الاستشارة الطبية.
            الهدف هو مساعدتك على تقييم موثوقية المعلومات الصحية.
        </div>
        """
    )

trust_strip()

render_html(
    """
    <div class="section-heading">
        <span>كيف تعمل بَيِّنة؟</span>
        <h2>ثلاث خطوات من الادعاء إلى الدليل</h2>
        <p>
            واجهة بسيطة، بينما تعمل خلفها سلسلة تحقق تعتمد على الاسترجاع
            من مصادر موثوقة وتوليد إجابة مؤسّسة على الدليل.
        </p>
    </div>
    """
)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    render_html(
        """
        <article class="step-card">
            <div class="step-number">01</div>
            <div class="step-icon">✎</div>
            <h3>أرسل المعلومة</h3>
            <p>
                الصق نصًا عربيًا أو ارفع ملاحظة صوتية،
                حتى لو احتوت على أكثر من ادعاء صحي.
            </p>
        </article>
        """
    )

with col2:
    render_html(
        """
        <article class="step-card">
            <div class="step-number">02</div>
            <div class="step-icon">⌕</div>
            <h3>نبحث في المصادر</h3>
            <p>
                يُستخرج كل ادعاء على حدة ثم تُسترجع له
                المقاطع الطبية الأكثر صلة من قاعدة المعرفة.
            </p>
        </article>
        """
    )

with col3:
    render_html(
        """
        <article class="step-card">
            <div class="step-number">03</div>
            <div class="step-icon">✓</div>
            <h3>اقرأ الحكم والدليل</h3>
            <p>
                تحصل على نتيجة واضحة، مستوى الخطورة،
                تفسير مختصر، والمصادر المستخدمة عند توفر دليل مناسب.
            </p>
        </article>
        """
    )

render_html(
    """
    <section class="source-section">
        <div>
            <span class="mini-label">مصمم للثقة لا للتخمين</span>
            <h2>عندما لا يكفي الدليل، نقول ذلك بوضوح.</h2>
        </div>

        <p>
            لا تجبر بَيِّنة النظام على مطابقة الادعاء بمصدر غير مناسب.
            إذا لم تكن المعلومات المسترجعة كافية، تظهر النتيجة
            «معلومات غير كافية» بدل إعطاء ثقة زائفة.
        </p>
    </section>
    """
)
