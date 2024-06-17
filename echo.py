def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    echo_text = ""
    for i in range(repetitions, 0, -1):
        echo_text += f"{text[-i:]}\n"
    return f"{echo_text.lower()}."

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))