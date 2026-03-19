try:
    from .recommender import load_songs, recommend_songs
except ImportError:
    from recommender import load_songs, recommend_songs


def main():
    songs = load_songs()

    user_prefs = {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.4,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 60)
    print("Top Recommendations")
    print("=" * 60)

    for index, (song, score, explanation) in enumerate(recommendations, start=1):
        print()
        print(f"#{index}  {song['title']} — {song['artist']}")
        print(f"   Score: {score:.2f}")
        print(f"   Reasons: {explanation}")
        print("-" * 60)

    print("=" * 60)


if __name__ == "__main__":
    main()
