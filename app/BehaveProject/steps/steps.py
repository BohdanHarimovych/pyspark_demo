from behave import step
from pyspark.sql import SparkSession
from logging import getLogger

logger = getLogger("main")


@step('Run Spark Query')
def step_impl(context):
    print("Creating Spark Session")
    spark = SparkSession.builder \
        .appName("My App") \
        .getOrCreate()
    query = """
    SELECT COUNT(*) FROM enr_data_solutions_db.campaign_performance_agg_backup_history
    """
    print("Executing Spark query")
    df = spark.sql(query)
    print(f"There are {df.count()} rows in 'enr_data_solutions_db.campaign_performance_agg_backup_history' table")
