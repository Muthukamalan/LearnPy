import typer


def main(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)


# Terminal
# $ python main.py --help
# $ python main.py Muthu
# $ typer main.py run         >> Implicitly create `typer.Typer` for you