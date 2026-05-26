"""
Secure Password Generator
- CLI mode: run directly with `python password_generator.py`
- Web mode: run with `python password_generator.py --web` then open http://localhost:5000
"""

import secrets
import string
import math
import argparse
import sys

# ── Character pools ──────────────────────────────────────────────────────────
POOL_UPPER   = string.ascii_uppercase           # A-Z  (26)
POOL_LOWER   = string.ascii_lowercase           # a-z  (26)
POOL_DIGITS  = string.digits                    # 0-9  (10)
POOL_SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,.<>?"    # common symbols (26)
POOL_EXTRA   = "~`\\/\"' "                      # rare / extra symbols (7)


def build_pool(upper=True, lower=True, digits=True,
               symbols=True, extra=False) -> str:
    pool = ""
    if upper:   pool += POOL_UPPER
    if lower:   pool += POOL_LOWER
    if digits:  pool += POOL_DIGITS
    if symbols: pool += POOL_SYMBOLS
    if extra:   pool += POOL_EXTRA
    if not pool:
        raise ValueError("At least one character class must be selected.")
    return pool


def generate_password(length: int, pool: str) -> str:
    """
    Uses secrets.choice — cryptographically secure (CSPRNG).
    Guarantees at least one character from each active class.
    """
    # Guarantee coverage of each requested class
    guaranteed = []
    if any(c in pool for c in POOL_UPPER):
        guaranteed.append(secrets.choice(POOL_UPPER))
    if any(c in pool for c in POOL_LOWER):
        guaranteed.append(secrets.choice(POOL_LOWER))
    if any(c in pool for c in POOL_DIGITS):
        guaranteed.append(secrets.choice(POOL_DIGITS))
    if any(c in pool for c in POOL_SYMBOLS):
        guaranteed.append(secrets.choice(POOL_SYMBOLS))

    remaining = length - len(guaranteed)
    if remaining < 0:
        remaining = 0

    password_chars = [secrets.choice(pool) for _ in range(remaining)]
    all_chars = password_chars + guaranteed

    # Fisher-Yates shuffle via secrets
    for i in range(len(all_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        all_chars[i], all_chars[j] = all_chars[j], all_chars[i]

    return "".join(all_chars)


def entropy_bits(length: int, pool_size: int) -> float:
    """Shannon entropy: H = log2(pool_size) * length"""
    return math.log2(pool_size) * length


def crack_time_label(bits: float) -> str:
    """Time to brute-force at 1 trillion guesses/second."""
    ops_per_sec = 1e12
    seconds = (2 ** bits) / ops_per_sec

    if seconds < 60:         return "< 1 minute"
    if seconds < 3600:       return f"{seconds / 60:.0f} minutes"
    if seconds < 86400:      return f"{seconds / 3600:.0f} hours"
    if seconds < 31_536_000: return f"{seconds / 86400:.0f} days"
    years = seconds / 31_536_000
    if years < 1_000:        return f"{years:.1f} years"
    if years < 1_000_000:    return f"{years / 1_000:.1f} thousand years"
    if years < 1e9:          return f"{years / 1_000_000:.1f} million years"
    return "∞ (effectively uncrackable)"


def strength_label(bits: float) -> str:
    if bits < 40:  return "Weak"
    if bits < 60:  return "Fair"
    if bits < 80:  return "Strong"
    if bits < 120: return "Very strong"
    return "Unbreakable"


# ── CLI mode ──────────────────────────────────────────────────────────────────
def cli_mode():
    parser = argparse.ArgumentParser(
        description="Secure password generator (CLI + Web)"
    )
    parser.add_argument("--web",     action="store_true",  help="Launch Flask web UI")
    parser.add_argument("--length",  type=int,   default=32,  help="Password length (default 32)")
    parser.add_argument("--count",   type=int,   default=5,   help="How many passwords to generate")
    parser.add_argument("--no-upper",   action="store_false", dest="upper")
    parser.add_argument("--no-lower",   action="store_false", dest="lower")
    parser.add_argument("--no-digits",  action="store_false", dest="digits")
    parser.add_argument("--no-symbols", action="store_false", dest="symbols")
    parser.add_argument("--extra",      action="store_true",  help="Include extra/rare symbols")
    args = parser.parse_args()

    if args.web:
        web_mode()
        return

    pool = build_pool(
        upper=args.upper, lower=args.lower,
        digits=args.digits, symbols=args.symbols,
        extra=args.extra
    )
    bits   = entropy_bits(args.length, len(pool))
    print(f"\n{'─'*52}")
    print(f"  Length     : {args.length} characters")
    print(f"  Pool size  : {len(pool)} characters")
    print(f"  Entropy    : {bits:.1f} bits")
    print(f"  Strength   : {strength_label(bits)}")
    print(f"  Crack time : {crack_time_label(bits)}")
    print(f"{'─'*52}")
    for i in range(args.count):
        pw = generate_password(args.length, pool)
        print(f"  [{i+1}] {pw}")
    print(f"{'─'*52}\n")


# ── Flask web mode ────────────────────────────────────────────────────────────
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Secure Password Generator</title>
<style>
  :root {
    --blue:   #1A6FD4;
    --green:  #1D9E75;
    --purple: #534AB7;
    --red:    #E24B4A;
    --amber:  #EF9F27;
    --bg:     #f5f7fa;
    --card:   #ffffff;
    --border: rgba(0,0,0,0.1);
    --text:   #1a1a1a;
    --muted:  #6b7280;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: system-ui, sans-serif; background: var(--bg);
         color: var(--text); min-height: 100vh; display: flex;
         align-items: center; justify-content: center; padding: 2rem; }
  .card { background: var(--card); border-radius: 16px;
          border: 1px solid var(--border); padding: 2rem;
          width: 100%; max-width: 600px; box-shadow: 0 4px 24px rgba(0,0,0,0.07); }
  h1 { font-size: 22px; font-weight: 600; margin-bottom: 0.4rem; }
  .sub { font-size: 14px; color: var(--muted); margin-bottom: 1.5rem; }
  .pw-row { display: flex; align-items: center; gap: 10px;
            background: #f9fafb; border: 1px solid var(--border);
            border-radius: 50px; padding: 10px 16px; margin-bottom: 6px; }
  #pw-out { flex: 1; font-family: monospace; font-size: 15px;
             color: var(--text); word-break: break-all; }
  .badge { font-size: 12px; font-weight: 600; padding: 4px 12px;
           border-radius: 50px; white-space: nowrap; }
  .w-weak   { background:#FCEBEB; color:#A32D2D; }
  .w-fair   { background:#FAEEDA; color:#854F0B; }
  .w-strong { background:#EAF3DE; color:#3B6D11; }
  .w-verystrong  { background:#E1F5EE; color:#0F6E56; }
  .w-unbreakable { background:#E6F1FB; color:#0C447C; }
  .bar-wrap { height: 5px; border-radius: 3px; background:#e5e7eb; margin-bottom: 1.5rem; }
  .bar { height: 5px; border-radius: 3px; transition: all 0.4s; }
  label { font-size: 13px; color: var(--muted); display: block; margin-bottom: 6px; }
  .slider-row { display: flex; align-items: center; gap: 10px; margin-bottom: 1.25rem; }
  input[type=range] { flex: 1; accent-color: var(--blue); }
  .len-val { font-size: 15px; font-weight: 600; min-width: 28px; text-align: center; }
  .adj { width: 32px; height: 32px; border-radius: 50%;
         border: 1px solid var(--border); background: white;
         cursor: pointer; font-size: 18px; display: flex;
         align-items: center; justify-content: center; }
  .checks { display: flex; gap: 14px; flex-wrap: wrap; margin-bottom: 1.25rem; }
  .chk { display: flex; align-items: center; gap: 6px;
          font-size: 14px; font-weight: 500; cursor: pointer; }
  .chk input { width: 16px; height: 16px; accent-color: var(--blue); }
  .stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 1.5rem; }
  .stat { background: #f9fafb; border-radius: 10px; padding: 10px 14px; }
  .stat-val { font-size: 18px; font-weight: 600; }
  .stat-lbl { font-size: 11px; color: var(--muted); margin-top: 2px; }
  .btns { display: flex; gap: 10px; }
  button.primary { background: var(--blue); color: white; border: none;
                   border-radius: 50px; padding: 10px 22px; font-size: 14px;
                   font-weight: 500; cursor: pointer; transition: opacity 0.15s; }
  button.primary:hover { opacity: 0.88; }
  button.gen { background: var(--purple); }
  button.copied { background: var(--green) !important; }
</style>
</head>
<body>
<div class="card">
  <h1>🔐 Secure Password Generator</h1>
  <p class="sub">Cryptographically secure · Real-time entropy · Crack-time estimate</p>

  <div class="pw-row">
    <span id="pw-out">—</span>
    <span class="badge w-verystrong" id="badge">—</span>
  </div>
  <div class="bar-wrap"><div class="bar" id="bar" style="width:0%;background:var(--green)"></div></div>

  <label>Password length: <strong id="len-lbl">32</strong></label>
  <div class="slider-row">
    <button class="adj" id="dec">−</button>
    <input type="range" id="slider" min="4" max="128" value="32" step="1">
    <button class="adj" id="inc">+</button>
    <span class="len-val" id="len-val">32</span>
  </div>

  <label>Characters used:</label>
  <div class="checks">
    <label class="chk"><input type="checkbox" id="cu" checked> ABC</label>
    <label class="chk"><input type="checkbox" id="cl" checked> abc</label>
    <label class="chk"><input type="checkbox" id="cn" checked> 123</label>
    <label class="chk"><input type="checkbox" id="cs" checked> #$&</label>
    <label class="chk"><input type="checkbox" id="ce"> 🔥 Extra</label>
  </div>

  <div class="stats">
    <div class="stat"><div class="stat-val" id="s-bits">—</div><div class="stat-lbl">entropy bits</div></div>
    <div class="stat"><div class="stat-val" id="s-pool">—</div><div class="stat-lbl">pool size</div></div>
    <div class="stat"><div class="stat-val" id="s-crack">—</div><div class="stat-lbl">crack time</div></div>
  </div>

  <div class="btns">
    <button class="primary gen" onclick="generate()">Generate</button>
    <button class="primary" id="copy-btn" onclick="copyPw()">Copy</button>
  </div>
</div>

<script>
async function generate() {
  const params = new URLSearchParams({
    length: document.getElementById('slider').value,
    upper:  document.getElementById('cu').checked,
    lower:  document.getElementById('cl').checked,
    digits: document.getElementById('cn').checked,
    symbols:document.getElementById('cs').checked,
    extra:  document.getElementById('ce').checked,
  });
  const res = await fetch('/api/generate?' + params);
  const d = await res.json();
  document.getElementById('pw-out').textContent = d.password;

  const badge = document.getElementById('badge');
  badge.textContent = d.strength;
  badge.className = 'badge ' + d.strength_cls;

  const pct = Math.min(d.bits / 128 * 100, 100);
  const bar = document.getElementById('bar');
  bar.style.width = pct + '%';
  bar.style.background = d.bar_color;

  document.getElementById('s-bits').textContent  = d.bits.toFixed(1);
  document.getElementById('s-pool').textContent  = d.pool_size;
  document.getElementById('s-crack').textContent = d.crack_time;
}

function setLen(v) {
  document.getElementById('slider').value = v;
  document.getElementById('len-lbl').textContent = v;
  document.getElementById('len-val').textContent = v;
  generate();
}

document.getElementById('slider').addEventListener('input', function() {
  document.getElementById('len-lbl').textContent = this.value;
  document.getElementById('len-val').textContent = this.value;
  generate();
});
document.getElementById('dec').onclick = () => {
  const s = document.getElementById('slider');
  if (+s.value > 4) setLen(+s.value - 1);
};
document.getElementById('inc').onclick = () => {
  const s = document.getElementById('slider');
  if (+s.value < 128) setLen(+s.value + 1);
};
['cu','cl','cn','cs','ce'].forEach(id =>
  document.getElementById(id).addEventListener('change', generate));

async function copyPw() {
  const pw = document.getElementById('pw-out').textContent;
  if (!pw || pw === '—') return;
  await navigator.clipboard.writeText(pw);
  const btn = document.getElementById('copy-btn');
  btn.textContent = '✓ Copied!';
  btn.classList.add('copied');
  setTimeout(() => { btn.textContent = 'Copy'; btn.classList.remove('copied'); }, 2000);
}

generate();
</script>
</body>
</html>
"""


def web_mode():
    try:
        from flask import Flask, request, jsonify
    except ImportError:
        print("Flask not installed. Run: pip install flask")
        sys.exit(1)

    app = Flask(__name__)

    @app.route("/")
    def index():
        return HTML_TEMPLATE

    @app.route("/api/generate")
    def api_generate():
        length  = int(request.args.get("length", 32))
        length  = max(4, min(128, length))
        upper   = request.args.get("upper",   "true") == "true"
        lower   = request.args.get("lower",   "true") == "true"
        digits  = request.args.get("digits",  "true") == "true"
        symbols = request.args.get("symbols", "true") == "true"
        extra   = request.args.get("extra",   "false") == "true"

        pool = build_pool(upper=upper, lower=lower, digits=digits,
                          symbols=symbols, extra=extra)
        pw   = generate_password(length, pool)
        bits = entropy_bits(length, len(pool))
        sl   = strength_label(bits)
        cls_map = {
            "Weak": "w-weak", "Fair": "w-fair", "Strong": "w-strong",
            "Very strong": "w-verystrong", "Unbreakable": "w-unbreakable"
        }
        bar_map = {
            "Weak": "#E24B4A", "Fair": "#EF9F27", "Strong": "#639922",
            "Very strong": "#0F6E56", "Unbreakable": "#185FA5"
        }
        return jsonify({
            "password":    pw,
            "bits":        bits,
            "pool_size":   len(pool),
            "crack_time":  crack_time_label(bits),
            "strength":    sl,
            "strength_cls": cls_map[sl],
            "bar_color":   bar_map[sl],
        })

    print("\n  🔐 Password Generator running at http://localhost:5000\n")
    app.run(debug=False, port=5000)


if __name__ == "__main__":
    cli_mode()