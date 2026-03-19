# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: VibeCheck  

---

## 2. Intended Use  


This recommender suggests songs based on a user’s preferences. It tries to find songs that match the user’s genre, mood, and energy level.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.
The system uses a small dataset of about 20 songs stored in a CSV file. Each song includes features like genre, mood, energy, tempo, valence, danceability, and acousticness. The dataset is limited, so it does not cover all music styles equally.



---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

Each song gets a score based on how well it matches the user’s preferences. The system gives points for matching genre and mood, and also adds points if the song’s energy is close to the user’s target. Songs are then ranked from highest score to lowest, and the top results are recommended.

---


The system tends to favor genre too much, which can create a filter bubble. Songs from other genres are often ignored even if they match the mood or energy. The system also relies heavily on energy, which can cause songs with similar energy but different styles to rank highly.



---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

I tested the system using different user profiles like “High-Energy Pop,” “Chill Lofi,” and “Deep Intense Rock.” I looked at the top 5 results and checked if they matched what a person would expect. I also changed the scoring weights to see how the rankings changed. One surprising result was that some songs appeared even when the mood did not match.


---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  
This system is designed as a simple simulation of how music recommenders work. It is meant for learning and experimentation. It should not be used for real-world music recommendations because the dataset is small and the logic is very basic.

## Ideas for Improvement
- Add more songs and more diverse genres to the dataset  
- Improve the scoring system to better balance genre, mood, and energy  
- Allow partial matches (e.g., treat "indie pop" similar to "pop")  

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
