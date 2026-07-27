from load_csv import load
import matplotlib.pyplot as plt


def display_graph(years: list, country: list):
    """Display life expectancy graph for a country."""

    plt.title("Morocco Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")

    BiggestYear = max(years)
    SmallestYear = min(years)
    plt.xticks(range(SmallestYear, BiggestYear, 40))
    plt.plot(years, country)
    plt.show()


def aff_life_country(country: str):
    """Load dataset and display life expectancy graph for a country."""

    df = load("life_expectancy_years.csv")
    if df is None:
        raise Exception("Error loading csv files")

    selected_country = df[df["country"] == country]
    if selected_country.empty:
        raise ValueError("Error: Country not found in dataset.")
    country_series = selected_country.iloc[0, 1:]
    if country_series.isna().all():
        raise ValueError(
            "Error: no life expectancy data available for Morocco."
        )
    years = selected_country.columns[1:].astype(int).tolist()
    country = country_series.astype(float).tolist()
    display_graph(years, country)


def main():
    """Main function to execute the program."""

    try:
        aff_life_country("Morocco")
    except Exception as error:
        print("Error:", error)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
