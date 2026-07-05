class ProfileAnalyzer:

    def analyze_profile(self, name, profession, interests, event):
        return {
            "name": name,
            "profession": profession,
            "interests": interests,
            "event": event,
            "summary": f"{name} is a {profession} attending {event} with interests in {interests}.",
            "networking_goal": "Connect with professionals having similar interests."
        }