class ProfileAnalyzer:
    """
    Analyzes user profile information.
    """

    def analyze_profile(self, name, interests, event):
        profile = {
            "name": name,
            "interests": interests,
            "event": event
        }

        return profile