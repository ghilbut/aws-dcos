from ansible import errors
from netaddr import IPAddress, IPNetwork

def subnet_name(item, aws):
  """
  get subnet name from aws.network.subnets:
    {{ "ip" | subnet_name(aws) }}
    -> subnet_name
  """
  for name, subnets in aws.network.subnets.iteritems():
    for subnet in subnets:
      if IPAddress(item) in IPNetwork(subnet.cidr):
        return 'subnet-' + subnet.suffix
  return None
 
class FilterModule(object):
  ''' A filter to append text after target item '''
  def filters(self):
    return { 'subnet_name': subnet_name }
