import json

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.list_items = []
        self.file = open('euler.json', 'w')

    def close_spider(self, spider):
        ordered_list = [None for i in range(len(self.list_items))]

        self.file.write("[\n")

        for i in self.list_items:
            ordered_list[int(i['id']-1)] = json.dumps(dict(i))

        for i in ordered_list:
            self.file.write(str(i)+",\n")

        self.file.write("]\n")
        self.file.close()

    def process_item(self, item, spider):
        self.list_items.append(item)
        return item
