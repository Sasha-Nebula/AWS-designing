from diagrams import Diagram,Edge
from diagrams.aws.general import Users
from diagrams.aws.network import Route53
from diagrams.aws.storage import SimpleStorageServiceS3 as S3
from diagrams.aws.network import CloudFront as CF
from diagrams.aws.security import IdentityAndAccessManagementIamRole as IAMRole


with Diagram("Solution1",show=True) as diag:
    Users("User") >> Edge(color="firebrick",style="dashed") >> \
    Route53("Route53") >> Edge(color="firebrick",style="dashed") >> \
    CF("Cloud Front")  >> Edge(color="firebrick",style="dashed") >> \
    S3("Simple Storage Service")  >> Edge(color="firebrick",style="dashed") 


