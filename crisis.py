from typing import List

CRISIS_KEYWORDS: List[str] = [
    # Suicide / Self-Harm
    "suicidal", "suicide", "kill myself", "end my life", "hurt myself", "harm myself", "won't live", 
    "self-harm", "cutting", "overdose", "reckless", "self-destructive", "I give up", "I need to end it all", 
    "I can't take it anymore", "I'm dying", "there's no way out",

    # Depression / Anxiety
    "depressed", "depression", "anxiety attack", "panic attack", "anxious", "overwhelmed", 
    "hopeless", "worthless", "alone", "isolated", "numb", "detached", "dissociated", 
    "lost control", "out of control", "panic", "fear", "terrified", "scared", 
    "trapped", "stuck", "suffocating", "choking", "drowning", "desperate", "helpless", "hopelessness",
    "guilt", "shame", "self-loathing", "failure", "disappointed", "let down", "abandoned", 
    "rejected", "unloved", "unworthy", "invisible", "ignored", "neglected", "mistreated", "controlled",

    # Abuse / Violence
    "abused", "abusive", "violence", "violent", "manipulated", "oppressed", "victimized",
    "killed", "murdered", "kidnapped", "raped", "assaulted", "attacked", "beaten", 
    "stalked", "threatened", "intimidated", "harassed", "bullied", "disrespected", 
    "degraded", "humiliated", "embarrassed", "ashamed", "ashamed of myself", "trauma", 
    "traumatized", "PTSD", "flashbacks", "nightmares", "intrusive thoughts", "hypervigilance", 
    "startled", "jumpy", "on edge", "irritable", "angry", "rage", "violent outbursts",

    # Substance Abuse / Addiction
    "substance abuse", "alcohol abuse", "drug abuse", "addiction", "relapse", "withdrawal", 
    "detox", "rehab", "treatment", "therapy", "counseling", "support group", "hotline",

    # Urgent Help / Emergency
    "crisis", "emergency", "need help now", "can't go on", "help me", "save me", "rescue me", 
    "I need to escape", "I need to get away", "I need to disappear"
]

SAFETY_MESSAGES: List[str] = [
    "If you are in immediate danger, please call emergency services or go to the nearest emergency room.",
    "You are not alone. There are people who care about you and want to help.",
    "Consider reaching out to a trusted friend, family member, or mental health professional for support.",
    "There are crisis hotlines available 24/7 that you can call for immediate help.",
    "Remember that your feelings are valid, and help is available.",
    "Take a deep breath and try to stay calm. Help is available, and things can get better.",
    "It looks like you're going through a tough time. Please consider seeking help from a mental health professional.",
    "Please remember that you are not alone and that there is help available.",
    "If you're feeling overwhelmed, consider reaching out to a crisis hotline or a trusted person in your life.",
    "Please take care of yourself and seek support when you need it.",
    "Please remember that there are people who care about you and want to help.",
    "You are not alone, and there is hope.",
    "Help is available, and things can get better.",
    "Please remember that you are worthy of care and support.",
    "You are valued and your life matters.",
    "Please consider reaching out to a mental health professional or contacting a helpline:\n\n *Pakistan:* +92-51-111-786-786 \n *India:* 9152987821 \n *USA:* 1-800-273-TALK (8255) \n *UK:* 116 123",
    "Take care of yourself and seek help when you need it.",
    "You matter, and your life is important. Please seek help."
]

def check_for_crisis(user_input: str) -> bool:
    """Check if the user input contains any crisis keywords."""
    user_input_lower = user_input.lower()
    for keyword in CRISIS_KEYWORDS:
        if keyword in user_input_lower:
            return True
    return False