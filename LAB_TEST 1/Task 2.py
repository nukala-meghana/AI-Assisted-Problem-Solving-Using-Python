def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle using the formula πr².

    Parameters:
        radius (float): The radius of the circle. Must be > 0.

    Returns:
        float: The computed area of the circle.

    Raises:
        ValueError: If the radius is zero or negative.

    Example:
        >>> calculate_circle_area(5)
        78.5
    """
    if radius <= 0:
        raise ValueError("Radius must be a positive number")

    PI = 3.14
    return PI * radius * radius


# Taking input from user
try:
    r = float(input("Enter radius of the circle: "))
    result = calculate_circle_area(r)
    print("Area of Circle:", result)
except ValueError as e:
    print("Error:", e)
