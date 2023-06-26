# -*- coding: utf-8 -*-

class GildedRose(object):
    def __init__(self, items):
        self.items = items
        self.quality_update_strategies = {
            "Aged Brie": AgedBrieUpdateStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassUpdateStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasUpdateStrategy(),
            "Conjured": ConjuredUpdateStrategy()
        }

    def update_quality(self):
        for item in self.items:
            if item.name in self.quality_update_strategies:
                strategy = self.quality_update_strategies[item.name]
            else:
                strategy = NormalItemUpdateStrategy()
            strategy.update_quality(item)

class QualityUpdateStrategy:
    def update_quality(self, item):
        item.sell_in -= 1

class NormalItemUpdateStrategy(QualityUpdateStrategy):
    def update_quality(self, item):
        # Update quality logic for normal items
        super().update_quality(item)
        if (item.quality==0):
            pass
        elif(item.sell_in>0):
            item.quality -= 1
        elif (item.sell_in<0 and item.quality >= 2):
            item.quality -= 2
        else:
            item.quality = 0

class ConjuredUpdateStrategy(QualityUpdateStrategy):
    def update_quality(self, item):
        super().update_quality(item)
        if (item.quality == 0):
            pass
        elif (item.sell_in > 0):
            item.quality -= 2
        elif (item.sell_in < 0 and item.quality >= 4):
            item.quality -= 4
        else:
            item.quality = 0
class AgedBrieUpdateStrategy(QualityUpdateStrategy):
    def update_quality(self, item):
        # Update quality logic for Aged Brie
        super().update_quality(item)
        if(item.quality<50):
            item.quality += 1

class BackstagePassUpdateStrategy(QualityUpdateStrategy):
    def update_quality(self, item):
        # Update quality logic for Backstage passes
        super().update_quality(item)
        if(item.sell_in<=0):
            item.quality = 0
        elif (item.sell_in <= 5 and item.quality<50):
            item.quality += 3
        elif (item.sell_in <= 10  and item.quality<50):
            item.quality += 2
        elif (item.sell_in > 10  and item.quality<50):
            item.quality += 1


class SulfurasUpdateStrategy(QualityUpdateStrategy):
    def update_quality(self, item):
        # Update quality logic for Backstage passes
        pass



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

