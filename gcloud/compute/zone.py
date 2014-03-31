class Zone(object):

  def __init__(self, instance=None, creationTimestamp=None, description=None,
               id=None, name=None, region=None, selfLink=None, status=None):

    self.instance = instance
    self.creationTimestamp = creationTimestamp
    self.description = description
    self.id = id
    self.kind = "compute#zone"
    self.name = name
    self.region = region
    self.selfLink = selfLink
    self.status = status



