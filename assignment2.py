import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sn

font = {
        'size'   : 8
        }

matplotlib.rc('font', **font)


def create_dataframes(uri):
    """
    Parameters
    ----------
    uri : String
        file path as uri
    Returns
    -------
    df : DataFrame
        data frame object after reading data from file uri
    yearly_columned : DataFrame
        return the same dataframe by creating year as index and
        countries as columns

    """
    
    df = pd.read_csv(uri)
    df = df.dropna()
    df = df.set_index("Country Name")
    yearly_indexed = df.copy()
    yearly_indexed = yearly_indexed.drop(
        ['Indicator Name', 'Indicator Code', 'Country Code'], axis=1)

    yearly_indexed = yearly_indexed.T
    yearly_indexed = yearly_indexed.dropna()

    return df, yearly_indexed


def describe_agricultural_land(data):
    """

    Parameters
    ----------
    data : DataFrame
        Dataframe holding the data about agricultural land.
    Returns
    -------
    None.

    """
    countries = ['Zambia', 'Japan', 'Argentina', 'Bulgaria', 'Panama']
    initial_years_data = data.iloc[0:10]
    # initial_years_data = initial_years_data.iloc[:, [0, 1, 2, 3, 4]]
    initial_years_data = initial_years_data[countries]
    # last_years_data = last_years_data.T
    ax = initial_years_data.plot(kind='bar', figsize=(8,6))
    ax.set_title('Agricultural land by %age')
    ax.set_xlabel('Year')
    ax.set_ylabel('Percentage')
    plt.xticks(rotation=0)
    plt.yticks([i for i in range(0, 100, 10)])
    plt.legend(loc="upper right")
    plt.show()
    
    
def describe_electricity_usage(data):
    """

    Parameters
    ----------
    data : DataFrame
        Dataframe holding the data about agricultural land.
    Returns
    -------
    None.

    """
    countries = ['Zambia', 'Japan', 'Argentina', 'Bulgaria', 'Panama']
    initial_years_data = data.iloc[0:10]
    initial_years_data = initial_years_data[countries]
    # last_years_data = last_years_data.T
    ax = initial_years_data.plot(kind='bar', figsize=(8,6))
    ax.set_title('Access to electricity (% of users)')
    ax.set_xlabel('Year')
    ax.set_ylabel('Percentage')
    plt.xticks(rotation=0)
    plt.legend(loc="upper right")
    plt.show()
    

def describe_co2_series(data):
    """
      Parameters
      ----------
      data : DataFrame
          This parameter needs to hold the data for world's CO2 emmission 
          by country.
      
      Returns
      -------
      None.
    
    """
    countries = ['Zambia', 'Japan', 'Argentina', 'Bulgaria', 'Panama',
                 'Venezuela, RB', 'Samoa', 'China', 'Pakistan', 'United States',
                 'Canada', 'Ireland', 'Spain', 'Tunisia']
    countries_data = data[countries]
    plt.figure(figsize=(8,6))
    plt.plot(countries_data, linewidth=0.8)
    plt.xlabel("Year")
    plt.xticks(data.index.tolist()[::4])
    plt.ylabel("CO2 Emmission")
    plt.title("CO2 production in different countries")
    plt.legend(countries, bbox_to_anchor=(1.0, 1), fontsize="7", 
               loc="upper right")
    plt.show()
  

def describe_forest_series(data):
    """
    Parameters
    ----------
    data : DataFrame
        DataFrame object containint the data for forest area.

    Returns
    -------
    None.

    """
    countries = ['Zambia', 'Japan', 'Argentina', 'Bulgaria', 'Panama',
                 'Venezuela, RB', 'Samoa', 'China', 'United States', 'Canada',
                 'Ireland', 'Spain', 'Tunisia', 'Pakistan']
    countries_data = data[countries]
    plt.figure(figsize=(8,6))
    plt.plot(countries_data, linewidth=0.8)
    plt.xlabel("Year")
    plt.xticks(data.index.tolist()[::5])
    plt.ylabel("Forest Area (Sq. Km)")
    plt.title("Forest area in different countries")
    plt.legend(countries, bbox_to_anchor=(1.0, 1), fontsize="7", 
               loc="upper right")
    plt.show()
  

def explain_dataset(dataset):
    """
    Parameters
    ----------
    dataset : DataFrame

    Returns
    -------
    None.

    """
    print(dataset.min())
    print(dataset.max())
    print(dataset.describe())
    print(dataset.median())
    

def prepare_heatmap_data():
    """

    Returns
    -------
    heatmap_data : DataFrames
        Read the datasets for heatmap and return a new dataframe.

    """
    agricultural_data = ("/Users/saniarashid1/Downloads/" + 
    "sania/heatmap_datasets/API_AG.LND.AGRI.ZS_DS2_en_csv_v2_5337949.csv")
    agr_land_data, agr_land_data_year = create_dataframes(agricultural_data)
    
    electricity_access = ("/Users/saniarashid1/Downloads/" + 
    "sania/heatmap_datasets/API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_5336001.csv")
    electricity_access_data, electricity_access_data_year = \
        create_dataframes(electricity_access)
    
    gdp = ("/Users/saniarashid1/Downloads/" + 
    "sania/heatmap_datasets/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_5338426.csv")
    gdp_data, gdp_data_year = create_dataframes(gdp)
    
    life_expect_at_birth = ("/Users/saniarashid1/Downloads/" + 
    "sania/heatmap_datasets/API_SP.DYN.LE00.IN_DS2_en_csv_v2_5338365.csv")
    life_expect_at_birth_data, life_expect_at_birth_data_year = \
        create_dataframes(life_expect_at_birth)
    
    population_growth = ("/Users/saniarashid1/Downloads/" + 
    "sania/heatmap_datasets/API_SP.POP.GROW_DS2_en_csv_v2_5338437.csv")
    population_growth_data, population_growth_data_year = \
        create_dataframes(population_growth)
    
    co2_data_uri =  ("/Users/saniarashid1/Downloads/" + 
    "sania/API_EN.ATM.CO2E.KT_DS2_en_csv_v2_5181545.csv")
    co2_data, co2_data_year = create_dataframes(co2_data_uri)
    
    heatmap_data = pd.DataFrame({
            "Agricultural land (% of land area)": agr_land_data['2010'],
            "Access to electricity (% of population)": electricity_access_data['2010'],
            "GDP (current US$)": gdp_data['2010'],
            "Life expectancy at birth": agr_land_data['2010'],
            "Population growth (annual %)": population_growth_data['2010'],
            "CO2 Emission": co2_data['2010']
        })
    return heatmap_data
    

def create_heatmap(data):
    """
    Parameters
    ----------
    data : DataFrame

    Returns
    -------
    None.

    """
    fig, ax = plt.subplots(figsize = (12, 7))
    corr = data.corr()
    corr.style.background_gradient(cmap ='coolwarm')
    sn.heatmap(corr, annot = True)
    

def create_population_growth_box_plot():
    """
    Creates box plot for a country
    Returns
    -------
    None.

    """
    life_expect = ("/Users/saniarashid1/Downloads/" + 
    "sania/heatmap_datasets/API_SP.DYN.LE00.IN_DS2_en_csv_v2_5338365.csv")
    life_expect_data, life_expect_data_year = create_dataframes(life_expect)
    data = life_expect_data_year
    data['Country'] = "Pakistan"
    data = data[['Pakistan', 'Country']]
    data['Year'] = data.index
    box_plot = data.boxplot(by ='Country', column =['Pakistan'], grid = False, 
                            color='red')
    box_plot.plot()
    plt.title("Life Expectency at birth in Pakistan")
    plt.show()


def main():
    """
    Generic function to hold the main code

    Returns
    -------
    None.

    """
    agricultural_data = ("/Users/saniarashid1/Downloads/" + 
    "sania/API_AG.LND.AGRI.ZS_DS2_en_csv_v2_5069067.csv")
    agr_data, agr_data_year = create_dataframes(agricultural_data)
    describe_agricultural_land(agr_data_year)
    
    electrical_usage_data =  ("/Users/saniarashid1/Downloads/" + 
    "sania/API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_4902219.csv")
    elec_data, elec_data_year = create_dataframes(electrical_usage_data)
    describe_electricity_usage(elec_data_year)
    
    co2_data_uri =  ("/Users/saniarashid1/Downloads/" + 
    "sania/API_EN.ATM.CO2E.KT_DS2_en_csv_v2_5181545.csv")
    co2_data, co2_data_year = create_dataframes(co2_data_uri)
    describe_co2_series(co2_data_year)
    
    forest_data_uri =  ("/Users/saniarashid1/Downloads/" + 
    "sania/API_AG.LND.FRST.K2_DS2_en_csv_v2_5172005.csv")
    forest_data, forest_data_year = create_dataframes(forest_data_uri)
    describe_forest_series(forest_data_year)
    
    heatmap_data = prepare_heatmap_data()
    
    create_heatmap(heatmap_data)
    
    create_population_growth_box_plot()
    
    explain_dataset(elec_data)

main()
































