import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Bar Chart: Effectiveness of Different Adaptive Learning Techniques
techniques = ['AI-Based Tutoring', 'Gamification', 'Interactive Videos', 'Adaptive Quizzes']
effectiveness = [85, 75, 80, 90]  # Effectiveness in percentage

plt.figure(figsize=(7, 5))
sns.barplot(x=techniques, y=effectiveness, palette='viridis')
plt.ylabel('Effectiveness (%)')
plt.xlabel('Adaptive Learning Techniques')
plt.title('Effectiveness of Different Adaptive Learning Techniques')
plt.ylim(0, 100)
plt.xticks(rotation=20)
plt.show()

# Line Chart: Learning Progress Over Time
weeks = np.arange(1, 11)  # 10 weeks of learning
progress = np.cumsum(np.random.randint(5, 15, size=10))  # Cumulative progress in learning score

plt.figure(figsize=(7, 5))
plt.plot(weeks, progress, marker='o', linestyle='-', color='purple', label='Learning Progress')
plt.xlabel('Weeks')
plt.ylabel('Learning Score')
plt.title('Student Learning Progress Over Time')
plt.legend()
plt.grid(True)
plt.show()

