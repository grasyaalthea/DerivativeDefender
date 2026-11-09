import streamlit as st

st.set_page_config(page_title="Derivative Defender | Realm I", page_icon="🔮", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Inter:wght@400;500;600;700&display=swap');
.stApp {background:linear-gradient(135deg,#210d29 0%,#67265f 42%,#bc528f 78%,#f5a4ca 100%);background-attachment:fixed;color:#fff0f8;font-family:Inter,sans-serif;}
[data-testid="stAppViewContainer"] {color:#fff0f8;}
[data-testid="stAppViewContainer"] p, [data-testid="stAppViewContainer"] label {color:#fff0f8;}
[data-testid="stSidebar"] {background:#2c112e;}
.block-container {max-width:1050px;padding-top:2rem;padding-bottom:5rem;}
h1,h2,h3 {font-family:Cinzel,Georgia,serif!important;color:#fff2fa!important;}
.hero {padding:2.8rem 1.7rem;border:1px solid #f6aed5;border-radius:22px;text-align:center;background:linear-gradient(120deg,#32102de8,#732b65e8,#3a173be8);box-shadow:0 12px 45px #210d2960;margin-bottom:1.5rem;}
.hero h1 {font-size:clamp(2rem,5vw,3.6rem);text-shadow:0 0 24px #ff8ccc88;margin:.6rem 0;}
.hero p {color:#ffe0f0;line-height:1.7;}
.eyebrow {font-size:.8rem;letter-spacing:.26em;color:#ffc6e6;font-weight:700;}
.panel {background:linear-gradient(145deg,#4b1c48ed,#28112ff2);border:1px solid #e38abd;border-radius:16px;padding:1.35rem 1.5rem;margin:.7rem 0 1.2rem;box-shadow:0 10px 30px #210d2955;}
.panel h3 {margin-top:0;}
.small-label {color:#ffb8df;font-size:.8rem;font-weight:700;letter-spacing:.1em;}
.letter {display:inline-block;min-width:58px;padding:12px 17px;margin:5px;border:1px solid #ffc2e5;background:#682759;border-radius:10px;color:#ffe5a8;font-size:1.5rem;font-weight:bold;text-align:center;}
.locked {opacity:.45;color:#fff;}
.stButton>button {width:100%;background:linear-gradient(110deg,#a33382,#df69aa);border:1px solid #ffb4dd;border-radius:10px;color:white;font-weight:700;min-height:46px;}
.stButton>button:hover {background:#e178b6;color:white;border-color:white;}
[data-testid="stRadio"] label {color:#fff0f8!important;}
[data-testid="stAlert"] {border-radius:12px;}
</style>
""", unsafe_allow_html=True)

AGENTS = {
    "Chrona — Time Weaver": {"icon": "⏳", "power": "Time Reversal", "description": "Negate one wrong-answer health penalty in this realm."},
    "Axion — Rune Breaker": {"icon": "⚔️", "power": "Rune Strike", "description": "Begin the adventure with 120 HP instead of 100 HP."},
    "Lyra — Celestial Seer": {"icon": "🔮", "power": "Astral Vision", "description": "Reveal one free hint in this realm."},
}

LEVELS = [
    {"name": "The Bridge of Approaching Values", "subtitle": "LEVEL 01 · THE VANISHING BRIDGE", "letter": "F",
     "story": "A bridge of frozen light flickers above the Abyss of Time. Discover the values the stones approach to cross safely.",
     "questions": [
         {"prompt": r"Evaluate $\lim_{x\to 2}(3x+1)$.", "choices": ["5", "7", "9", "Does not exist"], "answer": "7", "hint": "Substitute x = 2 directly.", "why": "3(2) + 1 = 7."},
         {"prompt": r"Evaluate $\lim_{x\to 3}\frac{x^2-9}{x-3}$.", "choices": ["0", "3", "6", "Undefined limit"], "answer": "6", "hint": "Factor the numerator into (x−3)(x+3).", "why": "Cancel the common factor for x ≠ 3; the limit of x + 3 is 6."},
     ]},
    {"name": "The Cavern of One-Sided Paths", "subtitle": "LEVEL 02 · THE SPLIT PATH", "letter": "U",
     "story": "Two tunnels approach the same point from opposite directions. Their magic may not agree.",
     "questions": [
         {"prompt": r"If $f(x)=\begin{cases}2 & x<1\\5 & x\geq 1\end{cases}$, find $\lim_{x\to 1^-}f(x)$.", "choices": ["1", "2", "5", "Does not exist"], "answer": "2", "hint": "Approach 1 from the left (x < 1).", "why": "To the left of 1, f(x) is always 2."},
         {"prompt": r"For the same function, does $\lim_{x\to 1}f(x)$ exist?", "choices": ["Yes, it is 2", "Yes, it is 5", "Yes, it is 3.5", "No, it does not exist"], "answer": "No, it does not exist", "hint": "Compare the left-hand limit (2) and right-hand limit (5).", "why": "The two one-sided limits are unequal, so the two-sided limit does not exist."},
     ]},
    {"name": "The Tower of Continuity", "subtitle": "LEVEL 03 · THE LAST SEAL", "letter": "N",
     "story": "The tower's final seal recognizes only continuous magic. Repair its formulas to claim the last letter.",
     "questions": [
         {"prompt": r"Let $f(x)=\begin{cases}x+2 & x\neq 2\\k & x=2\end{cases}$. What $k$ makes $f$ continuous at $x=2$?", "choices": ["2", "3", "4", "0"], "answer": "4", "hint": "For continuity, f(2) must equal the limit at 2.", "why": "The limit of x + 2 at x = 2 is 4, so k = 4."},
         {"prompt": r"Which condition is required for $f$ to be continuous at $x=a$?", "choices": ["Only f(a) exists", "Only the limit exists", "The limit exists and equals f(a)", "The derivative must be zero"], "answer": "The limit exists and equals f(a)", "hint": "Continuity connects the function value to its limit.", "why": "f(a) must be defined and equal to the limit as x approaches a."},
     ]},
]

DEFAULTS = {"agent": None, "hp": 100, "level": 0, "question": 0, "letters": [], "power_used": False, "hint_visible": False, "feedback": None, "answered": False, "finished": False, "failed": False}

def reset_game():
    for key, value in DEFAULTS.items():
        st.session_state[key] = value.copy() if isinstance(value, list) else value

for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value.copy() if isinstance(value, list) else value

def choose_agent(agent):
    reset_game()
    st.session_state.agent = agent
    st.session_state.hp = 120 if agent.startswith("Axion") else 100
    st.rerun()

def submit_answer(answer, correct, why):
    if st.session_state.answered or st.session_state.failed:
        return
    if answer == correct:
        st.session_state.answered = True
        st.session_state.feedback = ("success", f"Correct! {why}")
    elif st.session_state.agent.startswith("Chrona") and not st.session_state.power_used:
        st.session_state.power_used = True
        st.session_state.feedback = ("warning", "Chrona used Time Reversal! No HP lost. Try again.")
    else:
        st.session_state.hp = max(0, st.session_state.hp - 20)
        st.session_state.feedback = ("error", f"Incorrect! You lost 20 HP. Try again. Hint: {why}" if st.session_state.hp else "Your health reached zero.")
        if st.session_state.hp == 0:
            st.session_state.failed = True
    st.rerun()

def advance():
    if not st.session_state.answered:
        return
    level = st.session_state.level
    q = st.session_state.question
    st.session_state.feedback = None
    st.session_state.hint_visible = False
    st.session_state.answered = False
    if q + 1 < len(LEVELS[level]["questions"]):
        st.session_state.question += 1
    else:
        letter = LEVELS[level]["letter"]
        if letter not in st.session_state.letters:
            st.session_state.letters.append(letter)
        if level + 1 < len(LEVELS):
            st.session_state.level += 1
            st.session_state.question = 0
        else:
            st.session_state.finished = True
    st.rerun()

st.caption("REALM 1 • GAME INTERFACE LOADED")
st.markdown('<div class="hero"><div class="eyebrow">THE LOST SECRETS OF AETHERIA</div><h1>DERIVATIVE DEFENDER</h1><p>REALM I · THE FRACTURED HORIZON<br>Restore the broken pathways of time through the power of Limits and Continuity.</p></div>', unsafe_allow_html=True)

if st.session_state.agent is None:
    st.subheader("Choose Your Agent")
    st.write("Choose one guardian. Your agent's power will help you survive the realm.")
    cols = st.columns(3)
    for col, (name, info) in zip(cols, AGENTS.items()):
        with col:
            st.markdown(f'<div class="panel"><h3>{info["icon"]} {name}</h3><p class="small-label">{info["power"]}</p><p>{info["description"]}</p></div>', unsafe_allow_html=True)
            if st.button(f"Choose {name.split(' — ')[0]}", key=name):
                choose_agent(name)
    st.stop()

with st.sidebar:
    st.title("🔮 Agent Status")
    st.write(st.session_state.agent)
    st.metric("Health", f"{st.session_state.hp} HP")
    st.progress(st.session_state.hp / (120 if st.session_state.agent.startswith("Axion") else 100))
    st.write("Sacred letters:", " ".join(st.session_state.letters) or "None yet")
    st.write("Ability:", "Used" if st.session_state.power_used else "Available")
    if st.button("Restart Adventure", key="restart"):
        reset_game()
        st.rerun()

if st.session_state.failed:
    st.error("Mission failed! Your agent has fallen in the Fractured Horizon.")
    if st.button("Try Again"):
        reset_game()
        st.rerun()
    st.stop()

if st.session_state.finished:
    st.balloons()
    st.success("Realm I complete! You have restored the Fractured Horizon.")
    st.markdown('<div class="panel"><h2>Three Sacred Letters Recovered</h2><div class="letter">F</div><div class="letter">U</div><div class="letter">N</div><p>Keep these letters for the final nine-letter Codex puzzle!</p></div>', unsafe_allow_html=True)
    if st.button("Play Realm I Again"):
        reset_game()
        st.rerun()
    st.stop()

level = LEVELS[st.session_state.level]
question = level["questions"][st.session_state.question]

c1, c2, c3 = st.columns(3)
c1.metric("Current Level", f"{st.session_state.level + 1} / 3")
c2.metric("Question", f"{st.session_state.question + 1} / {len(level['questions'])}")
c3.metric("Health", f"{st.session_state.hp} HP")
st.progress((st.session_state.level * 2 + st.session_state.question) / 6)

st.markdown(f'<div class="panel"><div class="small-label">{level["subtitle"]}</div><h2>{level["name"]}</h2><p>{level["story"]}</p></div>', unsafe_allow_html=True)
st.subheader("Solve the Guardian's Challenge")
st.markdown(question["prompt"])

answer = st.radio("Choose your answer:", question["choices"], index=None, key=f"choice_{st.session_state.level}_{st.session_state.question}", disabled=st.session_state.answered)

if st.session_state.agent.startswith("Lyra") and not st.session_state.power_used and not st.session_state.answered:
    if st.button("🔮 Use Astral Vision (one hint)"):
        st.session_state.power_used = True
        st.session_state.hint_visible = True
        st.rerun()
if st.session_state.hint_visible:
    st.info("Astral Vision: " + question["hint"])

if st.session_state.feedback:
    kind, message = st.session_state.feedback
    getattr(st, kind)(message)

if st.session_state.answered:
    if st.button("Continue Adventure →"):
        advance()
else:
    if st.button("Submit Answer", disabled=answer is None):
        submit_answer(answer, question["answer"], question["why"])

st.markdown("### Sacred Letter Collection")
st.markdown("".join(f'<div class="letter{ "" if i < len(st.session_state.letters) else " locked"}">{st.session_state.letters[i] if i < len(st.session_state.letters) else "?"}</div>' for i in range(3)), unsafe_allow_html=True)






