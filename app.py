from flask import Flask, request, jsonify, render_template
from collections import deque

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

def wordLadder(beginWord, endWord, wordList):
    wordSet = set(wordList)

    if endWord not in wordSet:
        return []

    queue = deque()
    queue.append((beginWord, [beginWord]))

    visited = set([beginWord])

    while queue:
        currentWord, path = queue.popleft()

        if currentWord == endWord:
            return path

        for i in range(len(currentWord)):
            for a in range(26):
                letter = chr(ord('a') + a)
                newWord = currentWord[:i] + letter + currentWord[i+1:]

                if newWord in wordSet and newWord not in visited:
                    queue.append((newWord, path + [newWord]))
                    visited.add(newWord)

    return []


@app.route("/ladder", methods=["POST"])
def ladder():
    data = request.json

    path = wordLadder(
        data["begin"],
        data["end"],
        data["words"]
    )

    return jsonify({
        "steps": len(path),
        "path": path
    })


if __name__ == "__main__":
    app.run(debug=True)