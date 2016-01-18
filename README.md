shop
====

- forzieri
  - :us: http://www.forzieri.com/
  - :cn: http://www.cn.forzieri.com/
- shopbop
  - :us: https://www.shopbop.com/
  - :cn: https://cn.shopbop.com/

## command

```bash
$ scrapy list
forzieri_en
forzieri_zh
shopbop_en
shopbop_zh

$ scrapy crawl forzieri_en -o forzieri_en.jl
$ scrapy crawl forzieri_zh -o forzieri_zh.jl
$ scrapy crawl shopbop_en -o shopbop_en.jl
$ scrapy crawl shopbop_zh -o shopbop_zh.jl

$ merge.py forzieri_*.jl
$ merge.py shopbop_*.jl
```

## result

```json
{
  "en": {
    "lang": "en",
    "cate": "Home Travel & Business Wallets",
    "url": "http://www.forzieri.com/wallets/michael-kors/ik160116-003-00",
    "brand": "Michael Kors",
    "site": "forzieri",
    "time": 1453106745.335382,
    "desc": "Bedford Black Leather Continental Wallet crafted in pebbled leather, has the refined MK appeal that is the perfect companion for your tote or bag. Featuring continental metal zip tab closure, logo at top line, center zip pocket, bill pockets, card slots and gold tone hardware detail.Genuine Michael Kors.",
    "id": "Ik160116-003-00",
    "name": "Bedford Black Leather Continental Wallet"
  },
  "zh": {
    "lang": "zh",
    "cate": "首页 商务旅行 手机袋",
    "url": "http://www.cn.forzieri.com/chn/product_view.asp?c=chn&dept_id=026&l=chn&sku=ik160116-003-00",
    "brand": "Michael Kors",
    "site": "forzieri",
    "time": 1453106762.925439,
    "desc": "Bedford黑色皮革欧式皮夹，以鹅卵石皮革制作，精致的MK格，是你的手提包或手袋一个完美的伴侣。拥有欧陆金属拉链标签闭合，标志于顶线，中间拉链袋，钞票袋，卡插槽和金色调硬件细节。原装Michael Kors。",
    "id": "Ik160116-003-00",
    "name": "Bedford黑色皮革欧式皮夹"
  },
  "id": "Ik160116-003-00"
}
```
