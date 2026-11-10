from blog import ui


def main() -> None:
    while True:
        print(
            """
            Menu%
            1 - Add a post
            2 - Show post
            0 - Exit
            """
        )

        choice = input("Choice ")
        if choice == "1":
            ui.create_post_menu()
        elif choice == "2":
            ui.show_posts_menu()
        elif choice == "0":
            print("Bye")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()