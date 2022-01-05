# https://replit.com/@Mmesek/fcc-probability-calculator
import copy
import random

random.seed(95)


class Hat:
    def __init__(self, **balls) -> None:
        self.contents = []
        for ball in balls:
            for i in range(balls[ball]):
                self.contents.append(ball)

    def draw(self, amount: int):
        if amount > len(self.contents):
            balls = self.contents
            self.contents = []
            return balls
        else:
            balls = random.sample(self.contents, k=amount)
        for ball in balls:
            self.contents.remove(ball)
        return balls


def experiment(hat: Hat, expected_balls: dict, num_balls_drawn: int, num_experiments: int) -> float:
    m = 0
    for i in range(num_experiments):
        _hat = copy.deepcopy(hat)
        balls = _hat.draw(num_balls_drawn)
        if all(balls.count(expected) >= value for expected, value in expected_balls.items()):
            m += 1
    return m / num_experiments


hat = Hat(blue=3, red=2, green=6)
hat.draw(2)
hat = Hat(blue=3, red=2, green=6)
print(experiment(hat=hat, expected_balls={"blue": 2, "green": 1}, num_balls_drawn=4, num_experiments=1000))
hat = Hat(yellow=5, red=1, green=3, blue=9, test=1)
probability = experiment(
    hat=hat, expected_balls={"yellow": 2, "blue": 3, "test": 1}, num_balls_drawn=20, num_experiments=100
)
print(probability)
