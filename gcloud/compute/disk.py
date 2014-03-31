class Disk(object):

  def __init__(self, connection=None, create_time=None, description=None,
               id=None, name=None, size=None, status=None, zone=None):

    self.connection = connection
    self.create_time = create_time
    self.description = description
    self.id = id
    self.kind = "compute#disk"
    self.name = name
    self.size = size
    self.status = status
    self.zone = zone

  @property
  def path(self):
    """The URL path to this disk."""

    if not self.name:
      raise ValueError('Cannot determine path without disk zone and name.')

    return ('projects/%s/zones/%s/disks/%s' %
            (self.connection.project_name, self.zone, self.name))

  @classmethod
  def from_dict(cls, disk_dict, connection=None):

    return cls(connection=connection,
               create_time=disk_dict['creationTimestamp'],
               description=disk_dict['description'],
               id=disk_dict['id'],
               name=disk_dict['name'],
               size=disk_dict['sizeGb'],
               status=disk_dict['status'],
               zone=disk_dict['zone'].split('/').pop())

  def get(self):
    return self.connection.get_disk(self.name, self.zone)

  def delete(self):
    return self.connection.delete_disk(self.name, self.zone)

  def snapshot(self):
    return self.connection.create_snapshot(self.name, self.zone)
