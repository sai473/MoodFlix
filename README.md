# 🎬 Mood-Based Movie Recommender (Flask App)

This is a Flask-based web application that recommends Indian movies based on your current mood. The system infers your mood from a set of 5 simple questions and maps it to relevant movie genres.

---

## 🚀 Features

- 🧠 Logic-based mood detection using weighted scoring
- 🎥 Genre-filtered movie recommendations
- 🔀 Randomized results on each submission for variety
- 💡 Clean HTML UI with aesthetic slideshow background (optional)

---

## 🧰 Tech Stack

- **Flask** (Python web framework)
- **Pandas** (for CSV filtering)
- **HTML/CSS** (Jinja templates)
- **VS Code + Git + GitHub**

---

## 📁 Project Structure

```
movie-recommender/
│
├── movie.py                  # Flask app
├── dataset_indian.csv        # Indian movie dataset (optional to upload)
├── requirements.txt          # Python package dependencies
├── .gitignore
├── README.md
│
├── static/                   # Poster images (for slideshow bg)
│   ├── poster1.jpg
│   ├── poster2.jpg
│   └── ...
│
└── templates/                # HTML Templates
    ├── index.html
    ├── recommend.html
    └── error.html
```

---

## 🧠 Mood Inference Logic

User answers to questions like:
- What type of activity would you prefer right now?
- What kind of pace do you enjoy in a movie?

...are mapped to moods like:
- `Excited` → Action, Sci-Fi, Thriller
- `Romantic` → Romance, Drama
- `Cheerful` → Comedy, Feel-good
- `Melancholic` → Historical, Drama
- `Mysterious`, `Curious`, `Scared`, etc.

Genres are filtered accordingly, and movies are randomly picked.

---

## ⚙️ Local Setup

### 🐍 Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### ▶️ Step 2: Run Flask App
```bash
python movie.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 📌 Notes

- If you're using `dataset_indian.csv`, you can `.gitignore` it to avoid pushing large files.
- This project is ideal for academic/portfolio/demo purposes.

---

## 📜 License

MIT License.  
You're free to use, modify, or extend this project. Attribution appreciated!

---

## 🌐 Author

Made with 💻 in Python & Flask by [Your Name]  
Feel free to ⭐️ the repo if you like it!