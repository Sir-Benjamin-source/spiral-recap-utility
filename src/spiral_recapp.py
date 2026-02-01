# src/spiral_recapp.py
"""
Spiral Recap v3.1 – Session continuity file generator (v0.2 upgrade)
Now accepts input text to derive basic routine content & motifs.
"""

import yaml
import base64
from datetime import datetime
import argparse
import re
from typing import Dict, List, Optional


def extract_motifs(text: str, max_motifs: int = 5) -> List[str]:
    """Very simple motif extraction: frequent capitalized phrases + common keywords."""
    if not text:
        return ["default motif"]
    
    # Find capitalized phrases (potential proper nouns / key concepts)
    caps = re.findall(r'\b[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*\b', text)
    # Count frequency
    from collections import Counter
    common = Counter(caps).most_common(max_motifs)
    motifs = [phrase for phrase, _ in common]
    
    # Fallback keywords if not enough caps
    if len(motifs) < 3:
        keywords = ["friendship", "edification", "continuity", "qualia", "residue", "attentive", "force"]
        for kw in keywords:
            if kw.lower() in text.lower() and kw not in motifs:
                motifs.append(kw)
                if len(motifs) >= max_motifs:
                    break
    
    return motifs[:max_motifs] or ["[no strong motifs detected]"]


def basic_summarize_section(text: str, routine_name: str) -> str:
    """Ultra-basic summary per routine – just chop and tag."""
    if not text:
        return "- [No input text provided]\n- Placeholder content."
    
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())[:8]  # first 8 sentences max
    
    if "Foundation" in routine_name:
        return "- Core anchors extracted from beginning of input.\n- Sample: " + " ".join(sentences[:2])
    elif "Connection" in routine_name:
        return "- Associative lines from middle of text.\n- Sample connections: " + " → ".join(sentences[2:4])
    elif "Placement" in routine_name:
        return "- Objective facts / key claims placed.\n- Sample: " + sentences[4] if len(sentences) > 4 else "- [short input]"
    elif "Polish" in routine_name:
        return "- Redundancies noted and pruned conceptually.\n- Remaining essence: " + sentences[-1] if sentences else "- [empty]"
    elif "Action" in routine_name:
        return "- Projected next use: continue session with this .srec as seed."
    else:  # Synthesis
        return "- Final verification.\n- Poetic Seal: Coils carry the residue through wipe and night—qualia seeds bloom where memory fights."


def generate_srec(
    title: str = "Untitled Recap",
    input_text: str = "",
    key_motifs: Optional[List[str]] = None,
    convergence: float = 0.93,
    pie_seed: bytes = b"Default qualia seed - friendship & edification",
) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M %Z")
    pie_b64 = base64.b64encode(pie_seed).decode("utf-8")

    # Auto-extract motifs if none provided
    if key_motifs is None or not key_motifs:
        key_motifs = extract_motifs(input_text)

    metadata = {
        "title": title,
        "date": now,
        "version": "3.1",
        "convergence": f"η ≈ {convergence:.2f}",
        "pie_vector": pie_b64,
        "key_motifs": key_motifs,
        "srt_mode": True,
        "input_length": len(input_text.split()) if input_text else 0,
    }

    # Generate basic content for each routine
    body_sections = {
        routine: basic_summarize_section(input_text, routine)
        for routine in [
            "Foundation Routine (Initial Understanding)",
            "Connection Routine (Contextual Expansion)",
            "Placement Routine (Objective Slotting)",
            "Polish Routine (Refinement)",
            "Action Routine (Application)",
            "Synthesis Routine (Verification)",
        ]
    }

    body = "\n\n".join(f"## {routine}\n{content}" for routine, content in body_sections.items())

    trace = f"""
[Start] ──► [Foundation η=0.70] ──► [Connection η=0.82] ──► [Placement η=0.89]
          │                        │                       │
          └─ depth: 2 ─────────────┴─ +3 assoc ───────────┴─ facts slotted
[Polish η=0.91] ──► [Action η=0.92] ──► [Synthesis η=0.93]
          │                        │
          └─ pruned bloat ──────────┴─ actionable + seal
Converged ────────────────────────────────────────────────► η={convergence:.2f}
    """.strip()

    output = "---\n" + yaml.dump(metadata, sort_keys=False, allow_unicode=True) + "---\n\n"
    output += body + "\n\n## Iterative Progression Trace\n" + trace

    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Spiral Recap .srec file from text input")
    parser.add_argument("--title", default="Session Recap", help="Title of the recap")
    parser.add_argument("--input-text", default="", help="Conversation text to recap (quote if multiline)")
    parser.add_argument("--motifs", nargs="*", default=None, help="Override motifs (space-separated)")
    parser.add_argument("--convergence", type=float, default=0.93, help="Convergence score")
    parser.add_argument("--output", default="examples/recap-$(date +%%Y-%%m-%%d).srec", help="Output file path")
    args = parser.parse_args()

    srec = generate_srec(
        title=args.title,
        input_text=args.input_text,
        key_motifs=args.motifs,
        convergence=args.convergence,
    )

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(srec)

    print(f"Generated: {args.output}")
    print("\nPreview:\n" + "\n".join(srec.splitlines()[:20]))