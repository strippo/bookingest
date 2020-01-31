from dbbackup.storage.ftp_storage import Storage as BaseFtpStorage


class Storage(BaseFtpStorage, object):
    def list_directory(self, raw=False):
        backup_dir = self.backup_dir()
        for x in super(Storage, self).list_directory(raw):
            yield x.replace(backup_dir, "")

    def delete_file(self, filepath):
        backup_dir = self.backup_dir()
        super(Storage, self).delete_file("{}{}".format(backup_dir, filepath))
