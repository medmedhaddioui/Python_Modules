from load_csv import load
import matplotlib.pyplot as plt

def display_graph(year_life_expectancy: list, year_gdp: list, year:str):

    plt.title(year)
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.xscale('log')
    plt.scatter(year_gdp, year_life_expectancy)
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.show()


def projection_life(year: str):
    df = load ("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df2 = load ("life_expectancy_years.csv")
    if (df is None or df2 is None):
        raise Exception("Error loading csv files")

    year_life_expectancy = df2[year].astype(float).tolist()
    year_gdp = df[year].astype(float).tolist()

    display_graph(year_life_expectancy, year_gdp, year)


def main ():
    try:
        projection_life("1900")
    except Exception as error:
        print ("Exception", error)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
