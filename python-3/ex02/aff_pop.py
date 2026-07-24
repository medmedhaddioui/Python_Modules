from load_csv import load
import matplotlib.pyplot as plt

def main():
    df = load("population_total.csv")
    if df is None:
        return
    my_country = df[df["country"] == "Morocco"]
    country_to_comapre = df[df["country"] == "France"]
    
if __name__ == "__main__":
    main ()
# wifi@1337++@