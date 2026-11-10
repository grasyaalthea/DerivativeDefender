
import streamlit as st

st.set_page_config(
    page_title="Derivative Defender",
    page_icon="⚔️",
    layout="wide"
)

# =====================================
# ENCHANTED FANTASY THEME — VISUAL ONLY
# =====================================
st.markdown(r"""
<style>
/* Night-sky background with layered magical starlight, no external images. */
.stApp, [data-testid="stAppViewContainer"] {
    background-color: #100b24 !important;
    background-image:
        radial-gradient(circle at 13% 18%, rgba(248,211,142,.75) 0 1px, transparent 2px),
        radial-gradient(circle at 77% 9%, rgba(255,255,255,.8) 0 1px, transparent 2px),
        radial-gradient(circle at 42% 44%, rgba(201,162,255,.75) 0 1px, transparent 2px),
        radial-gradient(circle at 87% 67%, rgba(248,211,142,.7) 0 1px, transparent 2px),
        radial-gradient(circle at 21% 80%, rgba(255,255,255,.7) 0 1px, transparent 2px),
        radial-gradient(ellipse at 15% 5%, rgba(114,57,164,.48), transparent 52%),
        radial-gradient(ellipse at 85% 78%, rgba(58,46,129,.46), transparent 53%),
        linear-gradient(145deg,#110b26 0%,#221239 47%,#0d142b 100%) !important;
    background-size: 260px 270px, 330px 290px, 380px 360px,
                     430px 340px, 510px 400px, auto, auto, auto;
    color: #f9f1ff !important;
}
[data-testid="stMainBlockContainer"] {
    max-width: 1150px;
    padding-bottom: 5rem !important;
}
/* Titles and text */
h1, h2, h3, [data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3 {
    color: #f8d99a !important;
    font-family: Georgia, 'Times New Roman', serif !important;
    text-shadow: 0 2px 18px rgba(221,154,255,.35);
    letter-spacing: .025em;
}
h1 {font-size: clamp(2rem, 4.5vw, 3.5rem) !important;}
p, label, .stCaption, [data-testid="stMarkdownContainer"],
[data-testid="stWidgetLabel"], [data-testid="stMetricLabel"],
[data-testid="stMetricValue"] { color: #f5eafa; }
/* Main selection and question cards */
[data-testid="stVerticalBlockBorderWrapper"] > div,
[data-testid="stExpander"] {
    border-color: rgba(229,184,115,.44) !important;
    border-radius: 17px !important;
    background: rgba(34,19,60,.78) !important;
    box-shadow: 0 8px 24px rgba(6,4,20,.22);
}
/* Realm and agent columns become subtle magical cards. */
[data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
    background: linear-gradient(165deg,rgba(73,39,104,.36),rgba(25,19,52,.40));
    border: 1px solid rgba(214,173,120,.26);
    border-radius: 18px;
    padding: 16px 14px;
    min-width: 0;
    box-shadow: inset 0 1px rgba(255,255,255,.07);
}

/* Equal-height fantasy selection cards; buttons share a bottom baseline. */
.st-key-agent_cards [data-testid="stHorizontalBlock"],
.st-key-realm_cards [data-testid="stHorizontalBlock"] {
    align-items: stretch !important;
}
.st-key-agent_cards [data-testid="stHorizontalBlock"] > [data-testid="stColumn"],
.st-key-realm_cards [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
    display: flex !important;
    flex-direction: column !important;
    align-self: stretch !important;
}
.st-key-agent_cards [data-testid="stColumn"] > [data-testid="stVerticalBlock"],
.st-key-realm_cards [data-testid="stColumn"] > [data-testid="stVerticalBlock"],
.st-key-agent_cards [data-testid="stColumn"] > div > [data-testid="stVerticalBlock"],
.st-key-realm_cards [data-testid="stColumn"] > div > [data-testid="stVerticalBlock"] {
    display: flex !important;
    flex-direction: column !important;
    flex: 1 1 auto !important;
    height: 100% !important;
}
.st-key-agent_cards [data-testid="stColumn"] [data-testid="stElementContainer"]:has(.stButton),
.st-key-realm_cards [data-testid="stColumn"] [data-testid="stElementContainer"]:has(.stButton),
.st-key-agent_cards [data-testid="stColumn"] [data-testid="stButton"],
.st-key-realm_cards [data-testid="stColumn"] [data-testid="stButton"] {
    margin-top: auto !important;
}

/* Buttons with visible hover/focus states */
.stButton > button {
    background: linear-gradient(110deg,#5b2b8a,#8c3fa1) !important;
    border: 1px solid #d9b677 !important;
    border-radius: 12px !important;
    color: #fff8e8 !important;
    font-weight: 750 !important;
    min-height: 44px;
    box-shadow: 0 4px 15px rgba(6,3,24,.3);
    transition: transform .15s ease, box-shadow .15s ease, filter .15s ease;
}
.stButton > button:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: 0 5px 24px rgba(204,133,249,.35);
    filter: brightness(1.18);
}
.stButton > button:focus-visible,
[data-testid="stRadio"] label:focus-within {
    outline: 3px solid #f7d795 !important;
    outline-offset: 3px;
}
.stButton > button:disabled {opacity:.52 !important; cursor:not-allowed;}
.stButton > button[kind="primary"] {
    background: linear-gradient(110deg,#8b3f94,#bc5a9d) !important;
}
/* Answers */
[data-testid="stRadio"] {
    padding: 14px 18px;
    background: rgba(24,16,47,.75);
    border: 1px solid rgba(225,184,119,.45);
    border-radius: 16px;
}
[data-testid="stRadio"] label {
    padding: 7px 10px;
    border-radius: 10px;
}
[data-testid="stRadio"] label:hover {background: rgba(182,122,230,.16);}
/* Math is kept bright and legible. */
[data-testid="stLatex"] { color:#fff8ee !important; }
/* Status feedback and progress */
[data-testid="stAlert"] {
    border-radius: 14px !important;
    border: 1px solid rgba(224,181,112,.35);
}
/* READABLE FANTASY NOTICES: dark surfaces and bright high-contrast text. */
[data-testid="stAlert"],
[data-testid="stAlert"] > div {
    background: linear-gradient(120deg, #29183f, #37214e) !important;
    color: #fff5e8 !important;
}
[data-testid="stAlert"] {
    border: 1px solid #cba66d !important;
    box-shadow: inset 0 0 14px rgba(193,134,229,.12) !important;
}
[data-testid="stAlert"] p,
[data-testid="stAlert"] span,
[data-testid="stAlert"] div,
[data-testid="stAlert"] [data-testid="stMarkdownContainer"],
[data-testid="stAlert"] [data-testid="stMarkdownContainer"] * {
    color: #fff5e8 !important;
    opacity: 1 !important;
    text-shadow: none !important;
}
[data-testid="stAlert"] svg { color: #f4ce83 !important; fill: none; }
[data-testid="stProgress"] > div > div {background-color:#d5a7f6 !important;}
hr {border-color:rgba(224,181,112,.35) !important;}
/* Floating status HUD: ornate but high contrast and easy to read. */
.dd-hud {
    background: linear-gradient(100deg,#1b1032 0%,#3d205c 53%,#251439 100%) !important;
    border-bottom: 2px solid #e9c581 !important;
    box-shadow: 0 5px 25px rgba(5,2,16,.75),0 0 25px rgba(159,99,215,.16) !important;
}
.dd-hud-item {
    background: rgba(13,10,33,.72) !important;
    border: 1px solid rgba(246,207,140,.55) !important;
    box-shadow: inset 0 0 16px rgba(143,87,180,.15);
}
.dd-hud-number {color:#fff5d7 !important;}
.dd-hud-track {background:rgba(0,0,0,.5) !important;}
/* Hide default menu/footer but preserve Streamlit's functional controls. */
#MainMenu, footer {visibility:hidden;}
@media(max-width:700px) {
    [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {padding:10px 9px;}
    .dd-hud-item {box-shadow:none;}
    h1 {font-size:2rem !important;}
}
@media(prefers-reduced-motion:reduce) {
    *,*::before,*::after {animation-duration:.01ms !important;transition-duration:.01ms !important;}
}
</style>
""", unsafe_allow_html=True)


#GAME DATA
AGENTS = {
    "Aether": {
        "icon": "🛡️", "title": "Guardian of Calculus",
        "power": "Shield of Wisdom",
        "abilities": "Instantly reveal half of the answer, Skip one question, Gain extra points",
        "description": "Block one wrong answer per realm."
    },
    "Lyra": {
        "icon": "🔮", "title": "Mystic of Knowledge",
        "power": "Oracle's Vision",
        "abilities": "Pause the question timer for 5 seconds, Retry your last incorrect answer, Gain bonus points for answering within 5 seconds",
        "description": "Reveal one answer once per realm."
    },
    "Kael": {
        "icon": "🔥", "title": "Warrior of Derivatives",
        "power": "Double Strike",
        "abilities": "Reveal the formula needed, Extra time, and One Hint",
        "description": "Double points for one correct answer per realm."
    }
}

REALMS = {
    "Limits Realm": {
        "icon": "🌌",
        "description": "Master limits and continuity.",
        "questions": [
            {
                "question": r"\lim_{x \to 2}(3x+4)",
                "choices": ["6", "8", "10", "12"],
                "answer": "10",
                "hint": "Substitute x = 2."
            },
            {
                "question": r"\lim_{x \to 3}(x^2+1)",
                "choices": ["6", "9", "10", "12"],
                "answer": "10",
                "hint": "Find 3 squared, then add 1."
            },
            {
                "question": r"\lim_{x \to 1}\frac{x^2-1}{x-1}",
                "choices": ["0", "1", "2", "3"],
                "answer": "2",
                "hint": "Factor x squared minus 1."
            }
        ]
    },
    "Algebraic Derivatives Realm": {
        "icon": "⚡",
        "description": "Defeat enemies using differentiation.",
        "questions": [
            {
                "question": r"\frac{d}{dx}(x^3)",
                "choices": [
                    r"3x^2", r"x^2", r"3x", r"x^3"
                ],
                "answer": r"3x^2",
                "hint": "Use the power rule."
            },
            {
                "question": r"\frac{d}{dx}(5x^2+3x)",
                "choices": [
                    r"5x+3", r"10x+3",
                    r"10x", r"5x^2+3"
                ],
                "answer": r"10x+3",
                "hint": "Differentiate each term."
            },
            {
                "question": r"\frac{d}{dx}(x^4-2x)",
                "choices": [
                    r"4x^3-2", r"4x^2-2",
                    r"x^3-2", r"4x^3"
                ],
                "answer": r"4x^3-2",
                "hint": "Apply the power rule to x^4."
            }
        ]
    },
    "Transcendental Functions Realm": {
        "icon": "🔮",
        "description": "Master trigonometric, exponential and logarithmic derivatives.",
        "questions": [
            {
                "question": r"\frac{d}{dx}(\sin (x))",
                "choices": [
                    r"\cos x", r"-\cos x",
                    r"\sin x", r"-\sin x"
                ],
                "answer": r"\cos x",
                "hint": "Recall the derivative of sine."
            },
            {
                "question": r"\frac{d}{dx}(e^x)",
                "choices": [
                    r"x e^x", r"e^x",
                    r"1", r"\ln x"
                ],
                "answer": r"e^x",
                "hint": "This exponential is its own derivative."
            },
            {
                "question": r"\frac{d}{dx}(\ln x)",
                "choices": [
                    r"x", r"\ln x",
                    r"\frac{1}{x}", r"e^x"
                ],
                "answer": r"\frac{1}{x}",
                "hint": "Recall the natural logarithm rule."
            }
        ]
    }
}

# =====================================
# SESSION STATE
# =====================================

defaults = {
    "page": "agent",
    "agent": None,
    "realm": None,
    "question_index": 0,
    "score": 0,
    "correct_count": 0,
    "wrong_count": 0,
    "health": 50,
    "health_notice": "",
    "energy": 40,
    "energy_notice": "",
    "ult_active": False,
    "power_used": False,
    "shield_used": False,
    "hint_visible": False,
    "answered": False,
    "last_correct": False,
    "last_points": 0,
    "completed": [],
    "attempts": 0
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


def change_page(page):
    st.session_state.page = page
    st.rerun()


def reset_challenge():
    st.session_state.question_index = 0
    st.session_state.power_used = False
    st.session_state.ult_active = False
    st.session_state.shield_used = False
    st.session_state.hint_visible = False
    st.session_state.answered = False
    st.session_state.last_correct = False
    st.session_state.last_points = 0
    st.session_state.attempts = 0


# =====================================
# GAME HEADER
# =====================================

st.title("⚔️ DERIVATIVE DEFENDER")
st.subheader("The Ultimate Calculus Adventure")

# =====================================
# COMPACT ALWAYS-VISIBLE GAME HUD
# =====================================
# These are the same session-state values used by the original game.
health_value = max(0, min(100, st.session_state.health))
energy_value = max(0, min(100, st.session_state.energy))
score = st.session_state.score
correct = st.session_state.correct_count
wrong = st.session_state.wrong_count
total_answers = correct + wrong
accuracy = round(correct / total_answers * 100) if total_answers else 0

if score < 50:
    rank, rank_start, next_rank = "🌱 Calculus Apprentice", 0, 50
elif score < 100:
    rank, rank_start, next_rank = "🛡️ Realm Explorer", 50, 100
elif score < 150:
    rank, rank_start, next_rank = "⚔️ Calculus Warrior", 100, 150
elif score < 200:
    rank, rank_start, next_rank = "🔮 Master of Derivatives", 150, 200
else:
    rank, rank_start, next_rank = "👑 Legendary Defender", 200, 200

progress = 100 if score >= 200 else int((score - rank_start) / (next_rank - rank_start) * 100)
progress_label = "Maximum rank achieved" if score >= 200 else f"{score} / {next_rank} XP to next rank"
health_color = "#34d399" if health_value > 60 else ("#fbbf24" if health_value > 25 else "#fb7185")
energy_color = "#60a5fa" if energy_value >= 50 else ("#fbbf24" if energy_value >= 30 else "#fb7185")
ult_status = "ULT READY" if energy_value >= 50 else f"{50 - energy_value} EP until ULT"

# Fixed top HUD stays visible even when scrolling through long questions.
st.markdown("""
<style>
/* Give the fixed HUD enough room without obscuring the page title. */
.main .block-container, [data-testid="stMainBlockContainer"] {
    padding-top: 7.5rem !important;
}
.dd-hud {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 999999;
    background: linear-gradient(110deg, #261236, #522064 55%, #8d3276);
    border-bottom: 2px solid #efb3db;
    box-shadow: 0 5px 18px rgba(0,0,0,.35);
    color: #fff;
    padding: 11px max(14px, calc((100vw - 1100px)/2));
    font-family: system-ui, sans-serif;
}
.dd-hud-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; }
.dd-hud-item {
    min-width: 0;
    padding: 9px 12px;
    border-radius: 13px;
    border: 1px solid rgba(255,255,255,.25);
    background: rgba(255,255,255,.09);
}
.dd-hud-line { display: flex; align-items: center; justify-content: space-between; gap: 8px; }
.dd-hud-label { font-weight: 800; font-size: 14px; letter-spacing: .3px; }
.dd-hud-number { font-weight: 900; font-size: 19px; white-space: nowrap; }
.dd-hud-track { height: 9px; margin-top: 7px; background: rgba(255,255,255,.2); border-radius: 20px; overflow: hidden; }
.dd-hud-fill { height: 100%; border-radius: 20px; }
.dd-hud-note { font-size: 11px; margin-top: 5px; opacity: .92; }
@media (max-width: 640px) {
    .dd-hud { padding: 8px 6px; }
    .dd-hud-grid { gap: 5px; }
    .dd-hud-item { padding: 7px 5px; border-radius: 9px; }
    .dd-hud-label { font-size: 11px; }
    .dd-hud-number { font-size: 13px; }
    .dd-hud-note { font-size: 9px; }
    .main .block-container, [data-testid="stMainBlockContainer"] { padding-top: 7.1rem !important; }
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="dd-hud" role="status" aria-label="Live player statistics">
  <div class="dd-hud-grid">
    <div class="dd-hud-item" aria-label="Health {health_value} out of 100">
      <div class="dd-hud-line"><span class="dd-hud-label">❤️ HEALTH</span><span class="dd-hud-number">{health_value}/100</span></div>
      <div class="dd-hud-track"><div class="dd-hud-fill" style="width:{health_value}%;background:{health_color};"></div></div>
      <div class="dd-hud-note">+10 correct · −10 wrong</div>
    </div>
    <div class="dd-hud-item" aria-label="Energy {energy_value} out of 100">
      <div class="dd-hud-line"><span class="dd-hud-label">⚡ ENERGY</span><span class="dd-hud-number">{energy_value}/100</span></div>
      <div class="dd-hud-track"><div class="dd-hud-fill" style="width:{energy_value}%;background:{energy_color};"></div></div>
      <div class="dd-hud-note">{ult_status} · ULT costs 50</div>
    </div>
    <div class="dd-hud-item" aria-label="Total score {score} experience points">
      <div class="dd-hud-line"><span class="dd-hud-label">🏆 SCORE</span><span class="dd-hud-number">{score} XP</span></div>
      <div class="dd-hud-track"><div class="dd-hud-fill" style="width:{progress}%;background:#ffe18d;"></div></div>
      <div class="dd-hud-note">{correct} correct · {wrong} wrong · {accuracy}% accuracy</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# Keep existing feedback notifications, but remove the bulky battery panels.
if st.session_state.health_notice:
    st.info(st.session_state.health_notice)
    st.session_state.health_notice = ""
if st.session_state.energy_notice:
    st.info(st.session_state.energy_notice)
    st.session_state.energy_notice = ""

with st.expander("🏅 View rank and detailed scoreboard"):
    st.subheader(rank)
    st.caption(progress_label)
    st.progress(progress / 100)
    col_a, col_b, col_c = st.columns(3)
    col_a.metric("Correct answers", correct)
    col_b.metric("Mistakes", wrong)
    col_c.metric("Accuracy", f"{accuracy}%")

st.divider()

# =====================================
# PAGE 1: AGENT SELECTION
# =====================================

if st.session_state.page == "agent":

    st.header("CHOOSE YOUR AGENT")

    st.write(
        "Three legendary defenders await your command. "
        "Choose wisely, for each possesses a unique power."
    )

    with st.container(key="agent_cards"):
        cols = st.columns(3)

        for col, (name, agent) in zip(cols, AGENTS.items()):

            with col:
                st.markdown(f"### {agent['icon']} {name}")
                st.write(f"**{agent['title']}**")
                st.write(f"Power: **{agent['power']}**")
                st.write(f"Abilities: **{agent['abilities']}**")
                st.info(agent["description"])

                if st.button(
                    f"Select {name}",
                    key=f"select_{name}",
                    use_container_width=True
                ):
                    st.session_state.agent = name
                    change_page("realm")


# =====================================
# PAGE 2: REALM SELECTION
# =====================================

elif st.session_state.page == "realm":

    agent = AGENTS[st.session_state.agent]

    st.success(
        f"{agent['icon']} Your Agent: "
        f"{st.session_state.agent}"
    )

    st.write(f"Special Power: {agent['power']}")

    st.header("🗺️ CHOOSE YOUR REALM")

    st.write(
        "Three realms have fallen into darkness. "
        "Choose which realm you wish to uncover."
    )

    with st.container(key="realm_cards"):
        cols = st.columns(3)

        for col, (name, realm) in zip(cols, REALMS.items()):

            with col:
                st.markdown(f"### {realm['icon']} {name}")
                st.write(realm["description"])

                if name in st.session_state.completed:
                    st.success("Realm Completed!")

                if st.button(
                    "Enter Realm",
                    key=f"realm_{name}",
                    use_container_width=True
                ):
                    st.session_state.realm = name
                    reset_challenge()
                    change_page("battle")

    st.divider()

    st.metric("Total Score", st.session_state.score)

    if st.button("⬅ Change Agent"):
        change_page("agent")


# =====================================
# PAGE 3: BATTLE
# =====================================

elif st.session_state.page == "battle":

    realm_name = st.session_state.realm
    realm = REALMS[realm_name]

    agent_name = st.session_state.agent
    agent = AGENTS[agent_name]

    questions = realm["questions"]
    index = st.session_state.question_index

    st.header(f"{realm['icon']} {realm_name}")

    left, middle, right = st.columns(3)

    left.metric("Agent", agent_name)
    middle.metric("Score", st.session_state.score)
    right.metric(
        "Challenge",
        f"{index + 1}/{len(questions)}"
    )

    st.progress(index / len(questions))

    st.divider()

    question = questions[index]

    st.subheader("⚔️ Enemy Encounter!")

    st.write("Solve the calculus problem to attack:")

    st.latex(question["question"])

    # =================================
    # SPECIAL ABILITY — ENERGY-PAID ULT
    # =================================

    st.subheader(f"✨ Special Ability: {agent['power']}")
    st.caption("Ultimate cost: 50 EP • Available once per realm")

    if st.session_state.power_used:
        st.caption("Ultimate already purchased in this realm.")
    elif st.session_state.answered:
        st.caption("Continue to the next challenge to use your ultimate.")
    else:
        if agent_name == "Aether":
            st.info("Spend 50 EP to activate a shield that blocks your next wrong answer.")
        elif agent_name == "Lyra":
            st.info("Spend 50 EP to reveal a hint for the current equation.")
        elif agent_name == "Kael":
            st.info("Spend 50 EP to earn 20 points on your next correct answer.")

        if st.session_state.energy < 50:
            st.warning(f"Not enough energy! Earn {50 - st.session_state.energy} more EP to activate your ULT.")

        if st.button(
            "⚡ ACTIVATE ULT — 50 EP",
            disabled=st.session_state.energy < 50,
            use_container_width=True,
        ):
            st.session_state.energy -= 50
            st.session_state.power_used = True
            st.session_state.ult_active = agent_name in ("Aether", "Kael")
            if agent_name == "Lyra":
                st.session_state.hint_visible = True
            st.session_state.energy_notice = f"✨ {agent['power']} activated! −50 EP"
            st.rerun()

    if agent_name == "Lyra" and st.session_state.hint_visible:
        st.info(f"🔮 Oracle's Vision — Hint: {question['hint']}")
    if agent_name == "Aether" and st.session_state.ult_active:
        st.success("🛡️ Shield ready: your next incorrect answer will be blocked.")
    if agent_name == "Kael" and st.session_state.ult_active:
        st.success("🔥 Double Strike ready: your next correct answer earns 20 points.")

    # =================================
    # ANSWER SELECTION
    # =================================

    st.subheader("Choose Your Answer")

    if not st.session_state.answered:

        answer = st.radio(
            "Select the correct answer:",
            question["choices"],
            index=None,
            key=f"answer_{realm_name}_{index}"
        )

        if st.button(
            "⚔️ Submit Answer",
            type="primary",
            use_container_width=True
        ):

            if answer is None:
                st.warning("Please choose an answer.")

            elif answer == question["answer"]:

                points = 10

                if (
                    agent_name == "Kael"
                    and st.session_state.ult_active
                ):
                    points = 20
                    st.session_state.ult_active = False

                st.session_state.energy = min(100, st.session_state.energy + 15)
                st.session_state.energy_notice = "⚡ Correct answer! +15 EP"
                st.session_state.health = min(100, st.session_state.health + 10)
                st.session_state.health_notice = "✅ Correct answer! +10 HP"
                st.session_state.score += points
                st.session_state.correct_count += 1
                st.session_state.last_points = points
                st.session_state.last_correct = True
                st.session_state.answered = True

                st.rerun()

            else:

                st.session_state.attempts += 1
                st.session_state.wrong_count += 1

                if (
                    agent_name == "Aether"
                    and st.session_state.ult_active
                ):
                    st.session_state.ult_active = False
                    st.session_state.shield_used = True
                    st.warning(
                        "🛡️ Shield of Wisdom activated! "
                        "Your wrong answer was blocked. "
                        "Try again!"
                    )

                else:
                    st.session_state.energy = max(0, st.session_state.energy - 5)
                    st.session_state.energy_notice = "⚡ Incorrect answer! −5 EP"
                    st.session_state.health = max(0, st.session_state.health - 10)
                    st.session_state.health_notice = "❌ Incorrect answer! −10 HP"
                    st.error(
                        "❌ Incorrect! The enemy is still standing. "
                        "Try again!"
                    )
                    st.rerun()

    # =================================
    # CORRECT ANSWER / NEXT CHALLENGE
    # =================================

    else:

        st.success(
            "🎉 Correct! You defeated the enemy!"
        )

        st.write(
            f"⭐ You earned "
            f"{st.session_state.last_points} points!"
        )

        st.balloons()

        if st.button(
            "➡ Continue Adventure",
            type="primary",
            use_container_width=True
        ):

            if index + 1 < len(questions):

                st.session_state.question_index += 1
                st.session_state.answered = False
                st.session_state.hint_visible = False
                st.session_state.last_correct = False
                st.rerun()

            else:

                if realm_name not in st.session_state.completed:
                    st.session_state.completed.append(realm_name)

                change_page("victory")

    st.divider()

    if st.button("⬅ Return to Realm Selection"):
        change_page("realm")


# =====================================
# PAGE 4: VICTORY
# =====================================

elif st.session_state.page == "victory":

    st.title("🏆 REALM CONQUERED!")

    st.success(
        f"Congratulations, {st.session_state.agent}! "
        f"You successfully conquered "
        f"{st.session_state.realm}!"
    )

    st.balloons()

    st.metric("Total Score", st.session_state.score)

    st.write(
        f"Realms Conquered: "
        f"{len(st.session_state.completed)}/3"
    )

    if len(st.session_state.completed) == 3:

        st.header("👑 THE ULTIMATE DEFENDER")

        st.success(
            "You have conquered all three realms! "
            "The world of Calculus is saved!"
        )

    if st.button(
        "🗺️ Explore Another Realm",
        type="primary"
    ):
        change_page("realm")

    if st.button("🔄 Restart Entire Game"):

        for key, value in defaults.items():
            st.session_state[key] = (
                value.copy() if isinstance(value, list)
                else value
            )

        st.rerun()













