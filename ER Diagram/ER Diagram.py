from graphviz import Digraph

er = Digraph("ER_Diagram", format="png")
er.attr(rankdir="TB", fontsize="12")

# Entities
er.node("User",
"""USER PROFILE
-----------------------
PK UserID
BioText
CurrentEventCache
""", shape="record")

er.node("Session",
"""NETWORKING SESSION
-----------------------
PK SessionID
FK UserID
FK EventID
SessionTimestamp
""", shape="record")

er.node("Event",
"""EVENT CONTEXT
-----------------------
PK EventID
EventDescription
AnalyzedThemes
""", shape="record")

er.node("Starter",
"""GENERATED STARTER
-----------------------
PK StarterID
FK SessionID
StarterText
ContextPromptUsed
""", shape="record")

er.node("Fact",
"""WIKIPEDIA FACT CHECK
-----------------------
PK FactCheckID
FK SessionID
VerifiedQueryText
VerificationStatus
WikipediaSourceURL
""", shape="record")

er.node("Log",
"""LOG ENTRY
-----------------------
PK LogID
FK SessionID
ActionType
PayloadJSON
Timestamp
""", shape="record")

# Relationships
er.edge("User", "Session", label="1 : Many")
er.edge("Event", "Session", label="1 : Many")
er.edge("Session", "Starter", label="1 : Many")
er.edge("Session", "Fact", label="1 : Many")
er.edge("Session", "Log", label="1 : Many")

# Save diagram
er.render("ER_Diagram", cleanup=True)

print("ER Diagram generated successfully!")
