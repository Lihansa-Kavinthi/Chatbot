CRISIS_KEYWORDS = ["suicide", "kill myself", "end my life", "self harm", "hurt myself"]

def is_crisis(text):
    return any(kw in text.lower() for kw in CRISIS_KEYWORDS)

def crisis_message():
    return (
        "💙 I'm really concerned about you. "
        "Please reach out to a crisis helpline immediately.\n\n"
        "🇱🇰 **Sri Lanka:** Sumithrayo — 011 2696 666\n"
        "🌍 **International:** befrienders.org"
    )