# import pandas as pd
#
# # Replace 'your_input_file.csv' with the actual path to your CSV file
# input_file_path = 'ResultadoElectorales_2023_Generales.csv'
#
# # Load the CSV file into a DataFrame
# df = pd.read_csv(input_file_path)
#
# # Filter rows where the 'Presidente' column has the value 'Presidente'
# filtered_df = df[df['cargo_id'] == 1]
#
# # Replace 'your_output_file.csv' with the desired output path for the filtered data
# output_file_path = 'res.csv'
#
# # Save the filtered DataFrame to a new CSV file
# filtered_df.to_csv(output_file_path, index=False)
#
# print(f"Filtered data saved to: {output_file_path}")

# import pandas as pd
#
# # Replace 'your_input_file.csv' with the actual path to your CSV file
# input_file_path = 'res.csv'
#
# # Load the CSV file into a DataFrame
# df = pd.read_csv(input_file_path)
#
# # Filter rows based on values in the 'votos_tipo' column
# filtered_df = df[~df['votos_tipo'].isin(['COMANDO', 'IMPUGNADO', 'NULO', 'RECURRIDO'])]
#
# # Replace 'your_output_file.csv' with the desired output path for the filtered data
# output_file_path = 'res2.csv'
#
# # Save the filtered DataFrame to a new CSV file
# filtered_df.to_csv(output_file_path, index=False)
#
# print(f"Filtered data saved to: {output_file_path}")

# import pandas as pd
#
# # Replace 'your_input_file.csv' with the actual path to your CSV file
# input_file_path = 'res2.csv'
#
# # Load the CSV file into a DataFrame
# df = pd.read_csv(input_file_path)
#
# # Keep only the desired columns
# selected_columns = [ 'distrito_nombre', 'seccion_nombre', 'agrupacion_nombre', 'votos_cantidad']
# filtered_df = df[selected_columns]
#
# # Replace 'your_output_file.csv' with the desired output path for the selected columns
# output_file_path = 'res3.csv'
#
# # Save the selected columns to a new CSV file
# filtered_df.to_csv(output_file_path, index=False)
#
# print(f"Selected columns saved to: {output_file_path}")

# import pandas as pd
#
# # Replace 'your_input_file.csv' with the actual path to your CSV file
# input_file_path = 'res3.csv'
#
# # Load the CSV file into a DataFrame
# df = pd.read_csv(input_file_path)
#
# #Remove rows with no agrupacion nombre
# filtered_df = df[df['agrupacion_nombre'].notna()]
#
#
# # Replace 'your_output_file.csv' with the desired output path for the selected and filtered columns
# output_file_path = 'res4.csv'
#
# # Save the selected and filtered columns to a new CSV file
# filtered_df.to_csv(output_file_path, index=False)
#
# print(f"Selected and filtered columns saved to: {output_file_path}")

# import pandas as pd
#
# # Replace 'your_input_file.csv' with the actual path to your CSV file
# input_file_path = 'res4.csv'
#
# # Load the CSV file into a DataFrame
# df = pd.read_csv(input_file_path)
#
# # Remove rows where 'agrupacion_nombre' is an empty string
# filtered_df = df[df['agrupacion_nombre'] != '']
#
# # Group by 'distrito_nombre', 'seccion_nombre', and 'agrupacion_nombre', and sum up 'votos_cantidad'
# aggregated_df = filtered_df.groupby(['distrito_nombre', 'seccion_nombre', 'agrupacion_nombre'], as_index=False)['votos_cantidad'].sum()
#
# # Replace 'your_output_file.csv' with the desired output path for the aggregated data
# output_file_path = 'res5.csv'
#
# # Save the aggregated DataFrame to a new CSV file
# aggregated_df.to_csv(output_file_path, index=False)
#
# print(f"Aggregated data saved to: {output_file_path}")

import pandas as pd

# Replace 'your_input_file.csv' with the actual path to your CSV file
input_file_path = 'res5.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(input_file_path)

# Remove rows where 'agrupacion_nombre' is an empty string
filtered_df = df[df['agrupacion_nombre'] != '']

# Group by 'distrito_nombre', 'seccion_nombre', and 'agrupacion_nombre', and sum up 'votos_cantidad'
aggregated_df = filtered_df.groupby(['distrito_nombre', 'seccion_nombre', 'agrupacion_nombre'], as_index=False)['votos_cantidad'].sum()

# Pivot the DataFrame to have separate columns for each 'agrupacion_nombre'
pivoted_df = aggregated_df.pivot(index=['distrito_nombre', 'seccion_nombre'], columns='agrupacion_nombre', values='votos_cantidad').reset_index()

# Replace 'your_output_file.csv' with the desired output path for the pivoted data
output_file_path = 'res6.csv'

# Save the pivoted DataFrame to a new CSV file
pivoted_df.to_csv(output_file_path, index=False)

print(f"Pivoted data saved to: {output_file_path}")


