from pyspark.sql import SparkSession
from logging import getLogger

logger = getLogger("main")

# Create a SparkSession


def run_query():
    spark = SparkSession.builder \
        .appName("My App") \
        .getOrCreate()
    query = """
    SELECT COUNT(*) FROM enr_data_solutions_db.campaign_performance_agg_backup_history
    """
    df = spark.sql(query)
    logger.info(f"There are {df.count()} rows in 'enr_data_solutions_db.campaign_performance_agg_backup_history' table")
