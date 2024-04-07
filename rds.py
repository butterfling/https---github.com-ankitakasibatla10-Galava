import boto3
from botocore.exceptions import ClientError
import logging

# Make sure to replace 'logger' with a valid logger instance.
logger = logging.getLogger()
logger.setLevel(logging.INFO)

class InstanceWrapper:
    """Encapsulates Amazon RDS DB instance actions."""

    def __init__(self, rds_client):
        """
        :param rds_client: A Boto3 Amazon RDS client.
        """
        self.rds_client = rds_client

    @classmethod
    def from_client(cls):
        """
        Instantiates this class from a Boto3 client.
        """
        rds_client = boto3.client("rds")
        return cls(rds_client)

    def create_db_instance(
        self,
        db_name,
        instance_id,
        parameter_group_name,
        db_engine,
        db_engine_version,
        instance_class,
        storage_type,
        allocated_storage,
        admin_name,
        admin_password,
    ):
        """
        Creates a DB instance.
        """
        try:
            response = self.rds_client.create_db_instance(
                DBName=db_name,
                DBInstanceIdentifier=instance_id,
                DBParameterGroupName=parameter_group_name,
                Engine=db_engine,
                EngineVersion=db_engine_version,
                DBInstanceClass=instance_class,
                StorageType=storage_type,
                AllocatedStorage=allocated_storage,
                MasterUsername=admin_name,
                MasterUserPassword=admin_password,
            )
            db_inst = response["DBInstance"]
        except ClientError as err:
            logger.error(
                "Couldn't create DB instance %s. Here's why: %s: %s",
                instance_id,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
        else:
            return db_inst

# Initialize the InstanceWrapper with a Boto3 RDS client
wrapper = InstanceWrapper.from_client()

# Call the create_db_instance method with your desired parameters
# Make sure to replace the placeholders with your actual parameters
db_instance = wrapper.create_db_instance(
    db_name="database2",
    instance_id="database",
    parameter_group_name="ankita",
    db_engine="MySQL",
    db_engine_version="8.0.35",
    instance_class="db.t3.micro",
    storage_type="gp3",
    allocated_storage=30,  # This should be an integer
    admin_name="ankita",
    admin_password="ankita2003"
)


