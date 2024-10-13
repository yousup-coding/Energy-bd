
import pandas as pd

# Data
data = {
    'Year': [2020, 2020, 2020, 2020, 2020, 2020,
             2025, 2025, 2025, 2025, 2025, 2025,
             2030, 2030, 2030, 2030, 2030, 2030],
    'Energy_Source': ['Natural Gas', 'Coal', 'Solar', 'Biomass', 'Wind', 'Hydro',
                      'Natural Gas', 'Coal', 'Solar', 'Biomass', 'Wind', 'Hydro',
                      'Natural Gas', 'Coal', 'Solar', 'Biomass', 'Wind', 'Hydro'],
    'Consumption_MWh': [30000000, 10000000, 5000000, 2000000, 1000000, 2000000,
                        32000000, 12000000, 8000000, 3000000, 2000000, 3000000,
                        34000000, 14000000, 15000000, 4000000, 4000000, 5000000],
    'Installed_Capacity_MW': [12000, 5000, 2000, 1000, 500, 1500,
                               12500, 6000, 4000, 1500, 1000, 2000,
                               13000, 7000, 6000, 2000, 2500, 2500],
    'Percentage_Contribution': [60, 20, 10, 5, 2.5, 2.5,
                                58, 18, 15, 4, 3, 2,
                                55, 16, 20, 4, 4, 5],
    'CO2_Emissions_tons': [10000000, 15000000, 500000, 300000, 100000, 200000,
                           10500000, 16000000, 400000, 250000, 80000, 150000,
                           11000000, 18000000, 300000, 200000, 60000, 100000],
    'Investment_BDT': [200000000, 100000000, 50000000, 20000000, 30000000, 40000000,
                       220000000, 110000000, 100000000, 30000000, 40000000, 50000000,
                       250000000, 120000000, 150000000, 40000000, 60000000, 70000000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('bangladesh_energy_scenario.csv', index=False)

print("Energy scenario dataset created successfully!")
