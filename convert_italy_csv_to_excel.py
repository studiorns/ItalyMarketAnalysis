import pandas as pd
import os

def convert_csv_to_excel(csv_file, excel_file):
    """
    Convert a CSV file to Excel format while preserving formatting.
    
    Args:
        csv_file (str): Path to the CSV file
        excel_file (str): Path to the output Excel file
    """
    # Read the CSV file
    with open(csv_file, 'r') as f:
        lines = f.readlines()
    
    # Create a pandas DataFrame
    data = []
    for line in lines:
        data.append(line.strip().split(','))
    
    # Create Excel writer
    writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
    
    # Convert to DataFrame and write to Excel
    df = pd.DataFrame(data)
    df.to_excel(writer, sheet_name='Forecast', header=False, index=False)
    
    # Get the xlsxwriter workbook and worksheet objects
    workbook = writer.book
    worksheet = writer.sheets['Forecast']
    
    # Add formats
    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'top',
        'bg_color': '#D9E1F2',
        'border': 1
    })
    
    section_format = workbook.add_format({
        'bold': True,
        'bg_color': '#E2EFDA',
        'border': 1
    })
    
    percent_format = workbook.add_format({
        'num_format': '0.0%',
    })
    
    # Format the worksheet
    worksheet.set_column('A:Z', 15)  # Set column width
    
    # Save the Excel file
    writer.close()
    
    print(f"Converted {csv_file} to {excel_file}")

def main():
    # Directory containing the CSV files
    directory = os.path.dirname(os.path.abspath(__file__))
    
    # List of CSV files to convert
    csv_files = [
        'Travel_Queries_Forecast_Italy.csv',
        'Travel_Queries_Forecast_Italy_Enhanced.csv',
        'Italy_Travel_Queries_2025_Forecast.csv'
    ]
    
    # Convert each CSV file to Excel
    for csv_file in csv_files:
        csv_path = os.path.join(directory, csv_file)
        excel_file = csv_path.replace('.csv', '.xlsx')
        
        if os.path.exists(csv_path):
            convert_csv_to_excel(csv_path, excel_file)
        else:
            print(f"File not found: {csv_path}")

if __name__ == "__main__":
    main()
