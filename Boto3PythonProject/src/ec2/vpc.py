class VPC:

    def __init__(self, client):
        self._client = client

    def create_vpc(self):
        print("Creating VPC")
        return self._client.create_vpc(
            CidrBlock='10.0.0.0/16',
        )

    def add_tag_to_vpc(self, resource_id, resource_name):
        print('Add tag name with ID' + resource_id + " with name" + resource_name)
        return self._client.create_tags(
            Resources=[resource_id],
            Tags=[{
                'Key': 'Name',
                'Value': resource_name
            }]
        )

    def create_internet_gateway(self):
        print('Creating the internet gateway')
        return self._client.create_internet_gateway()

    def attach_internet_gateway(self, vpc_id, igw_id):
        print("Attaching internet gateway: " + igw_id + " to vpc:" + vpc_id)
        return self._client.attach_internet_gateway(
            InternetGatewayId=igw_id,
            VpcId=vpc_id
        )

    def create_subnet(self, vpc_id, cidr_block):
        print('creating subnet with VpcId' + vpc_id + 'ciderBlock' + cidr_block)
        return self._client.create_subnet(
            VpcId=vpc_id,
            CidrBlock=cidr_block
        )

    def create_public_route_table(self, vpc_id):
        print("creating public Route Table for vpc" + vpc_id)
        return self._client.create_route_table(
            VpcId=vpc_id
        )

    def create_igw_route_to_public_route_table(self, rtb_id, igw_id):
        print("Creating Internet gateway route to public table :" + rtb_id)
        return self._client.create_route(
            RouteTableId=rtb_id,
            GatewayId=igw_id,
            DestinationCidrBlock='0.0.0.0/0'
        )

    def associate_subnet_with_route_table(self, subnet_id, rtb_id):
        print("Associating subnet with route table:" + rtb_id + "for subnet :" + subnet_id)
        return self._client.associate_route_table(
            SubnetId=subnet_id,
            RouteTableId=rtb_id
        )

    def allow_auto_assign_public_ip_address_to_subnet(self, subnet_id):
        print("Auto assigning public ip address to subnet" + subnet_id)
        return self._client.modify_subnet_attribute(
            SubnetId=subnet_id,
            MapPublicIpOnLaunch={'Value': True}
        )
