class Disk(object):

  def __init__(self, create_time=None, description=None,
               id=None, name=None, size=None, status=None, zone=None):

    self.create_time = create_time
    self.description = description
    self.id = id
    self.kind = "compute#disk"
    self.name = name
    self.size = size
    self.status = status
    self.zone = zone

  @classmethod
  def from_dict(cls, disk_dict, connection=None):

    return cls(connection=connection,
               create_time=disk_dict['creationTimestamp'],
               description=disk_dict['description'],
               id=disk_dict['id'],
               name=disk_dict['name'],
               size=disk_dict['sizeGb'],
               status=disk_dict['status']
               zone=disk_dict['zone'].split('/').pop())

  def create():


  def get():


  def attach():


  def list():


  def aggregatedLight():


  def createSnapshot():


  def delete():
