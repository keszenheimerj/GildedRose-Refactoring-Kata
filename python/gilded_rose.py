# -*- coding: utf-8 -*-


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            category = self.categorize()
            category.updateOneItem(item)

    def categorize(item):
        return ItemCategory()


class ItemCategory:

    def incrementQuality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1

    def decrementQuality(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1

    def updateExpired(self, item):
        if item.name == "Aged Brie":
            self.incrementQuality(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            item.quality = 0
        elif item.name != "Sulfuras, Hand of Ragnaros":
            return
        else:
            self.decrementQuality(item)

    def updateSellIn(self, item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1

    def updateQuality(self, item):
        if item.name == "Aged Brie":
            self.incrementQuality(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.incrementQuality(item)

            if item.sell_in < 11:
                self.incrementQuality(item)
            if item.sell_in < 6:
                self.incrementQuality(item)
        elif item.name != "Sulfuras, Hand of Ragnaros":
            return
        else:
            self.decrementQuality(item)

    def updateOneItem(self, item):
        self.updateQuality(item)

        self.updateSellIn(item)

        if item.sell_in < 0:
            self.updateExpired(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
