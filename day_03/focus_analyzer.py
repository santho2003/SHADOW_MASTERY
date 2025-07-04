import matplotlib.pyplot as plt


focus_minutes = [60, 75, 30, 90, 45, 120]

total_ft = sum(focus_minutes)
avg_ft = total_ft/len(focus_minutes)
best_focus = max(focus_minutes)
worst_focus = min(focus_minutes)

with open("focus_stats.txt", "w") as file:
    file.write(f"Total: {total_ft} mins\n")
    file.write(f"Average: {avg_ft:.2f} mins\n")
    file.write(f"Best Focus: {best_focus} mins\n")
    file.write(f"Worst Focus: {worst_focus} mins\n")

# plot
plt.bar(range(1,len(focus_minutes)+1), focus_minutes, color='skyblue')
plt.xlabel("Session")
plt.ylabel("Focus Minutes")
plt.title("Focus Minutes Per Session")
plt.savefig("Focus_chart.png")
plt.show()

    