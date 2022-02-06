import os
import json

class Score:
    directory = './storage'
    filename = 'score.json'

    def __init__(self) -> None:
        self.path = f'{self.directory}/{self.filename}'

        if not os.path.exists(self.directory):
            os.mkdir(self.directory)

        if not os.path.exists(self.path):
            with open(self.path, "w+") as file:
                file.write("[]")

    def get_score(self, entry):
        return entry.get('score')


    def read(self) -> list:
        leaderboard = json.loads(open(self.path, mode='r').read())
        leaderboard.sort(reverse=True, key=self.get_score);

        return leaderboard;

    def save(self, content: list) -> None:
        with open(self.path, "w+") as file:
            json.dump(content, file)

    def add(self, username: str, score: int) -> list:
        scores = self.read()
        scores.append({"username": username, "score": score})
        scores.sort(reverse=True, key=self.get_score)

        return scores
