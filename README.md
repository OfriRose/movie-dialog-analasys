# 🎬 Movie Dialogue Sentiment Analysis

## 📖 Overview
A sentiment analysis project that processes a movie script to uncover the emotional tone of each character and the overall story arc.  
Includes text cleaning, sentiment scoring, and visualizations — a practical NLP and data visualization exercise.

---

## 🛠️ Tech Stack
- **Python**
- **Pandas** – data manipulation
- **Matplotlib & Seaborn** – visualization
- **TextBlob** – sentiment scoring
- **WordCloud** – frequent vocabulary visualization
- **Poetry** – dependency management

---
## 📊 Example Results
see example_result.pdf for an analasys of "Sounds of Music"


## 🚀 How to Run
```bash
# 1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# 2. Install dependencies
poetry install

# 3. Create a directory for the output visualizations
mkdir output

# 4. Run analysis
poetry run python -m src.movie_dialog_analasys.main script.txt output

Outputs (.png files) will appear in the output directory.

