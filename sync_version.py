import colorama
from services import get_weather


def main():
    print(colorama.Fore.GREEN +
          "------------------------------------------\n"
          "| App created by alexfrunza              |\n"
          "| Welcome to weather app (sync version)  |\n"
          "| Enter a city name to get weather       |\n"
          "| Or type x to close it                  |\n"
          "------------------------------------------\n")

    while True:
        city_name = input()

        if city_name == "x":
            print("App is closing...")
            break

        get_weather(city_name)


if __name__ == '__main__':
    main()
