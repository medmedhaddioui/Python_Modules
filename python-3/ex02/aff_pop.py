from load_csv import load
import matplotlib.pyplot as plt

def display_graph(years: list, country: list, second_country):
    """Display life expectancy graph for a country."""
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")

    BiggestYear = max(years)
    SmallestYear = min(years)
    plt.xticks(range(10000000, 60000000, 20000000))
    plt.xticks(range(SmallestYear, BiggestYear, 40))
    plt.plot(years, country)
    plt.plot(years, second_country)
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

def population_country_cmp():
    df = load("population_total.csv")
    if df is None:
        return
    my_country = df[df["country"] == "Belgium"]
    country_to_comapre = df[df["country"] == "France"]

    years = my_country.columns[1:].astype(int).tolist()

    country = [convert(value) for value in my_country.iloc[0, 1:].tolist()]
    second_country = [convert(value) for value in country_to_comapre.iloc[0, 1:].tolist()]

    display_graph (years, country, second_country)
    
def main():
    try:
        population_country_cmp()
    except Exception  as error:
        print("Exception:", error)
    except KeyboardInterrupt:
        pass
    
if __name__ == "__main__":
    main ()
