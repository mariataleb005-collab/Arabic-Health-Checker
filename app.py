from pathlib import Path
import sys

import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parent
SRC_DIR = PROJECT_ROOT / "src"

# Compatibility with the existing backend, whose modules import one another
# as top-level modules (e.g. "from extract_claims import extract_claims").
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from ui.styles import inject_global_styles


st.set_page_config(
    page_title="بَيِّنة | مدقق المعلومات الصحية",
    page_icon="/workspaces/Arabic-Health-Checker/assets/bayyinah_logo.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_global_styles()

home_page = st.Page(
    "views/home.py",
    title="الرئيسية",
    icon=":material/home:",
    url_path="home",
    default=True,
)

checker_page = st.Page(
    "views/checker.py",
    title="تحقق من معلومة",
    icon=":material/fact_check:",
    url_path="checker",
)

# page = st.navigation(
#     [home_page, checker_page],
#     position="top",
# )
page = st.navigation(
    [home_page, checker_page],
    position="hidden",
)

page.run()
