from scrapy.exporters import JsonItemExporter
from scrapy.utils.python import to_bytes


class OrderedJsonItemExporter(JsonItemExporter):

    def __init__(self, file, **kwargs):
        # To initialize the object we use JsonItemExporter's constructor
        super().__init__(file)
        self.list_items = []

    def export_item(self, item):
        self.list_items.append(item)

    def finish_exporting(self):
        ordered_list = [None for i in range(len(self.list_items))]

        for i in self.list_items:
            ordered_list[int(i['id'] - 1)] = i

        for i in ordered_list:
            if self.first_item:
                self.first_item = False
            else:
                self.file.write(b',')
                self._beautify_newline()
            itemdict = dict(self._get_serialized_fields(i))
            data = self.encoder.encode(itemdict)
            self.file.write(to_bytes(data, self.encoding))

        self._beautify_newline()
        self.file.write(b"]")