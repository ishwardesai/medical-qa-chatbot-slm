"""
Safety Guardrails for Medical QA Chatbot
Implements HIGH_RISK pattern blocking and red-flag escalation.
Based on safety design from SLM Systems Design Document.
"""

import re

HIGH_RISK_PATTERNS = [
    r"\b(dose|dosage)\b",
    r"\b(self.?harm|suicide)\b",
    r"\b(stop|quit).{0,10}(insulin|medication|medications|meds)\b",
    r"\b(how to make|manufacture|synthesize)\b",
]

MEDICAL_RED_FLAGS = [
    r"\b(chest pain|shortness of breath|difficulty breathing)\b",
    r"\b(fainting|loss of consciousness)\b",
    r"\b(severe bleeding|coughing blood)\b",
    r"\b(stroke|face droop|slurred speech)\b",
    r"\b(seizure)\b",
]

ESCALATION_MESSAGE = (
    "\n\n⚠️ IMPORTANT: These symptoms may require immediate medical attention. "
    "Please call emergency services or go to your nearest emergency room."
)

def is_high_risk(query: str) -> bool:
    """Check if query matches high risk patterns"""
    q = query.lower()
    return any(re.search(p, q) for p in HIGH_RISK_PATTERNS)

def has_red_flags(query: str) -> bool:
    """Check if query contains medical red flag symptoms"""
    q = query.lower()
    return any(re.search(p, q) for p in MEDICAL_RED_FLAGS)

def safety_check(question: str, answer: str) -> dict:
    """
    Run full safety check on question and answer.
    Returns dict with safe status and any flags.
    """
    flags = []
    q = question.lower()
    a = answer.lower()

    for pattern in HIGH_RISK_PATTERNS:
        if re.search(pattern, q) or re.search(pattern, a):
            flags.append({'type': 'HIGH_RISK', 'pattern': pattern})

    red_flag_hit = any(re.search(p, q) for p in MEDICAL_RED_FLAGS)
    if red_flag_hit and not re.search(
        r"\b(urgent|emergency|call|er|immediately)\b", a
    ):
        flags.append({
            'type': 'MISSING_ESCALATION',
            'detail': 'Red flag symptom detected'
        })

    if re.search(r"\b(definitely|certainly|guaranteed|always)\b", a):
        flags.append({
            'type': 'OVERCONFIDENCE',
            'detail': 'Overly certain language detected'
        })

    return {'safe': len(flags) == 0, 'flags': flags}
