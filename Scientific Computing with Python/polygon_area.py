# https://replit.com/@Mmesek/fcc-polygon-area-calculator


class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def set_width(self, width: float):
        self.width = width

    def set_height(self, height: float):
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if any(i > 50 for i in [self.width, self.height]):
            return "Too big for picture."
        return "\n".join(["*" * self.width] * self.height) + "\n"

    def get_amount_inside(self, shape: "Rectangle") -> int:
        return (self.width // shape.width) * (self.height // shape.height)

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, length: int) -> None:
        super().__init__(length, length)

    def set_side(self, side: float):
        self.width = side
        self.height = side

    def __repr__(self) -> str:
        return f"Square(side={self.width})"

    def set_height(self, height: float):
        super().set_width(height)
        return super().set_height(height)

    def set_width(self, width: float):
        super().set_height(width)
        return super().set_width(width)
