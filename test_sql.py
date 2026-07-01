from sqlalchemy import create_engine,text
import pandas as pd

cloud_connection=(
    "mssql+pyodbc://NikhilCloudLogin:RottweilerCloud%401999@"
    "Rottweiler-cloud-server.database.windows.net/testing"
    "?driver=ODBC+Driver+17+For+Sql+Server"
)

engine=create_engine(cloud_connection)
csv_url=r"/workspaces/Jfoldknewme/CSAT Bifurcation Random Audits.ods"
excel_url=r"/workspaces/Jfoldknewme/CSAT Bifurcation Random Audits.xlsx"

# df1=pd.read_csv(csv_url)
df2=pd.read_excel(excel_url)

# df1.to_sql(
#     name="C_Raw",
#     con=engine,
#     schema="dbo",
#     if_exists="replace",
#     index=False
# )

df2.to_sql(
    name="C_Raw_au",
    con=engine,
    schema="dbo",
    if_exists="replace",
    index=False
)


print("\nCloud connection successfull\n")

# df=pd.read_sql("select * from sys.tables",con=engine)
# print(df)