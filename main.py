import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))

def draw_workflow(ax, title, nodes, lines, is_proposed=False):
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    for node in nodes:
        x, y, w, h, txt, col = node
        rect = patches.FancyBboxPatch((x-w/2, y-h/2), w, h, boxstyle="round,pad=0.2",
                                     fc=col, ec="black", lw=2)
        ax.add_patch(rect)
        ax.text(x, y, txt, ha='center', va='center', fontsize=9, fontweight='bold')

    for line in lines:
        x1, y1, x2, y2, txt = line
        ax.annotate(txt, xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", lw=1.5),
                    fontsize=8, ha='center')

# --- CURRENT STATE ---
nodes1 = [
    (5, 9, 2, 1, "MEMBER CALLS", "white"),
    (5, 7, 3, 1, "CONTACT CENTRE\n(Verify Only)", "skyblue"),
    (5, 4, 3, 1, "FRAUD TEAM / BUREAU\n(The Bottleneck)", "#e74c3c"),
    (5, 1.5, 3, 1, "UNBLOCK / RESOLVE", "#2ecc71")
]
lines1 = [
    (5, 8.5, 5, 7.5, ""),
    (5, 6.5, 5, 4.5, "100% Escalation\n(Long Wait)"),
    (5, 3.5, 5, 2, "")
]

# --- PROPOSED STATE ---
nodes2 = [
    (5, 9, 2, 1, "MEMBER CALLS", "white"),
    (5, 7, 3, 1, "CONTACT CENTRE\n(Triage)", "skyblue"),
    (2.5, 4.5, 2.5, 1, "SENIOR CC OFFICER\n(Low-Risk Auth)", "#f1c40f"),
    (7.5, 4.5, 2.5, 1, "FRAUD TEAM\n(High-Risk Only)", "#e74c3c"),
    (5, 1.5, 3, 1, "UNBLOCK / RESOLVE", "#2ecc71")
]
lines2 = [
    (5, 8.5, 5, 7.5, ""),
    (4, 6.6, 2.5, 5.1, "Tier 1: Confirmed\n(Fast Track)"),
    (6, 6.6, 7.5, 5.1, "Tier 2 & 3\n(Specialist)"),
    (2.5, 3.9, 4.5, 2, ""),
    (7.5, 3.9, 5.5, 2, "")
]

draw_workflow(ax1, "CURRENT STATE:\nThe Bottleneck", nodes1, lines1)
draw_workflow(ax2, "PROPOSED STATE:\nRisk-Based Triage", nodes2, nodes2, is_proposed=True) # Reusing list for simplicity in dummy call

# Re-calling proposed lines properly
for line in lines2:
    ax2.annotate(line[4], xy=(line[2], line[3]), xytext=(line[0], line[1]),
                arrowprops=dict(arrowstyle="->", lw=1.5), fontsize=8, ha='center')

plt.tight_layout()
plt.savefig('fraud_workflow_optimization.png')
print("Diagram saved.")
