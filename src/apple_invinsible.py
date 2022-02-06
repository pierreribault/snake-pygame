from src.apple import Apple

class InvinsibleApple(Apple):
    color = (179, 179, 179)
    point = 50
    duration = 300

    def power(self) -> int:
        return self.duration
