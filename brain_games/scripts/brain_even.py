from brain_games.cli import welcome_user
from brain_games.even_game import run_game
from brain_games.greeting import greet


def main():
    greet()
    user_name = welcome_user()
    run_game(user_name)


if __name__ == "__main__":
    main()
