from tests.settings import *

# create tests for normal items here...


@pytest.mark.xfail(reason="Brie shouldnt be decreasing in Value!")
def test_agedBrie_increasing():
    item = Item("Aged Brie", 5, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 4
    assert item.quality == 19

@pytest.mark.xfail(reason="Brie aging correctly")
def test_agedBrie_increasing():
    item = Item("Aged Brie", 5, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 4
    assert item.quality == 21

def test_backstagePasses_QualityIncreaseByTwo():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 22
    assert item.sell_in == 8

def test_backstagePasses_QualityIncreaseByThree():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 23
    assert item.sell_in == 4

def test_backstagePasses_QualityOutdated():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 0


def test_sulfuras():
    item = Item("Sulfuras, Hand of Ragnaros", 5, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 5
    assert item.quality == 20

def test_ifQualityDropsBelowZero():
    item = Item("Apple", 5, 0)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 0
    assert item.sell_in == 4

def test_ifQualityDropsBelowZero_afterSellBy():
    item = Item("Apple", 0, 1)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 0
    assert item.sell_in == -1


def test_QualityDegrade_AfterSellByDate():
    item = Item("Apple", 0, 10)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 8
    assert item.sell_in == -1

def test_maxQuality():
    item = Item("Aged Brie", 10, 49)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    gilded_rose.update_quality()
    gilded_rose.update_quality()
    assert item.quality == 50



@pytest.mark.xfail(xfail_new_features, reason="new feature:conjured not working, aging like regular item ")
def test_conjuredItems():
    item = Item("Conjured", 10, 49)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 9
    assert item.quality == 48

@pytest.mark.xfail(xfail_new_features, reason="new feature:conjured working as intended ")
def test_conjuredItems():
    item = Item("Conjured", 10, 49)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 9
    assert item.quality == 47
