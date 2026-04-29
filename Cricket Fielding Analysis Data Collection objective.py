import pandas as pd

# -----------------------------------
# Step 1: Dataset (You can modify this)
# -----------------------------------
data = [
    [1, 1, "MI", "Player A", 2, "Point", "Stops boundary", "Clean Pick", "None", 2, 3, "Mumbai"],
    [1, 1, "MI", "Player A", 4, "Cover", "Takes catch", "Catch", "None", 1, 5, "Mumbai"],
    [1, 1, "MI", "Player A", 1, "Point", "Misfield", "Fumble", "None", -2, 8, "Mumbai"],

    [1, 1, "MI", "Player B", 3, "Midwicket", "Good stop", "Clean Pick", "None", 1, 2, "Mumbai"],
    [1, 1, "MI", "Player B", 5, "Deep", "Misfield", "Fumble", "None", -3, 6, "Mumbai"],
    [1, 1, "MI", "Player B", 2, "Deep", "Run out missed", "Good Throw", "Missed Run Out", -2, 10, "Mumbai"],

    [1, 1, "MI", "Player C", 1, "Wicketkeeper", "Run out", "Clean Pick", "Run Out", 2, 4, "Mumbai"],
    [1, 1, "MI", "Player C", 3, "Wicketkeeper", "Good stop", "Clean Pick", "None", 1, 7, "Mumbai"],
    [1, 1, "MI", "Player C", 6, "Wicketkeeper", "Miss", "Fumble", "None", -1, 9, "Mumbai"],
]

columns = [
    "Match No", "Innings", "Team", "Player Name", "Ballcount",
    "Position", "Short Description", "Pick", "Throw",
    "Runs", "Overcount", "Venue"
]

df = pd.DataFrame(data, columns=columns)

print("\n📊 DATASET:\n")
print(df)

# -----------------------------------
# Step 2: Fielding Metrics
# -----------------------------------

# Total chances
total_chances = df.groupby("Player Name").size()

# Clean picks
clean_picks = df[df["Pick"] == "Clean Pick"].groupby("Player Name").size()

# Errors
errors = df[df["Pick"].isin(["Fumble", "Drop Catch", "Bad Throw"])].groupby("Player Name").size()

# Run outs
run_outs = df[df["Throw"] == "Run Out"].groupby("Player Name").size()

# Runs saved
runs_saved = df[df["Runs"] > 0].groupby("Player Name")["Runs"].sum()

# Runs conceded
runs_conceded = df[df["Runs"] < 0].groupby("Player Name")["Runs"].sum()

# -----------------------------------
# Step 3: Performance Matrix
# -----------------------------------
summary = pd.DataFrame({
    "Total Chances": total_chances,
    "Clean Picks": clean_picks,
    "Errors": errors,
    "Run Outs": run_outs,
    "Runs Saved": runs_saved,
    "Runs Conceded": runs_conceded
}).fillna(0)

# Net Impact
summary["Net Impact"] = summary["Runs Saved"] + summary["Runs Conceded"]

# Efficiency Score
summary["Efficiency"] = (summary["Clean Picks"] / summary["Total Chances"]) * 100

print("\n📈 PERFORMANCE SUMMARY:\n")
print(summary)

# -----------------------------------
# Step 4: Best Player
# -----------------------------------
best_player = summary["Net Impact"].idxmax()

print(f"\n🏆 BEST FIELDER: {best_player}")

# -----------------------------------
# Step 5: Save to Excel (for submission)
# -----------------------------------
summary.to_excel("fielding_analysis_output.xlsx")

print("\n📁 Excel file saved as 'fielding_analysis_output.xlsx'")