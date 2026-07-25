from load_csv import load
import matplotlib.pyplot as plt

def display_graph(years: list, country: list, second_country:list, country_name: str, second_country_name: str):
    """Display life expectancy graph for a country."""
    
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")

    end = 2050 - 1800 + 1
    BiggestYear = max(years[:end])
    SmallestYear = min(years[:end])

    plt.plot(years[:end], country[:end], color="green", label=country_name)
    plt.plot(years[:end], second_country[:end], label=second_country_name)

    plt.yticks([20000000, 40000000, 60000000], ["20M", "40M", "60M"])
    plt.xticks(range(SmallestYear, BiggestYear, 40))

    plt.legend(loc='lower right')
    plt.show()


def convert(value):
    if value.endswith("M"):
        return float(value[:-1]) * 1_000_000
    elif value.endswith("B"):
        return float(value[:-1]) * 1_000_000_000
    elif value.endswith("K"):
        return float(value[:-1]) * 1_000
    else:
        return float(value)


def population_country_cmp(country_name: str, second_country_name: str):

    df = load("population_total.csv")
    if df is None:
        raise Exception("Error loading csv file")

    my_country = df[df["country"] == country_name]
    country_to_comapre = df[df["country"] == second_country_name]

    years = my_country.columns[1:].astype(int).tolist()
    country = [convert(value) for value in my_country.iloc[0, 1:].tolist()]
    second_country = [convert(value) for value in country_to_comapre.iloc[0, 1:].tolist()]
    display_graph (years, country, second_country, country_name, second_country_name)


def main():
    try:
        population_country_cmp("France", "Belgium")
    except Exception  as error:
        print("Exception:", error)
    except KeyboardInterrupt:
        pass
    
if __name__ == "__main__":
    main ()
