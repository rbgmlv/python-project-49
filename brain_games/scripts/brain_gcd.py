from brain_games.cli import welcome_user
from brain_games.game_flow import run_game
from brain_games.greeting import greet


def main():
    game_type = "gcd"
    greet()
    user_name = welcome_user()
    run_game(user_name, game_type)


if __name__ == "__main__":
    main()
